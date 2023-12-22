---
title: Yalnızca güncellenen hücreleri doğrulamak yerine tüm çalışma sayfasını doğrulayın
type: docs
weight: 80
url: /tr/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---
##  **Olası Kullanım Senaryoları**
GridWeb varsayılan olarak yalnızca güncellenen hücreleri doğrular ve çalışma sayfasının tamamını doğrulamaz. Ancak GridWeb isteği sunucuya göndermeden önce çalışma sayfasının tamamını istemci tarafında doğrulamak istiyorsanız acwmain.js içindeki needValidateall değişkenini true olarak ayarlamanız gerekir.
##  **Yalnızca güncellenen hücreleri doğrulamak yerine tüm çalışma sayfasını doğrulayın**
Aşağıdaki ekran görüntüsü acwmain.js'deki needValidateall değişkenini göstermektedir. Lütfen bunu true olarak ayarlayın; GridWeb artık yalnızca güncellenen hücreleri değil tüm çalışma sayfanızı doğrulayacaktır.

![yapılacak şey:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


