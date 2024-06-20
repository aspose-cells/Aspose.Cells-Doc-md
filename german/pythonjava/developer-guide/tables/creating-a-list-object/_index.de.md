---
title: Erstellen eines Listenobjekts
type: docs
weight: 20
url: /de/python-java/creating-a-list-object/
---

Die Verwendung von Arbeitsblättern macht es einfach, mit verschiedenen Arten von Listen zu arbeiten, z. B. Telefonlisten, Aufgabenlisten usw. Aspose.Cells unterstützt das Erstellen und Verwalten von Listen.

## **Vorteile eines Listenobjekts**

Es gibt einige Vorteile, wenn Sie eine Liste von Daten in ein tatsächliches Listenobjekt konvertieren:

- Neue Zeilen und Spalten werden automatisch einbezogen.
- Am unteren Rand Ihrer Liste kann ganz einfach eine Gesamtzeile hinzugefügt werden, um SUMME, DURCHSCHNITT, ANZAHL usw. anzuzeigen.
- Hinzugefügte Spalten rechts werden automatisch in das Listenobjekt aufgenommen.
- Diagramme, die auf Zeilen und Spalten basieren, werden automatisch erweitert.
- Benannte Bereiche, die Zeilen und Spalten zugeordnet sind, werden automatisch erweitert.
- Die Liste ist vor versehentlichem Löschen von Zeilen und Spalten geschützt.

## **Erstellen eines Listenobjekts mit Microsoft Excel**

**Auswahl des Datenbereichs zum Erstellen eines Listenobjekts** 

![todo:image_alt_text](picture1.png)

Dies zeigt das Dialogfeld 'Liste erstellen' an.

**Dialogfeld 'Liste erstellen'** 

![todo:image_alt_text](picture2.png)

Implementieren des Listenobjekts und Festlegen der Gesamtzeile (Wählen Sie **Daten**, dann **Liste** und dann **Gesamtzeile**).

**Erstellen eines Listenobjekts** 

![todo:image_alt_text](picture3.png)

## **Erstellen eines Listenobjekts mit Aspose.Cells API**

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook), bereit, die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)-Sammlung, die den Zugriff auf jede Arbeitsmappe in einer Excel-Datei ermöglicht.

Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Arbeitsmappe. Verwenden Sie die [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)-Sammlungseigenschaft der Klasse [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet), um ein [**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects) in einer Arbeitsmappe zu erstellen. Jede [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) ist tatsächlich ein Objekt der Klasse [**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection), das die Methode [**add**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) zum Hinzufügen eines Listenobjekts und Festlegen eines Zellenbereichs für die Liste bereitstellt.

Entsprechend dem angegebenen Zellenbereich wird das Listobjekt in der Arbeitsmappe von Aspose.Cells erstellt. Verwenden Sie Attribute (z. B. ShowTotals, ListColumns usw.) der Klasse [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject), um die Liste zu steuern.

Im untenstehenden Beispiel haben wir dasselbe [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) unter Verwendung von Aspose.Cells für Python via Java API erstellt, wie wir es im obigen Abschnitt mit Microsoft Excel erstellt haben.

## Quellcode

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
