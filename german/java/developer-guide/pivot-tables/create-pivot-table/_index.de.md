---
title: Pivot Tabelle erstellen
type: docs
weight: 10
url: /de/java/create-pivot-table/
---

## **Pivot-Tabelle erstellen**

### **Pivot-Tabelle mit Aspose.Cells erstellen**

{{% alert color="primary" %}}

Mit Aspose.Cells ist es möglich, Pivot-Tabellen zu Arbeitsmappen hinzuzufügen. Aspose.Cells verfügt über eine Reihe spezieller Klassen, die speziell zur Erstellung und Steuerung von Pivot-Tabellen verwendet werden. Diese Klassen werden zum Erstellen und Setzen der Eigenschaften eines [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)-Objekts verwendet, das als Bausteine der Pivot-Tabelle dient.

Die Pivot-Tabellenobjekte sind:

- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): es repräsentiert ein Feld in einer Pivot-Tabelle.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): es repräsentiert eine Sammlung aller [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)-Objekte in der Pivot-Tabelle.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): es repräsentiert eine Pivot-Tabelle.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): es repräsentiert die Sammlung aller Pivot-Tabellenobjekte auf dem Arbeitsblatt.

{{% /alert %}}

### **Erstellen einer einfachen Pivot-Tabelle**

Um eine Pivot-Tabelle mit Aspose.Cells zu erstellen, befolgen Sie bitte die folgenden Schritte:

1. Fügen Sie einige Daten zu Arbeitsblattzellen hinzu, indem Sie die [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-Methode des [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)-Objekts verwenden. Diese Daten werden als Datenquelle für die Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die Methode [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-java.lang.String-) der Klasse [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) aufrufen, die im [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-Objekt encapsulated ist.
1. Greifen Sie von der [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) auf das [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)-Objekt zu, indem Sie den [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)-Index übergeben.
1. Verwenden Sie eines der oben erklärten Pivot-Tabellenobjekte, die im [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)-Objekt encapsulated sind, um die Pivot-Tabelle zu verwalten.

{{% alert color="primary" %}}

Beim Zuweisen eines Zellenbereichs als Datenquelle muss der Bereich von links oben nach rechts unten festgelegt sein. Zum Beispiel ist "A1:C3" gültig; "C3:A1" ist ungültig.

{{% /alert %}}

Das nachfolgende Codebeispiel zeigt, wie man eine einfache Pivot-Tabelle gemäß den oben aufgeführten Grundschritten erstellt. Beim Ausführen des Codes wird eine Pivot-Tabelle dem Arbeitsblatt hinzugefügt:

**Erstellen einer Pivot-Tabelle basierend auf einem entsprechenden Feld**

![todo:image_alt_text](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
