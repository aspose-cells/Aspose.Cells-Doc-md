---
title: Verwalten von Kommentaren in einem Arbeitsblatt
type: docs
weight: 110
url: /de/net/managing-comments-in-a-worksheet/
---
{{% alert color="primary" %}} 

In MS Excel müssen Sie mit der Kommentarfunktion vertraut sein, mit der Benutzer Kommentare zu Zellen hinzufügen können. Diese Funktion ist in den Fällen hilfreich, in denen es erforderlich ist, den Benutzern einige Informationen bereitzustellen, wenn sie im Begriff sind, Werte in die Zellen einzugeben. Immer wenn ein Benutzer seinen Mauszeiger auf eine kommentierte Zelle platziert, erscheint eine kleine Popup-Nachricht, um dem Benutzer einige Informationen bereitzustellen. Mit Aspose.Cells.GridDesktop können Entwickler Kommentare zu Zellen erstellen. In diesem Thema erklären wir die Verwendung dieser Funktion im Detail.

{{% /alert %}} 
## **Kommentare hinzufügen**
Um einen Kommentar zu einer Zelle mit Aspose.Cells.GridDesktop hinzuzufügen, führen Sie bitte die folgenden Schritte aus:

-  Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Hinzufügen**Kommentar** in das Arbeitsblatt, indem Sie die Zelle angeben (unter Verwendung ihres Namens oder ihrer Zeilen- und Spaltennummer), in der der Kommentar hinzugefügt werden soll.

 Der folgende Code fügt Kommentare zu hinzu**b2** und**b4** Zellen des Arbeitsblatts.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


**Kommentare** Sammlung im**Arbeitsblatt** Objekt stellt eine überladene bereit**Hinzufügen** Methode. Entwickler können jede überladene Version von verwenden**Hinzufügen** Methode nach ihren spezifischen Bedürfnissen.
## **Zugriff auf Kommentare**
Um auf einen vorhandenen Kommentar im Arbeitsblatt zuzugreifen und ihn zu ändern, können Entwickler über den Kommentar auf den Kommentar zugreifen**Kommentare** Sammlung der**Arbeitsblatt** indem Sie die Zelle angeben (unter Verwendung des Zellennamens oder ihrer Position in Bezug auf Zeilen- und Spaltennummer), in die der Kommentar eingefügt wird. Sobald auf den Kommentar zugegriffen wird, können Entwickler seinen Text zur Laufzeit ändern.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **Kommentare entfernen**
 Um einen vorhandenen Kommentar zu entfernen, können Entwickler einfach auf ein gewünschtes Arbeitsblatt zugreifen und dann**Entfernen** Kommentar von der**Kommentare** Sammlung der**Arbeitsblatt** durch Angabe der Zelle (unter Verwendung ihres Namens oder ihrer Zeilen- und Spaltennummer), die den Kommentar enthält.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
