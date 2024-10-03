let item = document.querySelectorAll('.delete')

item.forEach(item=>{
    item.addEventListener('click', function(){
        document.location = 'deletar/'+this.getAttribute('deletar')
    })
})