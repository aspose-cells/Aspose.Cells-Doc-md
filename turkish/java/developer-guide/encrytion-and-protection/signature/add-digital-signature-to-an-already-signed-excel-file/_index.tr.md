---
title: Zaten İmzalanmış Bir Excel Dosyasına Dijital İmza Eklemek
type: docs
weight: 20
url: /tr/java/add-digital-signature-to-an-already-signed-excel-file/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, zaten imzalanmış bir Excel dosyasına dijital imza eklemek için [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature-com.aspose.cells.DigitalSignatureCollection-) yöntemini sağlar.

{{% alert color="primary" %}}

Lütfen dikkat, zaten imzalanmış bir Excel belgesine dijital imza eklerken, eğer orijinal belge Aspose.Cells tarafından oluşturulan bir belge ise, iyi çalışır. Ancak orijinal belge diğer motorlar (örneğin Microsoft Excel vb.) tarafından oluşturulmuşsa, Aspose.Cells, dosyayı yükleyip yeniden kaydettikten sonra aynı tutamayacaktır, bu da orijinal imzanın geçersiz olmasına neden olacaktır.

{{% /alert %}}

## **Daha önceden imzalanmış Excel dosyasına Dijital İmza ekleme**

Aşağıdaki örnek kod, zaten imzalanmış bir Excel dosyasına dijital imza eklemek için [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature-com.aspose.cells.DigitalSignatureCollection-) yönteminin nasıl kullanıldığını açıklar. Bu kodda kullanılan [örnek Excel dosyasını](50528287.xlsx) kontrol edin. Bu dosya zaten dijital olarak imzalanmıştır. Kodun ürettiği [çıktı Excel dosyasını](50528288.xlsx) kontrol edin. Bu kodda *aspose* adlı demo sertifikası kullanılmıştır. Ek olarak, bu kodda kullanılan [AsposeTest.pfx](50528289.pfx) adlı sertifikasının bir şifresi olan *aspose* vardır. Ekran görüntüsü, örnek kodun örnekleme Excel dosyası üzerindeki etkisini gösterir.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
{{< app/cells/assistant language="java" >}}
