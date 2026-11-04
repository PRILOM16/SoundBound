document.addEventListener("DOMContentLoaded", function () {
  const existingArtist = document.getElementById("existing-artist-container");
  const newArtist = document.getElementById("new-artist-container");

  const showNewButton = document.getElementById("show-new-artist");
  const showExistingButton = document.getElementById("show-existing-artist");

  const artistInput = document.getElementById("id_new_artist");
  const artistSelect = document.getElementById("id_artist_choice");

  // Проверяем наличие необходимых элементов
  if (
    !existingArtist ||
    !newArtist ||
    !showNewButton ||
    !showExistingButton ||
    !artistInput ||
    !artistSelect
  ) {
    return;
  }

  // Переключение на добавление нового автора
  showNewButton.addEventListener("click", function () {
    existingArtist.classList.add("hidden");
    newArtist.classList.remove("hidden");

    artistSelect.value = "";
    artistInput.required = true;
    artistInput.focus();
  });

  // Возвращение к выбору существующего автора
  showExistingButton.addEventListener("click", function () {
    newArtist.classList.add("hidden");
    existingArtist.classList.remove("hidden");

    artistInput.value = "";
    artistInput.required = false;
  });
});
