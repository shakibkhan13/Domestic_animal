var updateBtns = document.getElementsByClassName('update-cart')

for(i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var ProductId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',ProductId , 'Action:',action)


        console.log('USER:', user)
        if(user == 'AnonymouseUser'){
            console.log('User is not authenticated')
        }else{
            console.log('User is authenticated, sending data ...')
        }
    })
}

// document.addEventListener('DOMContentLoaded', function() {
//     var updateBtns = document.querySelectorAll('.update-cart');
  
//     updateBtns.forEach(function(btn) {
//       btn.addEventListener('click', function(event) {
//         event.preventDefault(); // Prevent default form submission
        
//         var productId = this.getAttribute('data-product');
//         var action = this.getAttribute('data-action');
//         console.log('productId:', productId, 'Action:', action);

//         console.log('USER:', user)
//         if(user ==='AnonymouseUser'){
//             console.log('Not logged in')
//         }else{
//             console.log('User is logged in, sending data ...')
//         }

//       });
//     });
//   });
  