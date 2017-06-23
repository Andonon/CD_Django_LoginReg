# CD_Django_LoginReg
Troy Center troycenter1@gmail.com June 2017 
Coding Dojo Django / Python assignment "Login and Registration" 

<strong>Assignment: Login and Registration</strong>
Rebuild the Login and Registration assignment from the flask chapter, this time using Django.

We’ve learned how to integrate models, validations, and controllers to our projects. Our next goal is to create a fully functional login and registration app! This will combine your knowledge of MVC patterns, validations, and password encryption.


<strong>Build the following:</strong>
<ul>
    <li>Show validation error messages if validations fail the following tests</li>
        <ul>
            <li>First Name - Required; No fewer than 2 characters; letters only</li>
            <li>Last Name - Required; No fewer than 2 characters; letters only</li>
            <li>Email - Required; Valid Format</li>
            <li>Password - Required; No fewer than 8 characters in length; matches Password Confirmation</li>
        </ul>
    <li>Don't worry about hashing passwords for now. We'll take a closer look at hashing tomorrow.</li>
</ul>
<strong>Bonus:</strong> Birthday Field - Before today, or go creative and do it in an age range
<strong>Bonus:</strong> Implement Flash Messages

<img src="http://s3.amazonaws.com/General_V88/boomyeah/company_209/chapter_3834/handouts/chapter3834_6625_login-reg.png" alt="Coding Dojo Assignment Image">

One thing we've noticed as people build their login and registrations that you should consider:

<strong>User.objects.get(email = email)</strong>
If there is not a matching email for a .get(), Django throws an error (try and except could come in handy), otherwise it returns the User object associated with the matching user. e.g. Userobject.

<strong>User.objects.filter(email = email)</strong>
Filter, on the other hand, returns a list, so if there is no user that matches, it returns an empty list.  If there is a single matching user the list will contain a single User object: e.g. [Userobject].