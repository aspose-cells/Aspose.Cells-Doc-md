---
title: Zellenausrichtung ändern und bestehendes Format beibehalten mit Golang über C++
description: Verwenden Sie die Aspose.Cells Bibliothek, um die Zellenausrichtung zu ändern und das vorhandene Format beizubehalten
keywords: Aspose.Cells, C++, Zellen Ausrichtung, bestehendes Format beibehalten
type: docs
weight: 340
url: /de/go-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Mögliche Verwendungsszenarien**

Manchmal möchten Sie die Ausrichtung mehrerer Zellen ändern, aber das bestehende Format beibehalten. Aspose.Cells ermöglicht dies durch die Eigenschaft [**GetAlignments()**](https://reference.aspose.com/cells/go-cpp/styleflag/getalignments/). Wenn Sie sie auf **true** setzen, werden Änderungen an der Ausrichtung vorgenommen, andernfalls nicht. Bitte beachten Sie, dass das [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag)-Objekt als Parameter an die Methode [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) übergeben wird, die tatsächlich das Format auf einen Zellbereich anwendet.

## **Zellenausrichtung ändern und vorhandenes Format beibehalten**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](67338585.xlsx), erstellt den Bereich und zentriert ihn horizontal und vertikal und behält das vorhandene Format bei. Der folgende Screenshot vergleicht die Beispiel-Excel-Datei und die [Ausgabedatei](67338586.xlsx) und zeigt, dass das gesamte vorhandene Format der Zellen gleich bleibt, außer dass die Zellen jetzt horizontal und vertikal zentriert sind.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeCellsAlignmentAndKeepExistingFormatting.go" >}}
