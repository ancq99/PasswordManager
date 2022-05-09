# -*- coding: utf-8 -*-

main = """
<div style="display:none" id="ajax_script"></div>
  <div class="container-fluid bg-dark fixed-top p-2" style="color: rgba(255,255,255,.5)">
    <div class="row ">
      <div class="col-sm-1">
        <img src="../resources/lock.svg" alt="logo" style="width:40px;">
      </div>
      
      <div class="col-sm-9 text-left " style="color: #fff; font-size: 80%; line-height: 1">
        <span class="align-middle ml-3" id="user_name"> Zalogowany użytkownik: </span>
        <br>
        <span class="align-middle ml-3" id="user_ip"> Adres_IP: </span>
      </div>
      <div class="col-sm-1 pl-0">
        <button class="btn btn-success float-right" type="button" id="changePassword">Zmień hasło</button>
      </div>
      <div class="col-sm-1 pr-0">
        <button class="btn btn-success float-middle" type="button" onclick="location.reload(true); document.cookie = 'token=';">Wyloguj</button>
      </div>
    </div>
  </div>
  
  <div class="conteiner" id="respons" style="width: 90%; height: 100%">
    <div class="w-100 mt-2 pt-4 text-left">
      <h3>Twoje hasła:</h3>
    </div>
    <div class="table-wrapper-scroll-y my-custom-scrollbar">
    <table class="table table-hover table-striped text-center " >
      <thead class="thead-dark">
        <tr>
          <th>#</th>
          <th>Strona</th>
          <th>Hasło</th>
          <th>Komu udostępnione [email]</th>
          <th>
            <button class="btn btn-success float-middle btn-block btn-sm" type="button" data-toggle="modal" data-target="#addModal">Dodaj</button>
          </th>
        </tr>
      </thead>
      <tbody id="user_data">
        {}
      </tbody>
    </table>
    </div>
    <div class="w-100 mt-4 pt-4 text-left" style="border-top: 4px solid #dee2e6">
      <h3>Udostępnione hasła:</h3>
    </div>
     <div class="table-wrapper-scroll-y my-custom-scrollbar" style="max-height: 35%">
    <table class="table  table-hover table-striped text-center" >
      <thead class="thead-dark">
        <tr>
          <th>#</th>
          <th>Właściciel</th>
          <th>Strona</th>
          <th>Hasło</th>
        </tr>
      </thead>
      <tbody id="share_user">
        {}
      </tbody>
    </table>
  </div>
</div>

<iframe name="dummyframe" id="dummyframe" style="display: none"></iframe>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Edytuj dane:</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
         <form  method="POST" id="updateFrom" target="dummyframe"> 
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text label">Zastosowanie</span>
            </div>
            <input type="text" class="form-control" placeholder="Username" id="modal_zast">
          </div>

          <div class="input-group mb-3">
            <div class="input-group-append">
              <span class="input-group-text label">Hasło</span>
            </div>
            <input type="password" class="form-control" placeholder="Hasło" id="modal_pass">
            <div class="input-group-append">
            <span class="input-group-text">
                <i class="fa fa-eye-slash"></i>
            </span>
            </div>
          </div>
          
          <div class="input-group mb-3">
            <div class="input-group-append">
              <span class="input-group-text label">Potwierdź hasło</span>
            </div>
            <input type="password" class="form-control" placeholder="Potwierdź hasło" id="modal_confirm">
            <div class="input-group-append">
            <span class="input-group-text">
                <i class="fa fa-eye-slash"></i>
            </span>
            </div>
          </div>

           <div class="form-group mb-3 text-left">
              <label for="comment">Komu udostępnione:</label>
              <textarea class="form-control" rows="5" placeholder="Udostępnione" id="modal_shared" data-content="Każdy mail powinnien być w nowym wierszu"></textarea>
            </div> 

        </form> 
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" id="saveBtn">Save changes</button>
      </div>
    </div>
  </div>
</div>

<!-- Pass Modal -->
<div class="modal fade" id="changePasswordModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Zmień hasło:</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
         <form  method="POST" id="updateFrom" target="dummyframe"> 
          
          <div class="input-group mb-3">
            <div class="input-group-append">
              <span class="input-group-text label">Stare hasło</span>
            </div>
            <input type="password" class="form-control" placeholder="Stare hasło" id="modalPassOld"  autocomplete="new-password" value="">
            
          </div>
          
          <div class="input-group mb-3">
            <div class="input-group-append">
              <span class="input-group-text label">Nowe hasło</span>
            </div>
            <input type="password" class="form-control" placeholder="Nowe hasło" id="modalPass">
            <div class="input-group-append">
            <span class="input-group-text">
                <i class="fa fa-eye-slash"></i>
            </span>
            </div>
          </div>

           <div class="input-group mb-3">
            <div class="input-group-append">
              <span class="input-group-text label">Potwierdź hasło</span>
            </div>
            <input type="password" class="form-control" placeholder="Potwierdź nowe hasło" id="modalPassConfirm">
            <div class="input-group-append">
            <span class="input-group-text">
                <i class="fa fa-eye-slash"></i>
            </span>
            </div>
          </div> 

        </form> 
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" id="changePassBtn">Save changes</button>
      </div>
    </div>
  </div>
</div>

<!-- Modal2 -->
<div class="modal fade" id="addModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Dodaj nowe dane:</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      
      <div class="modal-body">
         <form  method="POST" id="addFrom" target="dummyframe">
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text label">Zastosowanie</span>
            </div>
            <input type="text" class="form-control" placeholder="Username" id="modal_zast1" name="zast">
          </div>

          <div class="input-group mb-3">
            <div class="input-group-append">
              <span class="input-group-text label">Hasło</span>
            </div>
            <input type="password" class="form-control" placeholder="Hasło" id="modal_pass1" name="pass">
            <div class="input-group-append">
            <span class="input-group-text">
                <i class="fa fa-eye-slash"></i>
            </span>
            </div>
          </div>

          <div class="input-group mb-3">
            <div class="input-group-append">
              <span class="input-group-text label">Potwierdź hasło</span>
            </div>
            <input type="password" class="form-control" placeholder="Potwierdź hasło" id="modal_confirm1" name="confirmPass">
            <div class="input-group-append">
            <span class="input-group-text">
                <i class="fa fa-eye-slash"></i>
            </span>
            </div>
          </div>

           <div class="form-group mb-3">
              <label for="comment">Komu udostępnione:</label>
              <textarea class="form-control" rows="5" placeholder="Każdy adres w nowej linii" id="modal_shared1" name="share" data-content="Każdy mail powinnien być w nowym wierszu"></textarea>
            </div> 

        </form> 
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Zamknij</button>
        <button type="button" class="btn btn-primary" id="addBtn">Dodaj</button>
      </div>
    </div>
  </div>
</div>
"""

