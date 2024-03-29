const inputValue = document.querySelector("#search");
const searchButton = document.querySelector(".searchButton");
const nameContainer = document.querySelector(".main__profile-name");
const unContainer = document.querySelector(".main__profile-username");
const reposContainer = document.querySelector(".main__profile-repos");
const urlContainer = document.querySelector(".main__profile-url");

const client_id = "Iv1.849bb535c300ab42"
const client_secret = "dd22626007a64ddd1c45421fb260744e01c53f1d"

const Users = async (user) => {
    const api = await fetch('https://api.github.com/users/${user}?client_id={client_id}&client_secret=${client_secret}');

    const data = await api.json();
    return { data }
};

const Display = () => {
    Users(inputValue.value).then((res)) => {


     nameContainer.innerHTML = 'Name: <span class="main__profile-value">${res.data.name}</span>';

     unContainer.innerHTML = 'Username: <span class="main__profile-value">${res.data.login}</span>';

     nameContainer.innerHTML = 'Repos: <span class="main__profile-value">${res.data.public_repos}</span>';

     nameContainer.innerHTML = 'URL: <span class="main__profile-value">${res.data.html_url}</span>';
    })
};

searchButton.addEventListener("click",() => {
    Display();
})