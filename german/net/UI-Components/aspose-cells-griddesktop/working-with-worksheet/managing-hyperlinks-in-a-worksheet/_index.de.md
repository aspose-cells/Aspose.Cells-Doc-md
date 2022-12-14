---
title: Verwalten von Hyperlinks in einem Arbeitsblatt
type: docs
weight: 90
url: /de/net/managing-hyperlinks-in-a-worksheet/
---
{{% alert color="primary" %}} 

Mit Aspose.Cells.GridDesktop ist es auch möglich, Hyperlinks zu einfachen Werten hinzuzufügen, die in Zellen eines Arbeitsblatts gespeichert sind. Angenommen, Sie haben in einigen Zellen einige Werte, die Sie mit detaillierteren Informationen auf einer Webseite verknüpfen möchten. In diesem Fall wäre es wünschenswert, dieser Zelle einen Hyperlink hinzuzufügen, damit ein Benutzer, wenn er auf die Zelle klickt, zu dieser Webseite geleitet würde. In diesem Thema erklären wir, wie Entwickler Hyperlinks in ihren Arbeitsblättern hinzufügen und bearbeiten können.

{{% /alert %}} 
## **Hinzufügen von Hyperlinks**
Um mit Aspose.Cells.GridDesktop einen Hyperlink zu einer Zelle hinzuzufügen, führen Sie bitte die folgenden Schritte aus:

-  Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Greifen Sie auf eine gewünschte zu**Cell** in dem Arbeitsblatt, das verlinkt wird
- Fügen Sie der zu verknüpfenden Zelle einen Wert hinzu
-  Hinzufügen**Hyperlinks** zum Arbeitsblatt hinzufügen, indem Sie den Zellennamen angeben, auf den der Hyperlink angewendet werden soll

**Hyperlinks** Sammlung im**Arbeitsblatt** Objekt stellt eine überladene bereit**Hinzufügen** Methode. Entwickler können jede überladene Version von verwenden**Hinzufügen** Methode nach ihren spezifischen Bedürfnissen.

 Der folgende Code fügt einen Hyperlink hinzu**B2** und**C3** Zellen des Arbeitsblatts.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **Zugriff auf Hyperlinks**
Sobald ein Hyperlink zu einer Zelle hinzugefügt wird, kann es auch erforderlich sein, zur Laufzeit auf den Hyperlink zuzugreifen und ihn zu ändern. Dazu können Entwickler einfach auf den Hyperlink von zugreifen**Hyperlinks** Sammlung der**Arbeitsblatt** durch Angabe der Zelle (unter Verwendung des Zellennamens oder ihrer Position in Form von Zeilen- und Spaltennummer), zu der der Hyperlink hinzugefügt wird. Sobald auf den Hyperlink zugegriffen wird, können Entwickler seine URL zur Laufzeit ändern.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **Entfernen von Hyperlinks**
 Um einen vorhandenen Hyperlink zu entfernen, können Entwickler einfach auf ein gewünschtes Arbeitsblatt zugreifen und dann**Entfernen** Hyperlink von der**Hyperlinks** Sammlung der**Arbeitsblatt** durch Angabe der mit Hyperlink versehenen Zelle (unter Verwendung ihres Namens oder ihrer Zeilen- und Spaltennummer).



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

Wenn Sie einer Zelle einen Hyperlink hinzufügen und die Hyperlink-URL in der Zelle anstelle eines Werts anzeigen möchten, fügen Sie der Zelle keinen Wert hinzu und fügen Sie einfach den Hyperlink zu dieser Zelle hinzu. Dadurch wird die Zelle mit einem Hyperlink versehen und die Hyperlink-URL wird auch in der Zelle als ihr Wert angezeigt.

{{% /alert %}}
