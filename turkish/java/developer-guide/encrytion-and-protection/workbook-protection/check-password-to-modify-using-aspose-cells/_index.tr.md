---
title: Aspose.Cells Kullanarak Değiştirme Şifresini Kontrol Etme
type: docs
weight: 190
url: /tr/java/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Microsoft Excel'de çalışma kitaplarını oluştururken **Açmak için Parola** ve **Değiştirmek için Parola** atayabilirsiniz. Bu parolaları belirtmek için Microsoft Excel'in sağladığı arayüzü gösteren bu ekran görüntüsüne bakınız.

![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)

Bazen, verilen parolanın **Değiştirmek için Parola** ile eşleşip eşleşmediğini programlı olarak kontrol etmeniz gerekebilir. Aspose.Cells, verilen parolanın doğru olup olmadığını kontrol etmek için [**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword-java.lang.String-) yöntemini sağlar.

{{% /alert %}}

## Aspose.Cells kullanarak Değiştirmek için Parolayı kontrol etmek için Java kodu

Aşağıdaki örnek kodlar [kaynak Excel](5473057.xlsx) dosyasını yükler. Bu dosyanın açmak için parolası *1234* ve değiştirmek için parolası *5678* vardır. Kod önce *567* 'nin doğru parola olup olmadığını kontrol eder ve **false** döndürür ve ardından *5678* 'nin parola olup olmadığını kontrol eder ve **true** döndürür.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Aspose.Cells tarafından oluşturulan Java kodu tarafından oluşturulan Konsol Çıktısı

Yukarıdaki örnek kodun [kaynak Excel](5473057.xlsx) dosyasını yükledikten sonra Konsol Çıktısı

{{< highlight java >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
