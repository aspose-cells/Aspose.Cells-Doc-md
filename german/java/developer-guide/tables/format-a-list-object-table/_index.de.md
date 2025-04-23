---
title: Formatieren Sie ein List Objekt  Tabelle
type: docs
weight: 50
url: /de/java/format-a-list-object-table/
---

{{% alert color="primary" %}}

Um eine Gruppe von verwandten Daten zu verwalten und zu analysieren, ist es möglich, einen Bereich von Zellen in ein Listenobjekt (auch bekannt als Excel-Tabelle) umzuwandeln. Eine Tabelle ist eine Reihe von Zeilen und Spalten, die verwandte Daten enthalten und unabhängig von den Daten in anderen Zeilen und Spalten verwaltet werden. Standardmäßig ist in jeder Spalte der Tabelle in der Kopfzeile die Filterung aktiviert, sodass Sie Ihre Listenaufzugsdaten schnell filtern oder sortieren können. Sie können eine Gesamtzeile (eine spezielle Zeile in einer Liste, die eine Auswahl von Aggregatfunktionen bereitstellt, die für die Arbeit mit numerischen Daten nützlich sind) zu dem Listenobjekt hinzufügen, um eine Dropdown-Liste von Aggregatfunktionen für jede Zellen in der Gesamtzeile bereitzustellen. Aspose.Cells bietet Optionen zum Erstellen und Verwalten von Listen (oder Tabellen).

{{% /alert %}}

## **Formatierung eines Listenobjekts**

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)-Sammlung, die den Zugriff auf jede Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um ein [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) in einem Arbeitsblatt zu erstellen, verwenden Sie die Sammlungseigenschaft [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) der Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Jedes [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) ist in der Tat ein Objekt der Klasse [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection), das die add-Methode bereitstellt, um eine List-Objekt hinzuzufügen und den Zellbereich anzugeben, den es umfassen soll. Entsprechend dem angegebenen Zellbereich wird durch Aspose.Cells ein [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) im Arbeitsblatt erstellt. Verwenden Sie Attribute (z.B. [**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType-) der Klasse [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)), um die Tabelle nach Ihren Anforderungen zu formatieren.

Das folgende Beispiel fügt Beispieldaten einem Arbeitsblatt hinzu, fügt ein [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) hinzu und wendet Standardstile darauf an. [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) Stile werden von Microsoft Excel 2007/2010 unterstützt.

Die folgende Ausgabe wird generiert, wenn der Code ausgeführt wird.

**Eine formatierte Tabelle wird im Arbeitsblatt erstellt** 

![todo:image_alt_text](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
{{< app/cells/assistant language="java" >}}
