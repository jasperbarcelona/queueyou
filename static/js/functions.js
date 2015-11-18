var msisdn = '';
var stop = false;

function generate_svc(){
  msisdn = $('#login-msisdn').val();
  $.post('/user/authenticate',{
        msisdn:msisdn,
    },
    function(data){
      if(data['error']){
        if (data['error'] == 401){
          $('#login-error').html(data['message']);
        }
        else if (data['error'] == 404){
         $('#login-error').html('Mobile number is required.');
        }
      }
      else{
        $('#main-login').html(data);
      }
    });
}

function login_user(){
  svc = $('#svc').val();
  $.post('/user/login',{
        svc:svc,
        msisdn:msisdn
    },
    function(data){
      if(data['error']){
        if (data['error'] == 401){
          $('#confirm-error').html(data['message']);
        }
        else if (data['error'] == 404){
         $('#confirm-error').html('Please key in your security verification code.');
        }
      }
      else{
        window.location.replace('/')
      }
    });
}

function poll(){
   setTimeout(function(){
      $.post('/data/update',
      function(data){
        if (data['queue_no'] != null){
          $('#now-serving').html(data['now_serving']);
          $('#queue-number').html(data['queue_no']);
          $('#client-name').html(data['client_name']);
          $('#hours').html(data['hours']);
          $('#minutes').html(data['minutes']);
          $('#no-transaction').hide();
          $('#loading').hide();
          $('#places-btn-cover').hide();
          poll()
        }
        else{
          $('#no-transaction').show();
          $('#loading').hide();
          $('#places-btn-cover').show();
        }
        console.log('done');
      });
  }, 2000);
};