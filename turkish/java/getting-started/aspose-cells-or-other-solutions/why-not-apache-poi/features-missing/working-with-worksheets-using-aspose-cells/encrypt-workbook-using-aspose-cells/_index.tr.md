---
title: Aspose.Cells ile Çalışma Kitabını Şifrele
type: docs
weight: 60
url: /tr/java/encrypt-workbook-using-aspose-cells/
---

## **Aspose.Cells - Çalışma Kitabını Şifrele**
Aşağıdaki örnek, Aspose.Cells API'sını kullanarak bir Excel dosyasını şifrelemenin / parolayla korumanın nasıl yapılabileceğini göstermektedir.

**Java**

{{< highlight java >}}

 //Instantiate a Workbook object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Password protect the file.

workbook.getSettings().setPassword("1234");

//Specify XOR encryption type.

workbook.setEncryptionOptions(EncryptionType.XOR, 40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.setEncryptionOptions(EncryptionType.STRONG_CRYPTOGRAPHIC_PROVIDER, 128);

//Save the excel file.

workbook.save(dataDir + "AsposeEncryptedWorkBook.xls");

{{< /highlight >}}
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeEncryptSpreadsheets.java)

{{% alert color="primary" %}} 

Daha fazla detay için [Excel Dosyalarını Şifreleme](/cells/tr/java/encrypting-excel-files/) sayfasını ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
