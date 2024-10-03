let abrirMenu = document.querySelector('.abrir-menu')
let fecharMenu = document.querySelector('.button-aside')

fecharMenu.addEventListener('click', function(){
    document.querySelector('aside').style.width = '40px'
    document.querySelector('aside').style.textAlign = 'center'
    this.style.display = 'none'
    document.querySelector('aside ul').style.opacity = '0'
    abrirMenu.style.display = 'inline-block'
})

abrirMenu.addEventListener('click', function(){
    document.querySelector('aside').style.width = '400px'
    document.querySelector('aside').style.textAlign = 'right'
    this.style.display = 'none'
    document.querySelector('aside ul').style.opacity = '1'
    fecharMenu.style.display = 'inline-block'
})