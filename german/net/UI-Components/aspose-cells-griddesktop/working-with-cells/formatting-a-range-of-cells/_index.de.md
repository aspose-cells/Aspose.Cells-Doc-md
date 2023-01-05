---
title: Formatieren eines Bereichs von Cells
type: docs
weight: 60
url: /de/net/formatting-a-range-of-cells/
---
{{% alert color="primary" %}} 

Dieses Thema gehört auch zu der Reihe von Themen, die sich mit der Anwendung von Schrifteinstellungen und anderen Formatierungsstilen auf Zellen befassen. Unsere letzten Themen haben den Umgang mit solchen Funktionen gut behandelt. Sie können sich zum Beispiel darauf beziehen[Ändern der Schriftart und Farbe einer Cell](/cells/de/net/changing-the-font-and-color-of-a-cell/) und[Anwenden von Stilen unter Cells](/cells/de/net/applying-styles-on-cells/) Themen, um mehr über dieselben Funktionen zu erfahren. Was ist dann neu in diesem Thema, wenn wir diese Konzepte bereits behandelt haben? Nun, der einzige Unterschied dieses Themas zu den vorherigen besteht darin, dass wir Formatierungseinstellungen (in Bezug auf Schriftarten und andere Stile) auf eine Reihe von Zellen anwenden, anstatt nur auf eine einzelne Zelle. Wir hoffen, dass Sie dieses Thema weiterhin für Sie nützlich finden.

{{% /alert %}} 
## **Festlegen von Schriftart und Stil eines Bereichs von Cells**
 Bevor wir über Formatierungseinstellungen sprechen (über die wir in unseren vorherigen Themen bereits viel gesprochen haben), sollten wir wissen, wie man eine Reihe von Zellen erstellt. Nun, wir können eine Reihe von Zellen erstellen, indem wir verwenden**CellRange** Klasse, deren Konstruktor einige Parameter übernimmt, um den Zellbereich anzugeben. Wir können den Zellbereich mit angeben**Namen** oder**Zeilen- und Spaltenindizes** von Start- und Endzellen.

 Sobald wir eine erstellt haben**CellRange** Objekt dann können wir die überladenen Versionen von verwenden**SetStyle**, **SetFont** & **SetFontColor** Methoden des Arbeitsblatts, die ein nehmen können**CellRange** -Objekt, um Formatierungseinstellungen auf den angegebenen Zellbereich anzuwenden.

Schauen wir uns ein Beispiel an, um dieses grundlegende Konzept zu verstehen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
