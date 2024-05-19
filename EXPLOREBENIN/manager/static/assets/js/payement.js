const transaction_sum = document.querySelector('div[id="amount"]');
const circuit_id = parseInt(document.getElementById('circuit_id').textContent, 10);

const texteTrans = transaction_sum.textContent;
const entier = parseInt(texteTrans, 10);

const monBouton = document.getElementById('payement-kkia');
var ADDRESS = window.location.origin;

document.addEventListener('DOMContentLoaded', function() {
  const monBouton = document.getElementById('payement-kkia');
  var ADDRESS = window.location.origin;

  monBouton.addEventListener('click', function() {
  openKkiapayWidget({
    amount:entier,
    position:"right",
    callback:ADDRESS + "/valid_reservation/"+circuit_id,
    data: "Payement réservation",
    theme:"#0095ff",
    sandbox:"true",
    key:"c276ddc0161c11efa236d9f517e0c841"
  }
  )
})});