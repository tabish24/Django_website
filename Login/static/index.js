const navBar=document.getElementById('nav-phone');
const navTab=document.getElementById('nav');
let flag=false;
navBar.addEventListener('click',()=>{
    if(flag===false){
        flag=true
        navTab.style.display='block';
    }
    else if(flag===true){
        flag=false
        navTab.style.display='none';
    }
    
});



flag=false
const sideBar=document.getElementById('menu-bar')
const elem = document.getElementById("men");  
sideBar.addEventListener('click',()=>{
  if(flag==false){
        elem.style.display="block";
        flag=true;
        myMove();
    }else{
        flag=false;
        elem.style.display="none";
    }
});

flag=false
const sideBar1=document.getElementById('menu-bar1')
const elem1 = document.getElementById("men");  
sideBar1.addEventListener('click',()=>{
  if(flag==false){
        elem1.style.display="block";
        flag=true;
        myMove();
    }else{
        flag=false;
        elem1.style.display="none";
    }
});


    function myMove() {
        let id = null;
        console.log(elem);
        let pos = 0;
        clearInterval(id);
        id = setInterval(frame, 2);
        function frame() {
          if (pos >= 400) {
            clearInterval(id);
          } else {
            pos=pos+10; 
            elem.style.marginLeft = pos + "px"; 
          }
        }
      }


// dropdown

const about=document.getElementById('about');
const course=document.getElementById('course')
const admission=document.getElementById('admission');
const dropDownAbout=document.getElementById('about-us');
const dropDownCourse=document.getElementById('courses');
const dropDownAdmission=document.getElementById('admission-procedure');


about.addEventListener('mouseover',()=>{
  dropDownAbout.style.display='block';
});
about.addEventListener('mouseout',()=>{
  dropDownAbout.style.display='none';
});
course.addEventListener('mouseover',()=>{
  dropDownCourse.style.display='block';
});
course.addEventListener('mouseout',()=>{
  dropDownCourse.style.display='none';
});
admission.addEventListener('mouseover',()=>{
  dropDownAdmission.style.display='block';
});
admission.addEventListener('mouseout',()=>{
  dropDownAdmission.style.display='none';
});




dropDownAbout.addEventListener('mouseover',()=>{
  dropDownAbout.style.display="block";
});
dropDownAbout.addEventListener('mouseout',()=>{
  dropDownAbout.style.display="none";
});

dropDownCourse.addEventListener('mouseover',()=>{
  dropDownCourse.style.display="block";
});
dropDownCourse.addEventListener('mouseout',()=>{
  dropDownCourse.style.display="none";
});

dropDownAdmission.addEventListener('mouseover',()=>{
  dropDownAdmission.style.display='block';
});
dropDownAdmission.addEventListener('mouseout',()=>{
  dropDownAdmission.style.display="none";
});