---
title: Aralık Sınırı Ayarlama
type: docs
weight: 600
url: /tr/net/set-range-border/
---

## **Olası Kullanım Senaryoları**
Bir Aralığa sınırı ayarlamak istediğinizde her bir hücreyi ayrı ayrı ayarlamanıza gerek yoktur. Aralık üzerinde sınırı ayarlayabilirsiniz. Aspose.Cells bu özelliği sunmaktadır.
Bu makale, Aspose.Cells'i kullanarak bir aralığa sınırı ayarlamak için bir örnek kod sağlamaktadır.

## **Excel'de Aralık Sınırı Ayarlama**
Excel'de bir aralığın sınırını ayarlamak için şu adımları takip edebilirsiniz:
1. Sınırlıyı uygulamak istediğiniz hücre aralığını seçin.
2. Kurdele'nin "Ana Sayfa" sekmesinde, "Yazı Tipi" grubunu bulun.
3. "Yazı Tipi" grubu içinde, "Kenarlıklar" açılır düğmesine tıklayın.
<br>
<img src="border.png" />
4. Açılır menüde istenilen kenar tipini seçin. Ön ayarlı kenar stilleri arasından seçim yapabilir veya kendi kenarınızı özelleştirebilirsiniz.
5. İstenilen kenar stili seçildikten sonra, kenar seçilen hücre aralığına uygulanır.

## **Aspose.Cells Kullanarak Aralık Sınırı Ayarlama**
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturma.
1. İlk çalışma sayfasındaki hücrelere veri ekleme.
1. Bir [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) oluşturma.
1. Aralık iç kenarını ayarlama.
1. Aralık dış kenarını ayarlama.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-set-border.cs" >}}
