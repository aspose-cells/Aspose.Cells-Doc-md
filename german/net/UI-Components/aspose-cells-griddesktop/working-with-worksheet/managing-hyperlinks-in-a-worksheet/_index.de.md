---
title: Verwalten von Hyperlinks in einem Arbeitsblatt
type: docs
weight: 90
url: /de/net/aspose-cells-griddesktop/manage-hyperlinks-in-a-worksheet/
keywords: GridDesktop, Hyperlin, Hyperlink, Hyperlinks
description: Dieser Artikel führt ein, wie mit Hyperlinks in GridDesktop gearbeitet wird.
---

{{% alert color="primary" %}} 

Mit Aspose.Cells.GridDesktop ist es auch möglich, Hyperlinks zu einfachen Werten in Zellen eines Arbeitsblatts hinzuzufügen. Angenommen, in einigen Zellen haben Sie Werte, die Sie mit ausführlicheren Informationen auf einer Webseite verknüpfen möchten. In diesem Fall wäre es wünschenswert, einen Hyperlink zu dieser Zelle hinzuzufügen, damit ein Benutzer, wenn er auf die Zelle klickt, zu dieser Webseite geleitet wird. In diesem Thema werden wir erläutern, wie Entwickler Hyperlinks in ihren Arbeitsblättern hinzufügen und manipulieren können.

{{% /alert %}} 
## **Hinzufügen von Hyperlinks**
Um einen Hyperlink zu einer Zelle mit Aspose.Cells.GridDesktop hinzuzufügen, befolgen Sie die folgenden Schritte:

- Fügen Sie das Steuerelement Aspose.Cells.GridDesktop zu Ihrem **Formular** hinzu
- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Greifen Sie auf eine gewünschte **Zelle** im Arbeitsblatt zu, die als Hyperlink fungieren soll
- Fügen Sie einen Wert zur Zelle hinzu, die als Hyperlink dienen soll
- Fügen Sie einen **Hyperlink** zum Arbeitsblatt hinzu, indem Sie den Zellennamen angeben, auf den der Hyperlink angewendet werden soll

Die **Hyperlinks**-Sammlung des **Arbeitsblatt**-Objekts bietet eine überladene **Add**-Methode. Entwickler können eine beliebige überladene Version der **Add**-Methode gemäß ihren spezifischen Anforderungen verwenden.

Der folgende Code fügt den Zellen **B2** und **C3** des Arbeitsblatts einen Hyperlink hinzu.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **Zugriff auf Hyperlinks**
Nachdem ein Hyperlink zu einer Zelle hinzugefügt wurde, ist es möglicherweise auch erforderlich, den Hyperlink zur Laufzeit zu öffnen und zu ändern. Entwickler können einfach auf den Hyperlink aus der **Hyperlinks**-Sammlung des **Arbeitsblatts** zugreifen, indem sie die Zelle angeben (unter Verwendung des Zellnamens oder ihrer Position in Bezug auf Zeilen- und Spaltennummer), zu der der Hyperlink hinzugefügt wurde. Sobald der Hyperlink zugegriffen wird, können Entwickler dessen URL zur Laufzeit ändern.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **Hyperlinks entfernen**
Um einen vorhandenen Hyperlink zu entfernen, können Entwickler einfach auf ein gewünschtes Arbeitsblatt zugreifen und dann den Hyperlink aus der **Hyperlinks**-Sammlung des **Arbeitsblatts** entfernen, indem sie die verlinkte Zelle angeben (unter Verwendung ihres Namens oder der Zeilen- und Spaltennummer).



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

Wenn Sie einen Hyperlink zu einer Zelle hinzufügen und die Hyperlink-URL in der Zelle statt eines Werts anzeigen möchten, fügen Sie keinen Wert zur Zelle hinzu und fügen Sie einfach den Hyperlink zu dieser Zelle hinzu. Auf diese Weise wird die Zelle verlinkt und die Hyperlink-URL wird auch als Wert in der Zelle angezeigt.

{{% /alert %}}
