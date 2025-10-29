---
title: Différentes façons d enregistrer des fichiers avec Node.js via C++
linktitle: Enregistrer des fichiers
type: docs
weight: 40
url: /fr/nodejs-cpp/different-ways-to-save-files/
description: Aspose.Cells for Node.js via C++ peut enregistrer des fichiers dans différents formats, notamment PDF, HTML, DOCX, PPTX, JSON et MHTML.
keywords: Aspose.Cells Enregistrer Excel au format PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML et plus encore en utilisant Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells rend possible la création et l'enregistrement de fichiers. Cet article explique les différentes façons dont les fichiers peuvent être enregistrés.

{{% /alert %}}

## **Différentes façons d'enregistrer des fichiers**

Aspose.Cells fournit le [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Microsoft Excel et offre les propriétés et méthodes nécessaires pour travailler avec des fichiers Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) fournit la méthode [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) utilisée pour enregistrer des fichiers Excel. La méthode [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) a de nombreuses surcharge qui sont utilisées pour enregistrer des fichiers de différentes manières.

Le format de fichier dans lequel le fichier est enregistré est déterminé par l'énumération [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat).

|**Types de formats de fichier**|**Description**|
| :- | :- |
|CSV|Représente un fichier CSV|
|Excel97To2003|Représente un fichier Excel 97 - 2003|
|Xlsx|Représente un fichier Excel 2007 XLSX|
|Xlsm|Représente un fichier Excel 2007 XLSM|
|Xltx|Représente un modèle Excel 2007 XLTX|
|Xltm|Représente un modèle activé par macro Excel 2007 XLTM|
|Xlsb|Représente un fichier XLSB binaire Excel 2007|
|SpreadsheetML|Représente un fichier XML de feuille de calcul|
|TSV|Représente un fichier de valeurs séparées par des tabulations|
|TabDelimited|Représente un fichier de texte à onglets|
|ODS|Représente un fichier ODS|
|Html|Représente un fichier HTML|
|MHtml|Représente un fichier MHTML|
|Pdf|Représente un fichier PDF|
|XPS|Représente un document XPS|
|TIFF|Représente le format de fichier TIFF (Tagged Image File Format)|

## **Comment enregistrer un fichier dans différents formats**

