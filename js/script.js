zast = pass = share = ""

function validateForm() {
  var email = $("#inputEmail")
  var pass = $("#inputPassword")

  var emailPattern = /^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i;
  var passPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,}$/;

  if (!passPattern.test(pass.val()) || !emailPattern.test(email.val())) {
    email.addClass("not-valid")
    pass.addClass("not-valid")
    $("#answer").html("Błędne dane logowania")
    return false
  }

  return true
}

function validateRegisterFrom() {
  var name = $("#name")
  var surname = $("#surname")
  var email = $("#regEmail")
  var pass = $("#regPassword")
  var confirm = $("#inputRegPassword")
  var questionSelect = $('#questionSelect')
  var question = $('#question')

  var emailPattern = /^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i;
  var passPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,}$/;

  var forbidenPattern = /['"\\!@#$%^&*()\-+=\[\]{}|<>?/]/g;

  if (forbidenPattern.test(name.val())) {
    name.addClass("not-valid")
    return false
  } else {
    name.removeClass("not-valid")
  }

  if (forbidenPattern.test(surname.val())) {
    surname.addClass("not-valid")
    return false
  } else {
    surname.removeClass("not-valid")
  }

  if (!emailPattern.test(email.val())) {
    email.addClass("not-valid")
    return false
  } else {
    email.removeClass("not-valid")
  }

  if (!passPattern.test(pass.val())) {
    pass.addClass("not-valid")
    return false
  } else {
    pass.removeClass("not-valid")
  }

  if (confirm.val() != pass.val()) {
    confirm.addClass("not-valid")
    return false
  } else {
    confirm.removeClass("not-valid")
  }

  if (parseInt(questionSelect.val()) == 0 || !question.val() || forbidenPattern.test(question.val())) {
    questionSelect.addClass("not-valid")
    question.addClass("not-valid")
    return false

  } else {
    questionSelect.removeClass("not-valid")
    question.removeClass("not-valid")
  }

  return true
}

function validateUpdateForm() {

  var zast = $("#modal_zast")
  var pass = $("#modal_pass")
  var confirm = $("#modal_confirm")
  var shared = $("#modal_shared")

  var passPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,}$/;
  var emailPattern = /^$|^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i;
  var forbidenPattern = /['"!@#$%^&*()+=\[\]{}|<>?]/g;

  if (forbidenPattern.test(zast.val())) {
    zast.addClass("not-valid")
    return false
  } else {
    zast.removeClass("not-valid")
  }

  if (!passPattern.test(pass.val())) {
    pass.addClass("not-valid")
    return false
  } else {
    pass.removeClass("not-valid")
  }

  if (confirm.val() != pass.val()) {
    confirm.addClass("not-valid")
    return false
  } else {
    confirm.removeClass("not-valid")
  }

  var test = false
  var emails = shared.val().split("\n")
  for (n in emails) {
    if (!emailPattern.test(emails[n])) {
      test = true;
      break;
    }
  }

  if (!test && !shared.val().includes(document.cookie.split("=")[1])) {
    shared.removeClass("not-valid")
  } else {
    shared.addClass("not-valid")
    return false
  }
  return true
}

function validateAddFrom() {

  var zast = $("#modal_zast1")
  var pass = $("#modal_pass1")
  var confirm = $("#modal_confirm1")
  var shared = $("#modal_shared1")

  var passPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,}$/;
  var emailPattern = /^$|^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i;
  var forbidenPattern = /['"!@#$%^&*()+=\[\]{}|<>?]/g;

  if (forbidenPattern.test(zast.val())) {
    zast.addClass("not-valid")
    return false
  } else {
    zast.removeClass("not-valid")
  }

  if (!passPattern.test(pass.val())) {
    pass.addClass("not-valid")
    return false
  } else {
    pass.removeClass("not-valid")
  }

  if (confirm.val() != pass.val()) {
    confirm.addClass("not-valid")
    return false
  } else {
    confirm.removeClass("not-valid")
  }

  var test = false
  var emails = shared.val().split("\n")
  for (n in emails) {
    if (!emailPattern.test(emails[n])) {
      test = true;
      break;
    }
  }

  if (!test && !shared.val().includes(document.cookie.split("=")[1])) {
    shared.removeClass("not-valid")
  } else {
    shared.addClass("not-valid")
    return false
  }
  return true
}

