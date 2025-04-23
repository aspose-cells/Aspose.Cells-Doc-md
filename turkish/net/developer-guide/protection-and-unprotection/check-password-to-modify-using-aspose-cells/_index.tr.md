---
title: Aspose.Cells Kullanarak Değiştirme Şifresini Kontrol Etme
type: docs
weight: 2400
url: /tr/net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Bazı durumlarda, verilen şifrenin programlı olarak **Değiştirme Şifresi** ile eşleşip eşleşmediğini kontrol etmeniz gerekebilir. Aspose.Cells, doğru veya yanlış olduğunu kontrol etmek için WorkbookSettings.WriteProtection.ValidatePassword() metodunu sağlar.

{{% /alert %}}

## **Microsoft Excel'de Değiştirme Şifresini Kontrol Etme**

Microsoft Excel'de çalışma kitapları oluştururken **Açma Şifresi** ve **Değiştirme Şifresi** atayabilirsiniz. Bu şifreleri belirlemek için Microsoft Excel'in sağladığı arayüzü gösteren bu ekran görüntüsüne bakınız.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Aspose.Cells Kullanarak Değiştirme Şifresini Kontrol Etme**

Aşağıdaki örnek kod, [kaynak Excel](5112232.xlsx) dosyasını yükler. Dosyanın Açma Şifresi 1234 ve Değiştirme Şifresi 5678'dir. Kod önce 567'nin doğru Değiştirme Şifresi olup olmadığını kontrol eder ve yanlış döndürür, ardından 5678'in Değiştirme Şifresi olup olmadığını kontrol eder ve doğru döndürür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Konsol Çıktısı**

Yukarıdaki örnek kodun [kaynak Excel](5112232.xlsx) dosyasını yükledikten sonraki Konsol Çıkışı burada.

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
