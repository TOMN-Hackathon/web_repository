/** @type {HTMLInputElement} */
const input = document.getElementById("input");
if (!input) throw new Error("Input element not found");

input.addEventListener("keyup", (e) => {
  if (e.key === "Enter") input.value = "";
});
