//Write a function, 'countVowels(word)', that takes in a string and returns the number of vowels

function countVowels(word) {
    let vowelCounter = 0;
    let vowels = ['a', 'e', 'i', 'o', 'u'];
    for (let i = 0; i < word.length; i++) {
        if (vowels.includes(word[i])) {
            vowelCounter++;
        }
    }
    return vowelCounter;
}