---
title: Zusammenführen und Zusammenführung aufheben Cells
type: docs
weight: 60
url: /de/net/merge-and-unmerge-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb hat eine praktische Hilfsfunktion, mit der Sie Zellen zu einer großen Zelle zusammenführen können. In diesem Thema wird beschrieben, wie Zellen programmgesteuert zusammengeführt werden.

{{% /alert %}} 
## **Cells zusammenführen**
Führen Sie mehrere Zellen in einem Arbeitsblatt zu einer einzelnen Zelle zusammen, indem Sie die Merge-Methode der Sammlung Cells aufrufen. Geben Sie den Zellbereich an, der beim Aufrufen der Merge-Methode zusammengeführt werden soll.

{{% alert color="primary" %}} 

Wenn Sie mehrere Zellen zusammenführen und jede Zelle Daten enthält, wird nur der Inhalt der obersten linken Zelle im Bereich nach der Zusammenführung beibehalten. Daten in den anderen Zellen gehen nicht verloren. Wenn Sie die Zellverschmelzung aufheben, stellt jede Zelle ihre Daten wieder her.

{{% /alert %}} 

**Vier Zellen verschmolzen zu einer** 

![todo: Bild_alt_Text](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **Trennen von Cells**
Um die Zellverschmelzung aufzuheben, verwenden Sie die UnMerge-Methode der Cells-Sammlung, die dieselben Parameter wie die Merge-Methode verwendet und die Zellverschmelzung aufhebt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
