---  
title: Verwaltung von Bildern mit Node.js via C++  
linktitle: Bilder verwalten  
type: docs  
weight: 10  
url: /de/nodejs-cpp/managing-pictures/  
description: Lernen Sie, wie man Bilder in Tabellen mit Aspose.Cells for Node.js via C++ hinzufügt und positioniert.  
---  

Aspose.Cells ermöglicht es Entwicklern, Bilder zur Laufzeit zu Tabellenkalkulationen hinzuzufügen. Darüber hinaus kann die Positionierung dieser Bilder zur Laufzeit kontrolliert werden, was in den folgenden Abschnitten detaillierter erläutert wird.

Dieser Artikel erklärt, wie man Bilder hinzufügt und eine Bild einfügt, die den Inhalt bestimmter Zellen zeigt.

## **Bilder hinzufügen**

Das Hinzufügen von Bildern zu einer Tabelle ist sehr einfach. Es dauert nur wenige Zeilen Code:  
Rufen Sie einfach die [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-)-Methode der [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection)-Sammlung auf (verkapselt im [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Objekt). Die [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-)-Methode nimmt folgende Parameter: 

- **Index der oberen linken Zeile**, der Index der oberen linken Zeile.
- **Index der oberen linken Spalte**, der Index der oberen linken Spalte.
- **Bilddateiname**, der Name der Bilddatei inklusive des Pfads.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Bilder positionieren**

Es gibt zwei mögliche Methoden, um die Positionierung von Bildern mithilfe von Aspose.Cells zu kontrollieren:

- Proportionale Positionierung: Definieren Sie eine Position proportional zur Zeilenhöhe und -breite.
- Absolute Positionierung: Legen Sie die genaue Position auf der Seite fest, an der das Bild eingefügt wird, z.B. 40 Pixel links und 20 Pixel unterhalb des Zellrands.

### **Proportionale Positionierung**

Entwickler können die Bilder proportional zur Zeilenhöhe und Spaltenbreite mit den Eigenschaften [**getUpperDeltaX()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaX--) und [**getUpperDeltaY()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaY--) des [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)-Objekts positionieren. Ein [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)-Objekt kann durch Übergabe seines Bildindex aus der [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection)-Sammlung erhalten werden. Dieses Beispiel platziert ein Bild in der Zelle F6.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Positioning the picture proportional to row height and column width
picture.setUpperDeltaX(200);
picture.setUpperDeltaY(200);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Absolute Positionierung**

Entwickler können Bilder auch absolut positionieren, indem sie die Eigenschaften [**getLeft()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeft--) und [**getTop()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTop--) des [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)-Objekts verwenden. Dieses Beispiel platziert ein Bild in Zelle F6, 60 Pixel vom linken Rand und 10 Pixel vom oberen Rand der Zelle entfernt.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "logo.jpg");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, filePath);

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Absolute positioning of the picture in unit of pixels
picture.setLeft(60);
picture.setTop(10);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Einfügen eines Bildes basierend auf Zellverweis**

Mit Aspose.Cells können Sie den Inhalt einer Arbeitsblattzelle in eine Bildform darstellen. Sie können das Bild mit der Zelle verknüpfen, die die Daten enthält, die Sie anzeigen möchten. Da die Zelle oder Zellenbereich mit dem Grafikobjekt verknüpft ist, erscheinen Änderungen, die Sie an den Daten in dieser Zelle oder dem Zellenbereich vornehmen, automatisch im Grafikobjekt.

Fügen Sie ein Bild durch Aufruf der [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-)-Methode der [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection)-Sammlung hinzu (verkapselt im [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Objekt). Geben Sie den Zellbereich durch Verwendung des [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--)-Attributs des [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)-Objekts an.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

const picts = workbook.getWorksheets().get(0).getPictures();
// Add a blank picture to the D1 cell
const picIndex = picts.add(0, 3, 10, 6, null);
const pic = picts.get(picIndex);

// Specify the formula that refers to the source range of cells

pic.setFormula("A1:C10");

// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Erweiterte Themen**
- [Hinzufügen eines bedingten Symbolsets mit dem Zelltext](/cells/de/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/)
- [Verknüpftes Bild aus Webadresse einfügen](/cells/de/nodejs-cpp/insert-a-linked-picture-from-web-address/)
- [Bild anhand von Zellenverweis einfügen](/cells/de/nodejs-cpp/insert-a-picture-based-on-cell-reference/)
- [Laden Sie ein Web-Bild von einer URL in eine Excel-Arbeitsmappe](/cells/de/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="nodejs-cpp" >}}
