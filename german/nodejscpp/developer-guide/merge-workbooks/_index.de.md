---
title: Zusammenführen mehrerer Arbeitsmappen in eine einzelne Arbeitsmappe mit Node.js über C++
linktitle: Arbeitsmappen Zusammenführung
type: docs
weight: 66
url: /de/nodejs-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Erfahren Sie, wie Sie mehrere Arbeitsmappen mit Aspose.Cells for Node.js via C++ in eine einzige Arbeitsmappe zusammenfassen. 
---

{{% alert color="primary" %}}

Manchmal müssen Sie Arbeitsmappen mit verschiedenen Inhalten wie Bildern, Diagrammen und Daten in eine einzige Arbeitsmappe zusammenführen. Aspose.Cells for Node.js via C++ unterstützt diese Funktion. Dieser Artikel zeigt, wie man eine Konsolenanwendung erstellt und Arbeitsmappen mit wenigen, einfachen Codezeilen mithilfe von Aspose.Cells zusammenführt.

{{% /alert %}}

## **Arbeitsbücher mit Bildern und Diagrammen kombinieren**

Der Beispielcode verbindet zwei Arbeitsmappen zu einer einzigen Arbeitsmappe mithilfe von Aspose.Cells for Node.js via C++. Der Code lädt die Quellarbeitsmappen, verwendet die [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-)-Methode, um sie zu kombinieren, und speichert die Ausgabearbeitsmappe.

### **Quell-Arbeitsbücher**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Ausgabearbeitsbücher**

- [combined.xlsx](5473095.xlsx)

### **Screenshots**

Nachfolgend finden Sie Screenshots der Quell- und Ausgabearbeitsbücher.

{{% alert color="primary" %}}

Sie können beliebige Quellarbeitsmappen verwenden. Diese Bilder dienen nur zur Veranschaulichung.

{{% /alert %}}

**Die erste Arbeitsblatt der Diagramme Arbeitsmappe - gestapelt** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Zweites Arbeitsblatt der Diagramme Arbeitsmappe - Linie** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Erstes Arbeitsblatt der Bild Arbeitsmappe - Bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Alle drei Arbeitsblätter in der kombinierten Arbeitsmappe - gestapelt, Linie, Bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define the first source
// Open the first excel file.
const sourceBook1 = new AsposeCells.Workbook(path.join(dataDir, "SampleChart.xlsx"));

// Define the second source book.
// Open the second excel file.
const sourceBook2 = new AsposeCells.Workbook(path.join(dataDir, "SampleImage.xlsx"));

// Combining the two workbooks
sourceBook1.combine(sourceBook2);

const outputPath = path.join(dataDir, "Combined.out.xlsx");
// Save the target book file.
sourceBook1.save(outputPath);
```

## **Erweiterte Themen**
- [Mehrere Arbeitsblätter in ein einziges Arbeitsblatt kombinieren](/cells/de/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Dateien zusammenführen](/cells/de/nodejs-cpp/merge-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}
