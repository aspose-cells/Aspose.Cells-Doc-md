---
title: PivotTable einfügen
linktitle: PivotTable einfügen
description: Erstellen und formatieren Sie PivotTables in Excel-Arbeitsmappendateien.
keywords: PivotTable erstellen, PivotTable einfügen, PivotTable formatieren.
type: docs
weight: 160
url: /de/net/create-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Was ist eine PivotTable?**
Eine PivotTable ist ein interaktiver Zusammenfassungsbericht: Sie verdichtet einen großen Block zeilenweise erfasster Rohdaten in einer kompakten Matrix, ohne eine einzige Formel zu verwenden. Sie legen fest, welche Spalten zu Zeilenbeschriftungen, welche zu Spaltenbeschriftungen werden und welche als Werte aggregiert werden – die PivotTable übernimmt die Gruppierung und die Berechnung:
- **Zusammenfassen** – Gesamtumsatz pro Produkt, pro Region oder pro Quart anstelle langer Formelketten.
- **Vergleichen** – Kategorien in den Zeilen und Zeiträume in den Spalten verwandeln eine flache Liste in einen Kreuzbericht, in dem Trends auf einen Blick erkennbar sind.
- **Detaillierte Daten anzeigen** – Doppelklicken Sie auf einen Zusammenfassungswert, um die zugrunde liegenden Quellzeilen einzusehen.
- **Aktualisieren** – Wenn sich die Quelldaten ändern, berechnet eine einzige Aktualisierung den gesamten Bericht neu.
Typische Anwendungsfälle sind Vertriebs-Dashboards, Kostenaufschlüsselungen und Bestandsanalysen. Mit PivotTables lassen sich zudem Fragen der Form „Wie lassen sich diese Zahlen nach Kategorie und Zeit aufschlüsseln?“ beantworten. Aspose.Cells for .NET erstellt dieselben PivotTables programmatisch, sodass die von Ihrer Anwendung generierten Arbeitsmappen einsatzbereite Berichte statt ausschließlich Rohdaten enthalten können.

### **Objektmodell der PivotTable**
Aspose.Cells stellt eine Reihe spezialisierter Klassen im [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) namespace bereit, mit denen PivotTables erstellt und gesteuert werden. Mit diesen Klassen werden [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-Objekte erstellt und konfiguriert, die den Kern einer PivotTable bilden. Die Objekte sind:
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) stellt ein Feld in einer [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) dar.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) stellt eine Sammlung aller [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)-Objekte in der [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) dar.
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) repräsentiert eine PivotTable auf einem Arbeitsblatt.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) repräsentiert eine Sammlung aller [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-Objekte auf einem Arbeitsblatt.

### **Erstellen einer einfachen PivotTable mit Aspose.Cells**
Eine PivotTable wird in drei Schritten erstellt und anschließend gespeichert:
1. Fügen Sie mithilfe der Methode [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) des [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-Objekts Daten zu einem Arbeitsblatt hinzu. Diese Daten dienen als Datenquelle der PivotTable.
2. Fügen Sie dem Arbeitsblatt eine PivotTable hinzu, indem Sie die Methode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) der Sammlung [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) aufrufen: `Add(sourceData, row, column)`. `sourceData` ist der Quellbereich (zum Beispiel "A1:C8"); `row` und `column` sind die 0-basierten Koordinaten der Zielzelle am linken oberen Eck der PivotTable (Zelle E3 bedeutet Zeile 2, Spalte 4). Die Methode gibt das neue [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-Objekt direkt zurück.
3. Ordnen Sie die Felder mithilfe der Methode `AddFieldToArea` des [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-Objekts zu: Ein Feldname wird dem Zeilenbereich (`PivotFieldType.Row`), dem Spaltenbereich (`PivotFieldType.Column`) oder dem Datenbereich (`PivotFieldType.Data`) zugeordnet.
4. Speichern Sie die Arbeitsmappe – die PivotTable wird in die gespeicherte Datei geschrieben.
Nach der Ausführung des Beispielcodes wird dem Arbeitsblatt eine PivotTable hinzugefügt.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Eine neue Arbeitsmappe erstellen und das erste Arbeitsblatt abrufen
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// Die Quelldaten schreiben: Umsätze pro Sportart und Quartal
sheet.Cells["A1"].PutValue("Sport");
sheet.Cells["B1"].PutValue("Quarter");
sheet.Cells["C1"].PutValue("Sales");
sheet.Cells["A2"].PutValue("Golf");
sheet.Cells["B2"].PutValue("Qtr3");
sheet.Cells["C2"].PutValue(1500);
sheet.Cells["A3"].PutValue("Golf");
sheet.Cells["B3"].PutValue("Qtr4");
sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Tennis");
sheet.Cells["B4"].PutValue("Qtr3");
sheet.Cells["C4"].PutValue(600);
sheet.Cells["A5"].PutValue("Tennis");
sheet.Cells["B5"].PutValue("Qtr4");
sheet.Cells["C5"].PutValue(1500);
sheet.Cells["A6"].PutValue("Tennis");
sheet.Cells["B6"].PutValue("Qtr3");
sheet.Cells["C6"].PutValue(4070);
sheet.Cells["A7"].PutValue("Tennis");
sheet.Cells["B7"].PutValue("Qtr4");
sheet.Cells["C7"].PutValue(5000);
sheet.Cells["A8"].PutValue("Golf");
sheet.Cells["B8"].PutValue("Qtr3");
sheet.Cells["C8"].PutValue(6430);

// Eine Pivot-Tabelle in der Zielzelle E3 hinzufügen, basierend auf A1:C8
PivotTable pivotTable = sheet.PivotTables.Add("A1:C8", 2, 4);

// Pivotfelder zuweisen: Sport zu Zeilen, Quarter zu Spalten, Sales zu Daten
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Quarter");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");

// Die Arbeitsmappe speichern
workbook.Save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Wenn ein Zellbereich als Datenquelle zugewiesen wird, muss der Bereich von oben links nach unten rechts verlaufen. Beispielsweise ist "A1:C3" gültig, "C3:A1" jedoch nicht.
{{% /alert %}}

## Verwandte Artikel
- [Filterfelder zu einer PivotTable in Aspose.Cells for .NET hinzufügen](/cells/de/net/add-page-field-in-pivot-table/)
- [Stile auf PivotTables in Aspose.Cells for .NET anwenden](/cells/de/net/apply-style-to-pivot-table/)
- [Layout des Seitenfelds in einer PivotTable ändern](/cells/de/net/change-page-field-layout/)
- [PivotTables nach Beschriftung oder Wert filtern](/cells/de/net/filter-by-label-or-value-of-pivot-table/)
- [Wertfelder von PivotTables in Aspose.Cells for .NET verwalten](/cells/de/net/manage-value-fields/)

{{< app/cells/assistant language="csharp" >}}