function loadFallenEagles() {
  const gallery = document.querySelector("#fallen-gallery");

  try {
    const photos = window.fallenEaglesPhotos;
    if (!Array.isArray(photos)) {
      throw new Error("The photo list is missing or is not an array.");
    }

    gallery.replaceChildren(...photos.map((photo) => {
      if (typeof photo.file !== "string" || typeof photo.name !== "string") {
        throw new Error("Each photo must include a file and name.");
      }

      const figure = document.createElement("figure");
      const image = document.createElement("img");
      const caption = document.createElement("figcaption");

      image.src = `fep/${encodeURIComponent(photo.file)}`;
      image.alt = photo.name;
      image.loading = "lazy";
      if (photo.desaturate === true) {
        image.classList.add("desaturate");
      }

      caption.textContent = photo.name;
      figure.append(image, caption);
      return figure;
    }));
  } catch (error) {
    console.error("Unable to load the Fallen Eagles photos.", error);
    gallery.textContent = "Photos could not be loaded.";
  }
}

loadFallenEagles();
