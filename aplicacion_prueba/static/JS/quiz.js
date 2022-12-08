const form = document.getElementById("forms_questions");
const li = document.getElementById("respustas");
const url = window.location.href;
const consumir_json = async () => {
  try {
    const response = await fetch(`${url}/data/`);
    const datos = await response.json();
    let preguntas = "";
    datos.data.forEach((element) => {
      for (let [question, answers] of Object.entries(element)) {
        preguntas += `
        <h3>${question}</h3>
        `;
        for (const iterator of answers) {
          preguntas += `<li style="display:block;"><label for="${question}">
          <input type="radio" name="answers" id="${question}"/>
          ${iterator}  
          </label></li>`;
        }
      }
    });
    form.innerHTML = preguntas;
  } catch (error) {
    console.log(error);
  }
};
window.addEventListener("load", async () => {
  await consumir_json();
});
