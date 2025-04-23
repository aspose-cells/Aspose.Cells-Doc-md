---
title: Shared Formel mit Node.js über C++ festlegen
linktitle: Einstellung gemeinsamer Formel
type: docs
weight: 10
url: /de/nodejs-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

Wenn Sie eine Funktion in einem Arbeitsblatt hinzufügen möchten, die Berechnungen durchführt, erklärt dieser Artikel, wie Sie diese Aufgabe mit Aspose.Cells for Node.js via C++ erreichen.

{{% /alert %}}

## Gemeinsame Formel mit Aspose.Cells for Node.js via C++ festlegen

Angenommen, Sie haben ein Arbeitsblatt mit Daten im Format, das wie das folgende Beispieldatenblatt aussieht.

|**Eingabedatei mit einer Spalte Daten**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Sie möchten eine Funktion in B2 hinzufügen, die die Umsatzsteuer für die erste Datensatzreihe berechnet. Die Steuer beträgt **9%**. Die Formel zur Berechnung der Umsatzsteuer lautet: **"=A2*0,09"**. In diesem Artikel wird erläutert, wie diese Formel mit Aspose.Cells angewendet wird.

Mit Aspose.Cells können Sie eine Formel mit der Eigenschaft [**Cell.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) angeben. Es gibt zwei Optionen, um Formeln zu den anderen Zellen (B3, B4, B5 usw.) in der Spalte hinzuzufügen.

Entweder tun Sie das, was Sie für die erste Zelle gemacht haben, indem Sie die Formel effektiv für jede Zelle festlegen und die Zellreferenz entsprechend aktualisieren (A3*0.09, A4*0.09, A5*0.09 und so weiter). Dies erfordert, dass die Zellreferenzen für jede Zeile aktualisiert werden. Es erfordert auch, dass Aspose.Cells jede Formel einzeln parst, was bei großen Tabellen und komplexen Formeln zeitaufwendig sein kann. Es fügt auch zusätzliche Zeilen Code hinzu, obwohl Schleifen sie etwas reduzieren können.

Ein anderer Ansatz ist die Verwendung einer **gemeinsamen Formel**. Mit einer gemeinsamen Formel werden die Formeln automatisch für die Zellbezüge in jeder Zeile aktualisiert, sodass die Steuer ordnungsgemäß berechnet wird. Die Methode [**Cell.setSharedFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setSharedFormula-string-number-number-) ist effizienter als die erste Methode.

Das folgende Beispiel zeigt, wie es verwendet wird.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook from existing file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Get the cells collection in the first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Apply the shared formula in the range i.e.., B2:B14
cells.get("B2").setSharedFormula("=A2*0.09", 13, 1);

// Save the excel file
workbook.save(path.join(dataDir, "Output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
