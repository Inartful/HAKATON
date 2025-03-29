document.addEventListener("DOMContentLoaded", function () {
    const editButton = document.getElementById("edit-profile");
    const saveButton = document.getElementById("save-profile");
    const inputs = document.querySelectorAll(".profile-info input");

    editButton.addEventListener("click", function () {
        inputs.forEach(input => {
            input.removeAttribute("disabled");
            input.style.background = "rgba(255, 255, 255, 0.8)";
            input.style.color = "black";
        });
        saveButton.style.display = "inline-block";
        editButton.style.display = "none";
    });

    saveButton.addEventListener("click", function () {
        inputs.forEach(input => {
            input.setAttribute("disabled", "true");
            input.style.background = "transparent";
            input.style.color = "white";
        });
        saveButton.style.display = "none";
        editButton.style.display = "inline-block";
    });
});