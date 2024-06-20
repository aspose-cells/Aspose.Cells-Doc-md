---
title: Zusammenführen und Aufteilen von Zellen in GridDesktop
linktitle: Zusammenführen und Aufteilen von Zellen
type: docs
weight: 90
url: /de/net/aspose-cells-griddesktop/merge-and-unmerge-cells-griddesktop/
keywords: GridDesktop, zusammenführen, aufteilen
description: Dieser Artikel stellt das Zusammenführen und Aufteilen in GridDesktop vor.
---

{{% alert color="primary" %}} 

In diesem Thema werden wir eine Hilfsfunktion zum Zusammenführen und Aufteilen von Zellen eines Arbeitsblatts diskutieren. Diese Funktion ist nützlich, wenn wir einige Zeilen oder Spalten überbrücken müssen, um die Lesbarkeit der Daten zu verbessern.

{{% /alert %}} 
## **Zellen zusammenführen**
Um Zellen zu einer einzigen großen Zelle zusammenzuführen, befolgen Sie bitte die folgenden Schritte:

- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Erstellen Sie einen **Bereich von Zellen**, die zusammengeführt werden sollen
- **Führen Sie** den Bereich von Zellen zu einer großen Zelle zusammen

Sie können die **Merge**-Methode des **Arbeitsblatts** verwenden, um Zellen zu zusammenzuführen. Es kann jedoch ein Zellenbereich mithilfe des **CellRange**-Objekts definiert werden.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **Zellen aufteilen**
Um eine große Zelle in viele Zellen aufzuteilen, befolgen Sie bitte die folgenden Schritte:

- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Greifen Sie auf die zusammengeführte Zelle zu, die aufgeteilt werden soll
- **Teilen Sie** die große Zelle mithilfe des Standorts der zusammengeführten Zelle in viele Zellen auf.

Sie können die **Unmerge**-Methode des **Arbeitsblatts** verwenden, um eine Zelle unter Verwendung ihres Standorts aufzuteilen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

Wenn Sie Zellen zu einer einzelnen Zelle zusammenführen, werden die Formatierungseinstellungen der linken oberen Zelle (im Zellenbereich) auf die zusammengeführte Zelle angewendet. Wenn die Zelle jedoch aufgeteilt ist, behalten alle aufgeteilten Zellen ihre Formatierungseinstellungen bei.

{{% /alert %}}
