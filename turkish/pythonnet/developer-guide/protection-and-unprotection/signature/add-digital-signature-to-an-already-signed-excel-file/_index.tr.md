---
title: Zaten İmzalanmış Bir Excel Dosyasına Dijital İmza Eklemek
type: docs
weight: 20
url: /tr/python-net/add-digital-signature-to-an-already-signed-excel-file/
description: Bu makale, Aspose.Cells for Python via .NET kullanarak zaten imzalanmış bir Excel dosyasına Dijital İmza eklemeyi anlatmaktadır.
keywords: Zaten imzalanmış bir Excel dosyasına dijital imza eklemek, zaten imzalanmış bir Excel belgesine dijital imza eklemenin nasıl yapılacağını açıklar.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells for Python via .NET, kullanabileceğiniz [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) metodunu sağlar; bu metod, zaten imzalanmış Excel dosyasına dijital imza ekler.

{{% alert color="primary" %}}

Lütfen dikkat edin; eğer zaten imzalanmış bir Excel dosyasına dijital imza ekliyorsanız ve dosya Aspose.Cells for Python via .NET tarafından oluşturulmuşsa, iyi çalışır. Ancak, dosya başka motorlar (ör. Microsoft Excel vb.) tarafından oluşturulmuşsa, Aspose.Cells for Python via .NET yükleme ve yeniden kaydetme sonrası dosyayı aynı tutamayabilir, bu da orijinal imzayı geçersiz kılacaktır.

{{% /alert %}}

## **Zaten İmzalanmış Bir Excel Dosyasına Dijital İmza Eklemek**

Aşağıdaki örnek kod, zaten imzalanmış bir Excel dosyasına dijital imza eklemek için [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) yöntemini nasıl kullanacağını göstermektedir. Lütfen bu kodda kullanılan [örnek Excel dosyasını](50528280.xlsx) kontrol edin. Bu dosya zaten dijital imzalanmıştır. Kod tarafından oluşturulan [çıktı Excel dosyasını](50528281.xlsx) kontrol edin. Bu kodda **aspose** adında bir şifresi olan demo sertifikası olan [AsposeDemo.pfx](50528279.pfx) isimli demo sertifikayı kullandık. Ekran görüntüsü, örnek kodun örnek Excel dosyası üzerindeki etkisini gösterir.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AddDigitalSignatureToAnAlreadySignedExcelFile.py" >}}

{{< app/cells/assistant language="python-net" >}}
