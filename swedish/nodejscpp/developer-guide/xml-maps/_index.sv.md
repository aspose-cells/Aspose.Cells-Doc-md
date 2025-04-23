---
title: Importera XML till Excel arbetsbok med Node.js via C++
linktitle: XML mappar
type: docs
weight: 210
url: /sv/nodejs-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Importera data från XML filer till Excel med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells tillåter dig att importera XML-kartan inuti arbetsboken med hjälp av [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-)-metoden. Du kan importera XML-karta med Microsoft Excel med följande steg:

- Välj **Utvecklare**-fliken
- Klicka på **Importera** i XML-avsnittet och följ de nödvändiga stegen.

Du måste tillhandahålla dina XML-data för att slutföra importen. Här är ett [prov-XML-data](5115037.txt) som du kan använda för testning.

{{% /alert %}}

## **Importera XML-karta med Microsoft Excel**

Följande skärmbild visar hur man importerar XML-karta med Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Importera XML-karta med Aspose.Cells for Node.js via C++**

Följande kodexempel visar hur man använder [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-). Det genererar den [utdataexcel-filen](5115036.xlsx) som visas i den här skärmbilden.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Local XML file path
const XML = path.join(dataDir, "sampleXML.txt");

// Import your XML Map data starting from cell A1
workbook.importXml(XML, "Sheet1", 0, 0);

// Save workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

## **Avancerade ämnen**
- [Lägg till XML-karta inuti arbetsboken med XmlMapCollection.add() metod](/cells/sv/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Exportera XML-data som är länkad till XML-karta inuti arbetsboken](/cells/sv/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Hitta rotresursnamnet på XML-kartan](/cells/sv/nodejs-cpp/find-the-root-element-name-of-xml-map/)
- [Länka celler till XML-kartelement](/cells/sv/nodejs-cpp/link-cells-to-xml-map-elements/)

