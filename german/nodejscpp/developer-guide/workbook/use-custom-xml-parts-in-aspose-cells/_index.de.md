---
title: Benutzerdefinierte XML Teile in Aspose.Cells mit Node.js über C++ verwenden
linktitle: Verwenden von benutzerdefinierten XML Teilen in Aspose.Cells
type: docs
weight: 390
url: /de/nodejs-cpp/use-custom-xml-parts-in-aspose-cells/
description: Erfahren Sie, wie Sie benutzerdefinierte XML Teile in Aspose.Cells for Node.js via C++ verwenden. Integrieren Sie externe XML Daten nahtlos in Excel Dateien.
--- 

## Verwendung von benutzerdefinierten XML-Teilen in Aspose.Cells

Benutzerdefinierte XML-Teile sind XML-Daten, die von verschiedenen Anwendungen wie SharePoint usw. innerhalb der Excel-Datei gespeichert werden. Diese Daten werden von Anwendungen genutzt, die sie benötigen. Microsoft Excel verwendet diese Daten nicht, daher gibt es keine GUI, um sie hinzuzufügen. Sie können diese Daten anzeigen, indem Sie die Erweiterung **.xlsx** in **.zip** ändern und diese dann mit **WinZip** öffnen. Sie können die ZIP-Datei auch mit jedem Drittanbieter-Windows-Zip-Programm wie WinRAR oder WinZip öffnen. Die Daten befinden sich im **customXml**-Ordner.

Sie können benutzerdefinierte XML-Teile mit Aspose.Cells über die [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/)-Methode hinzufügen.

Der folgende Beispielcode nutzt die [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) Methode und fügt den **Book Catalog XML** mit dem Namen **BookStore** hinzu. Das folgende Bild zeigt das Ergebnis dieses Codes. Wie Sie sehen können, wird der Book Catalog XML innerhalb des BookStore-Knotens hinzugefügt, der der Name dieser Eigenschaft ist.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Node.js-Code zur Verwendung benutzerdefinierter XML-Teile

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

## Verwandter Artikel

- [Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind](/cells/de/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
