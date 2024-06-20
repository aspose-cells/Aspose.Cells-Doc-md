---
title: Zellenausrichtung ändern und bestehendes Format beibehalten
description: Verwenden Sie die Aspose.Cells Bibliothek, um die Zellenausrichtung zu ändern und das vorhandene Format beizubehalten
keywords: Aspose.Cells, C#, Zellenausrichtung, bestehendes Format beibehalten
type: docs
weight: 340
url: /de/net/change-cells-alignment-and-keep-existing-formatting/
---

## **Mögliche Verwendungsszenarien**

Manchmal möchten Sie die Ausrichtung mehrerer Zellen ändern, aber das bestehende Format beibehalten. Mit Aspose.Cells können Sie dies mithilfe der Eigenschaft [**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) tun. Wenn Sie es auf **true** setzen, werden Änderungen in der Ausrichtung vorgenommen, andernfalls nicht. Bitte beachten Sie, dass ein [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)-Objekt als Parameter an die Methode [**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle) übergeben wird, die tatsächlich die Formatierung auf einen Bereich von Zellen anwendet.

## **Zellenausrichtung ändern und vorhandenes Format beibehalten**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](67338585.xlsx), erstellt den Bereich und zentriert ihn horizontal und vertikal und behält das vorhandene Format bei. Der folgende Screenshot vergleicht die Beispiel-Excel-Datei und die [Ausgabedatei](67338586.xlsx) und zeigt, dass das gesamte vorhandene Format der Zellen gleich bleibt, außer dass die Zellen jetzt horizontal und vertikal zentriert sind.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
