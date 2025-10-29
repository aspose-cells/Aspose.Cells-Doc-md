---  
title: Convertir Excel en PDF, en image et dans d autres formats  
linktitle: Conversions de classeur  
type: docs  
weight: 65  
url: /fr/nodejs-cpp/convert-workbook-to-different-formats/  
description: Convertir des fichiers Excel en Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML et plus encore en utilisant Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells prend en charge la conversion entre de nombreux formats. Techniquement, la conversion consiste à charger un classeur dans un format de fichier et à le sauvegarder dans un autre.  
{{% /alert %}}  

## **Convertir un classeur Excel en PDF**  
Les fichiers PDF sont largement utilisés pour échanger des documents entre les organisations, les secteurs gouvernementaux et les particuliers. Il s'agit d'un format de document standard et les développeurs de logiciels sont souvent invités à trouver un moyen de convertir des fichiers Microsoft Excel en documents PDF.  

Aspose.Cells prend en charge la conversion de fichiers Excel en PDF et maintient une haute fidélité visuelle dans la conversion.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save("output.pdf");
```  

## **Convertir un classeur Excel en JPG**  
Aspose.Cells prend en charge la conversion de fichiers Excel en JPG. L'exemple de code ci-dessous montre comment enregistrer un classeur en JPG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Convert workbook to JPG image.
workbook.save("Image1.jpg");
```  

## **Convertir un classeur Excel en image**  
Aspose.Cells prend en charge la conversion de fichiers Excel en images. L'exemple de code ci-dessous montre comment enregistrer un classeur en images.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const book = new AsposeCells.Workbook(filePath);

// Convert workbook to BMP image.
book.save("Image1.bmp");
// Convert workbook to JPG image.
book.save("Image1.jpg");
// Convert workbook to Png image.
book.save("Image1.png");
// Convert workbook to EMF image.
book.save("Image1.emf");
// Convert workbook to GIF image.
book.save("Image1.gif");
```  

## **Convertir un classeur Excel en XPS**  
Le format de document XPS se compose de balises XML structurées qui définissent la mise en page d'un document et l'apparence visuelle de chaque page, ainsi que des règles de rendu pour la distribution, l'archivage, le rendu, le traitement et l'impression de documents.  

Le langage de balisage pour XPS est un sous-ensemble de XAML qui lui permet d'incorporer des éléments graphiques vectoriels dans des documents, en utilisant XAML pour baliser les primitives de la Fondation Windows Presentation (WPF). Les éléments utilisés sont décrits en termes de chemins et d'autres primitives géométriques.  

Un fichier XPS est en fait une archive ZIP Unicode utilisant les Conventions d'Emballage Ouvert, contenant les fichiers constituant le document. Il comprend un fichier de balisage XML pour chaque page, du texte, des polices intégrées, des images raster, des graphiques vectoriels 2D, ainsi que des informations de gestion des droits numériques. Le contenu d'un fichier XPS peut être examiné simplement en l'ouvrant avec une application prenant en charge les fichiers ZIP.  

À partir de Aspose.Cells 6.0.0, la conversion de Microsoft Excel en XPS est prise en charge.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);


// Render the sheet to xps            
const options = new AsposeCells.XpsSaveOptions();
const sheetSet = new AsposeCells.SheetSet([sheet.getIndex()]);
options.setSheetSet(sheetSet);
workbook.save(path.join(dataDir, "out_printingxps.out.xps"), options);


// Export the whole workbook to XPS
workbook.save(path.join(dataDir, "out_whole_printingxps.out.xps"), new AsposeCells.XpsSaveOptions());
```  

## **Convertir Excel en Ods, Sxc et Fods (OpenOffice / LibreOffice Calc)**  
Aspose.Cells prend en charge la conversion de fichiers Excel en fichiers Ods, Sxc et Fods. L'exemple de code ci-dessous montre comment convertir le [modèle](book1.xlsx) en fichier Ods, Sxc et Fods.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const filePath = path.join(dataDir, "book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Save as ods file 
workbook.save("Out.ods");

