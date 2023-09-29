document.addEventListener("DOMContentLoaded", function () {
    const imageInput = document.getElementById("imageInput");
    const generateButton = document.getElementById("generateButton");
    const avatarPreview = document.getElementById("avatarPreview");

    generateButton.addEventListener("click", async () => {
        const file = imageInput.files[0];
        if (file) {
            const formData = new FormData();
            formData.append("image", file);

            try {
                const response = await fetch("/generate_avatar", {
                    method: "POST",
                    body: formData,
                });

                if (response.ok) {
                    const avatarUrl = await response.text();
                    avatarPreview.innerHTML = `<img src="${avatarUrl}" alt="Generated 3D Avatar">`;
                } else {
                    console.error("Error generating avatar.");
                }
            } catch (error) {
                console.error("Error:", error);
            }
        } else {
            console.error("Please select an image.");
        }
    });
});
