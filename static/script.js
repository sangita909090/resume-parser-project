function upload(){
    let file = document.getElementById("resume").files[0];
    let data = new FormData();
    data.append("resume", file);

    fetch("/upload",{
        method:"POST",
        body:data
    })
    .then(res=>res.json())
    .then(result=>{
        document.getElementById("output").innerText =
        JSON.stringify(result,null,2);
    });
}
