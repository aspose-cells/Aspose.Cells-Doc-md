---
title: Dinamik Dizi Formüllerini Ayarlama
description: Aspose.Cells kitaplığını kullanarak Microsoft Excel de dinamik dizi formüllerini hesaplama. Var olan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemi kullanarak dinamik dizi formülünü hesaplayabilir ve sonucu alabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydediyoruz.
keywords: Dinamik Dizi Formülleri, Excel de Dinamik Dizi Formülleri, dinamik dizi formlarını ayarlama, dinamik dizi formüllerinin hesaplanması, Excel in dinamik dizi formüllerini işletme.
type: docs
weight: 70
url: /tr/net/calculation-of-dynamic-array-formulas/
---
## **Excel Dizi Formülü Nedir**
Excel'de, bir dizi formülü, bireysel hücreler yerine veri dizileri üzerinde hesaplamalar yapmanıza olanak tanıyan özel bir formül türüdür. Dizi formülleri, karmaşık hesaplamalar yapmak, veri manipülasyonu yapmak ve belirli sorunları verimli bir şekilde çözmek için kullanılabilir. Bunlar normal formüllerden farklı bir şekilde girilir ve genellikle Ctrl + Shift + Enter kullanımını gerektirir.

İşte Excel'de dizi formülleri hakkında bazı temel noktalar:
1. Sözdizimi:
<br>
Dizi formları normal formüller gibi yazılmıştır, ancak değer dizileri üzerinde operasyonları içerir. Onlar { } ile çevriliyken { } onlar için dizi formülü olduğunu göstermek içindir. Ancak, bu süslü parantezleri kendiniz yazmazsınız; Excel, formülü doğru bir şekilde girdiğinizde onları otomatik olarak ekler.
1. Dizi Formüllerinin Girilmesi:
<br>
Bir dizi formülünü girmek için, formülü formül çubuğuna yazarsınız. Sonlandırmak için Enter'a basmak yerine, Ctrl + Shift + Enter'a basarsınız. Bu, Excel'e bunun bir dizi formülü olduğunu söyler. Doğru girildiğinde, Excel, bunun bir dizi formülü olduğunu belirtmek için formül çubuğunda süslü parantezler içinde formülü gösterir.
1. Kullanım Alanları:
<br>
Dizi formülleri, aynı anda birden fazla hücre veya aralık üzerinde hesaplamalar yapmak için kullanışlıdır. Bunlar, gelişmiş matematiksel hesaplamalar, koşullu işlemler, veri filtreleme ve daha fazlası için kullanılabilir.
1. Faydalar:
<br>
Dizi formülleri, çalışma sayfalarınızı geliştirebilecek ve işlemlerinizi basitleştirebilecek karmaşık hesaplamaları tek bir formülde yapmanıza olanak tanır. Büyük veri kümeleri ile başa çıkabilir ve birden fazla ara adım gerektiren hesaplamaları gerçekleştirebilirler.
1. Kısıtlamalar:
<br>
Dizi formülleri, normal formüllerden daha zor anlaşılır ve hata ayıklanması mümkün değil demektir. Özellikle yoğun bir şekilde veya büyük veri kümeleri ile kullanıldığında çalışma sayfası performansını yavaşlatabilir.
1. Örnekler:
<br>
Bir aralıktaki değerleri toplamak: **{=SUM(A1:A5*B1:B5)}**
<br>
Bir aralıktaki maksimum değeri bulmak: **{=MAX(A1:A5+B1:B5)}**
<br>
<image src="1.png" width="70%" />
<br>

Dizi formüllerinin dikkatlice kullanılması gerektiğini ve bunların çalışma sayfalarınıza uygulamadan önce nasıl çalıştığınızı anlamanın önemli olduğunu unutmayın. Excel'de veri analizi ve manipülasyonu için güçlü araçlar olabilirler.

## **Excel'de Dinamik Dizi Formülü Nedir**
Dinamik dizi formülleri, Excel 365 ve Excel 2021'de tanıtılan yeni bir özelliktir. Geleneksel dizi formülleriyle karşılaştırıldığında, dinamik dizi formülleri veri dizileriyle daha sorunsuz ve verimli bir şekilde çalışmanıza olanak tanır. Dinamik dizi formülleri otomatik olarak sonuçları komşu hücrelere yayarak Ctrl + Shift + Enter ihtiyacını ortadan kaldırır ve veri manipülasyonunu daha kolay hale getirir.

