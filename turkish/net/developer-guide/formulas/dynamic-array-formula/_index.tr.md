---
title: Dinamik Dizi Formüllerini Ayarlama
description: Microsoft Excel'de dinamik dizi formüllerini hesaplamak için Aspose.Cells kitaplığı nasıl kullanılır? Mevcut bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak Aspose.Cells'in sağladığı yöntemi kullanarak dinamik dizi formülünü hesaplayıp sonuca ulaşabiliriz. Son olarak değiştirdiğimiz Excel dosyasını diske kaydediyoruz.
keywords: Dynamic Array Formulas, Dynamic Array Formulas in Excel, Set dynamic array formulas, Calculation of dynamic array formulas, operate dynamic array formulas of Excel.
type: docs
weight: 70
url: /tr/net/calculation-of-dynamic-array-formulas/
---
##  **Excel Dizi Formülü Nedir?**
Excel'de dizi formülü, tek tek hücreler yerine veri dizileri üzerinde hesaplamalar yapmanızı sağlayan özel bir formül türüdür. Dizi formülleri karmaşık hesaplamalar gerçekleştirmek, verileri işlemek ve belirli sorunları verimli bir şekilde çözmek için kullanılabilir. Normal formüllerden farklı şekilde girilirler ve genellikle Ctrl + Shift + Enter tuşlarının kullanılmasını gerektirirler.

Excel'deki dizi formülleriyle ilgili bazı önemli noktalar şunlardır:
1. Sözdizimi:
<br>
Dizi formülleri normal formüller gibi yazılır ancak değer dizileri üzerinde işlemler içerir. Dizi formülleri olduklarını belirtmek için küme parantezleri { } içine alınırlar. Ancak bu kaşlı ayraçları kendiniz yazmazsınız; Formülü doğru girdiğinizde Excel bunları otomatik olarak ekler.
1. Dizi Formüllerinin Girilmesi:
<br>
Dizi formülü girmek için formülü formül çubuğuna yazarsınız. Bitirmek için Enter'a basmak yerine Ctrl + Shift + Enter tuşlarına basarsınız. Bu, Excel'e bunun bir dizi formülü olduğunu söyler. Doğru şekilde girildiğinde Excel, formülün bir dizi formülü olduğunu belirtmek için formül çubuğunda küme parantezleri içinde görüntüler.
1. Kullanım Durumları:
<br>
Dizi formülleri, birden çok hücre veya aralıkta aynı anda hesaplamalar gerçekleştirmek için kullanışlıdır. Gelişmiş matematiksel hesaplamalar, koşullu işlemler, verileri filtrelemek ve daha fazlası için kullanılabilirler.
1. Faydalar:
<br>
Dizi formülleri, karmaşık hesaplamaları tek bir formülde gerçekleştirmenize olanak tanır; bu da verimliliği artırabilir ve çalışma sayfalarınızı basitleştirebilir. Büyük veri kümelerini işleyebilir ve birden fazla ara adım gerektirecek hesaplamaları gerçekleştirebilirler.
1. Sınırlamalar:
<br>
Dizi formüllerinin anlaşılması ve sorun giderilmesi normal formüllere göre daha zor olabilir. Özellikle yoğun olarak veya büyük veri kümeleriyle kullanıldığında çalışma sayfası performansını yavaşlatabilirler.
1. Örnekler:
<br>
 Bir aralıktaki değerlerin toplanması:**{=TOPLA(A1:A5*B1:B5)}**
<br>
 Bir aralıktaki maksimum değeri bulma:**{=MAK(A1:A5+B1:B5)}**
<br>
<image src="1.png" width="70%" />
<br>

Dizi formüllerinin dikkatli kullanılması gerektiğini ve bunları çalışma sayfalarınıza uygulamadan önce nasıl çalıştıklarını anlamanın önemli olduğunu unutmayın. Excel'de veri analizi ve manipülasyonu için güçlü araçlar olabilirler.

##  **Excel Dinamik Dizi Formülü Nedir?**
Dinamik dizi formülleri, Excel 365 ve Excel 2021'de sunulan yeni bir özelliktir. Geleneksel dizi formüllerine kıyasla veri dizileriyle daha sorunsuz ve verimli çalışmanıza olanak tanır. Dinamik dizi formülleri, sonuçları otomatik olarak komşu hücrelere aktararak Ctrl + Shift + Enter ihtiyacını ortadan kaldırır ve verilerin daha kolay işlenmesine olanak tanır.

