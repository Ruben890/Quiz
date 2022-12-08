const contents = document.getElementById("forms_questions");
const forms_questions = document.getElementById("forms");
const crf_tokens = document.getElementsByName("csrfmiddlewaretoken");
const answer = [...document.getElementsByClassName("answers")];

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
          <input type="radio" name="answers" id="${question}" class="answers" value="${iterator}"/>
          ${iterator}  
          </label></li>`;
        }
      }
    });
    contents.innerHTML = preguntas;
  } catch (error) {
    console.log(error);
  }
};
window.addEventListener("load", async () => {
  await consumir_json();
});

const DataSave = () => {
  const data = {};
  data["csrfmiddlewaretoken"] = crf_tokens[0].value;
  answer.forEach((answers) => {
    if (answers.checked) {
      data[answers.name] = answers.value;
    } else {
      if (!data[answers.name]) {
        data[answers.name] = null;
      }
    }
  });

  $.ajax({
    type: "POST",
    url: `$${url}/save/`,
    data: data,
    success: function (response) {
      console.log(response);
    },
    error: function (error) {
      console.error(error);
    },
  });
};


forms_questions.addEventListener("submit", (e) => {
  e.preventDefault();
  DataSave();
});
