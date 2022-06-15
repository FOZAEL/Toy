// const myform = document.getElementById('myform');

// myform.addEventListener('submit', (e) => {
//     e.preventDefault();

//     const myform = new myform(this);

//     fetch('http://localhost:5000/hello/', {
//         method: 'POST',
//         body: myform
//     }).then(function (response) {
//         return response.text();
//     }).then(function (text) {
//         console.log(text);
//     })
// });


const request = new XMLHttpRequest();
const url = 'http://localhost:5000/hello/dfdh';
request.open('GET', url, true);
request.send();

request.onload = (e) => {
    alert(request.response);
}


// let response = fetch("http://127.0.0.1:5000/hello/dfdh");
// console.log(response);