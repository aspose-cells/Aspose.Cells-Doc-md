---
title: Zusammenführen und Trennen von Cells in GridDesktop
linktitle: Zusammenführen und Trennen Cells
type: docs
weight: 90
url: /de/net/merging-and-unmerging-cells-griddesktop/
---
{{% alert color="primary" %}} 

In diesem Thema besprechen wir eine Hilfsfunktion zum Zusammenführen und Aufheben der Zusammenführung von Zellen eines Arbeitsblatts. Diese Funktion ist in den Fällen nützlich, in denen wir einige Zeilen oder Spalten überspannen müssen, um die Lesbarkeit der Daten zu verbessern.

{{% /alert %}} 
## **Cells zusammenführen**
Führen Sie die folgenden Schritte aus, um Zellen zu einer einzigen großen Zelle zusammenzuführen:

-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Ein ... kreieren**Bereich von Cells** zusammengeführt werden
- **Verschmelzen** den Zellbereich in eine große Zelle

 Sie können verwenden**Verschmelzen** Methode von**Arbeitsblatt** Zellen zusammenführen. Es kann jedoch mit ein Bereich von Zellen definiert werden**CellRange** Objekt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **Trennen von Cells**
Führen Sie die folgenden Schritte aus, um eine große Zelle in viele Zellen aufzulösen:

-  Greifen Sie beliebig zu**Arbeitsblatt**
- Greifen Sie auf die verbundene Zelle zu, deren Verbindung aufgehoben werden muss
- **Zusammenführung aufheben** die große Zelle in viele Zellen unter Verwendung der Position der zusammengeführten Zelle

 Sie können verwenden**Zusammenführung aufheben** Methode von**Arbeitsblatt** um eine Zelle anhand ihrer Position zu trennen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

Wenn Sie Zellen zu einer einzelnen Zelle verbinden, werden die Formatierungseinstellungen der oberen linken Zelle (im Zellbereich) auf die verbundene Zelle angewendet, aber wenn die Verbindung der Zelle aufgehoben wird, behalten alle nicht verbundenen Zellen ihre Formatierungseinstellungen bei.

{{% /alert %}}