function validateChangePassFrom() {
  var oldPass = $("#modalPassOld")
  var newPass = $("#modalPass")
  var newConfirm = $("#modalPassConfirm")

  var passPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,}$/;

  if (!passPattern.test(oldPass.val())) {
    oldPass.addClass("not-valid")
    return false
  } else {
    oldPass.removeClass("not-valid")
  }

  if (!passPattern.test(newPass.val())) {
    newPass.addClass("not-valid")
    return false
  } else {
    newPass.removeClass("not-valid")
  }

  if (newConfirm.val() != newPass.val()) {
    newConfirm.addClass("not-valid")
    return false
  } else {
    newConfirm.removeClass("not-valid")
  }

  return true
}

$(document).ready(function() {
  $('#regPassword').PassRequirements({
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

  $('#regPassword').passwordEntropy();

  $('#registerBtn').on('click', function() {
    if (validateRegisterFrom()) {
      var $this = $(this);
      var loadingText = '<i class="fa fa-circle-o-notch fa-spin"></i> Przetwarzanie...';
      if ($(this).html() !== loadingText) {
        $this.data('original-text', $(this).html());
        $this.html(loadingText);
      }

      setTimeout(function() {
        $this.html($this.data('original-text'));
        $("#registerForm").submit()
      }, 2500);
    } else {
      alert("Błędne dane fomrularza")
    }
  });

  $(document).on('click', '#saveBtn', function() {

    if (validateUpdateForm()) {
      var $this = $(this);
      var loadingText = '<i class="fa fa-circle-o-notch fa-spin"></i> Przetwarzanie...';
      if ($(this).html() !== loadingText) {
        $this.data('original-text', $(this).html());
        $this.html(loadingText);
      }

      setTimeout(function() {
        var zast_new = $("#modal_zast").val()
        var pass_new = $("#modal_pass").val()
        var shared_new = $("#modal_shared").val()

        $.ajax({
          url: "/python/update.py",
          type: "post",
          datatype: "json",
          data: {
            'zast_new': zast_new,
            'pass_new': pass_new,
            'share_new': shared_new,
            'zast': zast,
            'pass': pass,
            'share': share
          },
          success: function(response) {
            $("#user_data").html(response.html);
            zast = pass = share = ""
          }
        });
      }, 500);
      setTimeout(function() {
        $this.html($this.data('original-text'));
        $("#exampleModal").modal('toggle');
      }, 2500);
    } else {
      alert("Błędne dane fomrularza")
    }
  });

  $('#send_email').on('click', function() {
    var email = $("#inputEmailForgot")
    var emailPattern = /^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i;

    if (emailPattern.test(email.val())) {
      var $this = $(this);
      var loadingText = '<i class="fa fa-circle-o-notch fa-spin"></i> Przetwarzanie...';
      if ($(this).html() !== loadingText) {
        $this.data('original-text', $(this).html());
        $this.html(loadingText);
      }
      $.ajax({
        url: "/python/passwordReset.py",
        type: "post",
        datatype: "json",
        data: {
          'email': email.val()
        },
        success: function(response) {
          $("#python1").html(response.html);
        }
      });

      setTimeout(function() {
        $this.html($this.data('original-text'));
      }, 20000);

    } else {
      alert("Błędne dane")
    }
  });

  $(document).on('click', '#addBtn', function() {
    if (validateAddFrom()) {
      var $this = $(this);
      var loadingText = '<i class="fa fa-circle-o-notch fa-spin"></i> Przetwarzanie...';
      if ($(this).html() !== loadingText) {
        $this.data('original-text', $(this).html());
        $this.html(loadingText);
      }

      setTimeout(function() {
        var zast = $("#modal_zast1").val()
        var pass = $("#modal_pass1").val()
        var shared = $("#modal_shared1").val()
        $.ajax({
          url: "/python/add.py",
          type: "post",
          datatype: "json",
          data: {
            'zast': zast,
            'pass': pass,
            'share': shared
          },
          success: function(response) {
            $("#user_data").html(response.html);
            $("#ajax_script").html(response.js);
          }
        });
      }, 500);
      setTimeout(function() {
        $this.html($this.data('original-text'));
        //$("#addFrom").submit()
        $("#addModal").modal('toggle');
      }, 2500);
    } else {
      alert("Błędne dane fomrularza")
    }
  });

  $(document).on('click', '#changePassBtn', function() {
    if (validateChangePassFrom()) {
      var $this = $(this);
      var loadingText = '<i class="fa fa-circle-o-notch fa-spin"></i> Przetwarzanie...';
      if ($(this).html() !== loadingText) {
        $this.data('original-text', $(this).html());
        $this.html(loadingText);
      }
      var oldPass = $("#modalPassOld").val()
      var newPass = $("#modalPass").val()

      $.ajax({
        url: "/python/changePass.py",
        type: "post",
        datatype: "json",
        data: {
          'oldPass': oldPass,
          'newPass': newPass
        },
        success: function(response) {
          console.log(response);

          setTimeout(function() {
            alert('Udało się zminieć hasło! Nastąpi wylogowanie!') ? "" : location.reload();
          }, 500);
        }
      });

      setTimeout(function() {
        $this.html($this.data('original'));
        $("#changePasswordModal").modal('toggle');
      }, 5000);
    } else {
      alert("Błędne dane fomrularza")
    }
  });

  $('#loginBtn').on('click', function() {
    if (validateForm()) {
      var $this = $(this);
      var loadingText = '<i class="fa fa-circle-o-notch fa-spin"></i> Przetwarzanie...';
      if ($(this).html() !== loadingText) {
        $this.data('original-text', $(this).html());
        $this.html(loadingText);
      }
      //$("#loginForm").submit()
      var email = $("#inputEmail")
      var pass = $("#inputPassword")

      $.ajax({
        url: "/python/login.py",
        type: "post",
        datatype: "json",
        data: {
          'email': email.val(),
          'password': pass.val()
        },
        success: function(response) {
          if (!response.success) {
            email.addClass("not-valid")
            pass.addClass("not-valid")
            $("#answer").html(response.htmlData)
          } else {
            $("#python").html(response.htmlData);
          }
          $this.html($this.data('original-text'));
        }
      });
      setTimeout(function() {
        $this.html($this.data('original-text'));
      }, 10000);
    } else {
      alert("Błędne dane logowania")
    }
  });

  $(document).on('click', 'tbody button', function() {
    var tr = this.parentNode.parentNode.children

    $('#exampleModal').modal('toggle');
    zast = tr[1].firstChild.textContent
    pass = $(tr[2].children[0].children[0]).val()

    $('#modal_zast').val(tr[1].firstChild.textContent)
    $('#modal_pass').val($(tr[2].children[0].children[0]).val())
    $('#modal_confirm').val($(tr[2].children[0].children[0]).val())

    try {
      share = tr[3].firstChild.textContent
      $('#modal_shared').val(tr[3].firstChild.textContent)

    } catch (e) {
      console.log(e)
    }
  });

  $(document).on('click', '#changePassword', function() {
    $('#changePasswordModal').modal('toggle');
  });

  $(document).on('click', '.input-group-text > i', function(a) {
    input = $(this.parentElement.parentElement.previousElementSibling)
    icon = $(this)

    if (input.attr("type") == "text") {
      input.attr('type', 'password');
      icon.addClass("fa-eye-slash");
      icon.removeClass("fa-eye");
    } else if (input.attr("type") == "password") {
      input.attr('type', 'text');
      icon.removeClass("fa-eye-slash");
      icon.addClass("fa-eye");
    }

  });

  setInterval(function() {

    $.ajax({
      url: "/python/refresh.py",
      type: "post",
      datatype: "json",
      data: {},
      success: function(response) {
        $("#share_user").html(response.html);
      }
    });

  }, 300000);

});