---
title: Pivot-Tabelle formatieren
type: docs
weight: 60
url: /de/java/formatting-pivot-table/
---
## **Aussehen der Pivot-Tabelle**

[So erstellen Sie eine Pivot-Tabelle](/cells/de/java/create-pivot-table/) zeigte, wie man eine einfache Pivot-Tabelle erstellt. Dieser Artikel geht weiter und erläutert, wie Sie das Erscheinungsbild einer Pivot-Tabelle anpassen, indem Sie Eigenschaften festlegen.

### **Formatoptionen für Pivot-Tabellen festlegen**

 Das[**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) -Klasse können Sie verschiedene Formatierungsoptionen für eine Pivot-Tabelle festlegen.

#### **Festlegen der AutoFormat- und PivotTableStyle-Typen**

 Das folgende Codebeispiel veranschaulicht, wie Sie den automatischen Formattyp und den Pivot-Tabellenstiltyp mithilfe von festlegen[**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) und[**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType) Eigenschaften.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Formatoptionen einstellen**

Das folgende Codebeispiel veranschaulicht, wie Sie eine Reihe von Formatierungsoptionen für einen Pivot-Tabellenbericht festlegen, einschließlich des Hinzufügens von Gesamtsummen für Zeilen und Spalten.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **Festlegen von PivotFields-Formatoptionen**

Neben der Steuerung der Formatierung der gesamten Pivot-Tabelle ermöglicht Aspose.Cells for Java eine fein abgestimmte Steuerung der Formatierung für Zeilenfelder, Spaltenfelder und Seitenfelder.

#### **Festlegen des Zeilen-, Spalten- und Seitenfeldformats**

Das folgende Codebeispiel zeigt, wie Sie auf Zeilenfelder zugreifen, auf eine bestimmte Zeile zugreifen, Zwischensummen festlegen, die automatische Sortierung anwenden und die Option autoShow verwenden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Festlegen des Datenfeldformats**

Die folgenden Codezeilen veranschaulichen, wie Datenfelder formatiert werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Ändern Sie den Schnellstil einer Pivot-Tabelle**

Die folgenden Codebeispiele zeigen, wie der auf eine Pivot-Tabelle angewendete Schnellstil geändert wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Pivot-Felder löschen**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) hat eine Methode namens[**klar()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear()), die Pivot-Felder löscht. Verwenden Sie es, um Pivot-Felder in allen Bereichen zu löschen, z. B. Seite, Spalte, Zeile oder Daten.
Das folgende Codebeispiel zeigt, wie alle Pivot-Felder im Datenbereich gelöscht werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Konsolidierungsfunktion**

### **ConsolidationFunction auf Datenfelder der Pivot-Tabelle anwenden**

 Aspose.Cells kann verwendet werden, um ConsolidationFunction auf Datenfelder (oder Wertfelder) der Pivot-Tabelle anzuwenden. In Microsoft Excel können Sie mit der rechten Maustaste auf das Wertefeld klicken und dann auswählen**Wertfeldeinstellungen...** Option und wählen Sie dann die Registerkarte aus**Werte zusammenfassen nach**. Von dort aus können Sie eine beliebige Konsolidierungsfunktion Ihrer Wahl auswählen, z. B. Summe, Anzahl, Durchschnitt, Max, Min, Produkt, Distinct Count usw.

 Aspose.Cells bietet[**Konsolidierungsfunktion**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) Enumeration zur Unterstützung der folgenden Konsolidierungsfunktionen.

- [**Konsolidierungsfunktion.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**Konsolidierungsfunktion.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**Konsolidierungsfunktion.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**Konsolidierungsfunktion.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**Konsolidierungsfunktion.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**Konsolidierungsfunktion.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**Konsolidierungsfunktion.PRODUKT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**Konsolidierungsfunktion.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**Konsolidierungsfunktion.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**Konsolidierungsfunktion.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**Konsolidierungsfunktion.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**Konsolidierungsfunktion.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

 Es gilt der folgende Code**Durchschnitt** Konsolidierungsfunktion zum ersten Datenfeld (oder Wertfeld) und**DistinctCount** Konsolidierungsfunktion auf zweites Datenfeld (oder Wertefeld).

{{% alert color="primary" %}}

Die DistinctCount-Konsolidierungsfunktion wird nur von Microsoft Excel 2013 unterstützt.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