Pour enregistrer des fichiers dans un emplacement de stockage, spécifiez le nom du fichier (avec le chemin de stockage complet) et le format de fichier souhaité (de l'énumération [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)) lors de l'appel à la méthode [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) de l'objet [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save in Excel 97 to 2003 format
workbook.save(path.join(dataDir, ".output.xls"));
// OR
workbook.save(path.join(dataDir, ".output.xls"), new AsposeCells.XlsSaveOptions());

// Save in Excel 2007 xlsx format
workbook.save(path.join(dataDir, ".output.xlsx"), AsposeCells.SaveFormat.Xlsx);

// Save in Excel 2007 xlsb format
workbook.save(path.join(dataDir, ".output.xlsb"), AsposeCells.SaveFormat.Xlsb);

// Save in ODS format
workbook.save(path.join(dataDir, ".output.ods"), AsposeCells.SaveFormat.Ods);

// Save in Pdf format
workbook.save(path.join(dataDir, ".output.pdf"), AsposeCells.SaveFormat.Pdf);

// Save in Html format
workbook.save(path.join(dataDir, ".output.html"), AsposeCells.SaveFormat.Html);

// Save in SpreadsheetML format
workbook.save(path.join(dataDir, ".output.xml"), AsposeCells.SaveFormat.SpreadsheetML);
```

## **Comment enregistrer un classeur au format PDF**
Le Format de Document Portable (PDF) est un type de document créé par Adobe dans les années 1990. L'objectif de ce format de fichier était d'introduire une norme pour la représentation de documents et autres matériaux de référence dans un format indépendant du logiciel applicatif, du matériel ainsi que du système d'exploitation. Le format PDF a la pleine capacité de contenir des informations telles que texte, images, hyperliens, champs de formulaire, médias riches, signatures numériques, pièces jointes, métadonnées, fonctionnalités géospatiales, et objets 3D pouvant devenir partie du document source.

Le code suivant montre comment sauvegarder un classeur en tant que fichier PDF avec Aspose.Cells :
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Set value to Cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World!");

const saveFilePath = path.join(dataDir, "pdf1.pdf");
workbook.save(saveFilePath);

// Save as Pdf format compatible with PDFA-1a
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

const pdfAFilePath = path.join(dataDir, "pdfa1a.pdf");
workbook.save(pdfAFilePath, saveOptions);
```

## **Comment enregistrer le classeur au format texte ou CSV**

Parfois, vous souhaitez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats texte (par exemple TXT, TabDelim, CSV, etc.), par défaut, à la fois Microsoft Excel et Aspose.Cells enregistrent uniquement le contenu de la feuille de calcul active.

L'exemple de code suivant explique comment enregistrer un classeur entier au format texte. Chargez le classeur source, qui peut être n'importe quel fichier de feuille de calcul Microsoft Excel ou OpenOffice (ainsi XLS, XLSX, XLSM, XLSB, ODS, etc.), avec n'importe quel nombre de feuilles de calcul.

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT

Vous pouvez modifier le même exemple pour enregistrer votre fichier au format CSV. Par défaut, [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) est la virgule, donc ne spécifiez pas de séparateur si vous enregistrez au format CSV. Veuillez noter : si vous utilisez la version d'évaluation et même si la propriété [**TxtSaveOptions.getExportAllSheets()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getExportAllSheets--) est définie sur vrai, le programme n'exportera qu'une seule feuille de calcul.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **Comment enregistrer un fichier en fichiers de texte avec un séparateur personnalisé**

Les fichiers texte contiennent des données de feuille de calcul sans mise en forme. Le fichier est un type de fichier texte brut qui peut avoir des délimiteurs personnalisés entre ses données

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```

## **Comment enregistrer un fichier dans un flux**

Pour enregistrer des fichiers dans un flux, créez un objet *MemoryStream* ou *FileStream* et enregistrez le fichier dans cet objet flux en appelant la méthode [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) de l'objet [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Spécifiez le format de fichier souhaité en utilisant l'énumération [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) lors de l'appel à la méthode [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function downloadExcel(req, res) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);
// Save the workbook to a memory stream
const stream = workbook.save(AsposeCells.SaveFormat.Xlsx);

// Set the content type and file name
const contentType = "application/octet-stream";
const fileName = "output.xlsx";

// Set the response headers
res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
res.setHeader("Content-Type", contentType);

// Write the file contents to the response body stream
res.send(stream);
}
```

## **Comment enregistrer un fichier Excel en fichiers Html et Mht**
Aspose.Cells peut simplement enregistrer un fichier Excel, JSON, CSV ou d'autres fichiers pouvant être chargés par Aspose.Cells en fichiers .html et .mht.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```


## **Comment enregistrer un fichier Excel au format OpenOffice (ODS, SXC, FODS, OTS)**
Nous pouvons enregistrer les fichiers au format OpenOffice : ODS, SXC, FODS, OTS, etc.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **Comment enregistrer un fichier Excel en JSON ou XML**

JSON (JavaScript Object Notation) est un format de fichier standard ouvert pour le partage de données qui utilise un texte lisible par l'homme pour stocker et transmettre des données. Les fichiers JSON sont stockés avec l'extension .json. JSON nécessite moins de mise en forme et est une bonne alternative à XML. JSON est dérivé de JavaScript mais est un format de données indépendant du langage. La génération et l'analyse du JSON sont prises en charge par de nombreux langages de programmation modernes. application/json est le type de support utilisé pour JSON.

Aspose.Cells prend en charge l'enregistrement de fichiers en JSON ou XML.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```


## **Sujets avancés**
- [Ajuster le niveau de compression du classeur](/cells/fr/nodejs-cpp/adjust-workbook-compression-level/)
- [Enregistrer le classeur au format strict Open XML Spreadsheet](/cells/fr/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Enregistrer le fichier dans l'objet Response](/cells/fr/nodejs-cpp/saving-file-to-response-object/)
{{< app/cells/assistant language="nodejs-cpp" >}}
