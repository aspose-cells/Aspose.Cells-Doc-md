---  
title: Configuration de page et options d impression avec Node.js via C++  
linktitle: Configuration de la mise en page et des options d impression  
type: docs  
weight: 60  
url: /fr/nodejs-cpp/page-setup-and-printing-options/  
---  

{{% alert color="primary" %}}  
Parfois, les développeurs doivent configurer la mise en page et les paramètres d'impression pour contrôler le processus d'impression. Les paramètres de mise en page et d'impression offrent diverses options et sont entièrement pris en charge dans Aspose.Cells.  

 Cet article explique comment créer une application console en Node.js via C++, et appliquer les options de configuration de page et d'impression à une feuille de calcul avec quelques lignes de code simples utilisant l'API Aspose.Cells.  
{{% /alert %}}  

## **Travailler avec la mise en page et les paramètres d'impression**  

 Pour cet exemple, nous avons créé un classeur dans Microsoft Excel et utilisé Aspose.Cells pour définir la configuration de page et les options d'impression.  

### **Utilisation d'Aspose.Cells pour définir les options de mise en page**  

Créez d'abord une feuille de calcul simple dans Microsoft Excel. Ensuite, appliquez des options de mise en page. L'exécution du code modifie les options de mise en page comme dans la capture d'écran ci-dessous.  

| **Fichier de sortie.** |  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|  

1. Créez une feuille de calcul avec des données dans Microsoft Excel:  
   1. Ouvrir un nouveau classeur dans Microsoft Excel.  
   1. Ajoutez des données.  
1. Définir les options de mise en page :  
   Appliquer les options de mise en page au fichier. Ci-dessous se trouve une capture d'écran des options par défaut, avant l'application des nouvelles options.  

| **Options de mise en page par défaut.** |  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|  

1. Téléchargez et installez Aspose.Cells :  
   1. [Télécharger](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++.  
   1. Installez-le sur votre ordinateur de développement.  
      Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits.  
1. Créer un projet :  
   1. Démarrez votre environnement Node.js.  
   1. Créez une nouvelle application console.  
       Cet exemple montrera une application console Node.js, mais vous pouvez aussi utiliser les liaisons C++.  
1. Ajouter des références:  
   1. Cet exemple utilise Aspose.Cells, donc ajoutez une référence à ce composant dans le projet. Par exemple :  
      …\Program Files\Aspose\Aspose.Cells\Bin\Node.js-Cpp\Aspose.Cells.node  
1. Écrivez l'application qui invoque l'API :  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "CustomerReport.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the orientation to Portrait
worksheet.getPageSetup().setOrientation(AsposeCells.PageOrientationType.Portrait);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Setting the paper size to A4
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Setting the print quality of the worksheet to 1200 dpi
worksheet.getPageSetup().setPrintQuality(1200);

// Setting the first page number of the worksheet pages
worksheet.getPageSetup().setFirstPageNumber(2);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_out.xlsx"));
```  

### **Paramétrage des options d'impression**  

Les paramètres de mise en page fournissent également plusieurs options d'impression (appelées également options de feuille) qui permettent aux utilisateurs de contrôler l'impression des pages de feuille de calcul. Ils permettent aux utilisateurs de :  

- Sélectionner une zone d'impression spécifique d'une feuille de calcul.
- Imprimer les titres.
- Imprimer les quadrillages.
- Imprimer les en-têtes de lignes/colonnes.
- Obtenir une qualité brouillon.
- Imprimer des commentaires.
- Imprimer les erreurs de cellules.
- Définir l'ordre des pages.  

L'exemple qui suit applique des options d'impression au fichier créé dans l'exemple ci-dessus (PageSetup.xls). La capture d'écran ci-dessous montre les options d'impression par défaut avant l'application de nouvelles options.  

|**Document d'entrée**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|  
L'exécution du code modifie les options d'impression.  

|**Fichier de sortie**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageSetup.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

const pageSetup = worksheet.getPageSetup();

// Specifying the cells range (from A1 cell to E30 cell) of the print area
pageSetup.setPrintArea("A1:E30");

// Defining column numbers A & E as title columns
pageSetup.setPrintTitleColumns("$A:$E");

// Defining row numbers 1 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_Print_out.xlsx"));
```  

