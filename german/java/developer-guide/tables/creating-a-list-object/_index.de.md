---
title: Erstellen einer Tabelle
type: docs
weight: 40
url: /de/java/creating-a-list-object/
---
{{% alert color="primary" %}}

Einer der Vorteile von Tabellenkalkulationen besteht darin, dass Sie verschiedene Arten von Listen erstellen können, z. B. Telefonlisten, Aufgabenlisten, Listen mit Transaktionen, Vermögenswerten oder Verbindlichkeiten. Mehrere Benutzer können zusammenarbeiten, um verschiedene Listen zu verwenden, zu erstellen und zu pflegen.

Aspose.Cells unterstützt das Erstellen und Verwalten von Listen.

{{% /alert %}}

## **Vorteile eines Tisches**

Es gibt einige Vorteile, wenn Sie eine Datenliste in ein tatsächliches Listenobjekt konvertieren:

- Neue Zeilen und Spalten werden automatisch eingefügt.
- Eine Summenzeile am Ende Ihrer Liste kann einfach hinzugefügt werden, um SUMME, MITTELWERT, ANZAHL usw. anzuzeigen.
- Rechts hinzugefügte Spalten werden automatisch in das List-Objekt übernommen.
- Diagramme, die auf Zeilen und Spalten basieren, werden automatisch erweitert.
- Benannte Bereiche, die Zeilen und Spalten zugewiesen sind, werden automatisch erweitert.
- Die Liste ist vor versehentlichem Löschen von Zeilen und Spalten geschützt.

## **Erstellen einer Tabelle mit Microsoft Excel**

**Auswahl des Datenbereichs zum Erstellen eines Listenobjekts** 

![todo: Bild_alt_Text](creating-a-list-object_1.png)

Dadurch wird das Dialogfeld „Liste erstellen“ angezeigt.

**Dialogfeld „Liste erstellen“.** 

![todo: Bild_alt_Text](creating-a-list-object_2.png)

 Implementieren des Listenobjekts und Festlegen der Gesamtzeile (Select**Daten** , dann**Aufführen** , gefolgt von**Gesamtreihe**).

**Erstellen eines List-Objekts** 

![todo: Bild_alt_Text](creating-a-list-object_3.png)

## **Erstellen einer Tabelle mit Verwenden von Aspose.Cells API**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten eines Arbeitsblatts. Um eine zu erstellen[**Listenobjekt**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) in einem Arbeitsblatt verwenden[**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) Collection-Eigenschaft der Worksheet-Klasse. Jeder[**Listenobjekt**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) ist in der Tat ein Objekt der[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)-Klasse, die außerdem die add-Methode zum Hinzufügen eines List-Objekts und zum Angeben eines Zellbereichs für die Liste bereitstellt.

Gemäß dem angegebenen Zellbereich wird das Listenobjekt im Arbeitsblatt von Aspose.Cells erstellt. Verwenden Sie Attribute (z. B. ShowTotals, ListColumns usw.) der[**Listenobjekt**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)Klasse, um die Liste zu steuern.

 In dem unten angegebenen Beispiel haben wir dasselbe erstellt[**Listenobjekt**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)Verwenden Sie Aspose.Cells API, wie wir es mit Microsoft Excel im obigen Abschnitt erstellt haben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
