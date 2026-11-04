const audioPlayer = document.getElementById("audio-player");
const playButton = document.getElementById("play-button");

const playerTitle = document.getElementById("player-title");
const playerArtist = document.getElementById("player-artist");

const progressBar = document.getElementById("progress-bar");
const currentTime = document.getElementById("current-time");
const duration = document.getElementById("duration");

// Перевод секунд в формат минуты:секунды
function formatTime(seconds) {
  if (!Number.isFinite(seconds)) {
    return "0:00";
  }

  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = Math.floor(seconds % 60);

  return `${minutes}:${String(remainingSeconds).padStart(2, "0")}`;
}

// Запуск выбранной композиции
function playSong(element) {
  audioPlayer.src = element.dataset.audio;

  playerTitle.textContent = element.dataset.title;
  playerArtist.textContent = element.dataset.artist;

  progressBar.value = 0;
  currentTime.textContent = "0:00";
  duration.textContent = "0:00";

  audioPlayer.play().catch((error) => {
    console.error("Ошибка воспроизведения:", error);
  });
}

// Воспроизведение и пауза
function togglePlay() {
  if (!audioPlayer.src) {
    return;
  }

  if (audioPlayer.paused) {
    audioPlayer.play();
  } else {
    audioPlayer.pause();
  }
}

// Перемотка назад на 10 секунд
function skipBackward() {
  if (!audioPlayer.src) {
    return;
  }

  audioPlayer.currentTime = Math.max(0, audioPlayer.currentTime - 10);
}

// Перемотка вперёд на 10 секунд
function skipForward() {
  if (!audioPlayer.src) {
    return;
  }

  audioPlayer.currentTime = Math.min(
    audioPlayer.duration || audioPlayer.currentTime + 10,
    audioPlayer.currentTime + 10,
  );
}

// Изменение значка при воспроизведении
audioPlayer.addEventListener("play", () => {
  playButton.textContent = "Ⅱ";
});

audioPlayer.addEventListener("pause", () => {
  playButton.textContent = "▶";
});

// Получение длительности композиции
audioPlayer.addEventListener("loadedmetadata", () => {
  duration.textContent = formatTime(audioPlayer.duration);
});

// Обновление времени и полосы прогресса
audioPlayer.addEventListener("timeupdate", () => {
  currentTime.textContent = formatTime(audioPlayer.currentTime);

  if (Number.isFinite(audioPlayer.duration)) {
    progressBar.value = (audioPlayer.currentTime / audioPlayer.duration) * 100;
  }
});

// Перемотка при перемещении ползунка
progressBar.addEventListener("input", () => {
  if (Number.isFinite(audioPlayer.duration)) {
    audioPlayer.currentTime = (progressBar.value / 100) * audioPlayer.duration;
  }
});

// Поиск композиций в каталоге
const searchInput = document.getElementById("song-search");

if (searchInput) {
  searchInput.addEventListener("input", function () {
    const searchValue = this.value.toLowerCase().trim();

    document.querySelectorAll(".song-card").forEach((card) => {
      const title = card.dataset.title.toLowerCase();
      const artist = card.dataset.artist.toLowerCase();

      if (title.includes(searchValue) || artist.includes(searchValue)) {
        card.style.display = "";
      } else {
        card.style.display = "none";
      }
    });
  });
}
