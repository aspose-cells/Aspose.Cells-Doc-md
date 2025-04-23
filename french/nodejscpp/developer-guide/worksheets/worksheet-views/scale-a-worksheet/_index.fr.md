---
title: Comment mettre à l échelle une feuille de calcul avec Node.js via C++
linktitle: Comment mettre à l échelle une feuille de calcul
type: docs
weight: 130
url: /fr/nodejs-cpp/how-to-scale-a-worksheet/
description: Cet article vous montre du code expliquant comment mettre à l échelle une feuille de calcul en utilisant Aspose.Cells for Node.js via C++.
keywords: Node.js mise à l échelle d une feuille de calcul, Comment mettre à l échelle une feuille de calcul en utilisant Node.js via C++, Mise à l échelle d une feuille via Node.js via C++.
---

## **Scénarios d'utilisation possibles**
Mettre à l'échelle une feuille de calcul peut être utile pour diverses raisons, en fonction du contexte dans lequel vous travaillez. Voici quelques raisons courantes :
1. Adapter à la page : pour s'assurer que tout le contenu tient sur une seule page ou un nombre spécifique de pages lors de l'impression, ce qui facilite la lecture et la gestion sans avoir à faire défiler plusieurs pages.

1. Présentation : pour rendre la feuille de calcul plus organisée et professionnelle, notamment lorsqu'elle est partagée lors de réunions ou dans des rapports.

1. Lisibilité : pour ajuster la taille du texte et d'autres éléments pour une meilleure lisibilité, en particulier pour les personnes ayant des difficultés à lire de petites polices.

1. Gestion de l'espace : pour optimiser l'utilisation de l'espace sur une feuille de calcul, en veillant à ce qu'il n'y ait pas d'espace blanc inutile et que toutes les informations importantes soient visibles sans défilement excessif.

1. Visualisation des données : dans le cas de graphiques et de diagrammes, la mise à l'échelle peut aider à les rendre plus compréhensibles en ajustant leur taille pour s'adapter à l'espace disponible.

1. Cohérence : pour maintenir une apparence cohérente à travers plusieurs feuilles de calcul ou documents, ce qui est particulièrement important dans des contextes professionnels et éducatifs.

## **Comment mettre à l'échelle une feuille de calcul dans Excel**
Mettre à l'échelle une feuille de calcul dans Excel peut vous aider à faire tenir votre contenu sur une seule page ou un nombre spécifié de pages lors de l'impression. Voici les étapes pour mettre à l'échelle une feuille :

1. Ouvrir votre feuille de calcul : ouvrez la feuille Excel que vous souhaitez mettre à l'échelle.

1. Aller à l'onglet Mise en Page : cliquez sur l'onglet Mise en Page dans le ruban.

1. Groupe Mise à l’échelle : dans l'onglet Mise en Page, trouvez le groupe Mise à l’échelle. Vous avez ici des options pour ajuster la mise à l’échelle. Largeur : permet de spécifier le nombre de pages en largeur pour l'impression. Hauteur : permet de spécifier le nombre de pages en hauteur pour l'impression. Échelle : vous pouvez également définir un pourcentage de mise à l’échelle personnalisé.
<br>
<img src="1.png" width=60% />

1. Ajuster la largeur et la hauteur : définir la largeur et la hauteur selon le nombre de pages souhaité. Par exemple, définir les deux à 1 page si vous souhaitez que la feuille tienne sur une seule page.

1. Ajuster le pourcentage de mise à l’échelle (si nécessaire) : si vous préférez définir un pourcentage spécifique, ajustez la case Échelle. Par exemple, le réglage à 50 % réduira tout à la moitié de la taille.


## **Comment mettre une feuille à l'échelle en utilisant Node.js via C++**
Aspose.Cells for Node.js via C++ est une bibliothèque puissante pour travailler avec des fichiers Excel de manière programmatique. Pour mettre une feuille à l'échelle en utilisant Aspose.Cells, vous devez suivre ces étapes : charger [fichier d'exemple](sample.xlsx) et ajuster les paramètres d'impression pour que le contenu tienne sur le nombre de pages souhaité ou pourcentage spécifique de la taille originale.

### **Exemple : Ajuster à la page**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the PageSetup object
const pageSetup = sheet.getPageSetup();

// Set the worksheet to fit to 1 page wide and 1 page tall
pageSetup.setFitToPagesWide(1);
pageSetup.setFitToPagesTall(1);

// Save the modified workbook
workbook.save("output_fit_to_page.xlsx");
```
<br>
<img src="3.png" width=60% />

### **Exemple : Mettre à l'échelle en pourcentage**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the PageSetup object
const pageSetup = sheet.getPageSetup();

// Set the scaling to a specific percentage (e.g., 75%)
pageSetup.setZoom(75);

// Save the modified workbook
workbook.save("output_scaled_percentage.xlsx");
```
<br>
<img src="2.png" width=60% />
