---
title: Golang ile C++ kullanarak Form Kontrolüne Makro atayın
linktitle: Form Kontrolüne Makro Atama
type: docs
weight: 60
url: /tr/go-cpp/assign-macro-to-form-control/
description: Aspose.Cells for C++ kullanarak bir Makro Kodunu Düğme gibi Bir Form Denetimine nasıl atayacağınızı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, Düğme gibi Bir Form Kontrolüne bir Makro Kodu atamanıza izin verir. Lütfen çalışma kitabının içindeki Form Kontrolüne yeni bir Makro Kodu atamak için [**Shape.GetMacroName()**](https://reference.aspose.com/cells/go-cpp/shape/getmacroname/) özelliğini kullanın.

{{% /alert %}}

Aşağıdaki örnek kod yeni bir çalışma kitabı oluşturur, bir Makro Kodunu Bir Form Düğmesine atar ve sonucu XLSM formatında kaydeder. Microsoft Excel'de çıktı XLSM dosyasını açtığınızda, aşağıdaki makro kodunu göreceksiniz.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## ** C++ ile Form Denetimine Makro Ata**

Çıktı XLSM dosyasını Makro Kodu ile oluşturmak için örnek kod burada.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AssignMacroToFormControl.go" >}}
