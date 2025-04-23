---
title: Définir les marges avec Node.js via C++
linktitle: Réglage des marges
type: docs
weight: 20
url: /fr/nodejs-cpp/setting-margins/
description: Dans cet article, vous apprendrez comment définir les marges d une feuille Excel à l aide d un code d exemple. Apprenez également comment définir de manière programmatique les marges pour le centrage de la page, l en tête et le pied de page avec l API Node.js via C++.
keywords: définir la marge de la feuille Excel au centre via Node.js avec C++, définir la marge de l en tête et du pied de page de la feuille via C++
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge pleinement les options de configuration de la mise en page de Microsoft Excel. Les développeurs peuvent avoir besoin de configurer les paramètres de mise en page pour les feuilles de calcul afin de contrôler le processus d'impression. Ce sujet traite de l'utilisation d'Aspose.Cells pour configurer les marges de la page.

{{% /alert %}}

## **Réglage des marges**

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) permettant d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

 La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit la propriété [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) utilisée pour définir les options de mise en page pour une feuille de calcul. L'attribut [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) est un objet de la classe [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) qui permet aux développeurs de définir différentes options de disposition pour une feuille imprimée. La classe [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) offre diverses propriétés et méthodes pour définir les options de mise en page.

### **Marges de la page**

Définir les marges de la page (gauche, droite, haut, bas) en utilisant les membres de la classe [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--). Voici quelques méthodes utilisées pour spécifier les marges de la page :

- [**PageSetup.getLeftMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getLeftMargin--)
- [**PageSetup.getRightMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getRightMargin--)
- [**PageSetup.getTopMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getTopMargin--)
- [**PageSetup.getBottomMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBottomMargin--)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Set bottom, left, right and top page margins
pageSetup.setBottomMargin(2);
pageSetup.setLeftMargin(1);
pageSetup.setRightMargin(1);
pageSetup.setTopMargin(3);

// Save the Workbook.
workbook.save(path.join(dataDir, "SetMargins_out.xls"));
```

### **Centrer sur la page**

Il est possible de centrer quelque chose horizontalement et verticalement sur une page. Pour cela, il existe des membres utiles de la classe [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--), [**PageSetup.getCenterHorizontally()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCenterHorizontally--) et [**PageSetup.getCenterVertically()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCenterVertically--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Specify Center on page Horizontally and Vertically
pageSetup.setCenterHorizontally(true);
pageSetup.setCenterVertically(true);

// Save the Workbook.
workbook.save(path.join(dataDir, "CenterOnPage_out.xls"));
```

### **Marges d'en-tête et de pied de page	**

Définir les marges d'en-tête et de pied de page avec les membres de classe [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) tels que [**PageSetup.getHeaderMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeaderMargin--) et [**PageSetup.getFooterMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooterMargin--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Specify Header / Footer margins
pageSetup.setHeaderMargin(2);
pageSetup.setFooterMargin(2);

// Save the Workbook.
workbook.save(path.join(dataDir, "CenterOnPage_out.xls"));
```
