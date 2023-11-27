<form id="registrationForm" method="post">
    <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" class="form-control" id="username" name="username" placeholder="enter username.." required>
    </div>

    <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" class="form-control" id="email" name="email" placeholder="your email address.." required>
    </div>

    <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" class="form-control" id="password" name="password" placeholder="enter password here.." required>
    </div>

    <div class="form-group">
        <label for="confirmPassword">Confirm Password:</label>
        <input type="password" class="form-control" id="confirmPassword" name="confirmPassword" placeholder="re-type password confirm" required>
    </div>

    <button type="submit" class="btn btn-primary">Register</button>
    <button type="button" class="btn btn-danger float-right" data-dismiss="modal">Close</button>
</form>