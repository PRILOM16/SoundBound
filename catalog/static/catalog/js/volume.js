document.addEventListener("DOMContentLoaded", function () {
  const audio = document.getElementById("audio-player");
  const volumeSlider = document.getElementById("volume-slider");
  const muteButton = document.getElementById("mute-button");
  const volumeValue = document.getElementById("volume-value");

  if (!audio || !volumeSlider || !muteButton || !volumeValue) {
    return;
  }

  // Начальная громкость — 50%
  audio.volume = 0.5;

  // Изменение громкости ползунком
  volumeSlider.addEventListener("input", function () {
    const volume = Number(volumeSlider.value) / 100;

    audio.volume = volume;
    audio.muted = volume === 0;

    updateVolumeDisplay();
  });

  // Отключение и включение звука
  muteButton.addEventListener("click", function () {
    audio.muted = !audio.muted;
    updateVolumeDisplay();
  });

  // Обновление отображения громкости
  function updateVolumeDisplay() {
    const isMuted = audio.muted || audio.volume === 0;

    muteButton.textContent = isMuted ? "🔇" : "🔊";
    muteButton.title = isMuted ? "Включить звук" : "Выключить звук";

    volumeValue.textContent = isMuted
      ? "0%"
      : `${Math.round(audio.volume * 100)}%`;

    volumeSlider.value = isMuted ? 0 : Math.round(audio.volume * 100);
  }
});
