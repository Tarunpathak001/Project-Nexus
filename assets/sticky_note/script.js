var random_margin = ["-5px", "1px", "5px", "10px", "7px"];
var random_colors = ["#c2ff3d","#ff3de8","#3dc2ff","#04e022","#bc83e6","#ebb328"];
var random_degree = ["rotate(3deg)", "rotate(1deg)", "rotate(-1deg)", "rotate(-3deg)", "rotate(-5deg)", "rotate(-8deg)"];
var index = 0;

window.onload = document.querySelector("#user_input").select();

document.querySelector("#add_note").addEventListener("click", () => {
  document.querySelector("#modal").style.display = "block";
});

document.querySelector("#hide").addEventListener("click", () => {
  document.querySelector("#modal").style.display = "none";
});

document.querySelector("#user_input").addEventListener('keydown', (event) => {
  if(event.key === 'Enter'){
    event.preventDefault(); 
    document.querySelector("#user_input").value += "\n"; 
  }
});

document.querySelector("#finish_button").addEventListener('click', () => {
  const text = document.querySelector("#user_input");
  createStickyNote(text.value);
  text.value = ""; 
});

createStickyNote = (text) => {
  let note = document.createElement("div");
  let details = document.createElement("div");
  let noteText = document.createElement("h1");

  note.className = "note";
  details.className = "details";
  noteText.textContent = text;

  details.appendChild(noteText);
  note.appendChild(details);

  if(index > random_colors.length - 1)
    index = 0;

  note.setAttribute("style", `background-color:${random_colors[index++]}; margin: ${random_margin[Math.floor(Math.random() * random_margin.length)]};transform: ${random_degree[Math.floor(Math.random() * random_degree.length)]};`);
// note.setAttribute("style",'background-color:blue');
  let isEditing = false;
  let editText;

  note.addEventListener("click", (e) => {
    if (!isEditing) {
      e.preventDefault();
      editText = prompt("Enter new text:");
      if (editText) {
        noteText.textContent = editText;
      }
    }
    isEditing = true;
  });

  note.addEventListener("dblclick", (e) => {
    e.preventDefault();
    let confirmDelete = confirm("Are you sure you want to delete this note?");
    if (confirmDelete) {
      note.remove();
    }
    isEditing = false;
  });

  document.querySelector("#all_notes").appendChild(note);
}