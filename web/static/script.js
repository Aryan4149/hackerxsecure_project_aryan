// ================= DOM ELEMENTS =================
const form = document.getElementById("uploadForm");
const statusDiv = document.getElementById("status");
const attackTable = document.querySelector("#attackTable tbody");
const benignTable = document.querySelector("#benignTable tbody");

const modalBg = document.getElementById("modalBg");
const modalContent = document.getElementById("modalContent");
const closeModal = document.getElementById("closeModal");

// ================= HELPERS =================
function escapeHTML(text) {
    if (!text) return "";
    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

// ================= FORM SUBMIT =================
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    statusDiv.innerText = "Analyzing traffic...";
    attackTable.innerHTML = "";
    benignTable.innerHTML = "";

    const formData = new FormData(form);

    try {
        const res = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        const data = await res.json();

        if (!res.ok) {
            statusDiv.innerText = "Error: " + (data.detail || "Unknown error");
            return;
        }

        statusDiv.innerText = "Analysis complete";

        // ================= ATTACKS =================
        if (Array.isArray(data.attacks)) {
            data.attacks.forEach((row) => {
                const tr = document.createElement("tr");

                const attackType = escapeHTML(row.attack_type || "Unknown");
                const severity = row.severity !== undefined ? row.severity : "-";
                const action = escapeHTML(row.action || "MONITOR");
                const message = escapeHTML(row.message || "No prevention message available.");
                const index = row.index !== undefined ? row.index : "-";

                tr.innerHTML = `
                    <td>${index}</td>
                    <td>${attackType}</td>
                    <td>${severity}</td>
                    <td>${action}</td>
                    <td>
                        <button class="view-btn"
                            data-label="${attackType}"
                            data-message="${message}">
                            View
                        </button>
                    </td>
                `;

                attackTable.appendChild(tr);
            });
        }

        // ================= BENIGN =================
        if (Array.isArray(data.benign)) {
            data.benign.forEach((row) => {
                const tr = document.createElement("tr");

                const label = escapeHTML(row.label || "Benign");
                const index = row.index !== undefined ? row.index : "-";

                tr.innerHTML = `
                    <td>${index}</td>
                    <td>${label}</td>
                    <td>Safe</td>
                `;

                benignTable.appendChild(tr);
            });
        }

    } catch (err) {
        console.error(err);
        statusDiv.innerText = "Server error. Check backend logs.";
    }
});

// ================= EVENT DELEGATION (VIEW BUTTON) =================
document.addEventListener("click", (e) => {
    if (e.target.classList.contains("view-btn")) {
        const label = e.target.getAttribute("data-label");
        const message = e.target.getAttribute("data-message");
        showPrevention(label, message);
    }
});

// ================= MODAL =================
function showPrevention(label, text) {
    modalContent.innerHTML = `
        <h3>${label} – Prevention Guide</h3>
        <p>${text}</p>
    `;
    modalBg.classList.remove("hidden");
}

closeModal.addEventListener("click", () => {
    modalBg.classList.add("hidden");
});

modalBg.addEventListener("click", (e) => {
    if (e.target === modalBg) {
        modalBg.classList.add("hidden");
    }
});
