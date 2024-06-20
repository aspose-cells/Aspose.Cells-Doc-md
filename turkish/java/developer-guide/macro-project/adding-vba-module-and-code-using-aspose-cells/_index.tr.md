---
title: Aspose.Cells Kullanarak VBA Modülü ve Kod Ekleme
type: docs
weight: 20
url: /tr/java/adding-vba-module-and-code-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells, Aspose.Cells kullanarak yeni bir VBA Modülü ve Makro Kodu eklemenizi sağlar. Yeni bir VBA Modülü eklemek için [**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet)) yöntemini kullanabilirsiniz.

{{% /alert %}}

## **Aspose.Cells Kullanarak VBA Modülü ve Kod Ekleme**

Aşağıdaki örnek kod yeni bir çalışma kitabı oluşturur ve yeni bir VBA Modülü ve Makro Kodu ekler ve çıktıyı XLSM biçiminde kaydeder. Bir kez çıktı XLSM dosyasını Microsoft Excel’de açarsanız ve **Geliştirici > Görsel Temel** menü komutlarına tıklayarak “TestModülü” adlı bir modül göreceksiniz ve içinde aşağıdaki makro kodunu göreceksiniz.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Örnek Kod

İşte VBA Modülü ve Makro Kodu içeren çıktı XLSM dosyasını oluşturmak için kullanılan örnek kod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
