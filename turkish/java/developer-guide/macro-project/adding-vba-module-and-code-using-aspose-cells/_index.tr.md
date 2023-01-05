---
title: Aspose.Cells kullanarak VBA Modülü ve Kodu Ekleme
type: docs
weight: 20
url: /tr/java/adding-vba-module-and-code-using-aspose-cells/
---
{{% alert color="primary" %}}

 Aspose.Cells, Aspose.Cells'i kullanarak yeni bir VBA Modülü ve Makro Kodu eklemenizi sağlar. Lütfen[**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet)) çalışma kitabına yeni VBA Modülü ekleme yöntemi

{{% /alert %}}

## **Aspose.Cells kullanarak VBA Modülü ve Kodu Ekleme**

Aşağıdaki örnek kod, yeni bir çalışma kitabı oluşturur ve yeni bir VBA Modülü ve Makro Kodu ekler ve çıktıyı XLSM biçiminde kaydeder. Bir kez, XLSM çıktı dosyasını Microsoft Excel'de açacaksınız ve**Geliştirici > Visual Basic** menü komutları, "TestModule" adında bir modül göreceksiniz ve içinde aşağıdaki makro kodunu göreceksiniz.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Basit kod

İşte XLSM çıktı dosyasını VBA Modülü ve Makro Kodu ile oluşturmak için örnek bir kod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
