---
title: Yalnızca güncellenen hücreler yerine tüm çalışma sayfasını doğrulayın
type: docs
weight: 80
url: /tr/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---
## **Olası Kullanım Senaryoları**
GridWeb varsayılan olarak yalnızca güncellenen hücreleri doğrular ve tüm çalışma sayfasını doğrulamaz. Ancak, GridWeb sunucuya istek göndermeden önce tüm çalışma sayfasını istemci tarafında doğrulamak istiyorsanız acwmain.js içindeki needValidateall değişkenini true olarak ayarlamalısınız.
## **Yalnızca güncellenen hücreler yerine tüm çalışma sayfasını doğrulayın**
Aşağıdaki ekran görüntüsü, acwmain.js'deki needValidateall değişkenini görüntüler. Lütfen bunu doğru olarak ayarlayın ve şimdi GridWeb yalnızca güncellenmiş hücreleri değil tüm çalışma sayfanızı doğrulayacaktır.

![yapılacaklar:resim_alternatif_metin](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


