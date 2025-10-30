---
title: Zellenausrichtung ändern und bestehendes Format beibehalten
description: Verwenden Sie die Aspose.Cells für Python via .NET Bibliothek, um die Zellenausrichtung zu ändern und das bestehende Format beizubehalten
keywords: Aspose.Cells für Python via .NET, Zellen Ausrichtung in Python, bestehendes Format beibehalten
type: docs
weight: 340
url: /de/python-net/change-cells-alignment-and-keep-existing-formatting/
---

## **Mögliche Verwendungsszenarien**

Manchmal möchten Sie die Ausrichtung mehrerer Zellen ändern und gleichzeitig das bestehende Format beibehalten. Aspose.Cells für Python via .NET ermöglicht dies mit der [**StyleFlag.alignments**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag/alignments)-Eigenschaft. Wenn Sie es auf **true** setzen, erfolgen Änderungen in der Ausrichtung, andernfalls nicht. Bitte beachten Sie, dass das [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag)-Objekt als Parameter an die [**Range.apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style)-Methode übergeben wird, die das Format auf einen Zellbereich anwendet.

## **Zellenausrichtung ändern und vorhandenes Format beibehalten**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](67338585.xlsx), erstellt den Bereich und zentriert ihn horizontal und vertikal und behält das vorhandene Format bei. Der folgende Screenshot vergleicht die Beispiel-Excel-Datei und die [Ausgabedatei](67338586.xlsx) und zeigt, dass das gesamte vorhandene Format der Zellen gleich bleibt, außer dass die Zellen jetzt horizontal und vertikal zentriert sind.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeCellsAlignmentAndKeepExistingFormatting.py" >}}

{{< app/cells/assistant language="python-net" >}}
