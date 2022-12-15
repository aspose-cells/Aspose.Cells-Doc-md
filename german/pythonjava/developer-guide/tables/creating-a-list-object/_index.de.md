---
title: Erstellen eines Listenobjekts
type: docs
weight: 20
url: /de/python-java/creating-a-list-object/
---
Die Verwendung von Arbeitsblättern erleichtert beispielsweise das Arbeiten mit verschiedenen Arten von Listen. Telefonlisten, Aufgabenlisten. etc. Aspose.Cells unterstützt das Erstellen und Verwalten von Listen.

## **Vorteile eines Listenobjekts**

Es gibt einige Vorteile, wenn Sie eine Datenliste in ein tatsächliches Listenobjekt konvertieren:

- Neue Zeilen und Spalten werden automatisch eingefügt.
- Eine Summenzeile am Ende Ihrer Liste kann einfach hinzugefügt werden, um SUMME, MITTELWERT, ANZAHL usw. anzuzeigen.
- Rechts hinzugefügte Spalten werden automatisch in das List-Objekt übernommen.
- Diagramme, die auf Zeilen und Spalten basieren, werden automatisch erweitert.
- Benannte Bereiche, die Zeilen und Spalten zugewiesen sind, werden automatisch erweitert.
- Die Liste ist vor versehentlichem Löschen von Zeilen und Spalten geschützt.

## **Erstellen eines Listenobjekts mit Microsoft Excel**

**Auswahl des Datenbereichs zum Erstellen eines Listenobjekts** 

![todo: Bild_alt_Text](picture1.png)

Dadurch wird das Dialogfeld „Liste erstellen“ angezeigt.

**Dialogfeld „Liste erstellen“.** 

![todo: Bild_alt_Text](picture2.png)

Implementieren des Listenobjekts und Festlegen der Gesamtzeile (Select**Daten**, dann**Aufführen**, gefolgt von**Gesamtreihe**).

**Erstellen eines List-Objekts** 

![todo: Bild_alt_Text](picture3.png)

## **Erstellen eines Listenobjekts mit Aspose.Cells API**

Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/python/asposecells.api/Workbook), die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten eines Arbeitsblatts. Um eine zu erstellen[**Listenobjekt**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)in einem Arbeitsblatt verwenden[**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects)Sammlungseigentum der[**Arbeitsblatt**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)Klasse. Jeder[**Listenobjekt**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)ist in der Tat ein Objekt der[**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection)Klasse, die außerdem die[**hinzufügen**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean))-Methode zum Hinzufügen eines List-Objekts und zum Angeben eines Zellbereichs für die Liste.

Gemäß dem angegebenen Zellbereich wird das Listenobjekt im Arbeitsblatt von Aspose.Cells erstellt. Verwenden Sie Attribute (z. B. ShowTotals, ListColumns usw.) der[**Listenobjekt**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)Klasse, um die Liste zu steuern.

In dem unten angegebenen Beispiel haben wir dasselbe erstellt[**Listenobjekt**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)Verwenden Sie Aspose.Cells for Python via Java API, wie wir es mit Microsoft Excel im obigen Abschnitt erstellt haben.

## Quellcode

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
