const find = (sel, parent = document) => parent.querySelector(sel);
const findAll = (sel, parent = document) => parent.querySelectorAll(sel);

const IDInput = find("#emp-id");

find("button#submit").addEventListener("click", () => {
	if (IDInput.value === "") {
		alert("Enter ID first.");
		return;
	}

	window.location.href = window.location.origin + "/emp/get_attendance?id=" + IDInput.value;
});