Excel'deki dinamik dizi formülleriyle ilgili önemli noktalar:
1. Otomatik Dökülme:
<br>
Dinamik dizi formülleri, çıktı verilerinin boyutuna göre sonuçları otomatik olarak bitişik hücrelere aktarır. Bu, formülü girmeden önce bir hücre aralığı seçmenize veya formülü onaylamak için Ctrl + Shift + Enter tuşlarını kullanmanıza gerek olmadığı anlamına gelir.
1. Tek-Cell Giriş:
<br>
Dinamik dizi formülleri tek bir hücreye girilir ve Excel, komşu hücreleri otomatik olarak sonuçlarla doldurur. Formülü yalnızca bir kez girmeniz gerektiğinden bu, formülleri yönetmeyi ve anlamayı kolaylaştırır.
1. Yeni İşlevler:
<br>
Dinamik dizi formülleri, dizileri yerel olarak işleyebilen *FİLTRE**, *SORT**, *BENZERSİZ**, *SIRALI**, *SIRALAMA** ve *RANDARRAY** gibi yeni işlevler sunar. Bu işlevler, karmaşık hesaplamaları basitleştirerek birden fazla değer döndürebilir veya dizileri doğrudan işleyebilir.
1. Esnek Menzil Kullanımı:
<br>
Dinamik dizi formülleri, giriş verilerinin boyutuna veya gerçekleştirilen hesaplamaya bağlı olarak dağılmış aralığın boyutunu dinamik olarak ayarlar. Bu esneklik, çalışma sayfası alanının daha verimli kullanılmasına olanak tanır ve formül oluşturmayı basitleştirir.
1. Geliştirilmiş Performans:
<br>
Dinamik dizi formülleri, özellikle büyük veri kümeleriyle veya karmaşık hesaplamalarla çalışırken, geleneksel dizi formüllerine kıyasla performansı artırabilir.
1. Uyumluluk:
<br>
Dinamik dizi formülleri Excel 365 ve Excel 2021'de mevcuttur. Excel'in eski sürümlerinde desteklenmeyebilirler.
1. Dinamik dizi formüllerine örnekler:
<br>
*FILTER**: Belirtilen kriterleri karşılayan bir değerler dizisi döndürür.
<br>
*SORT**: Bir aralık veya dizideki değerleri sıralar.
<br>
*BENZERSİZ**: Bir listeden veya aralıktan benzersiz değerler döndürür.
<br>
*SIRA**: Bir sayı veya tarih dizisi oluşturur.
<br>
*RANDARRAY**: Rastgele sayılardan oluşan bir dizi oluşturur.
<br>
<image src="2.png" width="70%" />
<br>

Dinamik dizi formülleri, Excel'de veri işleme ve analiz için güçlü yetenekler sunarak veri dizileriyle çalışmayı ve karmaşık hesaplamaları verimli bir şekilde gerçekleştirmeyi kolaylaştırır.

##  **Excel'deki Dizi Formülleri ile Dinamik Dizi Formüllerinin farkı nedir?**
Excel'de hem dizi formülleri hem de dinamik dizi formülleri aynı anda birden fazla değer üzerinde hesaplama yapmak için kullanılır, ancak işlevsellik ve uygulanma şekli açısından bazı farklılıklara sahiptirler.

###  **Dizi Formüllerinin Özellikleri**
1. Dizi formülleri, Excel'deki veri dizileri üzerinde hesaplamalar yapabilen geleneksel formüllerdir.
1. Excel'e bunun bir dizi formülü olduğunu söyleyen formülü yazdıktan sonra Ctrl + Shift + Enter tuşlarına basılarak girilirler.
1. Dizi formüllerinin, sonuçları bitişik hücrelere yayma yetenekleri açısından sınırlamaları vardır. Genellikle tek bir sonuç döndürürler, ancak bu sonuç bir hücre dizisi olabilir.
1. Uzun zamandır ortalıktalar ve Excel'in tüm sürümlerinde destekleniyorlar.

###  **Dinamik Dizi Formülleri Özellikleri**
1. Dinamik dizi formülleri, Excel 365 (Office 365 aboneliği) ve Excel 2021'de sunulan yeni bir özelliktir.
1. Girdi verilerinin boyutuna veya formülün hesaplamasına bağlı olarak sonuçları otomatik olarak bitişik hücrelere aktarırlar.
1. Dinamik dizi formülleri Ctrl + Shift + Enter tuşlarına basmayı gerektirmez; formülü tek bir hücreye yazmanız yeterlidir; Excel otomatik olarak bitişik hücreleri sonuçlarla doldurur.
1. Bu formüller, bir dizi formülüne veya Ctrl + Shift + Enter'a ihtiyaç duymadan doğrudan birden çok sonucu (bir hücre aralığı) döndürme yeteneğine sahiptir.
1. Dizileri yerel olarak işleyebilen ve sonuçları dinamik bir dizi biçiminde döndürebilen *FILTER**, *SORT**, *UNIQUE** vb. gibi yeni işlevlere sahiptirler.
Özetle, dinamik dizi formülleri, Excel'deki dizilerle çalışmanın daha modern ve kullanışlı bir yoludur; sonuçların otomatik olarak dağıtılmasını sağlar ve geleneksel dizi formüllerine kıyasla dizilerle çalışma sürecini basitleştirir. Ancak bunlar yalnızca Excel'in dinamik dizileri destekleyen daha yeni sürümlerinde mevcuttur.

