---
title: Zellenausrichtung ändern und bestehendes Format beibehalten
linktitle: Zellenausrichtung ändern und bestehendes Format beibehalten
description: Verwenden Sie die Aspose.Cells Bibliothek, um die Zellenausrichtung zu ändern und das bestehende Format in Node.js via C++ beizubehalten
keywords: Aspose.Cells, Zellenausrichtung, bestehendes Format beibehalten, Node.js via C++
type: docs
weight: 340
url: /de/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Mögliche Verwendungsszenarien**

 Manchmal möchten Sie die Ausrichtung mehrerer Zellen ändern, aber das bestehende Format beibehalten. Aspose.Cells for Node.js via C++ ermöglicht dies mit der [**StyleFlag.setAlignments(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/#setAlignments-boolean-) Methode. Wenn Sie sie auf **true** setzen, werden die Änderungen in der Ausrichtung vorgenommen, sonst nicht. Bitte beachten Sie, dass das [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) Objekt als Parameter an die [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-) Methode übergeben wird, die das Format auf einen Zellbereich anwendet.

## **Zellenausrichtung ändern und vorhandenes Format beibehalten**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](67338585.xlsx), erstellt den Bereich und zentriert ihn horizontal und vertikal und behält das vorhandene Format bei. Der folgende Screenshot vergleicht die Beispiel-Excel-Datei und die [Ausgabedatei](67338586.xlsx) und zeigt, dass das gesamte vorhandene Format der Zellen gleich bleibt, außer dass die Zellen jetzt horizontal und vertikal zentriert sind.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ChangeCellsAlignment.js" >}}
