const title_input = document.querySelector("input[name=title]")
const slug_input = document.querySelector("input[name=slug]")


const slugify = (val) => {
    return val.toString().toLowerCase().trim()
    .replace(/[\s\W-]+/g,'-')
}

title_input.addEventListener('keyup',(e)=>{
    slug_input.setAttribute('value', slugify(title_input.value))
});
