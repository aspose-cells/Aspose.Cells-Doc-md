---  
title: Dynamische Diagramme mit Node.js über C++ erstellen  
linktitle: Dynamische Diagramme erstellen  
description: Lernen Sie, wie man in Aspose.Cells for Node.js via C++ dynamische Diagramme erstellt. Dieser Leitfaden zeigt Ihnen, wie Sie Daten, Serien und Formatierung von Diagrammen basierend auf Ihren Anforderungen dynamisch aktualisieren können, sodass Sie wechselnde Daten visuell in Ihren Tabellen darstellen können.  
keywords: Aspose.Cells für Node.js, Diagramme, dynamische Diagramme, Daten, Serien, Formatierung, Arbeitsblätter, Aktualisierung.  
type: docs  
weight: 240  
url: /de/nodejs-cpp/create-dynamic-charts/  
---  

{{% alert color="primary" %}}  
Dynamische (oder interaktive) Diagramme haben die Möglichkeit, sich zu ändern, wenn sich der Datenbereich ändert. Mit anderen Worten können sich die dynamischen Diagramme automatisch ändern, wenn sich die Datenquelle ändert. Um die Änderung in der Datenquelle auszulösen, kann die Filteroption von Excel-Tabellen verwendet werden oder ein Steuerelement wie Dropdown-Liste oder Kombinationsfeld.

Dieser Artikel demonstriert die Verwendung von Aspose.Cells for Node.js via C++ APIs zur Erstellung dynamischer Diagramme unter Verwendung beider oben genannter Ansätze.  
{{% /alert %}}  

## **Verwendung von Excel-Tabellen**  

{{% alert color="primary" %}}  
Excel-Tabellen werden aus Sicht von Aspose.Cells als ListObjects bezeichnet, daher verwenden wir den Begriff "ListObject" anstelle von "Tabelle" zur Klarheit. Bitte lesen Sie ausführlich, wie man [ListObjects erstellt](/cells/de/nodejs-cpp/create-and-format-table/) mit Aspose.Cells for Node.js via C++.  
{{% /alert %}}  

ListObjects bieten integrierte Funktionen zum Sortieren und Filtern der Daten durch Benutzerinteraktion. Beide Optionen werden über Dropdown-Listen bereitgestellt, die automatisch in die Kopfzeile des [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) eingefügt werden. Durch diese Funktionen (Sortieren und Filtern) erscheint das [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) als idealer Kandidat, um als Datenquelle für ein dynamisches Diagramm zu dienen, da sich die Darstellung im Diagramm ändert, wenn das Sortieren oder Filtern geändert wird, um den aktuellen Zustand des [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) widerzuspiegeln.

Um die Demonstration einfach verständlich zu halten, erstellen wir den [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) von Grund auf neu und gehen Schritt für Schritt vor, wie unten beschrieben.

