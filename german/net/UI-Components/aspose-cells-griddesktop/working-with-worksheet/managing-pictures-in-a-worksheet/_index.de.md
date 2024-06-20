---
title: Verwaltung von Bildern in einem Arbeitsblatt
type: docs
weight: 100
url: /de/net/aspose-cells-griddesktop/manage-pictures-in-a-worksheet/
keywords: GridDesktop, Bild, Bilder
description: Dieser Artikel stellt vor, wie man mit einem Bild in einem Arbeitsblatt in GridDesktop arbeitet.
---

{{% alert color="primary" %}} 

Die meisten Menschen glauben, dass ein Bild Dinge besser erklären kann als Worte. Deshalb unterstützt Aspose.Cells.GridDesktop das Hinzufügen von Bildern zu Arbeitsblättern, um diesem Glauben der Menschen gerecht zu werden. In diesem Thema werden das Hinzufügen und Bearbeiten von Bildern in Arbeitsblättern diskutiert.

{{% /alert %}} 
## **Bilder hinzufügen**
Um einen Hyperlink zu einer Zelle mit Aspose.Cells.GridDesktop hinzuzufügen, befolgen Sie die folgenden Schritte:

- Fügen Sie das Steuerelement Aspose.Cells.GridDesktop zu Ihrem **Formular** hinzu
- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Fügen Sie dem Arbeitsblatt ein **Bild** hinzu, indem Sie den Dateipfad des Bildes und den Zellnamen angeben, in den das Bild eingefügt werden soll

Die **Bilder**-Sammlung des **Arbeitsblatt**-Objekts bietet eine überladene **Add**-Methode. Entwickler können eine beliebige überladene Version der **Add**-Methode gemäß ihren spezifischen Anforderungen verwenden. Mit diesen überladenen Versionen der **Add**-Methode ist es möglich, ein Bild aus einer Datei, einem Stream oder einem **Bild**-Objekt hinzuzufügen.

Unten finden Sie den Beispielcode zum Hinzufügen von Bildern in Arbeitsblätter.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **Zugriff auf Bilder**
Um auf ein vorhandenes Bild im Arbeitsblatt zuzugreifen und es zu ändern, können Entwickler das Bild aus der **Bildsammlung** des **Arbeitsblatts** aufrufen, indem sie die Zelle angeben (unter Verwendung des Zellnamens oder seiner Position in Bezug auf Zeilen- und Spaltennummer), in die das Bild eingefügt ist. Sobald das Bild aufgerufen wird, können Entwickler das Bild zur Laufzeit ändern.

Unten finden Sie den Beispielcode zum Zugriff auf Bilder und deren Änderung in einem Arbeitsblatt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **Bilder entfernen**
Um ein vorhandenes Bild zu entfernen, können Entwickler einfach auf ein gewünschtes Arbeitsblatt zugreifen und dann das Bild aus der **Bildsammlung** des **Arbeitsblatts** entfernen, indem sie die Zelle angeben (unter Verwendung seines Namens oder der Zeilen- und Spaltennummer), die das Bild enthält.

Im Code unten wird gezeigt, wie Bilder aus einem Arbeitsblatt entfernt werden können.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
