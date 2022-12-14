---
title: Verwalten von Bildern in einem Arbeitsblatt
type: docs
weight: 100
url: /de/net/managing-pictures-in-a-worksheet/
---
{{% alert color="primary" %}} 

Die meisten Menschen glauben, dass ein Bild die Dinge besser erklären kann als Worte. Aus diesem Grund unterstützt Aspose.Cells.GridDesktop das Hinzufügen von Bildern zu Arbeitsblättern, um diesen Glauben der Menschen umzusetzen. In diesem Thema besprechen wir das Hinzufügen und Bearbeiten von Bildern in Arbeitsblättern.

{{% /alert %}} 
## **Bilder hinzufügen**
Um mit Aspose.Cells.GridDesktop einen Hyperlink zu einer Zelle hinzuzufügen, führen Sie bitte die folgenden Schritte aus:

-  Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Hinzufügen**Bild** in das Arbeitsblatt, indem Sie den Dateipfad des Bildes und den Zellennamen angeben, wo das Bild eingefügt wird

**Bilder** Sammlung im**Arbeitsblatt** Objekt stellt eine überladene bereit**Hinzufügen** Methode. Entwickler können jede überladene Version von verwenden**Hinzufügen** Methode nach ihren spezifischen Bedürfnissen. Mit diesen überladenen Versionen von**Hinzufügen** Methode ist es möglich, ein Bild aus Datei, Stream oder hinzuzufügen**Bild** Objekt.

Nachfolgend finden Sie den Beispielcode zum Hinzufügen von Bildern zu Arbeitsblättern.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **Zugriff auf Bilder**
 Um auf ein vorhandenes Bild im Arbeitsblatt zuzugreifen und es zu ändern, können Entwickler über das auf das Bild zugreifen**Bilder** Sammlung der**Arbeitsblatt** indem Sie die Zelle angeben (unter Verwendung des Zellennamens oder ihrer Position in Form von Zeilen- und Spaltennummer), in die das Bild eingefügt wird. Sobald auf das Bild zugegriffen wird, können Entwickler sein Bild zur Laufzeit ändern.

Nachfolgend finden Sie den Beispielcode für den Zugriff auf und die Änderung der Bilder in einem Arbeitsblatt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **Bilder entfernen**
 Um ein vorhandenes Bild zu entfernen, können Entwickler einfach auf ein gewünschtes Arbeitsblatt zugreifen und dann**Entfernen** Bild von der**Bilder** Sammlung der**Arbeitsblatt** indem Sie die Zelle angeben (unter Verwendung ihres Namens oder ihrer Zeilen- und Spaltennummer), die das Bild enthält.

Im folgenden Code wird gezeigt, wie Bilder aus dem Arbeitsblatt entfernt werden.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
