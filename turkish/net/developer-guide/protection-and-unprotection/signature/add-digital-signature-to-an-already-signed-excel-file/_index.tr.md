---
title: Halihazırda imzalanmış bir Excel dosyasına Dijital İmza ekleme
type: docs
weight: 20
url: /tr/net/add-digital-signature-to-an-already-signed-excel-file/
---
## **Olası Kullanım Senaryoları**

 Aspose.Cells şunları sağlar:[**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature)Halihazırda imzalanmış bir Excel dosyasına dijital imza eklemek için kullanabileceğiniz bir yöntem.

{{% alert color="primary" %}}

Halihazırda imzalanmış bir Excel belgesine dijital imza eklerken, orijinal belgenin Aspose.Cells tarafından oluşturulmuş bir belge olması durumunda iyi çalıştığını lütfen unutmayın. Ancak orijinal belge başka motorlar tarafından oluşturulmuşsa (örn. Microsoft Excel vb.), Aspose.Cells dosyayı yükleyip yeniden kaydettikten sonra aynı tutamaz, bu orijinal imzayı geçersiz kılar.

{{% /alert %}}

## **Halihazırda imzalanmış bir Excel dosyasına Dijital İmza ekleme**

Aşağıdaki örnek kod, nasıl kullanılacağını gösterdi[**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) Halihazırda imzalanmış Excel dosyasına dijital imza ekleme yöntemi. lütfen kontrol ediniz[örnek excel dosyası](50528280.xlsx) bu kodda kullanılır. Bu dosya zaten dijital olarak imzalanmış. lütfen kontrol ediniz[çıktı excel dosyası](50528281.xlsx) kod tarafından oluşturulur. adlı demo sertifikasını kullandık.[AsposeDemo.pfx](50528279.pfx) şifresi olan bu kodda**varsaymak**Ekran görüntüsü, yürütmeden sonra örnek kodun örnek Excel dosyası üzerindeki etkisini gösterir.

![yapılacaklar:resim_alternatif_Metin](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
