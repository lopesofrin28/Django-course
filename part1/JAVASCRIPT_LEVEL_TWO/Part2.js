//PROBLEM 1
function sleepIn(weekday,vacation) {
  return (!weekday||vacation)
}

//PROBLEM 2
function monkeyTrouble(aSmile,bSmile) {
  return (aSmile && bSmile)||(!aSmile && !bSmile)
}


//PROBLEM 3
function stringTimes(str,n) {
  var returnStr="";
  var i=0;
  while(i<n){
    returnStr += str
    i++
  }
  return returnStr;
}

function stringTimes1(str,n) {
  var returnStr="";
  var i=0;
  for (i = 0; i <n; i++) {
    returnStr +=str;
  }
  return returnStr;
}

//PROBLEM 4
function luckySum(a,b,c) {
  if (a==13) {
    return 0
  }
  if (b=13) {
    return a
  }
  if (c=13) {
    return a+b
  }
  return a+b+c
}

function luckySum1(a,b,c) {
  if (a===13) {
    return 0;
  }else if (b===13) {
    return a;
  }else if (c===13) {
    return a+b;
  }else {
    return a+b+c;
  }
}

//PROBLEM 5
function caught_speeding(speed,is_birthday) {
  if (is_birthday) {
    speed-=5
  }



  if (speed<=60) {
    return 0
  }
  if(60<speed<=80){
    return 1
  }
  return 2
}

//BONUS QUESTION:

function makeBricks(small,big,goal) {
  return goal%5 >=0 && goal%5 - small <= 0 && small +5*big >= goal;

}
