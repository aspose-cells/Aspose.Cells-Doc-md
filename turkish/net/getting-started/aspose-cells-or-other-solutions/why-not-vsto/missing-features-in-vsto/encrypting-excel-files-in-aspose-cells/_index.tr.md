---
title: Aspose.Cells'de Excel Dosyalarını Şifreleme
type: docs
weight: 90
url: /tr/net/encrypting-excel-files-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007), elektronik tablolarınızı şifrelemenizi ve parolayla korumanızı sağlar. Bir şifreleme hizmeti sağlayıcısı tarafından sağlanan algoritmaları veya farklı özelliklere sahip bir dizi şifreleme algoritması olan CSP'yi kullanır. Varsayılan CSP, "Office 97/2000 Uyumlu" veya "Zayıf Şifreleme (XOR)" şeklindedir. Uygun şifreleme anahtarı uzunluğunu seçmek önemlidir. Bazı CSP'ler 40 veya 56 bitten fazlasını desteklemez. Bu zayıf bir şifreleme olarak kabul edilir. Güçlü şifreleme için minimum 128 bit anahtar uzunluğu gereklidir. Microsoft Windows, güçlü şifreleme türleri de sunan CSP'ler içerir, örneğin 'Microsoft Güçlü Şifreleme Sağlayıcı'. Size bir fikir vermesi için, bankaların İnternet Bankacılığı sistemleriyle bağlantıyı şifrelemek için kullandıkları 128 bit şifrelemedir.

Aspose.Cells, Microsoft Excel dosyalarını istediğiniz şifreleme türüyle şifrelemenizi ve parola korumanızı sağlar.

{{% /alert %}} 
## **Microsoft Excel'i kullanma**
Microsoft Excel'de (burada Microsoft Excel 2003) dosya şifreleme ayarlarını yapmak için:

1.  itibaren**Aletler** menü, seç**Seçenekler**.
 Bir iletişim kutusu görünür.
1.  seçin**Güvenlik** sekme.
1.  Bir şifre girin ve tıklayın**Gelişmiş** 
   **Seçenekler iletişim kutusu** 

![yapılacaklar:resim_alternatif_Metin](encrypting-excel-files-in-aspose-cells_1.png)




1.  Şifreleme türünü seçin ve parolayı onaylayın.

   **Şifreleme Türü iletişim kutusu** 

![yapılacaklar:resim_alternatif_Metin](encrypting-excel-files-in-aspose-cells_2.png)



## **Aspose.Cells ile şifreleme**
Aşağıdaki örnek, Aspose.Cells API kullanılarak bir excel dosyasının nasıl şifreleneceğini ve parolayla korunacağını gösterir.

**C#**

{{< highlight "csharp" >}}

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
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1))
