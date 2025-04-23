---
title: Zellen mit Node.js via C++ formatieren
description: Erfahren Sie, wie Sie Zellen in Aspose.Cells for Node.js via C++ formatieren und stylen, einschließlich Zahlenformatierung, Datumsformatierung, Schriftarten und andere Zellformatoptionen. Unser Leitfaden hilft Ihnen, attraktive und professionell aussehende Tabellenkalkulationen zu erstellen.
keywords: Aspose.Cells for Node.js via C++, Zellformatierung, Styling, Zahlenformatierung, Datumsformatierung, Schriftart, Zellstil Optionen, Tabellenkalkulation, erstellen, professionelles Aussehen, Zeilen und Spalten formatieren.
linktitle: Zellen formatieren
type: docs
weight: 120
url: /de/nodejs-cpp/cells-formatting/
---

## **Einführung**

{{% alert color="primary" %}}

Aspose.Cells bietet die [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) und [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) Methoden der [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) Klasse, die verwendet werden, um das Formatierungsstil einer Zelle zu erhalten/setzen. Aspose.Cells bietet auch eine [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) Klasse.

{{% /alert %}}

## **Wie man Zellen mit den Methoden GetStyle und SetStyle formatiert**

Auf Zellen verschiedene Arten von Formatierungsstilen anwenden, um Hintergrund- oder Vordergrundfarben, Rahmen, Schriftarten, horizontale und vertikale Ausrichtungen, Einrückungsebene, Textausrichtung, Drehwinkel und vieles mehr festzulegen.

### **Wie man die GetStyle und SetStyle Methoden verwendet**

Wenn Entwickler unterschiedliche Formatierungsstile auf verschiedene Zellen anwenden müssen, ist es besser, das [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) der Zelle mit der [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--)-Methode zu erhalten, die Stil-Attribute zu spezifizieren und dann die Formatierung mit der [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)-Methode anzuwenden. Ein Beispiel zeigt, wie dieser Ansatz angewendet wird, um verschiedene Formatierungen auf eine Zelle anzuwenden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Defining a Style object
let style;

// Get the style from A1 cell
style = cell.getStyle();

// Setting the vertical alignment
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text
style.getFont().setColor(AsposeCells.Color.Green);

// Setting to shrink according to the text contained in it
style.setShrinkToFit(true);

// Setting the bottom border color to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Applying the style to A1 cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Wie man das Style-Objekt verwendet, um verschiedene Zellen zu formatieren**

