---
title: Form Kontrolüne Makro Kodu Ata
type: docs
weight: 400
url: /tr/java/assign-macro-code-to-form-control/
---
{{% alert color="primary" %}} 

 Aspose.Cells, bir Form Kontrolüne Düğme gibi bir Makro Kodu atamanıza izin verir. lütfen[ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) çalışma kitabı içindeki bir Form Denetimine yeni bir Makro Kodu atama yöntemi.

{{% /alert %}} 
## **Aspose.Cells Kullanarak Form Kontrolüne Makro Kodu Atama**
Aşağıdaki örnek kod, yeni bir çalışma kitabı oluşturur, Form Buttom'a Makro Kodu atar ve çıktıyı XLSM biçiminde kaydeder. Bir kez, XLSM çıktı dosyasını Microsoft Excel'de açacaksınız, aşağıdaki makro kodunu göreceksiniz.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

İşte XLSM çıktı dosyasını Makro Kodu ile oluşturmak için örnek bir kod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
