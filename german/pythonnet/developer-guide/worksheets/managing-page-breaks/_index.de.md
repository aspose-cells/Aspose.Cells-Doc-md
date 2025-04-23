---
title: Verwalten von Seitenumbrüchen
type: docs
weight: 30
url: /de/python-net/managing-page-breaks/
description: Dieser Artikel bietet Beispiellcode und erklärt, wie man Seitenumbrüche hinzufügt, löscht oder bestimmte Seitenumbrüche in Excel Arbeitsblättern mit Aspose.Cells für Python via .NET APIs programmgesteuert entfernt.
keywords: Python Excel Bibliothek, Python Seitenumbrüche, Excel Seitenumbrüche in Python, Seitenumbruch in Python löschen.
---

{{% alert color="primary" %}}

Nach Definition ist ein Seitenumbruch eine Stelle in einem Textfluss, an der eine Seite endet und die nächste beginnt. Microsoft Excel ermöglicht es Benutzern, Seitenumbrüche in jede ausgewählte Zelle eines Arbeitsblatts einzufügen.

Der Ort der Zelle, an der der Seitenumbruch hinzugefügt wird; die Seite endet dort, und die Daten nach dem Seitenumbruch werden auf der nächsten Seite gedruckt. Einfach ausgedrückt, teilen Seitenumbrüche Ihr Arbeitsblatt in mehrere Seiten auf, entsprechend Ihren Vorgaben. Sie können auch laufend Seitenumbrüche in Ihren Arbeitsblättern mit Aspose.Cells für Python via .NET hinzufügen. Aspose.Cells für Python via .NET ermöglicht es Entwicklern, zwei Arten von Seitenumbrüchen hinzuzufügen:

- Horizontaler Seitenumbruch
- Vertikaler Seitenumbruch

Im weiteren Verlauf wird beschrieben, wie Sie horizontale oder vertikale Seitenumbrüche in Ihre Arbeitsblätter mit Aspose.Cells für Python via .NET einfügen können.

{{% /alert %}}

## **Seitenumbrüche**

Aspose.Cells für Python via .NET bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine Sammlung [**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden, die zur Verwaltung eines Arbeitsblatts verwendet werden.

Um die Seitenumbrüche hinzuzufügen, verwenden Sie die Eigenschaften [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) und [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

Die Eigenschaften [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) und [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) sind Sammlungen, die mehrere Seitenumbrüche enthalten können. Jede Sammlung enthält mehrere Methoden zur Verwaltung von horizontalen und vertikalen Seitenumbrüchen.

## **So fügen Sie Seitenumbrüche hinzu**

Um einen Seitenumbruch in einem Arbeitsblatt hinzuzufügen, fügen Sie vertikale und horizontale Seitenumbrüche an der angegebenen Zelle ein, indem Sie die Methoden [**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str) und [**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str) aufrufen. Jede **add**-Methode nimmt den Namen der Zelle, an der die Umbruchsmarkierung gesetzt werden soll.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

Im Vorschau-Modus für Seitenumbrüche oder im Druckvorschau-Modus können Sie sehen, wie diese Seitenumbrüche funktionieren.

{{% /alert %}}


## **Wichtig zu wissen**

Wenn Sie **Passend für Seiten**-Eigenschaften festlegen (d. h. [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall) und [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide)) in den Seiteneinrichtungseinstellungen, werden die Seitenumbrucheinstellungen beeinflusst. Daher werden die Seitenumbrucheinstellungen beim Drucken des Arbeitsblatts nicht berücksichtigt, obwohl sie immer noch eingestellt sind.
