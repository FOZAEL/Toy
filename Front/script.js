
const myform = document.getElementById('myform');
const url = "http://localhost:5000/hello/"


myform.addEventListener('submit', (e) => {
    e.preventDefault();
    url2 =url+myform.elements["input2"].value
    fetch(url2, {
        method: 'GET',
    }).then(function (response) {
        return response.json();
    }).then(function (json) {
        document.getElementById("APImassage").innerHTML = json.massage;
    })
});
