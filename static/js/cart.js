
// const updateBtns = document.getElementsByClassName('update-cart');

// updateBtns.forEach((btn) => {
//   btn.addEventListener('click', (event) => {
//     event.preventDefault();
//     const productId = btn.dataset.product;
//     const action = btn.dataset.action;
//     console.log(`productId: ${productId}, Action: ${action}`);

//     console.log('USER:', user);
//     if (user === 'AnonymouseUser') {
//       console.log('User is not authenticated');
//     } else {
//       handleUpdateOrder(productId, action);
//     }
//   });
// });

// function handleUpdateOrder(productId, action) {
//   console.log('User is authenticated, sending data...');

//   const url = '/update_item';
//   fetch(url, {
//     method: 'POST',
//     headers: {
//       'Content-type': 'application/json',
//       'X-CSRFToken': csrftoken,
//     },
//     body: JSON.stringify({ productId, action }),
//   })
//    .then((response) => response.json())
//    .then((data) => console.log('Data:', data))
//    .catch((error) => console.error('Error:', error));
// }



// sourcery skip: avoid-using-var
var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			console.log('User is not authenticated')
			
		}else{
			updateUserOrder(productId, action)
		}
	})
}

function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    console.log('Data:', data)
		});
}
// -----------------------------------------------------------------------------

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
  