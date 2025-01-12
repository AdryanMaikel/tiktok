const sectionBaixados = document.getElementById("baixados");
const sectionEditados = document.getElementById("editados");
const sectionPostados = document.getElementById("postados");

function createCardVideo({ id, link, descricao, estado}) {
    const div = document.createElement("div");
    div.className = "card";

    const buttonLink = document.createElement("button");
    buttonLink.value = link;
    buttonLink.innerText = link;
    buttonLink.onclick = () => window.open(link);
    // buttonLink.disabled = true;
    div.appendChild(buttonLink);
    
    const textareaDescricao = document.createElement("textarea");
    textareaDescricao.innerText = descricao;
    textareaDescricao.disabled = true;
    div.appendChild(textareaDescricao);

    const divButtons = document.createElement("div");
    divButtons.className = "buttons";

    const buttonDelete = document.createElement("button");
    buttonDelete.setAttribute("video-id", id);
    buttonDelete.innerText = "DELETAR"
    buttonDelete.onclick = deleteVideo;
    divButtons.appendChild(buttonDelete);

    const buttonAddBaixado = document.createElement("button");
    buttonAddBaixado.innerHTML = "Mover p/ Baixados";
    buttonAddBaixado.onclick = () => moveVideoBy(id, "baixado");

    const buttonAddEditado = document.createElement("button");
    buttonAddEditado.innerHTML = "Mover p/ Editados";
    buttonAddEditado.onclick = () => moveVideoBy(id, "editado");

    const buttonAddPostado = document.createElement("button");
    buttonAddPostado.innerHTML = "Mover p/ Postados";
    buttonAddPostado.onclick = () => moveVideoBy(id, "postado");

    switch (estado) {
        case "baixado":
            divButtons.appendChild(buttonAddEditado);
            divButtons.appendChild(buttonAddPostado);
            div.appendChild(divButtons);
            sectionBaixados.appendChild(div);
            break;
        case "editado":
            divButtons.appendChild(buttonAddBaixado);
            divButtons.appendChild(buttonAddPostado);
            div.appendChild(divButtons);
            sectionEditados.appendChild(div);
            break;
        case "postado":
            divButtons.appendChild(buttonAddBaixado);
            divButtons.appendChild(buttonAddEditado);
            div.appendChild(divButtons);
            sectionPostados.appendChild(div);
            break;
        default:
            break;
    }
}

async function fetchVideos() {
    try {
        const response = await fetch("/videos");
        const videos = await response.json();
        sectionBaixados.innerHTML = "";
        sectionEditados.innerHTML = "";
        sectionPostados.innerHTML = "";
        videos.forEach(video => createCardVideo(video));
    } catch (error) {
        console.error("Erro ao buscar vídeos:", error);
    }
}

window.onload = async function() {
    await fetchVideos()
}

async function addVideo() {
    const link = document.getElementById("link").value;
    const descricao = document.getElementById("descricao").value;
    const estado = document.getElementById("estado").value;
    try {
        const response = await fetch("/videos", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ link, descricao, estado }),
        });
        if (response.ok) {
            alert("Vídeo adicionado com sucesso!");
            await fetchVideos();
        }
    } catch (error) {
        console.error("Erro ao adicionar vídeo:", error);
    }
}

async function moveVideoBy(id, estado) {
    try {
        const response = await fetch(`/videos/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ link, descricao, estado }),
        });
        if (!response.ok) {
            const error = await response.json();
            alert("Erro: " + error.error);
        } else {
            alert("Vídeo movido com sucesso!");
            await fetchVideos();
        }
    } catch (error) {
        console.error("Erro ao adicionar vídeo:", error);
    }
}

async function deleteVideo(event) {
    const videoId = event.target.getAttribute("video-id");
    try {
        const response = await fetch(`/videos/${videoId}`, {
            method: "DELETE",
        });
        const result = await response.json();
        if (!response.ok) {
            alert("Erro: " + result.error);
        } else {
            alert(result.message);
            fetchVideos();
        }
    } catch (error) {
        console.error("Erro ao deletar vídeo:", error);
    }
}