---
title: Formatieren Sie ein Listenobjekt - Tabelle
type: docs
weight: 50
url: /de/java/format-a-list-object-table/
---
{{% alert color="primary" %}}

Um eine Gruppe verwandter Daten zu verwalten und zu analysieren, ist es möglich, einen Zellbereich in ein Listenobjekt (auch bekannt als Excel-Tabelle) umzuwandeln. Eine Tabelle ist eine Reihe von Zeilen und Spalten, die zugehörige Daten enthalten, die unabhängig von den Daten in anderen Zeilen und Spalten verwaltet werden. Standardmäßig ist für jede Spalte in der Tabelle die Filterung in der Kopfzeile aktiviert, sodass Sie Ihre Listenobjektdaten schnell filtern oder sortieren können. Sie können eine Summenzeile (eine spezielle Zeile in einer Liste, die eine Auswahl von Aggregatfunktionen bereitstellt, die für die Arbeit mit numerischen Daten nützlich sind) zu dem Listenobjekt hinzufügen, das eine Dropdown-Liste von Aggregatfunktionen für jede Summenzeilenzelle bereitstellt. Aspose.Cells bietet Optionen zum Erstellen und Verwalten von Listen (oder Tabellen).

{{% /alert %}}

## **Formatieren eines Listenobjekts**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um eine zu erstellen[**Listenobjekt**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) in einem Arbeitsblatt verwenden[**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) Sammlungseigentum der[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse. Jeder[**Listenobjekt**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) ist in der Tat ein Objekt der[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)-Klasse, die außerdem die add-Methode bereitstellt, um ein List-Objekt hinzuzufügen und den Zellbereich anzugeben, den es umfassen soll. Gemäß dem angegebenen Zellbereich a[**Listenobjekt**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) wird im Arbeitsblatt von Aspose.Cells erstellt. Verwenden Sie Attribute (z. B.[**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType) ) des[**Listenobjekt**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)Klasse, um die Tabelle für Ihre Anforderung zu formatieren.

 Das folgende Beispiel fügt Beispieldaten zu einem Arbeitsblatt hinzu, fügt a hinzu[**Listenobjekt**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) und wendet Standardstile darauf an.[**Listenobjekt**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)Stile werden von Microsoft Excel 2007/2010 unterstützt.

Die folgende Ausgabe wird generiert, wenn der Code ausgeführt wird.

**Im Arbeitsblatt wird eine formatierte Tabelle erstellt** 

![todo: Bild_alt_Text](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
