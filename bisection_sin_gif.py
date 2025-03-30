import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image
import os

# 1. 함수 정의
def f(x):
    return np.sin(x)

# 2. 이분법 (Bisection Method) 단계 추적
def get_bisection_steps(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        return []
    steps = []
    for _ in range(max_iter):
        c = (a + b) / 2
        steps.append((a, b, c, f(c)))
        if abs(f(c)) < tol or (b - a)/2 < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return steps

# 3. 루트가 존재하는 구간 탐색
def find_root_intervals(f, x_start, x_end, sub_interval=0.2):
    intervals = []
    x = x_start
    while x < x_end:
        a, b = x, x + sub_interval
        if f(a) * f(b) < 0:
            intervals.append((a, b))
        x += sub_interval
    return intervals

# 4. 전체 단계 수집
def collect_all_bisection_steps(f, x_start, x_end):
    intervals = find_root_intervals(f, x_start, x_end)
    all_steps = []
    for a, b in intervals:
        steps = get_bisection_steps(f, a, b)
        all_steps.extend(steps)
    return all_steps

# 5. 애니메이션 생성 및 저장
def create_bisection_animation(f, x_start, x_end, output_path, fps=1):
    all_steps = collect_all_bisection_steps(f, x_start, x_end)

    fig, ax = plt.subplots(figsize=(8, 5))
    x_vals = np.linspace(x_start - 1, x_end + 1, 1000)
    y_vals = f(x_vals)

    ax.plot(x_vals, y_vals, label="f(x) = sin(x)")
    ax.axhline(0, color='gray', linestyle='--')
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlim(x_start - 0.5, x_end + 0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Bisection Method for sin(x)")
    ax.legend()
    ax.grid(True)

    point, = ax.plot([], [], 'ro')
    a_line = ax.axvline(0, color='green', linestyle='--', label='a')
    b_line = ax.axvline(0, color='red', linestyle='--', label='b')
    text = ax.text(x_start, 1.2, '', fontsize=12)

    def init():
        point.set_data([], [])
        a_line.set_xdata([0, 0])  # ✅ 리스트로 변경
        b_line.set_xdata([0, 0])  # ✅ 리스트로 변경
        text.set_text('')
        return point, a_line, b_line, text

    def animate(i):
        a, b, c, fc = all_steps[i]
        point.set_data([c], [fc])
        a_line.set_xdata([a, a])  # ✅ 리스트로 변경
        b_line.set_xdata([b, b])  # ✅ 리스트로 변경
        text.set_text(f"Step {i + 1}: c = {c:.6f}")
        return point, a_line, b_line, text

    ani = animation.FuncAnimation(
        fig, animate,
        frames=len(all_steps),
        init_func=init,
        blit=True,
        repeat=False
    )

    ani.save(output_path, writer='pillow', fps=fps)
    print(f"✅ GIF 저장 완료: {output_path}")

# 6. 실행
if __name__ == "__main__":
    output_gif = "sin_bisection_roots.gif"
    create_bisection_animation(
        f=np.sin,
        x_start=-2*np.pi,
        x_end=2*np.pi,
        output_path=output_gif,
        fps=1
    )
