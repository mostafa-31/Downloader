document.getElementById("fetchFormats").addEventListener("click", async () => {
    let url = document.getElementById("videoUrl").value.trim();
    if (!url) {
        alert("Please enter a video URL.");
        return;
    }

    let response = await fetch(`http://127.0.0.1:5000/formats?url=${encodeURIComponent(url)}`);
    let data = await response.json();

    let formatSelect = document.getElementById("formatSelect");
    formatSelect.innerHTML = "";

    if (data.success) {
        data.formats.forEach(format => {
            let option = document.createElement("option");
            option.value = format.format_id;
            option.textContent = `${format.resolution} (${format.ext})`;
            formatSelect.appendChild(option);
        });
    } else {
        alert("Failed to fetch formats.");
    }
});

document.getElementById("downloadVideo").addEventListener("click", async () => {
    let url = document.getElementById("videoUrl").value.trim();
    let format = document.getElementById("formatSelect").value;

    if (!url || !format) {
        alert("Please select a format.");
        return;
    }

    document.getElementById("status").textContent = "Downloading...";

    let response = await fetch(`http://127.0.0.1:5000/download`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url, format })
    });

    let data = await response.json();
    document.getElementById("status").textContent = data.message;
});
