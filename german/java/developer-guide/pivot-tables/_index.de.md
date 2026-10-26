---
title: PivotTable erstellen
linktitle: PivotTable erstellen
description: Erstellen und formatieren Sie PivotTables mit Aspose.Cells for Java.
keywords: PivotTable erstellen, PivotTable einfügen, PivotTable formatieren.
type: docs
weight: 160
url: /de/java/create-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Was ist eine PivotTable?**
Eine PivotTable ist ein interaktiver Bericht mit Zusammenfassungen: Sie verdichtet einen großen Block roher, zeilenweise angeordneter Daten zu einer kompakten Matrix, ohne dass eine einzige Formel benötigt wird. Sie legen fest, welche Spalten zu Zeilenbeschriftungen, welche zu Spaltenbeschriftungen werden und welche als Werte aggregiert werden – die PivotTable übernimmt die Gruppierung und die Berechnung:
- **Zusammenfassen** – Gesamtumsatz pro Produkt, pro Region oder pro Quartal anstelle langer Formelketten.
- **Vergleichen** – Kategorien in den Zeilen und Perioden in den Spalten verwandeln eine flache Liste in einen Kreuzbericht, in dem Trends auf einen Blick erkennbar sind.
- **Detailebene öffnen** – Doppelklicken Sie auf einen beliebigen Zusammenfassungswert, um die zugrunde liegenden Quellzeilen einzusehen.
- **Aktualisieren** – Wenn sich die Quelldaten ändern, wird der gesamte Bericht mit einer einzigen Aktualisierung neu berechnet.
Typische Anwendungsfälle sind Vertriebs-Dashboards, Kostenaufschlüsselungen und Bestandsanalysen – jede Frage der Form „Wie lassen sich diese Zahlen nach Kategorie und Zeit aufschlüsseln?“. Aspose.Cells for Java erstellt entsprechende PivotTables programmatisch, sodass die von Ihrer Anwendung generierten Arbeitsmappen einsatzbereite Berichte statt ausschließlich roher Daten enthalten können.

### **Erstellen einer PivotTable mit Aspose.Cells**

{{% alert color="primary" %}}
Mit Aspose.Cells ist es möglich, PivotTables zu Arbeitsblättern hinzuzufügen. Aspose.Cells verfügt über eine Reihe spezieller Klassen, die gezielt zum Erstellen und Steuern von PivotTables verwendet werden. Diese Klassen dienen dazu, ein [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)-Objekt zu erstellen und dessen Eigenschaften festzulegen. Sie bilden die Grundbausteine für den Aufbau von PivotTables.
Die verfügbaren PivotTable-Objekte sind:
- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): stellt ein Feld in einer PivotTable dar.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): stellt eine Sammlung aller [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)-Objekte in der PivotTable dar.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): stellt eine PivotTable dar.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): stellt die Sammlung aller PivotTable-Objekte auf dem Arbeitsblatt dar.
{{% /alert %}}

### **Erstellen einer einfachen PivotTable**
Das Erstellen einer PivotTable erfolgt in drei Schritten: Schreiben Sie die Quelldaten in Zellen des Arbeitsblatts, fügen Sie die PivotTable an der Zielposition hinzu und ordnen Sie die PivotTable-Felder dem Zeilen-, Spalten- und Datenbereich zu.
1. Fügen Sie mithilfe der [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setValue-java.lang.Object-)-Methode des [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-Objekts Daten in Zellen des Arbeitsblatts ein (`putValue` in den meisten Beispielen). Diese Daten werden als Datenquelle der PivotTable verwendet.
2. Fügen Sie dem Arbeitsblatt eine PivotTable hinzu, indem Sie die [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-)-Methode der Klasse [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) aufrufen: `add(sourceData, row, column)`. `sourceData` ist der Quellbereich (zum Beispiel "A1:C8"); `row` und `column` sind die nullbasierten Koordinaten der Zielzelle, die sich an der oberen linken Ecke der PivotTable befindet (Zelle E3 bedeutet Zeile 2, Spalte 4). Die Methode gibt das neue [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)-Objekt direkt zurück.
3. Ordnen Sie die PivotTable-Felder mithilfe der `addFieldToArea`-Methode des [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)-Objekts zu: Der Name eines Felds wird dem Zeilenbereich (`PivotFieldType.ROW`), dem Spaltenbereich (`PivotFieldType.COLUMN`) oder dem Datenbereich (`PivotFieldType.DATA`) zugeordnet.
4. Speichern Sie die Arbeitsmappe – die PivotTable wird in die gespeicherte Datei geschrieben.
Das folgende Codebeispiel erstellt entsprechend diesen Schritten eine einfache PivotTable. Bei der Ausführung wird dem Arbeitsblatt eine auf den Quelldaten basierende PivotTable hinzugefügt:
![todo:image_alt_text](create-pivot-table_1.png)

```java
import com.aspose.cells.*;

// Erstellen Sie eine neue Arbeitsmappe und rufen Sie das erste Arbeitsblatt ab
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// Schreiben Sie die Quelldaten: Umsatz pro Sport und Quartal
cells.get("A1").putValue("Sport");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Sales");
cells.get("A2").putValue("Golf");
cells.get("B2").putValue("Qtr3");
cells.get("C2").putValue(1500);
cells.get("A3").putValue("Golf");
cells.get("B3").putValue("Qtr4");
cells.get("C3").putValue(2000);
cells.get("A4").putValue("Tennis");
cells.get("B4").putValue("Qtr3");
cells.get("C4").putValue(600);
cells.get("A5").putValue("Tennis");
cells.get("B5").putValue("Qtr4");
cells.get("C5").putValue(1500);
cells.get("A6").putValue("Tennis");
cells.get("B6").putValue("Qtr3");
cells.get("C6").putValue(4070);
cells.get("A7").putValue("Tennis");
cells.get("B7").putValue("Qtr4");
cells.get("C7").putValue(5000);
cells.get("A8").putValue("Golf");
cells.get("B8").putValue("Qtr3");
cells.get("C8").putValue(6430);

// Fügen Sie eine Pivot-Tabelle in der Zelle E3 hinzu, deren Datenquelle A1:C8 ist
PivotTable pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Weisen Sie die Pivot-Felder zu: Sport zu Zeilen, Quartal zu Spalten, Umsatz zu Daten
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");

// Speichern Sie die Arbeitsmappe
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Wenn ein Zellbereich als Datenquelle zugewiesen wird, muss der Bereich von der linken oberen Ecke bis zur rechten unteren Ecke angegeben werden. Beispielsweise ist "A1:C3" gültig; "C3:A1" ist ungültig.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}