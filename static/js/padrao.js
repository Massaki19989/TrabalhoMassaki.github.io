let abrirMenu = document.querySelector('.abrir-menu')
let fecharMenu = document.querySelector('.button-aside')

let abrir = document.querySelectorAll('.abrir')

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

for(let i = 0; i < abrir.length; i++){
    abrir[i].addEventListener('click', function(){
        let abr = this.getAttribute('abrir')
        let status = this.getAttribute('status')
        
        if(status == 1){
            this.querySelector('i').style.transform = 'rotate(0deg)'
            this.setAttribute('status', 0)
            document.querySelector('#'+abr).style.height = 0
        }else if(status == 0){
            this.querySelector('i').style.transform = 'rotate(180deg)'
            this.setAttribute('status', 1)       
            document.querySelector('#'+abr).style.height = 'auto'
        }
    })
}