function getRandomizedSubstitutionMap() {
    const alphabet = 'abcdefghijklmnopqrstuvwxyz';
    const shuffledAlphabet = alphabet.split('');
  
    // Function to shuffle the substitution map object using Fisher-Yates algorithm
    function shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
      return array;
    }
  
    // Shuffle the substitution map object directly
    shuffleArray(shuffledAlphabet);
  
    // Create the substitution map
    const randomizedSubstitutionMap = {};
    for (let i = 0; i < alphabet.length; i++) {
      randomizedSubstitutionMap[alphabet[i]] = shuffledAlphabet[i];
    }
  
    return randomizedSubstitutionMap;
  }
  
  function substitutionEncrypt(inputString, substitutionMap) {
    // Convert the inputString to lowercase
    const lowercaseInput = inputString.toLowerCase();
  
    // Encrypt the inputString using the substitutionMap
    let encrypted = '';
    for (let i = 0; i < lowercaseInput.length; i++) {
      const currentChar = lowercaseInput[i];
      const encryptedChar = substitutionMap[currentChar] || currentChar;
      encrypted += encryptedChar;
    }
  
    return encrypted;
  }
  
  // Get a randomized substitution map
  const randomSubstitutionMap = getRandomizedSubstitutionMap();
  
  // Example usage:
  const inputString = 'hello war';
  const encrypted = substitutionEncrypt(inputString, randomSubstitutionMap);
  console.log(encrypted);
  