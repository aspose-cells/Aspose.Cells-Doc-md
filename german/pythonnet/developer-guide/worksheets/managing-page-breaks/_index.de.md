---
title: Verwalten von Seitenumbrüchen
type: docs
weight: 30
url: /de/python-net/managing-page-breaks/
description: Dieser Artikel bietet Beispielscode und erläutert, wie man Seitenwechsel in Excel Arbeitsblättern programmgesteuert mithilfe der Aspose.Cells for Python via .NET APIs hinzufügt, löscht oder spezifische Seitenwechsel entfernt.
keywords: Python Excel Bibliothek, Python Seitenwechsel, Excel Seitenwechsel in Python, Seitenumbruch in Python löschen.
---

{{% alert color="primary" %}}

Nach Definition ist ein Seitenumbruch eine Stelle in einem Textfluss, an der eine Seite endet und die nächste beginnt. Microsoft Excel ermöglicht es Benutzern, Seitenumbrüche in jede ausgewählte Zelle eines Arbeitsblatts einzufügen.

Der Ort der Zelle, an dem der Seitenwechsel hinzugefügt wird, die Seite endet und der Rest der Daten nach dem Seitenwechsel auf der nächsten Seite gedruckt wird. Vereinfacht ausgedrückt, teilen Seitenwechsel Ihr Arbeitsblatt entsprechend Ihren Spezifikationen in mehrere Seiten auf. Sie können auch zur Laufzeit Seitenwechsel in Ihre Arbeitsblätter einfügen mithilfe von Aspose.Cells for Python via .NET. Aspose.Cells for Python via .NET ermöglicht Entwicklern, zwei Arten von Seitenwechseln hinzuzufügen:

- Horizontaler Seitenumbruch
- Vertikaler Seitenumbruch

Im weiteren Verlauf der Diskussion werden wir beschreiben, wie Sie horizontale oder vertikale Seitenwechsel in Ihre Arbeitsblätter mithilfe von Aspose.Cells for Python via .NET hinzufügen können.

{{% /alert %}}

## **Seitenumbrüche**

Aspose.Cells für Python via .NET bietet eine [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse, die eine Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-Sammlung, auf die jedes Arbeitsblatt in der Excel-Datei zugegriffen werden kann.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden, die zur Verwaltung eines Arbeitsblatts verwendet werden.

Um die Seitenumbrüche hinzuzufügen, verwenden Sie die Eigenschaften [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) und [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

Die Eigenschaften [**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks) und [**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks) sind Sammlungen, die mehrere Seitenumbrüche enthalten können. Jede Sammlung enthält mehrere Methoden zur Verwaltung von horizontalen und vertikalen Seitenumbrüchen.

## **Wie man Seitenwechsel hinzufügt**

Um einen Seitenwechsel in einem Arbeitsblatt hinzuzufügen, fügen Sie vertikale und horizontale Seitenwechsel in der angegebenen Zelle ein, indem Sie die [**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str)- und [**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str)-Methoden aufrufen. Jede **add**-Methode nimmt den Namen der Zelle, an der der Seitenwechsel hinzugefügt werden soll.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

Im Vorschau-Modus für Seitenumbrüche oder im Druckvorschau-Modus können Sie sehen, wie diese Seitenumbrüche funktionieren.

{{% /alert %}}


## **Wichtig zu wissen**

Wenn Sie **Passend für Seiten**-Eigenschaften festlegen (d. h. [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall) und [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide)) in den Seiteneinrichtungseinstellungen, werden die Seitenumbrucheinstellungen beeinflusst. Daher werden die Seitenumbrucheinstellungen beim Drucken des Arbeitsblatts nicht berücksichtigt, obwohl sie immer noch eingestellt sind.
