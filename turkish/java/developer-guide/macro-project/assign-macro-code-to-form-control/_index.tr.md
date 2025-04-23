---
title: Makro Kodunu Form Kontrolüne Atama
type: docs
weight: 400
url: /tr/java/assign-macro-code-to-form-control/
---

{{% alert color="primary" %}} 

Aspose.Cells, bir Forma Kontrolü gibi bir Button'a Makro Kodu atamanıza izin verir. Lütfen, çalışma kitabındaki bir Forma Kontrolüne yeni Makro Kodu atamak için [ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-) yöntemini kullanın.

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
{{< app/cells/assistant language="java" >}}
