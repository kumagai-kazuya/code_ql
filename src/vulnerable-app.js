// Intentionally vulnerable JavaScript code
function vulnerableFunction(userInput) {
    // Using eval directly without sanitizing the input
    return eval(userInput); // This introduces a potential code injection vulnerability
}

// Sample usage that could lead to exploitation
const input = "2 + 2"; // Replace with malicious input to see the impact
console.log("Result:", vulnerableFunction(input));
