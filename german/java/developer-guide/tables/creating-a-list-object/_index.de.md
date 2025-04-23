---
title: Tabelle erstellen
type: docs
weight: 40
url: /de/java/creating-a-list-object/
---

{{% alert color="primary" %}}

Einer der Vorteile von Tabellenkalkulationen besteht darin, dass Sie verschiedene Arten von Listen erstellen können, beispielsweise Telefonlisten, Aufgabenlisten, Listen von Transaktionen, Vermögenswerten oder Verbindlichkeiten. Mehrere Benutzer können zusammenarbeiten, um verschiedene Listen zu verwenden, zu erstellen und zu pflegen.

Aspose.Cells unterstützt das Erstellen und Verwalten von Listen.

{{% /alert %}}

## **Vorteile einer Tabelle**

Es gibt einige Vorteile, wenn Sie eine Liste von Daten in ein tatsächliches Listenobjekt konvertieren:

- Neue Zeilen und Spalten werden automatisch einbezogen.
- Am unteren Rand Ihrer Liste kann ganz einfach eine Gesamtzeile hinzugefügt werden, um SUMME, DURCHSCHNITT, ANZAHL usw. anzuzeigen.
- Hinzugefügte Spalten rechts werden automatisch in das Listenobjekt aufgenommen.
- Diagramme, die auf Zeilen und Spalten basieren, werden automatisch erweitert.
- Benannte Bereiche, die Zeilen und Spalten zugeordnet sind, werden automatisch erweitert.
- Die Liste ist vor versehentlichem Löschen von Zeilen und Spalten geschützt.

## **Erstellen einer Tabelle in Microsoft Excel**

**Auswahl des Datenbereichs zum Erstellen eines Listenobjekts** 

![todo:image_alt_text](creating-a-list-object_1.png)

Dies zeigt das Dialogfeld 'Liste erstellen' an.

**Dialogfeld 'Liste erstellen'** 

![todo:image_alt_text](creating-a-list-object_2.png)

Implementierung des List-Objekts und Festlegen der Gesamtzeile (Wählen Sie **Daten**, dann **Liste**, gefolgt von **Gesamtzeile**).

**Erstellen eines Listenobjekts** 

![todo:image_alt_text](creating-a-list-object_3.png)

## **Erstellen einer Tabelle mit der Aspose.Cells-API**

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)-Sammlung, die den Zugriff auf jede Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts. Um eine [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) in einem Arbeitsblatt zu erstellen, verwenden Sie die Eigenschaft [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) der Worksheet-Klasse. Jede [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) ist in der Tat ein Objekt der Klasse [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection), die die Methode zum Hinzufügen eines List-Objekts und zum Festlegen eines Zellenbereichs für die Liste bietet.

Gemäß dem angegebenen Zellenbereich wird das List-Objekt im Arbeitsblatt von Aspose.Cells erstellt. Verwenden Sie Attribute (z. B. ShowTotals, ListColumns usw.) der Klasse [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject), um die Liste zu steuern.

In dem unten gegebenen Beispiel haben wir dasselbe [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) erstellt, indem wir die Aspose.Cells-API verwendet haben, wie wir es im obigen Abschnitt mit Microsoft Excel erstellt haben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
{{< app/cells/assistant language="java" >}}