1. Erstellen Sie ein leeres [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Zugriff auf das [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) des ersten [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) im [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Fügen Sie einige Daten in die Zellen ein.
1. Erstellen Sie [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) basierend auf den eingefügten Daten.
1. Erstellen Sie [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) basierend auf den Datenbereich von [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject).
1. Speichern Sie das Ergebnis auf der Festplatte.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const book = new AsposeCells.Workbook();
// Access first worksheet from the collection
const sheet = book.getWorksheets().get(0);
// Access cells collection of the first worksheet
const cells = sheet.getCells();

// Insert data column-wise
cells.get("A1").putValue("Category");
cells.get("A2").putValue("Fruit");
cells.get("A3").putValue("Fruit");
cells.get("A4").putValue("Fruit");
cells.get("A5").putValue("Fruit");
cells.get("A6").putValue("Vegetables");
cells.get("A7").putValue("Vegetables");
cells.get("A8").putValue("Vegetables");
cells.get("A9").putValue("Vegetables");
cells.get("A10").putValue("Beverages");
cells.get("A11").putValue("Beverages");
cells.get("A12").putValue("Beverages");

cells.get("B1").putValue("Food");
cells.get("B2").putValue("Apple");
cells.get("B3").putValue("Banana");
cells.get("B4").putValue("Apricot");
cells.get("B5").putValue("Grapes");
cells.get("B6").putValue("Carrot");
cells.get("B7").putValue("Onion");
cells.get("B8").putValue("Cabbage");
cells.get("B9").putValue("Potato");
cells.get("B10").putValue("Coke");
cells.get("B11").putValue("Coladas");
cells.get("B12").putValue("Fizz");

cells.get("C1").putValue("Cost");
cells.get("C2").putValue(2.2);
cells.get("C3").putValue(3.1);
cells.get("C4").putValue(4.1);
cells.get("C5").putValue(5.1);
cells.get("C6").putValue(4.4);
cells.get("C7").putValue(5.4);
cells.get("C8").putValue(6.5);
cells.get("C9").putValue(5.3);
cells.get("C10").putValue(3.2);
cells.get("C11").putValue(3.6);
cells.get("C12").putValue(5.2);

cells.get("D1").putValue("Profit");
cells.get("D2").putValue(0.1);
cells.get("D3").putValue(0.4);
cells.get("D4").putValue(0.5);
cells.get("D5").putValue(0.6);
cells.get("D6").putValue(0.7);
cells.get("D7").putValue(1.3);
cells.get("D8").putValue(0.8);
cells.get("D9").putValue(1.3);
cells.get("D10").putValue(2.2);
cells.get("D11").putValue(2.4);
cells.get("D12").putValue(3.3);

// Create ListObject, Get the List objects collection in the first worksheet
const listObjects = sheet.getListObjects();

// Add a List based on the data source range with headers on
let index = listObjects.add(0, 0, 11, 3, true);

sheet.autoFitColumns();

// Create chart based on ListObject
index = sheet.getCharts().add(AsposeCells.ChartType.Column, 21, 1, 35, 18);
const chart = sheet.getCharts().get(index);
chart.setChartDataRange("A1:D12", true);
chart.getNSeries().setCategoryData("A2:B12");

// Save spreadsheet
book.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Verwendung dynamischer Formeln**  

Falls Sie den [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) nicht als Datenquelle für das dynamische Diagramm verwenden möchten, besteht eine andere Möglichkeit darin, Excel-Funktionen (oder Formeln) zu verwenden, um einen dynamischen Datensatz zu erstellen, und ein Steuerelement (wie ComboBox), um die Datenänderung auszulösen. In diesem Szenario verwenden wir die VLOOKUP-Funktion, um die passenden Werte basierend auf der Auswahl in der ComboBox abzurufen. Bei Änderung der Auswahl aktualisiert sich die VLOOKUP-Funktion und aktualisiert die Zellenwerte. Wenn eine Zellenreihe die VLOOKUP-Funktion nutzt, kann der gesamte Bereich bei Benutzerinteraktion aktualisiert werden, sodass er als Quelle für das dynamische Diagramm genutzt werden kann.

Um die Demonstration einfach zu verstehen zu halten, werden wir die Arbeitsmappe von Grund auf erstellen und Schritt für Schritt wie unten skizziert fortfahren.

1. Erstellen Sie ein leeres [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Zugriff auf das [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) des ersten [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) im [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Fügen Sie einige Daten in die Zellen ein, indem Sie einen benannten Bereich erstellen. Diese Daten dienen als Serie für das dynamische Diagramm.
1. Erstellen Sie [**ComboBox**](https://reference.aspose.com/cells/nodejs-cpp/combobox) basierend auf dem in der vorherigen Schritt erstellten benannten Bereich.
1. Fügen Sie einige weitere Daten in die Zellen ein, die als Quelle für die VLOOKUP-Funktion dienen sollen.
1. Fügen Sie eine VLOOKUP-Funktion (mit den entsprechenden Parametern) in einen Zellbereich ein. Dieser Bereich dient als Quelle für das dynamische Diagramm.
1. Erstellen Sie [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) basierend auf dem im vorherigen Schritt erstellten Bereich.
1. Speichern Sie das Ergebnis auf der Festplatte.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range in the second worksheet
const range = worksheet.getCells().createRange("C21", "C24");

// Name the range
range.setName("MyRange");

// Fill different cells with data in the range
range.get(0, 0).putValue("North");
range.get(1, 0).putValue("South");
range.get(2, 0).putValue("East");
range.get(3, 0).putValue("West");

const comboBox = worksheet.getShapes().addComboBox(15, 0, 2, 0, 17, 64);
comboBox.setInputRange("=MyRange");
comboBox.setLinkedCell("=B16");
comboBox.setSelectedIndex(0);
const cell = worksheet.getCells().get("B16");
const style = cell.getStyle();
style.getFont().setColor(AsposeCells.Color.White);
cell.setStyle(style);

worksheet.getCells().get("C16").setFormula("=INDEX(Sheet1!$C$21:$C$24,$B$16,1)");

// Put some data for chart source
// Data Headers
worksheet.getCells().get("D15").putValue("Jan");
worksheet.getCells().get("D20").putValue("Jan");

worksheet.getCells().get("E15").putValue("Feb");
worksheet.getCells().get("E20").putValue("Feb");

worksheet.getCells().get("F15").putValue("Mar");
worksheet.getCells().get("F20").putValue("Mar");

worksheet.getCells().get("G15").putValue("Apr");
worksheet.getCells().get("G20").putValue("Apr");

worksheet.getCells().get("H15").putValue("May");
worksheet.getCells().get("H20").putValue("May");

worksheet.getCells().get("I15").putValue("Jun");
worksheet.getCells().get("I20").putValue("Jun");

// Data
worksheet.getCells().get("D21").putValue(304);
worksheet.getCells().get("D22").putValue(402);
worksheet.getCells().get("D23").putValue(321);
worksheet.getCells().get("D24").putValue(123);

worksheet.getCells().get("E21").putValue(300);
worksheet.getCells().get("E22").putValue(500);
worksheet.getCells().get("E23").putValue(219);
worksheet.getCells().get("E24").putValue(422);

worksheet.getCells().get("F21").putValue(222);
worksheet.getCells().get("F22").putValue(331);
worksheet.getCells().get("F23").putValue(112);
worksheet.getCells().get("F24").putValue(350);

worksheet.getCells().get("G21").putValue(100);
worksheet.getCells().get("G22").putValue(200);
worksheet.getCells().get("G23").putValue(300);
worksheet.getCells().get("G24").putValue(400);

worksheet.getCells().get("H21").putValue(200);
worksheet.getCells().get("H22").putValue(300);
worksheet.getCells().get("H23").putValue(400);
worksheet.getCells().get("H24").putValue(500);

worksheet.getCells().get("I21").putValue(400);
worksheet.getCells().get("I22").putValue(200);
worksheet.getCells().get("I23").putValue(200);
worksheet.getCells().get("I24").putValue(100);

// Dynamically load data on selection of Dropdown value
worksheet.getCells().get("D16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,2,FALSE),0)");
worksheet.getCells().get("E16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,3,FALSE),0)");
worksheet.getCells().get("F16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,4,FALSE),0)");
worksheet.getCells().get("G16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,5,FALSE),0)");
worksheet.getCells().get("H16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,6,FALSE),0)");
worksheet.getCells().get("I16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,7,FALSE),0)");

// Create Chart
const index = worksheet.getCharts().add(AsposeCells.ChartType.Column, 0, 3, 12, 9);
const chart = worksheet.getCharts().get(index);
chart.getNSeries().add("='Sheet1'!$D$16:$I$16", false);
chart.getNSeries().get(0).setName("=C16");
chart.getNSeries().setCategoryData("=$D$15:$I$15");

// Save result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
