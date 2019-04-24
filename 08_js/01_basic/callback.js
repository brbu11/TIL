function numberEach(numbers, callback) {
    let acc;
    for (const number of numbers) {
        acc = callback(number, acc);
    }
    return acc;
}

function adder(number, sum = 0) {
    return number + sum;
}
function mul(number, sum=1){
    return number*sum;
}

console.log(numberEach([1, 2, 3, 4, 5], adder));
console.log(numberEach([1, 2, 3, 4, 5], mul));


function numbersEachAdd(numbers) {
    let acc = 0;
    for (const number of numbers) {
        acc += number;
    }
    return acc;
}

function numbersEachSub(numbers) {
    let acc = 0;
    for (const number of numbers) {
        acc -= number;
    }
    return acc;
}

function numbersEachMul(numbers) {
    let acc = 1;
    for (const number of numbers) {
        acc *= number;
    }
    return acc;
}

console.log(numbersEachAdd([1, 2, 3, 4, 5]));
console.log(numbersEachSub([1, 2, 3, 4, 5]));
console.log(numbersEachMul([1, 2, 3, 4, 5]));