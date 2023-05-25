---
title: Aralık Sınırını Ayarla
type: docs
weight: 600
url: /tr/net/set-range-border/
---
##  **Olası Kullanım Senaryoları**
Aralık için sınır ayarlamak istediğinizde, her hücreyi ayrı ayrı ayarlamanız gerekmez. Aralıktaki sınırı ayarlayabilirsiniz. Aspose.Cells bu özelliği sunuyor.
Bu makalede, aralık sınırını ayarlamak için Aspose.Cells kullanan bir örnek kod sağlanmaktadır.

##  **Excel'de Aralık kenarlığını ayarlama**
Excel'de bir aralığın kenarlığını ayarlamak için şu adımları izleyebilirsiniz:
1. Kenarlığı uygulamak istediğiniz hücre aralığını seçin.
2. Şeridin "Giriş" sekmesinde "Yazı Tipi" grubunu bulun.
3. "Yazı Tipi" grubu içinde "Kenarlıklar" açılır düğmesine tıklayın.
<br>
<img src="border.png" />
4. Açılır menüdeki seçeneklerden uygulamak istediğiniz kenarlık türünü seçin. Önceden ayarlanmış kenarlık stilleri arasından seçim yapabilir veya kendi kenarlığınızı özelleştirebilirsiniz.
5. İstediğiniz kenarlık stilini seçtiğinizde, kenarlık seçilen hücre aralığına uygulanacaktır.

##  **Aspose.Cells'i kullanarak Menzil sınırını ayarlayın**
Bu örnek, aşağıdakilerin nasıl yapıldığını gösterir:

1. Bir çalışma kitabı oluşturun.
1. İlk çalışma sayfasındaki hücrelere veri ekleyin.
1.  Oluşturmak[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. Aralığın iç kenarlığını ayarlayın.
1. Aralığın dış kenarlığını ayarlayın.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-set-border.cs" >}}