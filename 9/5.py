# log p(x) = -2D/2 * log(2pi) - 1/2 * log(|eps|) - 1/2 * (x - mu)^T eps^-1 (x - mu)

import timeit

import numpy as np
from scipy.linalg import cholesky, solve_triangular
from scipy.stats import multivariate_normal


def log_pdf_multivariate_normal(X, mu, cov):
    D = len(mu)
    log_det_cov = np.log(np.linalg.det(cov))
    cholesky_cov = cholesky(cov, lower=True)
    inv_cholesky_cov = solve_triangular(cholesky_cov, np.eye(D), lower=True).T
    centered_X = X - mu
    quadratic_term = np.sum(np.square(np.dot(centered_X, inv_cholesky_cov)), axis=1)
    log_pdf = -0.5 * (D * np.log(2 * np.pi) + log_det_cov + quadratic_term)
    return log_pdf


mu = np.array([0, 0])
cov = np.array([[1, 0.5], [0.5, 2]])
X = np.random.randn(1000, 2)
log_pdf_custom = log_pdf_multivariate_normal(X, mu, cov)
log_pdf_scipy = multivariate_normal(mu, cov).logpdf(X)

# Проверка отклонения результатов
print(
    "Среднее относительное отклонение:",
    np.mean(np.abs(log_pdf_custom - log_pdf_scipy) / np.abs(log_pdf_scipy)),
)

custom_time = timeit.timeit(lambda: log_pdf_multivariate_normal(X, mu, cov), number=100)


scipy_time = timeit.timeit(lambda: multivariate_normal(mu, cov).logpdf(X), number=100)

# Вывод результатов
print("Время выполнения функции:", custom_time)
print("Время выполнения библиотечной функции:", scipy_time)
