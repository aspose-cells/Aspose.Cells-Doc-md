---
title: Makro Kodunu Form Kontrolüne Atama
type: docs
weight: 400
url: /tr/java/assign-macro-code-to-form-control/
---

{{% alert color="primary" %}} 

Aspose.Cells, Form Düğmesi gibi bir Form Kontrolüne yeni bir Makro Kodu atamanızı sağlar. Yeni bir Makro Kodu atamak için [ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) yöntemini kullanabilirsiniz.

{{% /alert %}} 
## **Aspose.Cells Kullanarak Form Kontrolüne Makro Kodu Atama**
Aşağıdaki örnek kod, yeni bir çalışma kitabı oluşturur, bir Makro Kodu'nu bir Form Düğmesine atar ve çıktıyı XLSM formatında kaydeder. Çıktı XLSM dosyasını Microsoft Excel'de açtığınızda aşağıdaki makro kodunu göreceksiniz.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Makro Kodunu içeren çıktı XLSM dosyasını oluşturmak için kullanılan örnek kod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
