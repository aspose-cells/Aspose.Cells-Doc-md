---
title: Använd anpassade XML delar i Aspose.Cells med Node.js via C++
linktitle: Använd anpassade XML delar i Aspose.Cells
type: docs
weight: 390
url: /sv/nodejs-cpp/use-custom-xml-parts-in-aspose-cells/
description: Lär dig hur du använder anpassade XML delar i Aspose.Cells for Node.js via C++. Integrera extern XML data sömlöst i Excel filer.
--- 

## Användning av anpassade XML-delar i Aspose.Cells

Anpassade XML-delar är XML-data som lagras av olika applikationer som SharePoint etc. inuti Excel-filen. Denna data används av olika applikationer som behöver den. Microsoft Excel använder inte denna data så det finns ingen GUI för att lägga till den. Du kan visa denna data genom att byta ut extensionen på **.xlsx** till **.zip** och sedan öppna den med **WinZip**. Du kan också öppna ZIP-filen med vilken tredjeparts Windows zip-utility som helst, såsom WinRAR eller WinZip. Data finns i mappen **customXml**.

Du kan lägga till anpassade XML-delar med Aspose.Cells via [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) metoden.

Följande exempel använder [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) metoden och lägger till **Book Catalog XML** med namnet **BookStore**. Bilden nedan visar resultatet av denna kod. Som du kan se är Book Catalog XML tillagt i BookStore-noden, som är namnet på denna egenskap.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Node.js kod för att använda anpassade XML-delar

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "output.xlsx");

// The sample XML that will be injected to Workbook
const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

// Create an instance of Workbook class
const workbook = new AsposeCells.Workbook();

// Add Custom XML Part to ContentTypePropertyCollection
workbook.getContentTypeProperties().add("BookStore", booksXML);

// Save the resultant spreadsheet
workbook.save(filePath);
```

## Relaterad artikel

- [Lägga till anpassade egenskaper synliga inuti dokumentinformationspanelen](/cells/sv/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
