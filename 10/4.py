import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Функция для отображения суммы двух волн
def plot_sum(ax, wave1_freq, wave1_amplitude, wave2_freq, wave2_amplitude):
    x = np.linspace(0, 10, 1000)
    wave1 = wave1_amplitude * np.sin(wave1_freq * x)
    wave2 = wave2_amplitude * np.sin(wave2_freq * x)
    sum_wave = wave1 + wave2

    ax[0].clear()
    ax[1].clear()
    ax[2].clear()

    ax[0].plot(x, wave1, label='Волна 1')
    ax[1].plot(x, wave2, label='Волна 2')
    ax[2].plot(x, sum_wave, label='Сумма волн')

    ax[0].legend()
    ax[1].legend()
    ax[2].legend()

    plt.tight_layout()
    plt.draw()

# слайдеры
fig, ax = plt.subplots(3, 1, figsize=(10, 8))
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.3)
wave1_freq_slider = Slider(plt.axes([0.1, 0.05, 0.8, 0.03]), 'Частота волны 1', 0.1, 10, valinit=1)
wave1_amplitude_slider = Slider(plt.axes([0.1, 0.1, 0.8, 0.03]), 'Амплитуда волны 1', 0.1, 2, valinit=1)
wave2_freq_slider = Slider(plt.axes([0.1, 0.15, 0.8, 0.03]), 'Частота волны 2', 0.1, 10, valinit=1)
wave2_amplitude_slider = Slider(plt.axes([0.1, 0.2, 0.8, 0.03]), 'Амплитуда волны 2', 0.1, 2, valinit=1)

# обновление графика при изменении значений слайдеров
def update(val):
    wave1_freq = wave1_freq_slider.val
    wave1_amplitude = wave1_amplitude_slider.val
    wave2_freq = wave2_freq_slider.val
    wave2_amplitude = wave2_amplitude_slider.val
    plot_sum(ax, wave1_freq, wave1_amplitude, wave2_freq, wave2_amplitude)
    plt.subplots_adjust(bottom=0.35)

wave1_freq_slider.on_changed(update)
wave1_amplitude_slider.on_changed(update)
wave2_freq_slider.on_changed(update)
wave2_amplitude_slider.on_changed(update)

plot_sum(ax, 1, 1, 1, 1)
plt.subplots_adjust(bottom=0.35)
plt.show()
