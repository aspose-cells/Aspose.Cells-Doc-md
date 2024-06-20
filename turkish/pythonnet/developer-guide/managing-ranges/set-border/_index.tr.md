---
title: Aralık Sınırı Ayarlama
type: docs
weight: 600
url: /tr/python-net/set-range-border/
description: Bu makale, Aspose.Cells for Python via .NET API si ile bir aralık sınırı belirlemenin nasıl yapıldığını göstermektedir.
keywords: Python Excel Kitaplığı, Python aralık sınırı ayarlama, Python aralık sınırı ekleme.
---

## **Olası Kullanım Senaryoları**
Bir Aralık için sınır belirlemek istediğinizde, her hücreyi ayrı ayrı belirlemenize gerek yoktur. Aspose.Cells for Python via .NET, bu özelliği sunar.
Bu makale, Aspose.Cells for Python via .NET'yi kullanarak bir aralık sınırı belirlemek için örnek bir kod sunmaktadır.

## **Excel'de Aralık Sınırı Nasıl Ayarlanır**
Excel'de bir aralığın sınırını ayarlamak için şu adımları takip edebilirsiniz:
1. Sınırlıyı uygulamak istediğiniz hücre aralığını seçin.
2. Kurdele'nin "Ana Sayfa" sekmesinde, "Yazı Tipi" grubunu bulun.
3. "Yazı Tipi" grubu içinde, "Kenarlıklar" açılır düğmesine tıklayın.
<br>
<img src="border.png" />
4. Açılır menüde istenilen kenar tipini seçin. Ön ayarlı kenar stilleri arasından seçim yapabilir veya kendi kenarınızı özelleştirebilirsiniz.
5. İstenilen kenar stili seçildikten sonra, kenar seçilen hücre aralığına uygulanır.

## **Aspose.Cells for Python Excel Kütüphanesi ile Aralık Sınırı Nasıl Ayarlanır**
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturma.
1. İlk çalışma sayfasındaki hücrelere veri ekleme.
1. Bir [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) oluşturma.
1. Aralık iç kenarını ayarlama.
1. Aralık dış kenarını ayarlama.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-set-border.py" >}}
