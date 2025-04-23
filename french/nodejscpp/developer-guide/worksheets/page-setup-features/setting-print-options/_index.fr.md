---
title: Définir les options d impression avec Node.js via C++
linktitle: Réglage des options d impression
type: docs
weight: 40
url: /fr/nodejs-cpp/setting-print-options/
description: Cet article démontre comment définir de manière programmatique les options d impression de la fonctionnalité de mise en page de la feuille Excel en utilisant l API Node.js et la bibliothèque C++. Vous pouvez définir la zone d impression, les titres d impression et l ordre des pages.
keywords: définir la zone d impression Excel avec Node.js via C++, définir les titres d impression Excel avec Node.js via C++, définir l ordre des pages dans Excel avec Node.js via C++
---

{{% alert color="primary" %}}

Les paramètres de configuration de page de Microsoft Excel offrent plusieurs options d'impression (également appelées options de feuille) qui permettent aux utilisateurs de contrôler l'impression des pages de feuille de calcul.

{{% /alert %}}

## **Réglage des options d'impression**

Ces options d'impression permettent aux utilisateurs de :

- Sélectionner une zone d'impression spécifique sur une feuille de calcul.
- Imprimer les titres.
- Imprimer les quadrillages.
- Imprimer les en-têtes de lignes/colonnes.
- Obtenir une qualité brouillon.
- Imprimer des commentaires.
- Imprimer les erreurs de cellules.
- Définir l'ordre des pages.

Aspose.Cells for Node.js via C++ supporte toutes les options d'impression offertes par Microsoft Excel et les développeurs peuvent facilement configurer ces options pour les feuilles de calcul en utilisant les propriétés offertes par la classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). La façon dont ces propriétés sont utilisées est abordée plus en détail ci-dessous.

### **Définir la zone d'impression**

Par défaut, la zone d'impression intègre toutes les zones de la feuille de calcul contenant des données. Les développeurs peuvent établir une zone d'impression spécifique de la feuille de calcul.

Pour sélectionner une zone d'impression spécifique, utilisez la propriété [**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--) de la classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). Attribuez une plage de cellules qui définit la zone d'impression à cette propriété.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Specifying the cells range (from A1 cell to T35 cell) of the print area
pageSetup.setPrintArea("A1:T35");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintArea_out.xls"));
```

### **Définir les titres d'impression**

Aspose.Cells vous permet de désigner les en-têtes de ligne et de colonne à répéter sur toutes les pages d'une feuille de calcul imprimée. Pour ce faire, utilisez les propriétés [**PageSetup.getPrintTitleColumns()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleColumns--) et [**PageSetup.getPrintTitleRows()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleRows--) de la classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup).

Les lignes ou colonnes qui seront répétées sont définies en passant leurs numéros de ligne ou de colonne. Par exemple, les lignes sont définies comme $1:$2 et les colonnes sont définies comme $A:$B.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Defining column numbers A & B as title columns
pageSetup.setPrintTitleColumns("$A:$B");

// Defining row numbers 1 & 2 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintTitle_out.xls"));
```

### **Définir d'autres options d'impression**

La classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) fournit également plusieurs autres propriétés pour définir des options d'impression générales comme suit :

- [**PageSetup.getPrintGridlines()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintGridlines--) : une propriété booléenne qui définit si les lignes de la grille doivent être imprimées ou non.
- [**PageSetup.getPrintHeadings()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintHeadings--) : une propriété booléenne qui définit si les en-têtes de lignes et de colonnes doivent être imprimés ou non.
- [**PageSetup.getBlackAndWhite()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBlackAndWhite--) : une propriété booléenne qui définit si la feuille doit être imprimée en noir et blanc ou non.
- [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) : détermine si les commentaires d'impression doivent s'afficher sur la feuille ou à la fin de la feuille.
- [**PageSetup.getPrintDraft()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintDraft--) : une propriété booléenne qui définit si la feuille doit être imprimée sans graphiques.
- [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) : définit l'impression des erreurs de cellule telles qu'elles sont affichées, vides, trait d'union ou N/A.

 Pour définir les propriétés [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) et [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--), Aspose.Cells for Node.js via C++ fournit également deux énumérations, [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) et [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype) qui contiennent des valeurs prédéfinies à assigner aux propriétés [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) et [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) respectivement.

Les valeurs prédéfinies dans l'énumération [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) sont listées ci-dessous avec leurs descriptions.

|**Types de commentaires d'impression**|**Description**|
| :- | :- |
|PrintInPlace| Spécifie d'imprimer les commentaires tels qu'ils apparaissent sur la feuille de calcul.
|PrintNoComments| Spécifie de ne pas imprimer les commentaires.
|PrintSheetEnd| Spécifie d'imprimer les commentaires à la fin de la feuille de calcul.

Les valeurs prédéfinies de l'énumération [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype) sont listées ci-dessous avec leurs descriptions.

|**Types d'erreurs d'impression**|**Description**|
| :- | :- |
|PrintErrorsBlank|Indique de ne pas imprimer les erreurs.|
|PrintErrorsDash|Indique d'imprimer les erreurs sous forme de "--".|
|PrintErrorsDisplayed|Indique d'imprimer les erreurs telles qu'elles sont affichées.|
|PrintErrorsNA|Indique d'imprimer les erreurs sous forme de "#N/A".|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

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

// Save the workbook.
workbook.save(path.join(dataDir, "OtherPrintOptions_out.xls"));
```

### **Définir l'ordre des pages**

La classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) fournit la propriété [**PageSetup.getOrder()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getOrder--) qui est utilisée pour ordonner plusieurs pages de votre feuille de calcul à imprimer. Il y a deux possibilités pour ordonner les pages comme suit.

- **En bas puis à droite :** imprime toutes les pages en bas avant d'imprimer les pages à droite.
- **À droite puis en bas :** imprime les pages de gauche à droite avant d'imprimer les pages en dessous.

Aspose.Cells fournit une énumération, [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) qui contient tous les types d'ordre prédéfinis.

Les valeurs prédéfinies de l'énumération [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) sont listées ci-dessous.

|**Types d'ordre d'impression**|**Description**|
| :- | :- |
|DownThenOver|Représente l'ordre d'impression en bas puis à droite.|
|OverThenDown|Représente l'ordre d'impression à droite puis en bas.|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook.
workbook.save(path.join(dataDir, "SetPageOrder_out.xls"));
```
