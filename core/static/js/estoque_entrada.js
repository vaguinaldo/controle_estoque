$(document).ready(function() {
  // Insere classe no primeiro item de produto
  $('#id_estoque-0-produto').addClass('clProduto');
  $('#id_estoque-0-quantidade').addClass('clQuantidade');
  // Desabilita o primeiro campo 'Saldo'
  $('#id_estoque-0-saldo').prop('type', 'hidden')
  // Cria um span para mostrar o saldo na tela.
  $('label[for="id_estoque-0-saldo"]').append('<span id="id_estoque-0-saldo-span" class="lead" style="padding-left: 10px;"></span>')
  // Cria um campo com o estoque inicial.
  $('label[for="id_estoque-0-saldo"]').append('<input id="id_estoque-0-inicial" class="form-control" type="hidden" />')
  // Select2
  $('.clProduto').select2()
});
