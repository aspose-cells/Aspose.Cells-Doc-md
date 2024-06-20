---
title: Yalnızca güncellenen hücrelerin değil, tüm çalışma sayfasını doğrulamak
type: docs
weight: 80
url: /tr/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---

## **Olası Kullanım Senaryoları**
Varsayılan olarak, GridWeb yalnızca güncellenen hücreleri doğrular ve tüm çalışma sayfasını doğrulamaz. Bununla birlikte, sunucuya istek göndermeden önce GridWeb'in istemci tarafında tüm çalışma sayfasını doğrulamak istiyorsanız, acwmain.js içinde needValidateall değişkenini true olarak ayarlamanız gerekmektedir.
## **Yalnızca güncellenen hücrelerin değil, tüm çalışma sayfasını doğrulamak**
Aşağıdaki ekran görüntüsü, acwmain.js içindeki needValidateall değişkenini göstermektedir. Lütfen true olarak ayarlayın ve artık GridWeb tüm çalışma sayfanızı, sadece güncellenen hücreler değil, doğrulayacaktır.

![todo:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


