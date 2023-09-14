let check=0;
function validate(){
    let name=document.getElementById("name").value;
    let mail=document.getElementById("email").value;
    let id=document.getElementById("Uname").value;
    let password=document.getElementById("pass").value;
    let phno=document.getElementById("phno").value;
    let s=fun(name,mail,id,password,phno);
    if(check==0){
    if(s==true)
{
    alert("success");
}
else{
    alert("not success");
}
    }
}
function fun(name,id,password,phno){
    if(name.length==0 || mail.length==0 || id.length==0 || password.length==0 || phno.length==0)
    return false;
    if(!(/^[A-Za-z\s]*$/).test(name)){
    alert("invalid name");
    check=1;}
    if(!(/^[A-Za-z0-9.!#@$%&*_-]*$/).test(id) || id.length<8){
    alert("Invalid Username");
    check=1;}
    if(!(/^[A-Za-z0-9@!#$%&*_-]*$/).test(password) || password.length<=7){
    alert("Invalid Password");
    check=1;}
    if(!(/^[0-9]*$/).test(phno) || !(phno.length>7 && phno.length<11)){
    alert("Invalid mobile number");
    check=1;}
    return true;
}