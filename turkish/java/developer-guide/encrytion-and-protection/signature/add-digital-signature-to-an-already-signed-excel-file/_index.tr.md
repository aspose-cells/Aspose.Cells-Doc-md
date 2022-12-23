---
title: Halihazırda imzalanmış bir Excel dosyasına Dijital İmza ekleme
type: docs
weight: 20
url: /tr/java/add-digital-signature-to-an-already-signed-excel-file/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells şunları sağlar:[**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) önceden imzalanmış bir Excel dosyasına dijital imza eklemek için kullanabileceğiniz yöntem.

{{% alert color="primary" %}}

Halihazırda imzalanmış bir Excel belgesine dijital imza eklerken, orijinal belgenin Aspose.Cells tarafından oluşturulmuş bir belge olması durumunda iyi çalıştığını lütfen unutmayın. Ancak orijinal belge başka motorlar tarafından oluşturulmuşsa (örn. Microsoft Excel vb.), Aspose.Cells dosyayı yükleyip yeniden kaydettikten sonra aynı tutamaz, bu orijinal imzayı geçersiz kılar.

{{% /alert %}}

## **Halihazırda imzalanmış bir Excel dosyasına Dijital İmza ekleme**

Aşağıdaki örnek kod, nasıl kullanılacağını açıklar[**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) önceden imzalanmış Excel dosyasına dijital imza ekleme yöntemi. lütfen kontrol ediniz[örnek excel dosyası](50528287.xlsx)bu kodda kullanılır. Bu dosya zaten dijital olarak imzalanmış. lütfen kontrol ediniz[çıktı excel dosyası](50528288.xlsx)kod tarafından oluşturulur. adlı demo sertifikasını kullandık.[AsposeTest.pfx](50528289.pfx)şifresi olan bu kodda*varsaymak*Ekran görüntüsü, yürütmeden sonra örnek kodun örnek Excel dosyası üzerindeki etkisini gösterir.

![yapılacaklar:resim_alternatif_metin](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
