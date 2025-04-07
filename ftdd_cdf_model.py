import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz

# 원 함수 정의
def f(x):
    return 1 / (2 * np.sinh(1/x) + np.log(x))

# 정의역 설정 (x > 0 이어야 하므로 0.1부터 시작)
x = np.linspace(10, 100, 1000)

# 원래 함수 값
y_raw = f(x)

# 정규화 (면적이 1이 되도록)
area = np.trapz(y_raw, x)  # 수치적분으로 면적 구하기
y_pdf = y_raw / area       # 확률 밀도 함수처럼 정규화

# CDF 계산
y_cdf = cumtrapz(y_pdf, x, initial=0)

# CDF 그래프 그리기
plt.figure(figsize=(8, 5))
plt.plot(x, y_cdf, label="CDF of f(x)", color='green')
plt.title("Cumulative Distribution Function (CDF) of f(x)")
plt.xlabel("x")
plt.ylabel("CDF")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