Excel'de dinamik dizi formüllerinin önemli noktaları:
1. Otomatik Dökülme:
<br>
Dinamik dizi formülleri sonuçları otomatik olarak çıktı verilerinin boyutuna göre yan taraftaki hücrelere döker. Bu, formülü girmeden önce hücre aralığını seçmenize veya formülü onaylamak için Ctrl + Shift + Enter kullanmanıza gerek olmadığı anlamına gelir.
1. Tek Hücre Girişi:
<br>
Dinamik dizi formülleri tek bir hücreye girilir ve Excel otomatik olarak sonuçları yakındaki hücrelere doldurur. Bu, formülleri yönetmeyi ve anlamayı kolaylaştırır, çünkü formülü sadece bir kez girmeniz yeterli olur.
1. Yeni Fonksiyonlar:
<br>
Dinamik dizi formülleri, **FİLTRE**, **SIRALA**, **BENZERSİZ**, **SIRA**, **SIRALIYLA** ve **RASSALDİZİ** gibi dizileri doğal olarak işleyebilen yeni işlevler sunar. Bu işlevler birden fazla değer döndürebilir veya dizileri doğrudan manipüle edebilir, karmaşık hesaplamaları basitleştirir.
1. Esnek Aralık İşleme:
<br>
Dinamik dizi formülleri, dökülen aralığın boyutunu girdi verilerinin boyutuna veya yapılan hesaplamanın boyutuna göre dinamik olarak ayarlar. Bu esneklik, çalışsayfa alanının daha verimli kullanılmasına ve formül oluşturmanın basitleştirilmesine olanak tanır.
1. İyileştirilmiş Performans:
<br>
Dinamik dizi formülleri, özellikle büyük veri kümeleri veya karmaşık hesaplamalarla çalışırken geleneksel dizi formüllerine göre performansı artırabilir.
1. Uyumluluk:
<br>
Dinamik dizi formülleri Excel 365 ve Excel 2021'de mevcuttur. Eski sürümlerde desteklenmeyebilir.
1. Dinamik dizi formüllerinin örnekleri:
<br>
**FİLTRE**: Belirli kriterleri karşılayan değerlerin bir dizisini döndürür.
<br>
**SIRALA**: Bir aralıktaki veya dizideki değerleri sıralar.
<br>
**BENZERSİZ**: Bir listeden veya aralıktan benzersiz değerleri döndürür.
<br>
**SIRA**: Sayıların veya tarihlerin bir dizisini oluşturur.
<br>
**RASSALDİZİ**: Rastgele sayıların bir dizisini oluşturur.
<br>
<image src="2.png" width="70%" />
<br>

Dinamik dizi formülleri, Excel'de veri manipülasyonu ve analizi için güçlü yetenekler sunarak veri dizileriyle çalışmayı ve karmaşık hesaplamaları verimli bir şekilde gerçekleştirmeyi kolaylaştırır.

## **Excel'de Dizi Formülleri ve Dinamik Dizi Formülleri arasındaki fark nedir**
Excel'de hem dizi formülleri hem de dinamik dizi formülleri aynı anda birden fazla değer üzerinde hesaplama yapmak için kullanılır, ancak işlevsellik ve uygulanma şekilleri açısından bazı farklılıklar gösterirler.

### **Dizi Formülleri Özellikleri**
1. Dizi formülleri, Excel'de veri dizileri üzerinde hesaplama yapabilen geleneksel formüllerdir.
1. Formülü yazdıktan sonra Ctrl + Shift + Enter tuşlarına basarak girilirler, bu da Excel'e bunun bir dizi formülü olduğunu söyler.
1. Dizi formüllerinin sonuçları yan taraftaki hücrelere dökme yetenekleri konusunda sınırlamaları vardır. Genellikle 1. tek bir sonuç döndürürler, ancak bu sonuç bir hücre dizisi olabilir.
1. Uzun bir süredir mevcuttur ve tüm Excel sürümlerinde desteklenmektedir.

### **Dinamik Dizi Formülleri Özellikleri**
1. Dinamik dizi formülleri, Excel 365 (Office 365 aboneliği) ve Excel 2021'de tanıtılan yeni bir özelliktir.
1. Girdi verilerinin boyutuna veya formülün hesaplamasına göre sonuçları otomatik olarak yan taraftaki hücrelere döker.
1. Dinamik dizi formülleri Ctrl + Shift + Enter'a basılmasını gerektirmez; formülü sadece bir hücreye yazarsınız ve Excel otomatik olarak sonuçları yan taraftaki hücrelere doldurur.
1. Bu formüller, dizi formülü veya Ctrl + Shift + Enter gerekmeden doğrudan birden fazla sonucu (hücre aralığı) döndürme yeteneğine sahiptir.
1. **FİLTRE**, **SIRALA**, **BENZERSİZ** gibi yeni işlevlere sahiptirler, bu işlevler dizilerle doğal olarak çalışabilir ve sonuçları dinamik dizi biçiminde döndürebilir.
Özetle, dinamik dizi formülleri, Excel'de dizilerle çalışmanın daha modern ve uygun bir yolunu sağlayarak sonuçların otomatik olarak dökülmesini ve geleneksel dizi formüllerine göre dizilerle çalışma sürecini basitleştirir. Bununla birlikte, sadece dinamik dizileri destekleyen yeni Excel sürümlerinde kullanılabilirler.

