---
title: Aspose.Cells kullanarak değiştirmek için Parolayı kontrol edin
type: docs
weight: 190
url: /tr/java/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 atayabilirsiniz**açmak için şifre** ve bir**Değiştirilecek şifre** Microsoft Excel'de çalışma kitaplarınızı oluştururken. Lütfen Microsoft Excel'in bu şifreleri belirtmek için sağladığı arayüzü gösteren bu ekran görüntüsüne bakın.

![yapılacaklar:resim_alternatif_Metin](check-password-to-modify-using-aspose-cells_1.png)

 Bazen, verilen şifrenin şifreyle eşleşip eşleşmediğini kontrol etmeniz gerekir.**Değiştirilecek şifre** programlı olarak. Aspose.Cells sağlar[**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword(java.lang.String)) değiştirmek için verilen şifrenin doğru olup olmadığını kontrol etmek için kullanabileceğiniz yöntem.

{{% /alert %}}

## Java kodunu kontrol etmek için Şifre Aspose.Cells kullanılarak değiştirilecek

 Aşağıdaki örnek kodlar,[kaynak Excel](5473057.xlsx) dosya. Olarak açmak için bir şifresi var*1234* ve değiştirmek için şifre*5678* . Kod ilk önce olup olmadığını kontrol eder*567* değiştirilecek doğru paroladır ve geri döner**yanlış** ve sonra olup olmadığını kontrol eder*5678* değiştirilecek şifredir ve geri döner**doğru**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Java kodu tarafından oluşturulan Konsol Çıktısı

 Yükledikten sonra yukarıdaki örnek kodun Konsol Çıktısı:[kaynak Excel](5473057.xlsx) dosya.

{{< highlight "java" >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
