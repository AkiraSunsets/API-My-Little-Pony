async function puxar_api(){
    await axios.get ("http://127.0.0.1:8001/api/v1/mlp/").then((response) => {
        const mlp = response.data;
        const container = document.getElementById("mlp-container")
        mlp.forEach(element => {
            const mlpDiv = document.createElement("div");
            mlpDiv.classList.add("mlp");
            mlpDiv.innerHTML = `
            <h2>${element.nome}</h2>
            <h2>${element.habilidades}</h2>
            <h2>${element.tipo}</h2>
            <h2>${element.cor}</h2>
            <h2>${element.personalidade}</h2>
            `
            container.append(mlpDiv);
        });
    })
}

puxar_api()