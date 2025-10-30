---
title: Daten mithilfe der Originalwerte suchen
type: docs
weight: 380
url: /de/python-net/search-data-using-original-values/
description: Erfahren Sie, wie Sie Daten mithilfe der Originalwerte durchsuchen, durch die Aspose.Cells for Python via .NET API.
keywords: Python Excel Bibliothek, Python Suche Daten unter Verwendung der Originalwerte, Python Finden von Daten unter Verwendung der Originalwerte, Python Suche von Daten unter Verwendung der Originalwerte, Python Finden von Daten unter Verwendung der Originalwerte
---

{{% alert color="primary" %}}

Manchmal ist der Wert der Daten verborgen, weil er in irgendeiner Weise formatiert ist. Zum Beispiel, wenn die Zelle D4 die Formel =Sum(A1:A2) hat und ihr Wert 20 ist, aber sie als --- formatiert ist, dann ist der Wert 20 verborgen und kann nicht mithilfe der Microsoft Excel-Suchoptionen gefunden werden. Sie können ihn jedoch mithilfe von Aspose.Cells for Python via .NET unter Verwendung von [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype) finden.

{{% /alert %}}

Der folgende Beispielcode verdeutlicht den obigen Punkt. Er findet die Zelle D4, die mit den Suchoptionen von Microsoft Excel nicht gefunden werden kann, aber Aspose.Cells kann sie mithilfe von [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype) finden. Bitte lesen Sie die Kommentare im Code für weitere Informationen.

## Python-Code zum Suchen von Daten unter Verwendung der Originalwerte

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SearchDataUsingOriginalValues.py" >}}

## Von dem Beispielcode generierte Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