error = """
<!DOCTYPE html>
<html lang="pl">
<head>
  <title>Password Manager Project</title>
  <link rel="icon" type="image/x-icon" href="../resources/favicon.ico">
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>
  <link href="../css/style.css" rel="stylesheet">
  <script src="../js/PassRequirements.js"></script>
  <script src="../js/jquery.entropy.js"></script>
  <script src="../js/script.js"> </script>
</head>
<body class="text-center">
    <div class="container">
    <img class="mb-4" src="../resources/lock.svg" alt="" width="80" height="80"><br>
    
    {}
    </div>


</body>
</html>

"""

passReset = """
<!DOCTYPE html>
<html lang="pl">
<head>
  <title>Password Manager Project</title>
  <link rel="icon" type="image/x-icon" href="../resources/favicon.ico">
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>
  
  <link href="../css/style.css" rel="stylesheet">
  <script src="../js/PassRequirements.js"></script>
  <script src="../js/jquery.entropy.js"></script>
  <script > 

function validateForm() {
  var confirm = $("#inputConfirmPassword")
  var pass = $("#inputPassword")

  var passPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,}$/;

  if(!passPattern.test(pass.val()) || !passPattern.test(confirm.val()) || confirm.val() != pass.val()){
    confirm.addClass("not-valid")
    pass.addClass("not-valid")

    $("#answer").html("Hasło nie spełnia wymagań")
    return false
  }

  return true
} 

$( document ).ready(function() {
  $('#inputPassword').PassRequirements({
    rules: {
      minlength: {
        text: "Conajmniej minLength znaków",
        minLength: 10,
      },

      containSpecialChars: {
        text: "Conajmneij minLength znak specjalny [@$!%*?&]",
        minLength: 1,
        regex: new RegExp('([^@$!%*?&])', 'g')
      },

      containLowercase: {
        text: "Conajmneij minLength mała litera",
        minLength: 1,
        regex: new RegExp('[^a-z]', 'g')
      },

      containUppercase: {
        text: "Conajmneij minLength duża litera",
        minLength: 1,
        regex: new RegExp('[^A-Z]', 'g')
      },

      containNumbers: {
        text: "Conajmneij minLength cyfra",
        minLength: 1,
        regex: new RegExp('[^0-9]', 'g')
      }
    }
  });
    $('#inputPassword').passwordEntropy();
  $(document).on('click', '.input-group-text > i', function(a){
  input = $(this.parentElement.parentElement.previousElementSibling)
  icon = $(this)

  if(input.attr("type") == "text"){
    input.attr('type', 'password');
    icon.addClass( "fa-eye-slash" );
    icon.removeClass( "fa-eye" );
  }else if(input.attr("type") == "password"){
    input.attr('type', 'text');
    icon.removeClass( "fa-eye-slash" );
    icon.addClass( "fa-eye" );
}

});

  $('#resetPass').on('click', function() {
    if (validateForm()){
    var $this = $(this);
    var loadingText = '<i class="fa fa-circle-o-notch fa-spin"></i> Przetwarzanie...';
    if ($(this).html() !== loadingText) {
      $this.data('original-text', $(this).html());
      $this.html(loadingText);
    }
      var pass = $("#inputPassword").val()
      var token = window.location.href.split("?")[1].split("=")[1]

      $.ajax({
            url: "/python/reset.py",
            type: "get",
            datatype:"json",
            data: {'pass': pass, 'token' : token},
            success: function(response){
                $("#python").html(response.html);
            }
        });

      setTimeout(function() {
        $this.html($this.data('original-text'));
      }, 20000);

    } else {
      alert("Błędne dane")
    }
    });


});
  </script>
</head>
<body class="text-center" id="python">

    <form class="form-signin" id="loginForm">
      <img class="mb-4" src="../resources/lock.svg" alt="" width="80" height="80">
      <h1 class="h3 mb-3 font-weight-normal">Zmień hasło: </h1>
      <div class = "input-group">
      <label for="inputEmail" class="sr-only">Hasło</label>
      <input type="password" id="inputPassword" class="form-control" placeholder="Nowe hasło" name="password" style="margin-bottom: 10px;border-top-left-radius: 5px !important;border-top-right-radius: 5px !important;border-bottom-right-radius: 0 !important; border-bottom-left-radius: 0 !important; margin: 0; margin-bottom: -1px">
      <div class="input-group-append">
            <span class="input-group-text">
                <i class="fa fa-eye-slash"></i>
            </span>
            </div>
          </div>
      <label for="inputConfirmPassword" class="sr-only">Potwierdź hasło</label>
      <input type="password" id="inputConfirmPassword" class="form-control" placeholder="Potiwerdź nowe hasło" name="password">
      
	   <button type="button" class="btn btn-primary btn-block btn-large" id="resetPass" >Zmień hasło</button>

    </form>
  
    <span id="answer">
    </span>
	</body>
</html>

"""
