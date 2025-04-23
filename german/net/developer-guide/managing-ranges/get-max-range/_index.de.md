---
title: Holen Sie den maximalen Bereich in einem Arbeitsblatt ab
type: docs
weight: 360
url: /de/net/get-max-range-in-a-worksheet/
description: Dieser Artikel beschreibt, wie der Maximalbereich, der maximale Datenbereich und der maximale Anzeigebereich von Excel Dateien mithilfe der Aspose.Cells für .Net Bibliothek abgerufen werden können.
---

{{% alert color="primary" %}} 

Beim Lesen von Daten aus dem Arbeitsblatt müssen wir den maximalen Bereich kennen.

Beim Kopieren aller Daten aus einem Arbeitsblatt müssen wir den maximalen Bereich kennen.

Beim Exportieren eines bestimmten Bereichs in HTML und PDF müssen wir den maximalen Bereich kennen.

Aspose.Cells für .Net enthält verschiedene Möglichkeiten, den maximalen Bereich in einem Arbeitsblatt zu finden. 


{{% /alert %}} 



## **Den Maximalbereich abrufen**
In Aspose.Cells, wenn die [**row**](https://reference.aspose.com/cells/net/aspose.cells/row)- und [**column**](https://reference.aspose.com/cells/net/aspose.cells/column)-Objekte initialisiert sind, werden diese Zeilen und Spalten zum maximalen Bereich gezählt, auch wenn in leeren Zeilen oder Spalten keine Daten vorhanden sind.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

## **Maximalen Datenbereich abrufen**
In den meisten Fällen müssen wir nur alle Bereiche erhalten, die alle Daten enthalten, auch wenn die leeren Zellen außerhalb des Bereichs formatiert sind.
Und die Einstellungen zu Formen, Tabellen und Pivottabellen werden ignoriert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

## **Maximale Anzeigebereich erhalten**
Wenn wir alle Daten aus dem Arbeitsblatt in HTML, PDF oder Bildern exportieren, müssen wir einen Bereich erhalten, der alle sichtbaren Objekte enthält, einschließlich Daten, Styles, Grafiken, Tabellen und Pivot-Tabellen.
Die folgenden Codes zeigen, wie der maximale Anzeigebereich in HTML gerendert wird:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

Hier ist die [Quelldatei Excel](Book1.xlsx).
{{< app/cells/assistant language="csharp" >}}
