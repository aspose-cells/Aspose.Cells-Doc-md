---
title: Convertir un fichier XLSX en format PDF avec Node.js via C++
linktitle: Convertir un fichier XLSX au format PDF
type: docs
weight: 30
url: /fr/nodejs-cpp/convert-xlsx-file-to-pdf-format/
description: Ce guide explique comment convertir un fichier Excel (XLSX) en format PDF en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

PDF (Portable Document Format) représente des documents indépendamment du logiciel, du matériel et du système d'exploitation utilisé pour créer ces documents. Un fichier PDF peut être un document avec n'importe quelle combinaison de texte, de graphiques et d'images de manière indépendante de l'appareil et de la résolution. Les fichiers PDF sont souvent compressés, de sorte qu'ils occupent moins d'espace que le fichier d'origine.

Parfois, vous devez convertir un fichier Microsoft Excel en PDF. Pour cela, vous avez besoin d'une solution rapide, sécurisée, précise et fiable qui vous permet de distribuer des documents PDF dans le monde entier. Il existe de nombreux outils de conversion qui peuvent effectuer cette tâche. Mais vous devez vous assurer que la mise en page du document Excel original est conservée dans le fichier PDF de sortie. Les images, les graphiques, les formes, la mise en forme des données, les polices, les attributs, les couleurs, les paramètres de configuration de la page, l'orientation du texte, les bordures, les graphiques, etc., doivent être rendus avec précision. [Aspose.Cells](https://products.aspose.com/cells/nodejs-cpp/) garantit une conversion fidèle.

Ce document est conçu pour fournir une compréhension complète sur la façon dont un document Microsoft Excel (contenant des images, des graphiques, des formats, etc.) peut être converti en PDF. À cette fin, il montre comment créer une application console simple en Node.js qui convertit un fichier Excel en PDF en utilisant l'API Aspose.Cells. La conversion est effectuée avec un haut degré de précision et d'exactitude.

{{% /alert %}}

## **Conversion d'Excel en PDF**

Cet exemple utilise un fichier Excel (SampleInput.xlsx) comme modèle. Le classeur contient des feuilles avec des graphiques et des images. Chaque feuille contient différents types de formats utilisant des polices, des attributs, des couleurs, des effets de shading, et des bordures. Il y a un graphique en colonnes sur la première feuille et une image sur la dernière.

### **Le fichier Excel modèle**

Le fichier modèle comporte trois feuilles, dont des graphiques et des images en tant que médias. La première feuille comporte des graphiques et la dernière une image, comme le montrent les captures d'écran ci-dessous.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|La troisième feuille de calcul **(Saisie des données)**|La dernière feuille de calcul **(Image)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Le troisième feuillet **(Saisie de données)**|Le dernier feuillet **(Image)**|

### **Processus de conversion**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const designerFile = path.join(dataDir, "SampleInput.xlsx");
const pdfFile = path.join(dataDir, "Output.out.pdf");

try {
// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}}

Si le tableau contient des formules, il est préférable d'appeler la méthode [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) juste avant de rendre le tableau en PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées et que les bonnes valeurs sont rendues dans le PDF.

{{% /alert %}}

### **Résultat**

Lorsque le code ci-dessus est exécuté, un fichier PDF est créé dans le dossier Files de votre répertoire d'application.
Les captures d'écran suivantes montrent les pages PDF. Notez que les en-têtes et pieds de pages sont également conservés dans le fichier PDF de sortie.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|La troisième feuille de calcul **(Saisie des données)**|La dernière feuille de calcul **(Image)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Le troisième feuillet **(Saisie de données)**|Le dernier feuillet **(Image)**|