// Save as sxc file 
workbook.save("Out.sxc");

// Save as fods file 
workbook.save("Out.fods");
```  

## **Conversion de Classeur Excel en Fichiers MHTML**  
Le format MHTML combine du HTML normal avec des ressources externes (c'est-à-dire du contenu généralement lié tel que des images, des animations, de l'audio, etc.) dans un seul fichier. Ils sont utilisés pour les e-mails avec l'extension de fichier .mht.  

Aspose.Cells prend en charge la lecture et l'écriture des fichiers MHTML.  

L'exemple de code ci-dessous montre comment enregistrer un classeur sous forme de fichier MHTML.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "Book1.xlsx");

// Specify the HTML Saving Options
const sv = new AsposeCells.HtmlSaveOptions(AsposeCells.SaveFormat.MHtml);

// Instantiate a workbook and open the template XLSX file
const wb = new AsposeCells.Workbook(filePath);

// Save the MHT file
wb.save(`${filePath}.out.mht`, sv);
```  

## **Conversion de Classeur Excel en HTML**  
L’API Aspose.Cells offre un support pour l’exportation de feuilles de calcul au format HTML. À cette fin, Aspose.Cells utilise la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) pour offrir la flexibilité de contrôler plusieurs aspects du HTML de sortie.  

L'exemple de code ci-dessous montre comment enregistrer un classeur sous forme de fichier HTML.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  

## **Configuration des Préférences d'Image pour le HTML**  
Depuis la version 8.0.2, Aspose.Cells expose [**getImageOptions()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getImageOptions--) pour la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions), permettant aux développeurs de spécifier les préférences d’image lors de l’enregistrement de feuilles de calcul en HTML.  

Ci-dessous sont détaillés certains des réglages d'image qui peuvent être appliqués,  

