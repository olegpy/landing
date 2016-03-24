$(document).ready(function() {
    // add class active on menu    
    $('.navbar-nav a').on('click', function() {
        $('.navbar-nav li').removeClass('active');
        $(this).parent().addClass('active');
    });
    // search
    $('.search_btn').on('click', function(e) {
        e.preventDefault();
        if ($(window).width() > 767) {
            if ($('.search_input').hasClass('show')) {
                $('.search_input.show').attr('style', 'width: 0; padding: 0');
                setTimeout(function() {
                    $('.search_input').removeClass('show');
                }, 200);
            } else {
                $('.search_input').addClass('show').focus().attr('style', 'width: 200px');
            }
        }
    });
    $(document).click(function(e) {
        if ($(e.target).closest(".search_btn").length || $(e.target).closest(".search_input").length) return;
        $('.search_input.show').attr('style', 'width: 0; padding: 0');
        setTimeout(function() {
            $('.search_input').removeClass('show');
        }, 200);
        e.stopPropagation();
    });
    // activate plugin selectpicker
    $('.selectpicker').selectpicker({
        liveSearch: true,
        maxOptions: 1
    });
    // form submission
    $(document).on('click', '.submit', function(e) {
        e.preventDefault();
        var form = $(this).parent('form');
        $.ajax({
            url: '../contact_me.php',
            type: 'POST',
            data: {
                form: $(this).parent('form').serialize()
            },
            dataType: 'json',
            beforeSend: function() {
                form.find('.form-control').removeClass('error');
                form.find('.error-text').remove();

                var email = form.find('.email');
                var textarea = form.find('textarea').val();

                if (!email.val() || !isValidEmailAddress(email.val())) {
                    email.addClass('error').parent().append('<p class="error-text">Please fill Email</p>');
                    return false;
                }
            },
            success: function(response) {
                if (response.status == 'success') {
                    form[0].reset();
                    alert('Thanks for order ');
                }
            }
        });
    });

    $('a[href^="#"], a[href^="."]').not(".carousel-control").click(function() {
        var scroll_el = $(this).attr('href');
        if ($(scroll_el).length != 0) {
            $('html, body').animate({ scrollTop: $(scroll_el).offset().top }, 500);
        }
        return false;
    });

});

// validation email adress
function isValidEmailAddress(emailAddress) {
    var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
    return pattern.test(emailAddress);
}
