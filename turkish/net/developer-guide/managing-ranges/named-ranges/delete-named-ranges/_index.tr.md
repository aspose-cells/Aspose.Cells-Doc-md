---
title: Adlandırılmış Aralıkları Sil
type: docs
weight: 90
url: /tr/net/Delete-named-ranges/
description: Aspose.Cells for .Net ile Excel veya OpenOffice dosyalarından tanımlanmış adları veya adlandırılmış aralıkları nasıl kaldıracağınızı öğrenebilirsiniz.
---

## **Giriş**
Eğer Excel dosyalarında çok fazla tanımlanmış isim veya adlandırılmış aralık varsa, tekrar atıfta bulunulmadığından bazılarını temizlememiz gerekebilir.

## **MS Excel'de Adlandırılmış Aralığı Kaldır**

Excel'den adlandırılmış bir aralığı kaldırmak için şu adımları izleyebilirsiniz:
1. Microsoft Excel'i açın ve adlandırılmış aralığı içeren çalışma kitabını açın.
2. Excel kurdelesindeki "Formüller" sekmesine gidin.
3. "Tanımlı İsimler" grubundaki "Ad Yöneticisi" düğmesini tıklayın. Bu, Ad Yöneticisi iletişim kutusunu açacaktır.
4. Ad Yöneticisi iletişim kutusunda, kaldırmak istediğiniz adlandırılmış aralığı seçin.
5. "Sil" düğmesine tıklayın. İstenildiğinde silme işlemini onaylayın.
6. Ad Yöneticisi iletişim kutusunu kapatmak için "Kapat" düğmesine tıklayın.
7. Değişiklikleri korumak için çalışma kitabını kaydedin.


## **Aspose.Cells for .Net kullanarak Adlandırılmış Aralığı Silme**
Aspose.Cells for .Net ile, listeden [metin](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove) veya [index](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat) ile adlandırılmış aralıkları veya tanımlı isimleri kaldırabilirsiniz.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

Not: Tanımlı isim formüller tarafından başvuruluyorsa, kaldırılamaz. Sadece tanımlı ismin formülünü kaldırabiliriz.

## **Bazı Adlandırılmış Aralıkları Kaldırma**
Bir tanımlı ismi kaldırdığımızda, dosyadaki tüm formüller tarafından kullanılıp kullanılmadığını kontrol etmeliyiz.
Adlandırılmış aralıkları kaldırmak için performansı iyileştirmek için birlikte bazılarını kaldırabiliriz.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

## **Yinelenen Tanımlı İsimleri Kaldırma**
Bazı Excel dosyaları, bazı tanımlı isimlerin yinelenmesi nedeniyle bozulur. Bu yinelenen isimleri kaldırarak dosyayı onarabiliriz.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



{{< app/cells/assistant language="csharp" >}}
