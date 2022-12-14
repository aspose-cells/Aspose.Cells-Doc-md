---
title: Başlatma parametrelerini özelleştirin
type: docs
weight: 10
url: /tr/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
description: Aspose.Cells.GridWeb istemci tarafı komut dosyasında başlatma parametrelerinin nasıl özelleştirileceği.
---
{{% alert color="primary" %}} 

 Geliştiriciler, acwmain.js'de Aspose.Cells.GridWeb denetimi için farklı davranış gerçekleştirmek üzere farklı başlatma parametresi değeri ayarlayabilir.

{{% /alert %}} 
 
### **parametreler**
 
|**Parametre**|**Tanım**|
|:- |:- |
|needInitAlignmentAdjust|Başlatma sırasında hücre içeriği için dikey hizalama yapılıp yapılmaması, hizalama işini yapmak için biraz zamana neden olur, çalışma sayfasında büyük hücreler varsa, performans zayıf olur, eğer kullanıcı dikey hizalamayı önemsemezse, o zaman ayarlayabilir. yanlış olun, varsayılan değer doğrudur|
|Odaklanma| hücre aralığı içinde odaklanıp odaklanmayacağınız, varsayılan değer doğrudur|
|kopyalamak_ile birlikte_stil|stille kopyalanıp kopyalanmayacağını, varsayılan değer yanlıştır, bu yalnızca hücre içeriğini kopyala anlamına gelir|
|kullanımESCAsAyrıl|esc tuşuna basıldığında varsayılan davranış, hücrede iptal düzenleme işlemi olarak çalışır, bu değeri true olarak ayarlarsak, bunu yalnızca önceki değere dönmeden hücreden çıkmak için kısa bir tuş olarak ele alacağız ve aynı zamanda iç düzenleme yolunu da değiştirecektir. hızlı düzenleme yolu için varsayılan değer yanlıştır|
|ihtiyaçValidateall|doğrulama yapılırken aktif sayfadaki tüm doğrulamaların doğrulanıp doğrulanmayacağını,(aspx kontrol sayfasında set ForceValidation="True") . varsayılan değer yanlıştır|
|scrollToInvalidate|needValidateall true olarak ayarlandığında ilk geçersiz kılma hücresinin kaydırılıp görüntülenmeyeceği. varsayılan değer doğrudur.|
 
 
 Kod örneğinin çıktısı aşağıda gösterilmiştir, Lütfen kontrol edin[örnek excel dosyası](valign.xlsx):

**needInitAlignmentAdjust=true** 

![yapılacaklar:resim_alternatif_Metin](align_true.png)

**needInitAlignmentAdjust=yanlış** 

![yapılacaklar:resim_alternatif_Metin](align_false.png)

**odak içi = doğru** 
 düzenleme yolu içinde - metin girildiğinde, eski hücre değeri yine de korunur

![yapılacaklar:resim_alternatif_Metin](focus_inside_true.png)

**odak içi=yanlış** 
hızlı düzenleme yolu -- metin girildiğinde eski hücre değerinin üzerine yazılacaktır, eski hücre değerine göre düzenlemek isterseniz hücreye tıklayabilirsiniz

![yapılacaklar:resim_alternatif_Metin](focus_inside_false.png)

 
 