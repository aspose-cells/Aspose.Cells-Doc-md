---
title: Holen Sie den maximalen Bereich in einem Arbeitsblatt ab
type: docs
weight: 360
url: /de/python-net/get-max-range-in-a-worksheet/
description: Dieser Artikel beschreibt, wie Sie mit der Aspose.Cells für Python via .NET Bibliothek den maximalen Bereich, den maximalen Datenbereich und den maximalen Anzeigebereich von Excel Dateien erhalten.
keywords: Python Excel Bibliothek, Python erhalten Sie den maximalen Bereich, Python erhalten Sie den maximalen Datenbereich, Python erhalten Sie den maximalen Anzeigebereich.
---

{{% alert color="primary" %}} 

Beim Lesen von Daten aus dem Arbeitsblatt müssen wir den maximalen Bereich kennen.

Beim Kopieren aller Daten aus einem Arbeitsblatt müssen wir den maximalen Bereich kennen.

Beim Exportieren eines bestimmten Bereichs in HTML und PDF müssen wir den maximalen Bereich kennen.

Aspose.Cells für Python via .NET enthält verschiedene Möglichkeiten, den maximalen Bereich in einem Arbeitsblatt zu finden. 


{{% /alert %}} 



## **Wie man den maximalen Bereich erhält**
In Aspose.Cells für Python via .NET, wenn die Objekte [**row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) und [**column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) initialisiert sind, werden diese Zeilen und Spalten zum maximalen Bereich gezählt, auch wenn in leeren Zeilen oder Spalten keine Daten vorhanden sind.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Range.py" >}}

## **Wie man den maximalen Datenbereich erhält**
In den meisten Fällen müssen wir nur alle Bereiche erhalten, die alle Daten enthalten, auch wenn die leeren Zellen außerhalb des Bereichs formatiert sind.
Und die Einstellungen zu Formen, Tabellen und Pivottabellen werden ignoriert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Data-Range.py" >}}

## **Wie man den maximalen Anzeigebereich erhält**
Wenn wir alle Daten aus dem Arbeitsblatt in HTML, PDF oder Bildern exportieren, müssen wir einen Bereich erhalten, der alle sichtbaren Objekte enthält, einschließlich Daten, Styles, Grafiken, Tabellen und Pivot-Tabellen.
Die folgenden Codes zeigen, wie der maximale Anzeigebereich in HTML gerendert wird:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Display-Range.py" >}}

Hier ist die [Quelldatei Excel](Book1.xlsx).
{{< app/cells/assistant language="python-net" >}}
