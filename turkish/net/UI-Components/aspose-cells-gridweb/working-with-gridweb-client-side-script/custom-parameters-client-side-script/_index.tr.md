---
title: Başlangıç parametrelerini özelleştirme
type: docs
weight: 10
url: /tr/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
keywords: GridWeb,özelleştirme,özelleştirme parametreleri
description: Aspose.Cells.GridWeb istemci tarafı betiğinde başlangıç parametrelerini nasıl özelleştireceğiniz hakkında.
---

{{% alert color="primary" %}} 

Geliştiriciler, acwmain.js'de Aspose.Cells.GridWeb denetimi için farklı başlangıç parametre değerlerini ayarlayabilirler.  

{{% /alert %}} 

### **Parametreler**

|**Parametre**|**Açıklama**|
| :- | :- |
|needInitAlignmentAdjust| hücre içeriği için dikey hizalamayı başlatma sırasında yapılıp yapılmayacağı, büyük hücrelere sahip tabloda performansın kötü olacağı, dikey hizalamayı önemsemiyorsa kullanıcı false olarak ayarlayabilir, varsayılan değer true'dir |
|focusinside| hücre aralığında odaklanılacak mı, varsayılan değer true'dur |
|copy_with_style| stille kopyalanıp kopyalanmayacağı, varsayılan değer sadece hücre içeriğini kopyalamaktır |
|useESCAsLeave| esc tuşa basıldığında varsayılan davranış hücrede düzenleme işlemini iptal etme şeklinde çalışır, bu değeri true olarak ayarlarsak, sadece önceki değere dönmeden hücreden ayrılma kısa yolu olarak işlem yapar ve iç düzenleme yolunu hızlı düzenleme yolu olarak değiştirir, varsayılan değer false'tur |
|needValidateall| doğrulama yapılırken aktif sayfadaki tüm doğrulamaların geçerli olup olmayacağı,(aspx kontrol sayfasında ForceValidation="True" olarak ayarlanır). varsayılan değer false'tur |
|scrollToInvalidate| needValidateall true olarak ayarlandığında ilk geçersiz hücreyi ekrana getirip getirilmeyeceği. varsayılan değer true'dur |


Kod örneğinin çıktısı aşağıda gösterilmiştir, lütfen [örnek excel dosyasını](valign.xlsx) kontrol edin:

**needInitAlignmentAdjust=true** 

![todo:image_alt_text](align_true.png)

**needInitAlignmentAdjust=false** 

![todo:image_alt_text](align_false.png)

**focusinside=true** 
düzenleme iç yolu -- metin girildiğinde, eski hücre değeri hala saklı kalır   

![todo:image_alt_text](focus_inside_true.png)

**focusinside=false** 
hızlı düzenleme yolu -- metin girildiğinde, eski hücre değeri üzerine yazılır, eski hücre değerine dayalı düzenleme yapmak istiyorsanız, hücreye tıklayabilirsiniz

![todo:image_alt_text](focus_inside_false.png)



