// nodeJS
// auth: x_n0n (GitHub: X3n0nP0w3r3d)
// Day 2 Part 2 AoC Solution


const target = 19690720;

const originalInput=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0];

input[1]=12;
input[2]=2;

let iter = 0;
let opcode;
while ((opcode = input[iter]) !== 99) {
  const val1 = input[input[iter + 1]];
  const val2 = input[input[iter + 2]];
  input[input[iter + 3]] = opcode === 1 ? val1 + val2 : val1 * val2;
  iter += 4;
}

console.log(input[0]);


function main(code){
const input = [...originalInput];
input[1]= Math.floor(code/100);
input[2]= code % 100;

let iter = 0;
let opcode;
while ((opcode = input[iter]) !== 99) {
  const val1 = input[input[iter + 1]];
  const val2 = input[input[iter + 2]];
  input[input[iter + 3]] = opcode === 1 ? val1 + val2 : val1 * val2;
  iter += 4;
}

return input[0];

}

for(let i = 0; i < 9999; i++){
    const res = main(i) ;
    if(res===target){
        console.log(i);
        break;
    }
}
