
function checkForm(){
 var error=false; //to znaczy, że danych nie brakuje
 var errorText=""; //komunikat z błędem
 var contactName = document.getElementById("contactName");
 var contactForName = document.getElementById("contactForName");
 var contactEmail = document.getElementById("contactEmail"); 
 var contactinformation = document.getElementById("contactinformation");

 
 if (contactName.value == ""){
 errorText += document.getElementById(‘errorName’).className=’alert alertdanger’; 
 error=true;
 } 
 if (contactForName.value == ""){
 errorText += document.getElementById(‘errorName’).className=’alert alertdanger’; 
 error=true;
 } 
 if(contactEmail.value == ""){
 errorText += document.getElementById(‘errorName’).className=’alert alertdanger’; 
 error=true;
} 
  if (contactinformation.value == ""){
 errorText += document.getElementById(‘errorName’).className=’alert alertdanger’; 
 error=true;
 } 

 if(regex.test(email)==false)
 {
 errorText += "błędny email\n";
 error=true;
 }

 if (!error) return true; 
 else{
alert ("Nie wypełniłeś następujących pól:\n" + errorText);
 return false;
} 

}