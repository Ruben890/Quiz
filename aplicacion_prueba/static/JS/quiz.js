const contents = document.getElementById("forms_questions");
const forms_questions = document.getElementById("forms");
const crf_tokens = document.getElementsByName("csrfmiddlewaretoken");
const url = window.location.href;
const container = document.getElementById('constens');

$.ajax({
    type: "GET",
    url: `${url}/data/`,
    success:  (response) => {
      const data = response.data;
      const time =  response.time
      
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
    success:  (response) => {
      const result = response.Resuls
      forms_questions.classList.add('d-none');
      console.log(result);
      result.forEach(element => {
        const div = document.createElement('div');
        for (const [question, response] of Object.entries(element)){
      
          div.innerHTML = question
          const cls = ['container', 'tex-light', 'fs-4', 'm-3', 'p-1', 'rounded-1']
          div.classList.add(...cls);
          container.appendChild(div);

          if(response['corect_answer'] === null){
            const p = document.createElement('p');
            p.classList.add('fs-5', 'text-white');
            div.appendChild(p);
            p.innerHTML += 'no es la respuesta correcta';
            div.classList.add('bg-danger');
          }else{
            const corect_answer = response['corect_answer']
            const p = document.createElement('p');
            p.classList.add('fs-5', 'text-white');
            div.appendChild(p);
            p.innerHTML = corect_answer;
            div.classList.add('bg-success');
            
          }
        }
      });      
    },
    error:  (error)=> {
      console.error(error);
    },
  });
};

forms_questions.addEventListener("submit", (e) => {
  e.preventDefault();
  DataSave();
});
