---
title: Form Kontrolüne Makro Atama
type: docs
weight: 60
url: /tr/python-net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, bir Forma Kontrolü gibi bir makro kodu atamanıza izin verir. Çalışma kitabı içindeki bir Forma Kontrolüne yeni bir Makro Kodu atamak için [**Shape.macro_name**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/macro_name) özelliğini kullanın.

{{% /alert %}}

Aşağıdaki örnek kod, yeni bir çalışma kitabı oluşturur, Form Düğmesine bir Makro Kodu atar ve çıktıyı XLSM biçiminde kaydeder. Çıktı XLSM dosyasını Microsoft Excel'de açtığınızda aşağıdaki makro kodunu göreceksiniz.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Python'da Forma Kontrolüne Makro Atama**

Çıktı XLSM dosyasını Makro Kodu ile oluşturmak için örnek kod burada.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AssignMacroToFormControl-1.py" >}}
