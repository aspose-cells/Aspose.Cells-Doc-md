---
title: Aspose.Cells ile Excel Dosyalarının Şifrelenmesi
type: docs
weight: 90
url: /tr/net/encrypting-excel-files-in-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007), elektronik tablolarınızı şifrelemenize ve parola koruması yapmanıza olanak tanır. Farklı özelliklere sahip bir dizi şifreleme algoritmasını içeren bir şifreleme hizmet sağlayıcısı veya CSP tarafından sağlanan algoritmaları kullanır. Varsayılan CSP, 'Office 97/2000 Uyumlu' veya 'Zayıf Şifreleme (XOR)' olarak adlandırılır. Doğru şifreleme anahtar uzunluğunu seçmek önemlidir. Bazı CSP'ler 40 veya 56 biti aşmaz. Bu zayıf bir şifreleme olarak kabul edilir. Güçlü şifreleme için minimum 128 bitlik bir anahtar uzunluğu gereklidir. Microsoft Windows, örneğin 'Microsoft Güçlü Kriptografik Sağlayıcısı' gibi güçlü şifreleme türleri sunan CSP'leri içerir. 128 bitlik şifreleme, bankaların İnternet Bankacılığı sistemleriyle olan bağlantıyı şifrelemek için kullandıkları şeydir.

Aspose.Cells, istediğiniz şifreleme türüyle Microsoft Excel dosyalarını şifrelemeye ve parola korumaya olanak tanır.

{{% /alert %}} 
## **Microsoft Excel Kullanımı**
Microsoft Excel'de (burada Microsoft Excel 2003) dosya şifreleme ayarlarını yapmak için:

1. **Araçlar** menüsünden **Seçenekler**'i seçin.
   Bir iletişim kutusu görünür.
1. **Güvenlik** sekmesini seçin.
1. Bir parola girin ve **Gelişmiş**'i tıklayın. 
   **Seçenekler iletişim kutusu** 

![todo:image_alt_text](encrypting-excel-files-in-aspose-cells_1.png)




1. Şifreleme türünü seçin ve parolayı onaylayın. 

   **Şifreleme Türü iletişim kutusu** 

![todo:image_alt_text](encrypting-excel-files-in-aspose-cells_2.png)



## **Aspose.Cells ile Şifreleme**
Aşağıdaki örnek, Aspose.Cells API'sını kullanarak bir Excel dosyasını şifrelemek ve parolayla korumak için nasıl yapılacağını göstermektedir.

**C#**

{{< highlight csharp >}}

 //Instantiate a Workbook object.

//Open an excel file.

Workbook workbook = new Workbook("Book1.xls");

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR,40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save("encryptedBook1.xls");



{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Encrypting%20Excel%20Files)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1))