- [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/): Spécifie le type d'image. Veuillez noter que toutes les formes, y compris les graphiques, sont rendues sous forme d'images dans le HTML de sortie.   
- [**getQuality()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getQuality--) : Spécifie la qualité de l'image entre 0 et 100, lorsque [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) est spécifié en tant que Jpeg.  
- [**getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--): Obtient ou définit la résolution verticale de l'image en points par pouce.  
- [**getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--): Obtient ou définit la résolution horizontale de l'image en points par pouce.  
- [**TiffCompression**](https://reference.aspose.com/cells/nodejs-cpp/tiffcompression/) : Obtient ou définit le type de compression pour les images lorsque [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) est défini comme Tiff.  
- [**getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--): Indique si l'arrière-plan d'une image doit être transparent lorsque ImageFormat est spécifié comme Png.  

## **Convertir un classeur Excel en Markdown**  
L'API Aspose.Cells offre la prise en charge de l'exportation de feuilles de calcul au format Markdown. Pour exporter la feuille active en Markdown, passez [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) comme deuxième paramètre de la méthode [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Vous pouvez également utiliser la classe [**MarkdownSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/markdownsaveoptions) pour spécifier des paramètres supplémentaires pour l'exportation de la feuille de calcul en Markdown.  

L'exemple de code suivant montre comment exporter la feuille active en Markdown en utilisant le membre d'énumération [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Veuillez voir le [fichier Markdown de sortie](md_sample.txt) généré par le code pour référence.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir; // Adjust as needed for source directory
const outputDir = dataDir; // Adjust as needed for output directory

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.md"), AsposeCells.SaveFormat.Markdown);
```  

## **Convertir un classeur Excel en JSON**  
Aspose.Cells supporte la conversion d'un classeur en fichier Json (JavaScript Object Notation).  

L'exemple de code suivant montre comment exporter la feuille active en Json en utilisant le membre d'énumération [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Veuillez voir le code pour convertir le [fichier source](Book1.xlsx) en [fichier Json de sortie](Book1.Json) pour référence.  

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

## **Convertir Excel en XML**  
Aspose.Cells prend en charge la conversion d'un classeur en XML de feuille de calcul Excel 2003 et en données XML brutes.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save as Excel 2003 Spreadsheet XML
workbook.save("Spreadsheet.xml");

// Save as plain XML data
const xmlSaveOptions = new AsposeCells.XmlSaveOptions();
workbook.save("data.xml", xmlSaveOptions);
```  

## **Convertir un classeur Excel en TIFF**  
Aspose.Cells prend en charge la conversion d'un classeur en fichier TIFF.  

Le code ci-dessous montre comment convertir Excel en TIFF :  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save file to tiff
workbook.save("out.tiff");
```  

## **Convertir un classeur Excel en DOCX**  
L'API Aspose.Cells prend en charge la conversion de feuilles de calcul en format DOCX. Pour exporter le classeur en DOCX, passez [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) comme deuxième paramètre de la méthode [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Vous pouvez également utiliser la classe [**DocxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/docxsaveoptions) pour spécifier des paramètres supplémentaires pour l'exportation en DOCX.  

L'exemple de code suivant montre comment exporter la feuille active en DOCX en utilisant le membre d'énumération [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Veuillez voir le [fichier DOCX généré](Book1.docx) pour référence.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = dataDir;

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.docx"), AsposeCells.SaveFormat.Docx);
```  

## **Convertir un classeur Excel en PPTX**  
L'API Aspose.Cells prend en charge la conversion de feuilles de calcul en format PPTX. Pour exporter le classeur en PPTX, passez [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) comme deuxième paramètre de la méthode [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Vous pouvez également utiliser la classe [**PptxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pptxsaveoptions) pour spécifier des paramètres supplémentaires pour l'exportation en PPTX.  

L'exemple de code suivant montre comment exporter la feuille active en PPTX en utilisant le membre d'énumération [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat). Veuillez voir le [fichier PPTX généré](Book1.pptx) pour référence.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = path.join(dataDir, "output/");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.pptx"), AsposeCells.SaveFormat.Pptx);
```  

## **Convertir le classeur Excel en EPUB**  
L'API Aspose.Cells offre la prise en charge de la conversion de feuilles de calcul en format EPUB. Pour exporter le classeur en EPUB, passez [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) comme deuxième paramètre de la méthode [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Vous pouvez également utiliser la classe [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) pour spécifier des paramètres supplémentaires pour l'exportation en Epub.  

L'exemple de code suivant montre comment exporter la feuille active en EPUB en utilisant le membre d'énumération [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Save it in EPUB format
workbook.save(path.join(dataDir, "ConvertingToEPUBFiles_out.epub"), AsposeCells.SaveFormat.Epub);
```  

## **Convertir le classeur Excel en AZW3**  
L'API Aspose.Cells supporte la conversion de feuilles de calcul en format AZW3. Pour exporter le classeur en AZW3, passez [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) comme deuxième paramètre de la méthode [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-). Vous pouvez également utiliser la classe [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) pour spécifier des paramètres supplémentaires pour l'exportation en AZW3.  

L'exemple de code suivant montre comment exporter la feuille active en AZW3 en utilisant le membre d'énumération [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in AZW3 format
wb.save(path.join(dataDir, "ConvertingToEPUBFiles_out.azw3"), AsposeCells.SaveFormat.Azw3);
```  

## **Sujets avancés**  
- [Convertir la révision de XLSB en XLSM](/cells/fr/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/)  
- [HTML](/cells/fr/nodejs-cpp/convert-excel-to-html/)  
- [Image](/cells/fr/nodejs-cpp/convert-excel-to-image/)  
- [Json](/cells/fr/nodejs-cpp/convert-workbook-to-json/)  
- [Convertir un classeur Excel en Ods, Sxc et Fods (OpenOffice / LibreOffice calc).](/cells/fr/nodejs-cpp/convert-excel-to-ods/)  
- [Pdf](/cells/fr/nodejs-cpp/convert-excel-workbook-to-pdf/)  
- [Convertir Excel en CSV, TSV et Txt](/cells/fr/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/)  
- [Suivre la progression de la conversion des documents](/cells/fr/nodejs-cpp/track-document-conversion-progress/)  
- [Convertir CSV, TSV et TXT en Excel](/cells/fr/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