Wenn Entwickler denselben Formatierungsstil auf verschiedene Zellen anwenden möchten, können sie das [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt verwenden. Folgen Sie den untenstehenden Schritten, um das [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt zu verwenden:

1. Fügen Sie ein [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt hinzu, indem Sie die [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--)-Methode der [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse aufrufen
2. Greifen Sie auf das neu hinzugefügte [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt zu
3. Legen Sie die gewünschten Eigenschaften/Attribute des [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekts fest, um die gewünschten Formatierungseinstellungen anzuwenden
4. Weisen Sie das konfigurierte [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt Ihren gewünschten Zellen zu

Dieser Ansatz kann die Effizienz Ihrer Anwendungen erheblich verbessern und auch Speicherplatz sparen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the first worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Adding a new Style
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Assigning the Style object to the "A1" cell
cell.setStyle(style);

// Apply the same style to some other cells
worksheet.getCells().get("B1").setStyle(style);
worksheet.getCells().get("C1").setStyle(style);
worksheet.getCells().get("D1").setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Wie man die Microsoft Excel 2007 vordefinierten Stile verwendet**

Wenn Sie unterschiedliche Formatierungsstile für Microsoft Excel 2007 anwenden müssen, wenden Sie Stile mithilfe der Aspose.Cells API an. Ein Beispiel unten zeigt diesen Ansatz zur Anwendung eines vordefinierten Stils auf einer Zelle.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");


// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Create a style object.
const style = workbook.createStyle();

// Input a value to A1 cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Test");

// Apply the style to the cell.
workbook.getWorksheets().get(0).getCells().get("A1").setStyle(style);

// Save the Excel 2007 file.
workbook.save(path.join(dataDir, "book1.out.xlsx"));
```



## **Wie man ausgewählte Zeichen in einer Zelle formatiert**

Der Umgang mit Schriftart-Einstellungen erklärt, wie Text in Zellen formatiert wird, aber es erklärt nur, wie der gesamte Zellinhalt formatiert wird. Was ist, wenn Sie nur bestimmte Zeichen formatieren möchten?

Aspose.Cells unterstützt diese Funktion ebenfalls. Dieser Artikel erklärt, wie diese Funktion effektiv genutzt werden kann.

### **Wie man ausgewählte Zeichen formatiert**

Aspose.Cells stellt die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse enthält eine [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf jedes Tabellenblatt in einer Excel-Datei ermöglicht. Ein Tabellenblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse bietet eine [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung. Jedes Element in der [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung repräsentiert ein Objekt der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse.

Die [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse bietet die [**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-)-Methode, die die folgenden Parameter akzeptiert, um einen Zeichenbereich in einer Zelle auszuwählen:

- **Startindex**: Der Index des Zeichens, von dem die Auswahl beginnt.
- **Anzahl der Zeichen**: Die Anzahl der ausgewählten Zeichen.

Die [**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-)-Methode gibt eine Instanz der [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)-Klasse zurück, die es Entwicklern ermöglicht, die Charaktere auf die gleiche Weise zu formatieren wie eine Zelle, wie im folgenden Codebeispiel gezeigt. Im Ausgabedokument wird im A1-Feld das Wort 'Visit' mit der Standardschriftart formatiert, aber 'Aspose!' ist fett und blau.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first(default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the font of selected characters to bold
const font = cell.characters(6, 7).getFont();
font.isBold = true;

// Setting the font color of selected characters to blue
font.color = AsposeCells.Color.Blue;

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

{{% alert color="primary" %}}

Wenn Sie daran interessiert sind, einen Teil des Rich Texts in einer Zelle zu formatieren, können Sie die [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) & [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-)-Methoden verwenden. Die [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--)-Methode dient dazu, auf die Textabschnitte zuzugreifen, und Änderungen können mit der [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-)-Methode vorgenommen werden, während die **Get**-Methode ein Array [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)-Objekte zurückgibt, die manipuliert werden können, um verschiedene Eigenschaften wie Schriftart, Schriftfarbe, Fettdruck usw. festzulegen. Die **Set**-Methode kann verwendet werden, um die Änderungen anzuwenden.

{{% /alert %}}

## **Wie man Zeilen und Spalten formatiert**

Manchmal müssen Entwickler dieselbe Formatierung auf Zeilen oder Spalten anwenden. Die Formatierung einzelner Zellen nacheinander dauert oft länger und ist keine gute Lösung.
Um dieses Problem zu lösen, bietet Aspose.Cells einen einfachen, schnellen Weg, der in diesem Artikel ausführlich erörtert wird.

### **Formatierung von Zeilen & Spalten**

Aspose.Cells bietet die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse enthält eine [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf jedes Tabellenblatt in der Excel-Datei ermöglicht. Ein Tabellenblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse bietet eine [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung. Die [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung bietet eine [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--)-Sammlung.

### **Wie man eine Zeile formatiert**

Jeder Eintrag in der [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--)-Sammlung repräsentiert ein [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)-Objekt. Das [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)-Objekt bietet die [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-)-Methode, die verwendet wird, um die Zeilenformatierung festzulegen. Um eine gleiche Formatierung auf eine Zeile anzuwenden, verwenden Sie das [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt. Die unten dargestellten Schritte zeigen, wie es verwendet wird.

1. Fügen Sie ein [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt der [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse hinzu, indem Sie seine [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--)-Methode aufrufen.
2. Legen Sie die Eigenschaften des [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekts fest, um die Formatierungseinstellungen anzuwenden.
3. Schalten Sie die relevanten Attribute für das [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)-Objekt ein.
4. Weisen Sie das konfigurierte [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt dem [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)-Objekt zu.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a row from the Rows collection
const row = worksheet.getCells().getRows().get(0);

// Assigning the Style object to the Style property of the row
row.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Wie man eine Spalte formatiert**

Die [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung bietet auch eine [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--)-Sammlung. Jedes Element in der [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--)-Sammlung repräsentiert ein [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column)-Objekt. Ähnlich wie bei einem [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)-Objekt bietet auch das [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column)-Objekt die [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-)-Methode zum Formatieren einer Spalte.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a column from the Columns collection
const column = worksheet.getCells().getColumns().get(0);

// Applying the style to the column
column.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Erweiterte Themen**
- [Ausrichtungseinstellungen](/cells/de/nodejs-cpp/cells-alignment-settings/)
- [Rahmeneinstellungen](/cells/de/nodejs-cpp/cells-border-settings/)
- [Bedingte Formate von Excel- und ODS-Dateien festlegen.](/cells/de/nodejs-cpp/conditional-formatting/)
- [Excel-Themen und Farben](/cells/de/nodejs-cpp/excel-themes-and-colors/)
- [Fülleinstellungen](/cells/de/nodejs-cpp/cells-fill-settings/)
- [Schriftarteinstellungen](/cells/de/nodejs-cpp/cells-font-settings/)
- [Zellenformat in einer Arbeitsmappe](/cells/de/nodejs-cpp/format-worksheet-cells-in-a-workbook/)
- [Implementieren des 1904-Datumsformats](/cells/de/nodejs-cpp/implement-1904-date-system/)
- [Zusammenführen und Aufheben der Zellenzusammenführung](/cells/de/nodejs-cpp/merging-and-unmerging-cells/)
- [Nummern-Einstellungen](/cells/de/nodejs-cpp/cells-number-settings/)
- [Stil für Zellen abrufen und festlegen](/cells/de/nodejs-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

