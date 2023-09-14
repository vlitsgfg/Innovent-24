const find = (sel, parent = document) => parent.querySelector(sel);
const findAll = (sel, parent = document) => parent.querySelectorAll(sel);

find("button#submit").addEventListener("click", () => {
	if () {};

	window.location.href = window.location.origin + "/get_attendance?id="
});
