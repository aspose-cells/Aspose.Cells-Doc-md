---
title: Zellen zusammenführen und aufheben
type: docs
weight: 60
url: /de/net/aspose-cells-gridweb/merge-and-unmerge-cells/
keywords: GridWeb,zusammenführen,aufheben
description: Dieser Artikel zeigt, wie man Zellen in GridWeb zusammenführt/auflöst.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb verfügt über eine praktische Funktion, mit der Sie Zellen zu einer großen Zelle zusammenführen können. Dieser Artikel beschreibt, wie man Zellen programmgesteuert zusammenführt.

{{% /alert %}} 
## **Zellen zusammenführen**
Fassen Sie mehrere Zellen in einem Arbeitsblatt zu einer einzigen Zelle zusammen, indem Sie die Merge-Methode der Cells-Sammlung aufrufen. Geben Sie den Bereich der Zellen an, die bei Aufruf der Merge-Methode zusammengeführt werden sollen.

{{% alert color="primary" %}} 

Wenn Sie mehrere Zellen zusammenführen und jede Zelle Daten enthält, wird nur der Inhalt der oben links liegenden Zelle im Bereich nach dem Zusammenführen beibehalten. Daten in den anderen Zellen gehen nicht verloren. Wenn Sie die Zellen auflösen, erhält jede Zelle seine Daten zurück.

{{% /alert %}} 

**Vier Zellen zu einer zusammengefasst** 

![todo:image_alt_text](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **Auflösen von Zellen**
Verwenden Sie zur Auflösung von Zellen die UnMerge-Methode der Cells-Sammlung, die dieselben Parameter wie die Merge-Methode annimmt und die Auflösung der Zellen durchführt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
