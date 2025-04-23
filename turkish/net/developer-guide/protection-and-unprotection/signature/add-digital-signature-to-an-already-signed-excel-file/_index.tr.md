---
title: Zaten İmzalanmış Bir Excel Dosyasına Dijital İmza Eklemek
type: docs
weight: 20
url: /tr/net/add-digital-signature-to-an-already-signed-excel-file/
description: Bu makale, C# kodlarıyla Aspose.Cells for .Net kullanarak zaten imzalanmış bir Excel dosyasına dijital imza ekleme işlemini açıklar.
keywords: Zaten imzalanmış bir Excel dosyasına dijital imza eklemek, zaten imzalanmış bir Excel belgesine dijital imza eklemenin nasıl yapılacağını açıklar.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, zaten imzalanmış bir Excel dosyasına dijital imza eklemek için kullanabileceğiniz [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) yöntemini sağlar.

{{% alert color="primary" %}}

Lütfen dikkat, zaten imzalanmış bir Excel belgesine dijital imza eklerken, eğer orijinal belge Aspose.Cells tarafından oluşturulan bir belge ise, iyi çalışır. Ancak orijinal belge diğer motorlar (örneğin Microsoft Excel vb.) tarafından oluşturulmuşsa, Aspose.Cells, dosyayı yükleyip yeniden kaydettikten sonra aynı tutamayacaktır, bu da orijinal imzanın geçersiz olmasına neden olacaktır.

{{% /alert %}}

## **Zaten İmzalanmış Bir Excel Dosyasına Dijital İmza Eklemek**

Aşağıdaki örnek kod, zaten imzalanmış bir Excel dosyasına dijital imza eklemek için [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) yöntemini nasıl kullanacağını göstermektedir. Lütfen bu kodda kullanılan [örnek Excel dosyasını](50528280.xlsx) kontrol edin. Bu dosya zaten dijital imzalanmıştır. Kod tarafından oluşturulan [çıktı Excel dosyasını](50528281.xlsx) kontrol edin. Bu kodda **aspose** adında bir şifresi olan demo sertifikası olan [AsposeDemo.pfx](50528279.pfx) isimli demo sertifikayı kullandık. Ekran görüntüsü, örnek kodun örnek Excel dosyası üzerindeki etkisini gösterir.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
{{< app/cells/assistant language="csharp" >}}
