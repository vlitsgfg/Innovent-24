const find = (sel, parent = document) => parent.querySelector(sel);
const findAll = (sel, parent = document) => parent.querySelectorAll(sel);

const imageInput = find("#image-input");

if (parseInt(find("h2").dataset.timeout) >= (new Date(Date.now())).getHours()) {
	imageInput.disabled = true;
	find("#scanned-id").parentElement.style.opacity = 0.5;
	find("button#submit").disabled = true;
	find("button#submit").style.opacity = 0.5;
}

find("button#submit").addEventListener("click", async () => {
	if (imageInput.files.length === 0) {
		alert("Please scan the barcode first.");
		return;
	} else {
		const fd = new FormData();
		fd.set("file", imageInput.files[0]);

		const scannedID = await (await fetch(window.location.href + "submit", {
			method: "POST",
			body: fd
		})).text();
		find("#scanned-id").textContent = scannedID;
	}
});
