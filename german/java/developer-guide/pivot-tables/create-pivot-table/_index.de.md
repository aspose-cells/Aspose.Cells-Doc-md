---
title: Pivot-Tabelle erstellen
type: docs
weight: 10
url: /de/java/create-pivot-table/
---
## **Pivot-Tabelle erstellen**

### **Erstellen Sie eine Pivot-Tabelle mit Aspose.Cells**

{{% alert color="primary" %}}

 Mit Aspose.Cells ist es möglich, Tabellenkalkulationen Pivot-Tabellen hinzuzufügen. Aspose.Cells verfügt über eine Reihe spezieller Klassen, die speziell zum Erstellen und Steuern von Pivot-Tabellen verwendet werden. Diese Klassen werden verwendet, um die Eigenschaften von a zu erstellen und festzulegen[**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)-Objekt, das als Pivot-Tabellenbausteine verwendet wird.

Die Pivot-Tabellenobjekte sind:

- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): Es repräsentiert ein Feld in einer Pivot-Tabelle.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) : Es stellt eine Sammlung aller dar[**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)Objekte in der Pivot-Tabelle.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): Es stellt eine Pivot-Tabelle dar.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): Es stellt die Sammlung aller Pivot-Tabellenobjekte auf dem Arbeitsblatt dar.

{{% /alert %}}

### **Erstellen einer einfachen Pivot-Tabelle**

Um eine Pivot-Tabelle mit Aspose.Cells zu erstellen, führen Sie bitte die folgenden Schritte aus:

1.  Fügen Sie einige Daten zu Arbeitsblattzellen hinzu, indem Sie die verwenden[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Objekt[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)Methode. Diese Daten werden als Datenquelle für die Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die aufrufen[**hinzufügen**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add(com.aspose.cells.PivotTable,%20int,%20int,%20java.lang.String) ) Methode der[**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) Klasse, gekapselt in der[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)Objekt.
1.  Greife auf ... zu[**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) Objekt aus der[**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) durch das Passieren der[**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)Index.
1.  Verwenden Sie eines der (oben erläuterten) Pivot-Tabellenobjekte, die in gekapselt sind[**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)Objekt zum Verwalten der Pivot-Tabelle.

{{% alert color="primary" %}}

Bei der Zuweisung eines Zellbereichs als Datenquelle muss der Bereich von links oben nach rechts unten eingestellt werden. Beispielsweise ist "A1:C3" gültig; "C3:A1" ist ungültig.

{{% /alert %}}

Das folgende Codebeispiel zeigt, wie Sie anhand der oben aufgeführten grundlegenden Schritte eine einfache Pivot-Tabelle erstellen. Beim Ausführen des Codes wird dem Arbeitsblatt eine Pivot-Tabelle hinzugefügt:

**Erstellen einer Pivot-Tabelle basierend auf einem entsprechenden Feld**

![todo: Bild_alt_Text](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
