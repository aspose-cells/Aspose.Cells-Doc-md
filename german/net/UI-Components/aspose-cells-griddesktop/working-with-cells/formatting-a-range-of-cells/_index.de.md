---
title: Formatierung eines Zellenbereichs
type: docs
weight: 60
url: /de/net/aspose-cells-griddesktop/formatting-a-range-of-cells/
keywords: GridDesktop, Format, Stil, Zellen
description: Dieser Artikel zeigt, wie Stilformatierungen auf Zellen in GridDesktop angewendet werden.
---

{{% alert color="primary" %}} 

Dieses Thema gehört ebenfalls zur Serie von Themen, die sich mit der Anwendung von Schrifteinstellungen und anderen Formatierungsstilen auf Zellen befassen. Unsere letzten Themen haben diesbezüglich bereits gezeigt. Sie können beispielsweise die Themen [Ändern der Schriftart und -farbe einer Zelle](/cells/de-net/ändern-der-schriftart-und-farbe-einer-zelle/) und [Anwendung von Stilen auf Zellen](/cells/de-net/anwendung-von-stilen-auf-zellen/) nachschlagen, um mehr über die gleichen Funktionen zu erfahren. Was ist also neu an diesem Thema, wenn wir diese Konzepte bereits behandelt haben? Der einzige Unterschied dieses Themas zu den bisherigen besteht darin, dass wir die Formatierungseinstellungen (bezogen auf Schriften und andere Stile) auf einen Zellenbereich anwenden, anstatt nur auf eine einzelne Zelle. Wir hoffen, dass Sie dieses Thema dennoch nützlich finden werden.

{{% /alert %}} 
## **Einstellen von Schriftart & Stil eines Zellenbereichs**
Bevor wir über Formatierungseinstellungen sprechen (über die wir in unseren vorherigen Themen bereits viel gesprochen haben), sollten wir wissen, wie man einen Zellenbereich erstellt. Nun, wir können einen Zellenbereich mit der Klasse **CellRange** erstellen, deren Konstruktor einige Parameter erhält, um den Zellenbereich zu spezifizieren. Wir können den Zellenbereich mithilfe der **Namen** oder der **Zeilen- und Spaltenindizes** der Start- und Endzellen angeben.

Sobald wir ein **CellRange**-Objekt erstellt haben, können wir die überladenen Versionen der Methoden **SetStyle**, **SetFont** & **SetFontColor** des Arbeitsblatts verwenden, die ein **CellRange**-Objekt übernehmen können, um Formatierungseinstellungen auf den angegebenen Zellenbereich anzuwenden.

Schauen wir uns ein Beispiel an, um dieses Grundkonzept zu verstehen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
