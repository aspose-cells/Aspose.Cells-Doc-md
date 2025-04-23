---
title: Değiştirmek için Parola Kontrolü Aspose.Cells for Python via .NET ile
type: docs
weight: 2400
url: /tr/python-net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Bazen, sağlanan parolanın **Değiştirmek için Parola** ile eşleşip eşleşmediğini programatik olarak kontrol etmeniz gerekir. Aspose.Cells for Python via .NET, yanlış olup olmadığını kontrol etmek için kullanabileceğiniz WorkbookSettings.write_protection.validate_password() yöntemini sağlar.

{{% /alert %}}

## **Microsoft Excel'de Değiştirme Şifresini Kontrol Etme**

Microsoft Excel'de çalışma kitapları oluştururken **Açma Şifresi** ve **Değiştirme Şifresi** atayabilirsiniz. Bu şifreleri belirlemek için Microsoft Excel'in sağladığı arayüzü gösteren bu ekran görüntüsüne bakınız.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Değiştirmek için Parola Kontrolü Aspose.Cells for Python via .NET ile**

Aşağıdaki örnek kod, [kaynak Excel](5112232.xlsx) dosyasını yükler. Dosyanın Açma Şifresi 1234 ve Değiştirme Şifresi 5678'dir. Kod önce 567'nin doğru Değiştirme Şifresi olup olmadığını kontrol eder ve yanlış döndürür, ardından 5678'in Değiştirme Şifresi olup olmadığını kontrol eder ve doğru döndürür.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckPasswordToModifyUsingAsposeCells.py" >}}

### **Konsol Çıktısı**

Yukarıdaki örnek kodun [kaynak Excel](5112232.xlsx) dosyasını yükledikten sonraki Konsol Çıkışı burada.

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}

