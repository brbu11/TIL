function add(num1, num2){
    return num1 + num2;

}

function sub(num1, num2){
    return num1 - num2;
}

const mul = (num1, num2) => {
    return num1 * num2;
}
//1. function 을 없앤다
//2. ()와 {}사이에 => 를 넣는다

const square = num1 => num1*num1;



//인자가 하나라면 ()가 삭제가능
//함수안에 코드가 return 한줄이라면 {} return 키워드 삭제가능


const sayHello = name => `hi ${name}`;

console.log(add(1, 4));
console.log(sub(5, 4));
console.log(mul(5, 4));
console.log(square(5));
console.log(sayHello(" "));