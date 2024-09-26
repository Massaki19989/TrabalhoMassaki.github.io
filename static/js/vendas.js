let adicionar = document.getElementById('adicionar')

adicionar.addEventListener('click', function(){
    document.querySelector('.produto').innerHTML+= `
        <div class="produto">
            <input type="number" name="quantidade[]" placeholder="Quantidade">
            <input type="text" name="nome[]" placeholder="Nome do Produto">
        </div><!--produto-->
    `
})