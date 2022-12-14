---
title: Aspose.Cells kullanarak değiştirmek için Parolayı kontrol edin
type: docs
weight: 2400
url: /tr/net/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 Bazen, verilen şifrenin şifreyle eşleşip eşleşmediğini kontrol etmeniz gerekir.**Değiştirilecek şifre** programlı olarak. Aspose.Cells, değiştirilecek Parolanın doğru olup olmadığını kontrol etmek için kullanabileceğiniz WorkbookSettings.WriteProtection.ValidatePassword() yöntemini sağlar.

{{% /alert %}}

## **Microsoft Excel'de değiştirmek için Parolayı kontrol edin**

atayabilirsin**açmak için şifre** ve**Değiştirilecek şifre** Microsoft Excel'de çalışma kitaplarınızı oluştururken. Lütfen Microsoft Excel'in bu şifreleri belirtmek için sağladığı arayüzü gösteren bu ekran görüntüsüne bakın.

|![yapılacaklar:resim_alternatif_Metin](check-password-to-modify-using-aspose-cells_1.png)|
|:- |

## **Aspose.Cells kullanarak değiştirmek için Parolayı kontrol edin**

 Aşağıdaki örnek kodlar,[kaynak Excel](5112232.xlsx) dosya. 1234 olarak açmak için bir Parolası ve 5678 olarak değiştirmek için bir Parolası vardır. Kod, önce 567'nin değiştirilecek Parola'nın doğru olup olmadığını kontrol eder ve false döndürür ve ardından 5678'in değiştirilecek Parola olup olmadığını kontrol eder ve doğru döndürür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Konsol Çıkışı**

 Yükledikten sonra yukarıdaki örnek kodun Konsol Çıktısı:[kaynak Excel](5112232.xlsx) dosya.

{{< highlight "java" >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
