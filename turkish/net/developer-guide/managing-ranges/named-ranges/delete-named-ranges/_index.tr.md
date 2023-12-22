---
title: Adlandırılmış Aralıkları Sil
type: docs
weight: 90
url: /tr/net/Delete-named-ranges/
description: Aspose.Cells for .Net ile Excel veya OpenOffice dosyalarından tanımlanmış adların veya adlandırılmış aralıkların nasıl kaldırılacağını öğrenebilirsiniz.
---
##  **giriiş**
Excel dosyalarında çok fazla tanımlı ad veya adlandırılmış aralık varsa, bir daha yönlendirilmemeleri için bazılarını temizlememiz gerekir.

##  **MS Excel'de Adlandırılmış Aralığı Kaldır**

Adlandırılmış bir aralığı Excel'den kaldırmak için şu adımları uygulayabilirsiniz:
1. Microsoft Excel'i açın ve adlandırılmış aralığı içeren çalışma kitabını açın.
2. Excel şeridindeki "Formüller" sekmesine gidin.
3. "Tanımlı Adlar" grubundaki "Ad Yöneticisi" butonuna tıklayın. Bu, Ad Yöneticisi iletişim kutusunu açacaktır.
4. Ad Yöneticisi iletişim kutusunda kaldırmak istediğiniz adlandırılmış aralığı seçin.
5. "Sil" butonuna tıklayın. İstendiğinde silme işlemini onaylayın.
6. Ad Yöneticisi iletişim kutusunu kapatmak için "Kapat" düğmesine tıklayın.
7. Değişiklikleri korumak için çalışma kitabını kaydedin.


##  ** .Net için Aspose.Cells'i kullanarak Adlandırılmış Aralığı Siler**
 .Net için Aspose.Cells ile adlandırılmış aralıkları veya tanımlanmış adları şu şekilde kaldırabilirsiniz:[metin](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove) veya[indeks](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat) listede.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

Not: Tanımlanan ad formüllerle anılıyorsa kaldırılamaz. Sadece tanımlanan ismin formülünü kaldırabiliyoruz.

##  **Bazı Adlandırılmış Aralıkları Kaldırır**
Tanımlı bir ismi kaldırdığımızda dosyadaki tüm formüller tarafından referans alınıp alınmadığını kontrol etmemiz gerekir.
Adlandırılmış aralıkların kaldırılması performansını artırmak için bazılarını birlikte kaldırabiliriz.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

##  **Yinelenen Tanımlı Adları Kaldır**
Bazı tanımlanmış adlar yinelenen olduğundan bazı Excel dosyaları bozuk. Böylece dosyayı onarmak için bu yinelenen adları kaldırabiliriz.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



