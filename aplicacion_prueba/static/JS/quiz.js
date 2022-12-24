const contents = document.getElementById("forms_questions");
const forms_questions = document.getElementById("forms");
const crf_tokens = document.getElementsByName("csrfmiddlewaretoken");
const url = window.location.href;

$.ajax({
    type: "GET",
    url: `${url}/data/`,
    dataType: "json",
    success:  (response) => {
      const data = response.data;
      let preguntas = ''
      data.forEach(element => {
        for (let [question, answers] of Object.entries(element)) {
          preguntas += `<h3>${question}</h3>`;
          for (const response of answers) {
            preguntas += `<li style="display:block;"><label for="${question}">
            <input type="radio" name="${question}" id="${question}-${response}" class="answers" value="${response}"/>
            ${response}  
            </label></li>`;
          }
        }
        contents.innerHTML = preguntas
      });
    },
    error:  (data) => {
      console.error(data);}
      
})


const DataSave = () => {
  const answer = [...document.getElementsByClassName("answers")];
  const data = {};
  data["csrfmiddlewaretoken"] = crf_tokens[0].value;
  answer.forEach((element) => {
    if (element.checked) {
      data[element.name] = element.value;
    } else {
      if (!data[element.name]) {
        data[element.name] = null;
      }
    }
  });

  $.ajax({
    type: "POST",
    url: `${url}/save/`,
    data: data,
    success: function (response) {
      const result = response.result
      contents.classList('not-visible');
      console.log(result);
      
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
