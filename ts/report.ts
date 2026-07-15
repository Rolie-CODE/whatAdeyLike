import fs from 'fs'

const data = fs.readFileSync("student.json" , "utf-8");
const student = JSON.parse(data);

console.log("------STUDENT REPORT----------");
console.log(`Name ${student.student_name}`);

console.log();

console.log("Scores: ")

const subjects = ["Math", "English", "Science", "ICT", "Social Studies"];

subjects.forEach((subject , index ) => {
    console.log(`${subject} : ${student.student_scores[index]}`)
})

console.log();


console.log(`Total: ${student.total_mark}`);
console.log(`Average: ${student.average_mark.toFixed(2)}`);
console.log(`Grade: ${student.student_grade}`);
console.log(`Status: ${student.student_status}`);