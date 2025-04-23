---
title: Différentes manières d ouvrir des fichiers avec Node.js via C++
linktitle: Différentes façons d ouvrir des fichiers
type: docs
weight: 10
url: /fr/nodejs-cpp/different-ways-to-open-files/
description: Cet article explique comment ouvrir un fichier Excel en utilisant l API Aspose.Cells for Node.js via C++.
keywords: Node.js Ouvrir un fichier Excel sans Excel, comment ouvrir un fichier Excel avec Node.js.
---

{{% alert color="primary" %}}

Avec Aspose.Cells, il est simple d'ouvrir des fichiers, par exemple, pour récupérer des données, ou pour utiliser un modèle de conception afin d'accélérer le processus de développement.

{{% /alert %}}

## **Comment ouvrir un fichier Excel via un chemin**

Les développeurs peuvent ouvrir un fichier Microsoft Excel en utilisant son chemin de fichier sur l'ordinateur local en le spécifiant dans le constructeur de la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Il suffit de transmettre le chemin en tant que *chaîne*. Aspose.Cells détectera automatiquement le type de format du fichier.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(filePath);
console.log("Workbook opened using path successfully!");
```

## **Comment ouvrir un fichier Excel via un flux**

Il est également simple d'ouvrir un fichier Excel en tant que flux. Pour ce faire, utilisez une version surchargée du constructeur qui prend l'objet *Stream* contenant le fichier.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book2.xls");
// Opening through Stream
// Create a Stream object
const fstream = fs.createReadStream(filePath);

// Creating a Workbook object, open the file from a Stream object
// That contains the content of file and it should support seeking
const chunks = [];
fstream.on('data', (chunk) => {
chunks.push(chunk);
```

## **Comment ouvrir un fichier avec des données uniquement**

Pour ouvrir un fichier contenant uniquement des données, utilisez les classes [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) et [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) pour définir les attributs et options liés des classes pour le fichier de modèle à charger.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load only specific sheets with data and formulas
// Other objects, items etc. would be discarded

// Instantiate LoadOptions specified by the LoadFormat
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Set LoadFilter property to load only data & cell formatting
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), loadOptions);
console.log("File data imported successfully!");
```

## **Comment charger uniquement les feuilles visibles**

Lors du chargement d’un [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), il se peut que vous ayez uniquement besoin des données dans les feuilles visibles d’un classeur. Aspose.Cells vous permet d’ignorer les données des feuilles invisibles lors du chargement d’un classeur. Pour ce faire, créez une fonction personnalisée qui hérite de la classe [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) et passez son instance à la propriété [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sampleFile = "output.xlsx";
const samplePath = path.join(dataDir, sampleFile);

// Create a sample workbook
// and put some data in first cell of all 3 sheets
const createWorkbook = new AsposeCells.Workbook();
createWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet2").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet3").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().get("Sheet3").setIsVisible(false);
createWorkbook.save(samplePath);

// Load the sample workbook
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setLoadFilter(new AsposeCells.LoadFilter()); // Corrected line by defining LoadFilter properly

const loadWorkbook = new AsposeCells.Workbook(samplePath, loadOptions);
console.log(`Sheet1: A1: ${loadWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A2: ${loadWorkbook.getWorksheets().get("Sheet2").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A3: ${loadWorkbook.getWorksheets().get("Sheet3").getCells().get("A1").getValue()}`);
```

Voici l’implémentation de la classe *CustomLoad* référencée dans le morceau de code ci-dessus.

```javascript
const { Workbook, LoadDataFilterOptions } = require("aspose.cells.node");

class CustomLoad {
startSheet(sheet) {
if (sheet.isVisible()) {
// Load everything from visible worksheet
this.loadDataFilterOptions = LoadDataFilterOptions.All;
} else {
// Load nothing
this.loadDataFilterOptions = LoadDataFilterOptions.Structure;
}
}
}
```

{{% alert color="primary" %}}

Une exception sera levée si vous essayez d’ouvrir des fichiers Excel non natifs ou d’autres formats de fichiers (par exemple PPT/PPTX, DOC/DOCX, etc.) avec Aspose.Cells.

{{% /alert %}} 

{{% alert color="primary" %}}

Il y a de bonnes chances que le constructeur [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) puisse lancer une *OutOfMemoryError* lors du chargement de grands classeurs. Cette exception indique que la mémoire disponible est insuffisante pour charger complètement le classeur en mémoire ; par conséquent, le classeur doit être chargé tout en activant les préférences de mémoire.

{{% /alert %}}

