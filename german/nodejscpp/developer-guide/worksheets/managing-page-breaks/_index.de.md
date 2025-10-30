---
title: Seitenumbruchverwaltung mit Node.js über C++
linktitle: Verwalten von Seitenumbrüchen
type: docs
weight: 30
url: /de/nodejs-cpp/managing-page-breaks/
description: Dieser Artikel bietet Beispielcode und erklärt, wie man bestimmte Seitenumbrüche in Excel Arbeitsblättern programmatisch mit Aspose.Cells for Node.js via C++ hinzufügt, löscht oder löscht.
keywords: Seitenumbrüche Node.js via C++, Seitenumbrüche in Excel Node.js via C++, Seitenumbruch löschen Node.js via C++, Spezifischen Seitenumbruch in Node.js via C++ löschen
---

{{% alert color="primary" %}}

Nach Definition ist ein Seitenumbruch eine Stelle in einem Textfluss, an der eine Seite endet und die nächste beginnt. Microsoft Excel ermöglicht es Benutzern, Seitenumbrüche in jede ausgewählte Zelle eines Arbeitsblatts einzufügen.

Der Ort der Zelle, an dem der Seitenumbruch hinzugefügt wird, die Seite endet und der Rest der Daten nach dem Seitenumbruch auf der nächsten Seite gedruckt wird, während des Druckens. Einfach ausgedrückt, teilen Seitenumbrüche Ihr Arbeitsblatt gemäß Ihren Spezifikationen in mehrere Seiten auf. Sie können auch zur Laufzeit Seitenumbrüche zu Ihren Arbeitsblättern mit Aspose.Cells hinzufügen. Aspose.Cells ermöglicht Entwicklern, zwei Arten von Seitenumbrüchen hinzuzufügen:

- Horizontaler Seitenumbruch
- Vertikaler Seitenumbruch

Im weiteren Verlauf der Diskussion werden wir beschreiben, wie Sie horizontale oder vertikale Seitenumbrüche in Ihre Arbeitsblätter mit Aspose.Cells einfügen können.

{{% /alert %}}

## **Seitenumbrüche**

Aspose.Cells stellt eine Klasse bereit, die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine Sammlung von [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden, die zur Verwaltung eines Arbeitsblatts verwendet werden.

Um die Seitenumbrüche hinzuzufügen, verwenden Sie die Eigenschaften [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) und [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--) der Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

Die Eigenschaften [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) und [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--) sind Sammlungen, die mehrere Seitenumbrüche enthalten können. Jede Sammlung enthält mehrere Methoden zur Verwaltung von horizontalen und vertikalen Seitenumbrüchen.

### **Seitenumbrüche hinzufügen**

Um einen Seitenumbruch in einem Arbeitsblatt hinzuzufügen, fügen Sie vertikale und horizontale Seitenumbrüche an der angegebenen Zelle ein, indem Sie die Methoden [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#add-number-number-number-) und [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#add-number-number-number-) aufrufen. Jede **add**-Methode nimmt den Namen der Zelle, an der die Umbruchsmarkierung gesetzt werden soll.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Add a page break at cell Y30
workbook.getWorksheets().get(0).getHorizontalPageBreaks().add("Y30");
workbook.getWorksheets().get(0).getVerticalPageBreaks().add("Y30");

// Save the Excel file.
workbook.save(path.join(dataDir, "AddingPageBreaks_out.xls"));
```

{{% alert color="primary" %}}

Im Vorschau-Modus für Seitenumbrüche oder im Druckvorschau-Modus können Sie sehen, wie diese Seitenumbrüche funktionieren.

{{% /alert %}}

### **Bestimmten Seitenumbruch entfernen**

 Um einen spezifischen Seitenumbruch zu entfernen, rufen Sie die Methoden [**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#removeAt-number-) und [**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#removeAt-number-) auf. Jede **removeAt**-Methode nimmt den Index des zu entfernenden Seitenumbruchs.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageBreaks.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Removing a specific page break
workbook.getWorksheets().get(0).getHorizontalPageBreaks().removeAt(0);
workbook.getWorksheets().get(0).getVerticalPageBreaks().removeAt(0);

// Save the Excel file.
workbook.save(path.join(dataDir, "RemoveSpecificPageBreak_out.xls"));
```

## **Wichtig zu wissen**

 Wenn Sie die Eigenschaften **fitToPages** (also [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) und [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--)) in den Seiteneinrichtungsoptionen setzen, werden die Seitenumbruch-Einstellungen beeinflusst, sodass beim Drucken des Arbeitsblatts die Seitenumbrüche zwar gesetzt, aber nicht berücksichtigt werden.
{{< app/cells/assistant language="nodejs-cpp" >}}
