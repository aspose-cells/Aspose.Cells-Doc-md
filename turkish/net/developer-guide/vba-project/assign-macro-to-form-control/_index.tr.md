---
title: Form Kontrolüne Makro Atama
type: docs
weight: 60
url: /tr/net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells, Düğme gibi Bir Form Kontrolüne bir Makro Kodu atamanıza izin verir. Lütfen çalışma kitabının içindeki Form Kontrolüne yeni bir Makro Kodu atamak için [**Shape.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname) özelliğini kullanın.

{{% /alert %}}

Aşağıdaki örnek kod, yeni bir çalışma kitabı oluşturur, Form Düğmesine bir Makro Kodu atar ve çıktıyı XLSM biçiminde kaydeder. Çıktı XLSM dosyasını Microsoft Excel'de açtığınızda aşağıdaki makro kodunu göreceksiniz.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **C# Form Kontrolüne Makro Atama**

Çıktı XLSM dosyasını Makro Kodu ile oluşturmak için örnek kod burada.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
