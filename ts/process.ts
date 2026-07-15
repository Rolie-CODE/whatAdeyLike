
let stu_name = "Roland";
let scores = [85, 92, 78, 90, 88];
let total_score = scores.reduce((acc, score) => acc + score, 0);
let average_score = total_score / scores.length;

function find_grade(average_score: number): "A" | "B" | "C" | "D" | "F" {
    if (average_score >= 80) {
        return "A";
    } else if (average_score >= 70) {
        return "B";
    } else if (average_score >= 60) {
        return "C";
    } else if (average_score >= 50) {
        return "D";
    } else {
        return "F";
    }1
}

let grade = find_grade(average_score)

function stu_status(average_score: number): "Pass" | "Fail" {
    if (average_score >= 50) {
        return "Pass";
    } else {
        return "Fail";
    }
}

let status1 = stu_status(average_score)

console.log(`Student Name: ${stu_name}`);
console.log(`Scores: ${scores.join(", ")}`);
console.log(`Total Score: ${total_score}`);
console.log(`Average Score: ${average_score.toFixed(2)}`);
console.log(`Grade: ${grade}`);
console.log(`Status: ${status1}`);
