---
title: PivotTable einfügen
linktitle: PivotTable einfügen
description: Erstellen und formatieren Sie PivotTables mit Aspose.Cells for Node.js über C++.
keywords: PivotTable erstellen, PivotTable einfügen, PivotTable formatieren.
type: docs
weight: 160
url: /de/nodejs-cpp/create-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Was ist eine PivotTable?**
Eine PivotTable ist ein interaktiver Zusammenfassungsbericht: Sie verdichtet einen großen Bestand an Rohdaten, die Zeile für Zeile erfasst wurden, zu einer kompakten Matrix, ohne dass eine einzige Formel erforderlich ist. Sie legen fest, welche Spalten zu Zeilenbeschriftungen, welche zu Spaltenbeschriftungen und welche als Werte aggregiert werden – die PivotTable übernimmt die Gruppierung und die Berechnung:
- **Zusammenfassen** – den Gesamtumsatz pro Produkt, pro Region oder pro Quart anzeigen, anstatt lange Formelketten zu verwenden.
- **Vergleichen** – Kategorien in den Zeilen und Zeiträume in den Spalten verwandeln eine flache Liste in einen Kreuztabellenbericht, in dem Trends auf einen Blick erkennbar sind.
- **Details anzeigen** – Doppelklicken Sie auf einen Zusammenfassungswert, um die zugrunde liegenden Quellzeilen zu prüfen.
- **Aktualisieren** – Wenn sich die Quelldaten ändern, berechnet eine einzige Aktualisierung den gesamten Bericht neu.
Typische Anwendungsfälle sind Vertriebs-Dashboards, Kostenaufschlüsselungen und Bestandsanalysen, um Fragen der Form „Wie verteilen sich diese Zahlen nach Kategorie und Zeit?“ zu beantworten. Aspose.Cells for Node.js über C++ erstellt dieselben PivotTables programmatisch, sodass die von Ihrer Anwendung generierten Arbeitsmappen fertige Berichte statt ausschließlich Rohdaten enthalten können.

### **PivotTable-Objektmodell**
Aspose.Cells for Node.js über C++ stellt einen speziellen Satz von Klassen bereit, mit denen PivotTables erstellt und gesteuert werden. Diese Klassen dienen zum Erstellen und Konfigurieren von [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)-Objekten, den Bausteinen einer PivotTable. Die Objekte sind:
- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) stellt ein Feld in einer [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) dar.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) stellt eine Sammlung aller [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield)-Objekte in der [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) dar.
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) stellt eine PivotTable auf einem Arbeitsblatt dar.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) stellt eine Sammlung aller [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)-Objekte auf einem Arbeitsblatt dar.

### **Eine einfache PivotTable mit Aspose.Cells erstellen**
Das Erstellen einer PivotTable erfolgt in drei Schritten: Schreiben Sie die Quelldaten in Zellen eines Arbeitsblatts, fügen Sie die PivotTable an der Zielposition hinzu und platzieren Sie die PivotTable-Felder in den Zeilen-, Spalten- und Datenbereichen.
1. Fügen Sie mithilfe der Methode [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) des Objekts [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) Daten zu einem Arbeitsblatt hinzu. Diese Daten dienen als Datenquelle der PivotTable.
2. Fügen Sie die PivotTable zum Arbeitsblatt hinzu, indem Sie die Methode [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) der Sammlung [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) aufrufen: `add(sourceData, row, column)`. `sourceData` ist der Quellbereich (zum Beispiel "A1:C8"); `row` und `column` sind die nullbasierten Koordinaten der Zielzelle an der linken oberen Ecke der PivotTable (Zelle E3 bedeutet Zeile 2, Spalte 4). Die Methode gibt das neue Objekt [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) direkt zurück.
3. Platzieren Sie die PivotTable-Felder mit der Methode `addFieldToArea` des Objekts [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable): Ein Feldname wird dem Zeilenbereich (`PivotFieldType.Row`), dem Spaltenbereich (`PivotFieldType.Column`) oder dem Datenbereich (`PivotFieldType.Data`) zugeordnet.
4. Speichern Sie die Arbeitsmappe – die PivotTable wird in die gespeicherte Datei geschrieben.
Nach der Ausführung des Beispielcodes wird die PivotTable dem Arbeitsblatt hinzugefügt.

```javascript
const AsposeCells = require("aspose.cells.node");

// Erstellen Sie eine neue Arbeitsmappe und rufen Sie das erste Arbeitsblatt ab
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Schreiben Sie die Quelldaten: Umsätze pro Sportart und Quartal
sheet.getCells().get("A1").putValue("Sport");
sheet.getCells().get("B1").putValue("Quarter");
sheet.getCells().get("C1").putValue("Sales");
sheet.getCells().get("A2").putValue("Golf");
sheet.getCells().get("B2").putValue("Qtr3");
sheet.getCells().get("C2").putValue(1500);
sheet.getCells().get("A3").putValue("Golf");
sheet.getCells().get("B3").putValue("Qtr4");
sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Tennis");
sheet.getCells().get("B4").putValue("Qtr3");
sheet.getCells().get("C4").putValue(600);
sheet.getCells().get("A5").putValue("Tennis");
sheet.getCells().get("B5").putValue("Qtr4");
sheet.getCells().get("C5").putValue(1500);
sheet.getCells().get("A6").putValue("Tennis");
sheet.getCells().get("B6").putValue("Qtr3");
sheet.getCells().get("C6").putValue(4070);
sheet.getCells().get("A7").putValue("Tennis");
sheet.getCells().get("B7").putValue("Qtr4");
sheet.getCells().get("C7").putValue(5000);
sheet.getCells().get("A8").putValue("Golf");
sheet.getCells().get("B8").putValue("Qtr3");
sheet.getCells().get("C8").putValue(6430);

// Fügen Sie in der Zielzelle E3 eine Pivot-Tabelle hinzu, die aus A1:C8 stammt
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Weisen Sie die Pivot-Felder zu: Sportart zu Zeilen, Quartal zu Spalten, Umsätze zu Daten
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");

// Speichern Sie die Arbeitsmappe
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Beim Zuweisen eines Zellbereichs als Datenquelle muss der Bereich von oben links nach unten rechts verlaufen. Beispielsweise ist "A1:C3" gültig, "C3:A1" jedoch nicht.
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}