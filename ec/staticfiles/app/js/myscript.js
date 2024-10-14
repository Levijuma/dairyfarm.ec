// Initialize Owl Carousel
$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 2,  // Fixed number of items for mobile view
            nav: false,
            autoplay: true,
        },
        600: {
            items: 4,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 6,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
});

// Handle plus cart button click
$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]; 
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            eml.innerText = data.quantity; 
            document.getElementById("amount").innerText = data.amount; 
            document.getElementById("totalamount").innerText = data.totalamount;
        }
    });
});

// Handle minus cart button click
$('.minus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]; 
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            eml.innerText = data.quantity; 
            document.getElementById("amount").innerText = data.amount; 
            document.getElementById("totalamount").innerText = data.totalamount;
        }
    });
});

// Handle remove cart button click
$('.remove-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this;
    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id: id
        },
        success: function(data) {
            document.getElementById("amount").innerText = data.amount; 
            document.getElementById("totalamount").innerText = data.totalamount;
            eml.parentNode.parentNode.parentNode.parentNode.remove(); 
        }
    });
});

// Handle plus wishlist button click
$('.plus-wishlist').click(function() {
    var id = $(this).attr("pid").toString();
    $.ajax({
        type: "GET",
        url: "/pluswishlist",
        data: {
            prod_id: id
        },
        success: function(data) {
            // Redirect to product detail page
            window.location.href = `http://localhost:8000/product-detail/${id}`;
        }
    });
});

// Handle minus wishlist button click
$('.minus-wishlist').click(function() {
    var id = $(this).attr("pid").toString();
    $.ajax({
        type: "GET",
        url: "/minuswishlist",
        data: {
            prod_id: id
        },
        success: function(data) {
            // Redirect to product detail page
            window.location.href = `http://localhost:8000/product-detail/${id}`;
        }
    });
});