##  **Excel'de Dinamik Dizi Formülleri Nasıl Ayarlanır ve Hesaplanır**
 Excel'de dinamik dizi formüllerinin ayarlanması, veri dizileriyle çalışacak ve sonuçların otomatik olarak komşu hücrelere yayılmasına izin verecek şekilde tasarlanmış belirli işlevlerin kullanılmasını içerir.

Dinamik dizi formüllerini ayarlamaya yönelik adım adım kılavuz aşağıda verilmiştir:
1. Cell'i seçin:
<br>
Dinamik dizi formülü sonuçlarının görünmesini istediğiniz hücreyi seçin. Dinamik dizi formülleri, sonuçları bitişik hücrelere aktarır; bu nedenle, dağıtılan çıktı için yeterli alan olduğundan emin olun.
1. Formülü girin:
<br>
 Dinamik dizi formülünü seçilen hücrenin formül çubuğuna yazın. Excel 365 ve Excel 2021'de bulunan *FİLTRE**, *SIRALAMA**, *BENZERSİZ**, *SIRALI**, *SIRALAMA** veya *RANDARRAY** gibi dinamik dizi işlevlerinden birini kullanın.
<br>
Örneğin, belirli ölçütlere göre bir veri listesini filtrelemek için FİLTRE işlevini kullanabilirsiniz: *=FİLTRE(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.
<br>
<image src="3.png" width="70%" />
<br>
1. Enter tuşuna basın:
<br>
Formülü yazdıktan sonra klavyenizdeki Enter tuşuna basmanız yeterlidir. Geleneksel dizi formüllerinin aksine Ctrl + Shift + Enter tuşlarına basmanız gerekmez.
1. Dökülen Aralığı Gözlemleyin:
<br>
Excel, formülün sonuçlarını otomatik olarak komşu hücrelere aktarır. Dağıtılan aralık, çıktı verilerinin boyutuna veya formül tarafından gerçekleştirilen hesaplamaya göre dinamik olarak ayarlanır. Excel, dökülen veriyi içerdiğini belirtmek için dökülen aralığı bir kenarlık ve çapraz ok simgesiyle vurgular.
1. Spilled Range ile etkileşime gir:
<br>
Taşınan aralıkla tıpkı Excel'deki diğer hücre aralıkları gibi etkileşimde bulunabilirsiniz. Dağıtılan aralığı diğer formüllerde kullanın, üzerinde hesaplamalar yapın, biçimlendirin veya grafik veya tablolarda ona referans verin.
1. Formülü güncelleyin:
<br>
Dinamik dizi formülünü değiştirmeniz gerekiyorsa formülü girildiği orijinal hücrede düzenlemeniz yeterlidir.
Düzenlemeden sonra değişiklikleri onaylamak için tekrar Enter tuşuna basın. Excel gerekirse taşan aralığı otomatik olarak güncelleyecektir.
1. Dökülen Menzilin Temizlenmesi:
<br>
Dökülen verileri temizlemek istiyorsanız formülü orijinal hücreden silebilirsiniz. Excel, dökülen aralığı da temizleyecektir. Alternatif olarak, dökülen aralığı seçip Sil tuşuna basarak doğrudan silebilirsiniz.
<br>

Bu adımları izleyerek, veri dizilerini verimli bir şekilde analiz etmek ve yönetmek için Excel'de dinamik dizi formülleri ayarlayabilir, böylece veri analizi ve raporlama görevlerinin daha kolay yapılmasını sağlayabilirsiniz.

##  **Aspose.Cells Kullanılarak Dinamik Dizi Formülleri Nasıl Ayarlanır ve Yenilenir**
 Lütfen aşağıdaki örnek koda bakın.[örnek Excel dosyası](dynamicArrayFormula.xlsx) bazı sahte veriler içeriyor. Dosyayı yükledikten sonra çağrı yapın.[Cell.SetDynamicArrayFormula](https://reference.aspose.com/cells/net/aspose.cells/cell/setdynamicarrayformula/#setdynamicarrayformula) dinamik dizi formülünü ayarlama işlevi ve[Workbook.RefreshDynamicArrayFormulas](https://reference.aspose.com/cells/net/aspose.cells/workbook/refreshdynamicarrayformulas/#refreshdynamicarrayformulas) Formül hesaplamasını çağırmadan önce dinamik dizi formüllerini yenileme ve son olarak çalışma kitabını kaydetme işlevi[Excel dosyasının çıktısı](out.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-dynamic-array-formulas.cs" >}}

Çıkış anlık görüntüsü:
<br>
<image src="4.png" width="70%" />