function searchSection() {

    let input = document
        .getElementById("searchInput")
        .value
        .toLowerCase();

    let section = document.getElementById(input);

    if(section){
        section.scrollIntoView({
            behavior: "smooth"
        });
    }
    else{
        alert("Section not found!");
    }
}