## **Excel'de Dinamik Dizi Formüllerini Nasıl Ayarlayıp Hesaplarız**
Excel'de dinamik dizi formüllerini kurmak, veri dizileri ile çalışacak şekilde tasarlanmış belirli fonksiyonları kullanmayı ve sonuçların otomatik olarak bitişik hücrelere dökülmesine izin vermeyi içerir. 

İşte dinamik dizi formüllerini kurmak için adım adım kılavuz:
1. Hücreyi Seçin:
<br>
Dinamik dizi formülü sonuçlarının görüneceği hücreyi seçin. Dinamik dizi formülleri sonuçları bitişik hücrelere döker, bu nedenle dökülen çıktı için yeterli alanın olduğundan emin olun.
1. Formülü Girin:
<br>
Seçilen hücrenin formül çubuğuna dinamik dizi formülünü girin. Excel 365 ve Excel 2021'de mevcut olan **FİLTRE**, **SIRALA**, **BENZERSİZ**, **SIRALAMA**, **SIRALAARG** ve **RASGELEDİZİ** gibi dinamik dizi işlevlerinden birini kullanın. 
<br>
Örneğin, belirli kriterlere göre veri listesini filtrelemek için FİLTRE işlevini kullanabilirsiniz: **=FİLTRE(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.
<br>
<image src="3.png" width="70%" />
<br>
1. Enter tuşuna basın:
<br>
Formülü yazdıktan sonra, klavyenizde sadece Enter tuşuna basın. Geleneksel dizi formülleri gibi Ctrl + Shift + Enter tuşlarına basmanıza gerek yoktur.
1. Dökülen Aralığı Gözlemleyin:
<br>
Excel otomatik olarak formülün sonuçlarını bitişik hücrelere döker. Dökülen aralık, çıktı verilerinin boyutuna veya formül tarafından gerçekleştirilen hesaplamaya bağlı olarak dinamik olarak ayarlanır. Excel, dökülen aralığı bir sınır ve köşegen ok simgesi ile vurgular, bu simge dökülen verileri içerdiğini gösterir.
1. Dökülen Aralıkla Etkileşime Geçin:
<br>
Excel'de herhangi bir hücre aralığıyla etkileşimde bulunabileceğiniz gibi dökülen aralıkla da etkileşimde bulunabilirsiniz. Dökülen aralığı diğer formüllerde kullanabilir, üzerinde hesaplamalar yapabilir, biçimlendirebilir veya grafiklerde veya tablolarda referans olarak kullanabilirsiniz.
1. Formülü Güncelleme:
<br>
Dinamik dizi formülünü değiştirmeniz gerekiyorsa, sadece orijinal hücrede formülü düzenleyin.
Düzenleme yaptıktan sonra, değişiklikleri onaylamak için tekrar Enter tuşuna basın. Excel gerekirse dökülen aralığı otomatik olarak günceller.
1. Dökülen Aralığı Temizleme:
<br>
Dökülen verileri temizlemek istiyorsanız, orijinal hücreden formülü silebilirsiniz. Excel ayrıca dökülen aralığı da temizler. Alternatif olarak, dökülen aralığı doğrudan seçerek ve Delete tuşuna basarak silebilirsiniz.
<br>

Bu adımları takip ederek, Excel'de dinamik dizi formüllerini kurarak veri dizilerini etkili bir şekilde analiz etmenize ve manipüle etmenize olanak tanır, bu da daha kolay veri analizi ve raporlama görevlerine olanak sağlar.

## **Aspose.Cells Kullanarak Dinamik Dizi Formüllerini Nasıl Ayarlar ve Günceller**
Lütfen [örnek Excel dosyasını](dynamicArrayFormula.xlsx) yükleyen aşağıdaki örnek kodları inceleyin. Dosyayı yükledikten sonra, formül hesaplamadan önce dinamik dizi formülü ayarlamak için [Cell.SetDynamicArrayFormula](https://reference.aspose.com/cells/net/aspose.cells/cell/setdynamicarrayformula/#setdynamicarrayformula) işlevini ve dinamik dizi formüllerini güncellemek için [Workbook.RefreshDynamicArrayFormulas](https://reference.aspose.com/cells/net/aspose.cells/workbook/refreshdynamicarrayformulas/#refreshdynamicarrayformulas) işlevini çağırın ve son olarak çalışma kitabını [çıktı Excel dosyası](out.xlsx) olarak kaydedin. 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-dynamic-array-formulas.cs" >}}

Çıktı anlık görüntüsü:
<br>
<image src="4.png" width="70%" />
{{< app/cells/assistant language="csharp" >}}
