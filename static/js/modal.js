function showModal(name,desc,url, loc,cat){
    $("#img-label").text(name)
    $("#myModal").modal("show")
    $(".modal-title").text(name)
    $(".mod-img").attr("src",url)
    $("#img-desc").text(desc)
    $("#img-loc").text("Location: " + loc)
    $("#img-cat").text("Category: " + cat)
    $("#copy-url").val(window.location.origin + url)
}

function copy(){
    $("#copy-url").select()
    document.execCommand('copy');
    alert("Link has been copied")
}