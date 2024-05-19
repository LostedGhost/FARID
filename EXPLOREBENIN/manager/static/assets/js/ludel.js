// Fonction pour mélanger les éléments d'une classe donnée
function shuffleElements(className) {
    const elements = Array.from(document.querySelectorAll('.' + className));
    if (elements.length === 0) return; // Vérifie s'il y a des éléments à mélanger

    const parent = elements[0].parentNode;
    const shuffledElements = elements.slice(); // Copie du tableau pour ne pas modifier l'original

    // Mélange de Fisher-Yates
    for (let i = shuffledElements.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffledElements[i], shuffledElements[j]] = [shuffledElements[j], shuffledElements[i]];
    }

    // Réinsère les éléments mélangés dans le parent
    shuffledElements.forEach(element => parent.appendChild(element));
}

// Appel de la fonction après le chargement du DOM
if (document.readyState === 'complete' || document.readyState === 'interactive') {
    shuffleElements('shuffle');
} else {
    document.addEventListener('DOMContentLoaded', function() {
        shuffleElements('shuffle');
    });
}
document.addEventListener('DOMContentLoaded', function() {
    function replaceCharacterInParagraphs() {
        // Sélectionne tous les paragraphes avec la classe 'to_affiche'
        const paragraphs = document.querySelectorAll('.to_affiche');

        // Parcourt chaque paragraphe et remplace le caractère '°' par '<br>'
        paragraphs.forEach(paragraph => {
            const originalText = paragraph.innerHTML;
            const newText = originalText.replace(/°/g, '<br>');
            paragraph.innerHTML = newText;
        });
    }

    // Appelle la fonction pour remplacer les caractères
    replaceCharacterInParagraphs();
});



// Utilisation : Appeler cette fonction avec le nom de classe à mélanger
shuffleElements('shuffle');

function sortElements() {
    // Sélectionne tous les éléments avec la classe 'arrange'
    const elements = Array.from(document.querySelectorAll('.arrange'));

    // Trie les éléments en fonction de l'attribut data-order
    elements.sort((a, b) => {
        return parseInt(a.getAttribute('data-order')) - parseInt(b.getAttribute('data-order'));
    });

    // Récupère le parent des éléments triés
    const parent = elements[0].parentNode;

    // Réinsère les éléments triés dans le parent
    elements.forEach(element => {
        parent.appendChild(element);
    });
}

// Appelle la fonction pour trier les éléments après le chargement du DOM
if (document.readyState === 'complete' || document.readyState === 'interactive') {
    sortElements();
} else {
    document.onreadystatechange = function () {
        if (document.readyState === 'complete') {
            sortElements();
        }
    }
}
