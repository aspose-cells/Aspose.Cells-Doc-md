---  
title: Dinamik Dizi Formülleri Ayarlama Node.js ve C++ kullanarak  
linktitle: Dinamik Dizi Formüllerini Ayarlama  
description: Aspose.Cells kütüphanesini kullanarak Excel de dinamik dizi formüllerini Node.js ve C++ ile nasıl hesaplayacağınızı öğrenin. Dosyaları kolayca yükleyin, hesaplayın ve kaydedin.  
keywords: Dinamik Dizi Formülleri, Excel de Dinamik Dizi Formülleri, Node.js ve C++ ile Dinamik Dizi Formülleri Ayarlama, Dinamik Dizi Formüllerinin Hesaplanması Node.js ve C++ ile, Excel in dinamik dizi formülleri üzerinde çalışma.  
type: docs  
weight: 70  
url: /tr/nodejs-cpp/calculation-of-dynamic-array-formulas/  
---  
## **Excel Dizi Formülü Nedir**  
Excel'de, bir dizi formülü, bireysel hücreler yerine veri dizileri üzerinde hesaplamalar yapmanıza olanak tanıyan özel bir formül türüdür. Dizi formülleri, karmaşık hesaplamalar yapmak, veri manipülasyonu yapmak ve belirli sorunları verimli bir şekilde çözmek için kullanılabilir. Bunlar normal formüllerden farklı bir şekilde girilir ve genellikle Ctrl + Shift + Enter kullanımını gerektirir.

İşte Excel'de dizi formülleri hakkında bazı temel noktalar:  
1. Sözdizimi:  
<br>  
Dizi formları normal formüller gibi yazılmıştır, ancak değer dizileri üzerinde operasyonları içerir. Onlar { } ile çevriliyken { } onlar için dizi formülü olduğunu göstermek içindir. Ancak, bu süslü parantezleri kendiniz yazmazsınız; Excel, formülü doğru bir şekilde girdiğinizde onları otomatik olarak ekler.  
2. Dizi Formüllerini Girme:  
<br>  
Dizi formülü girerken, formülü formül çubuğuna yazarsınız. Bitirmek için Enter yerine Ctrl + Shift + Enter tuşlarına basarsınız. Bu, Excel'e bunun bir dizi formülü olduğunu söyler. Doğru girildiğinde, Excel formülü süslü parantezler içinde formül çubuğunda gösterir ve bunun bir dizi formülü olduğunu gösterir.  
3. Kullanım Durumları:  
<br>  
Dizi formülleri, aynı anda birden fazla hücre veya aralık üzerinde hesaplamalar yapmak için kullanışlıdır. Bunlar, gelişmiş matematiksel hesaplamalar, koşullu işlemler, veri filtreleme ve daha fazlası için kullanılabilir.  
4. Avantajlar:  
<br>  
Dizi formülleri, çalışma sayfalarınızı geliştirebilecek ve işlemlerinizi basitleştirebilecek karmaşık hesaplamaları tek bir formülde yapmanıza olanak tanır. Büyük veri kümeleri ile başa çıkabilir ve birden fazla ara adım gerektiren hesaplamaları gerçekleştirebilirler.  
5. Kısıtlamalar:  
<br>  
Dizi formülleri, normal formüllerden daha zor anlaşılır ve hata ayıklanması mümkün değil demektir. Özellikle yoğun bir şekilde veya büyük veri kümeleri ile kullanıldığında çalışma sayfası performansını yavaşlatabilir.  
6. Örnekler:  
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
2. Tek Hücre Girişi:  
<br>  
Dinamik dizi formülleri tek bir hücreye girilir ve Excel otomatik olarak sonuçları yakındaki hücrelere doldurur. Bu, formülleri yönetmeyi ve anlamayı kolaylaştırır, çünkü formülü sadece bir kez girmeniz yeterli olur.  
3. Yeni Fonksiyonlar:  
<br>  
Dinamik dizi formülleri, **FİLTRE**, **SIRALA**, **BENZERSİZ**, **SIRA**, **SIRALIYLA** ve **RASSALDİZİ** gibi dizileri doğal olarak işleyebilen yeni işlevler sunar. Bu işlevler birden fazla değer döndürebilir veya dizileri doğrudan manipüle edebilir, karmaşık hesaplamaları basitleştirir.  
4. Esnek Aralık İşleme:  
<br>  
Dinamik dizi formülleri, dökülen aralığın boyutunu girdi verilerinin boyutuna veya yapılan hesaplamanın boyutuna göre dinamik olarak ayarlar. Bu esneklik, çalışsayfa alanının daha verimli kullanılmasına ve formül oluşturmanın basitleştirilmesine olanak tanır.  
5. Geliştirilmiş Performans:  
<br>  
Dinamik dizi formülleri, özellikle büyük veri kümeleri veya karmaşık hesaplamalarla çalışırken geleneksel dizi formüllerine göre performansı artırabilir.  
6. Uyumluluk:  
<br>  
Dinamik dizi formülleri Excel 365 ve Excel 2021'de mevcuttur. Eski sürümlerde desteklenmeyebilir.  
7. Dinamik Dizi Formülleri Örnekleri:  
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
2. Formül yazdıktan sonra Ctrl + Shift + Enter tuşlarına basılarak girilir; bu, Excel'e bunun bir dizi formülü olduğunu söyler.  
3. Dizi formüllerinin sonuçları bitişik hücrelere sızdırma konusunda sınırlamaları vardır. Genellikle tek bir sonuç döndürürler, ancak bu sonuç bir hücre dizisi olabilir.  
4. Uzun süredir varlar ve tüm Excel sürümlerinde desteklenmektedirler.

### **Dinamik Dizi Formülleri Özellikleri**  
1. Dinamik dizi formülleri, Excel 365 (Office 365 aboneliği) ve Excel 2021'de tanıtılan yeni bir özelliktir.  
2. Giriş Verisine veya formülün hesaplamasına bağlı olarak sonuçlar otomatik olarak bitişik hücrelere yayılır.  
3. Dinamik dizi formülleri Ctrl + Shift + Enter tuşlarına basmayı gerektirmez; sadece formülü bir hücreye yazarsınız ve Excel otomatik olarak sonuçlarla bitişik hücreleri doldurur.  
4. Bu formüller, bir dizi formülü veya Ctrl + Shift + Enter gerekmeden doğrudan çoklu sonuçlar (bir hücre aralığı) döndürebilme yeteneğine sahiptir.  
5. **FILTER**, **SORT**, **UNIQUE** gibi yeni fonksiyonlar sağlar ve bunlar dizileri yerel olarak işleyip dinamik dizi formatında sonuçlar döndürebilir.  
Özetle, dinamik dizi formülleri, Excel'de dizilerle çalışmanın daha modern ve uygun bir yolunu sağlayarak sonuçların otomatik olarak dökülmesini ve geleneksel dizi formüllerine göre dizilerle çalışma sürecini basitleştirir. Bununla birlikte, sadece dinamik dizileri destekleyen yeni Excel sürümlerinde kullanılabilirler.

## **Excel'de Dinamik Dizi Formüllerini Nasıl Ayarlayıp Hesaplarız**  
Excel'de dinamik dizi formüllerini kurmak, veri dizileri ile çalışacak şekilde tasarlanmış belirli fonksiyonları kullanmayı ve sonuçların otomatik olarak bitişik hücrelere dökülmesine izin vermeyi içerir. 

İşte dinamik dizi formüllerini kurmak için adım adım kılavuz:  
1. Hücreyi Seçin:  
<br>  
Dinamik dizi formülü sonuçlarının görüneceği hücreyi seçin. Dinamik dizi formülleri sonuçları bitişik hücrelere döker, bu nedenle dökülen çıktı için yeterli alanın olduğundan emin olun.  
2. Formülü Girin:  
<br>  
Seçilen hücrenin formül çubuğuna dinamik dizi formülünü girin. Excel 365 ve Excel 2021'de mevcut olan **FİLTRE**, **SIRALA**, **BENZERSİZ**, **SIRALAMA**, **SIRALAARG** ve **RASGELEDİZİ** gibi dinamik dizi işlevlerinden birini kullanın.  
<br>  
Örneğin, belirli kriterlere göre veri listesini filtrelemek için FİLTRE işlevini kullanabilirsiniz: **=FİLTRE(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.  
<br>  
<image src="3.png" width="70%" />  
<br>  
3. Enter Tuşuna Basın:  
<br>  
Formülü yazdıktan sonra, klavyenizde sadece Enter tuşuna basın. Geleneksel dizi formülleri gibi Ctrl + Shift + Enter tuşlarına basmanıza gerek yoktur.  
4. Sızdırılan Aralığı Gözlemleyin:  
<br>  
Excel otomatik olarak formülün sonuçlarını bitişik hücrelere döker. Dökülen aralık, çıktı verilerinin boyutuna veya formül tarafından gerçekleştirilen hesaplamaya bağlı olarak dinamik olarak ayarlanır. Excel, dökülen aralığı bir sınır ve köşegen ok simgesi ile vurgular, bu simge dökülen verileri içerdiğini gösterir.  
5. Sızdırılan Aralık ile Etkileşime Geçin:  
<br>  
Excel'de herhangi bir hücre aralığıyla etkileşimde bulunabileceğiniz gibi dökülen aralıkla da etkileşimde bulunabilirsiniz. Dökülen aralığı diğer formüllerde kullanabilir, üzerinde hesaplamalar yapabilir, biçimlendirebilir veya grafiklerde veya tablolarda referans olarak kullanabilirsiniz.  
6. Formülü Güncelleyin:  
<br>  
Dinamik dizi formülünü modifiye etmeniz gerekiyorsa, formülü onu yazdığınız ilk hücrede düzenleyin. Düzenledikten sonra, değişiklikleri onaylamak için tekrar Enter tuşuna basın. Excel, gerekirse sızdırılan aralığı otomatik olarak güncelleyecektir.  
7. Sızdırılan Aralığı Temizleme:  
<br>  
Dökülen verileri temizlemek istiyorsanız, orijinal hücreden formülü silebilirsiniz. Excel ayrıca dökülen aralığı da temizler. Alternatif olarak, dökülen aralığı doğrudan seçerek ve Delete tuşuna basarak silebilirsiniz.  
<br>  

Bu adımları takip ederek, Excel'de dinamik dizi formüllerini kurarak veri dizilerini etkili bir şekilde analiz etmenize ve manipüle etmenize olanak tanır, bu da daha kolay veri analizi ve raporlama görevlerine olanak sağlar.

## **Aspose.Cells Kullanarak Dinamik Dizi Formüllerini Nasıl Ayarlar ve Günceller**  
Lütfen aşağıdaki örnek kodu inceleyin. Bu kod, bazı sahte veriler içeren [örnek Excel dosyasını](dynamicArrayFormula.xlsx) yükler. Dosya yüklendikten sonra, dinamik dizi formülü ayarlamak için [Cell.setDynamicArrayFormula(string, FormulaParseOptions, boolean)] fonksiyonunu çağırın ve formül hesaplamasından önce [Workbook.refreshDynamicArrayFormulas(boolean)] fonksiyonunu kullanarak dinamik dizi formüllerini yenileyin; ardından, çalışma kitabını [çıktı Excel dosyası](out.xlsx) olarak kaydedin.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "dynamicArrayFormula.xlsx");

// Instantiate an Workbook object
const wb = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const ws = wb.getWorksheets().get(0);

// Getting the F16 
const f16 = ws.getCells().get("F16");

// Set dynamic array formula
f16.setDynamicArrayFormula("=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=25),\"\")", new AsposeCells.FormulaParseOptions(), false);

// Refresh the dynamic array formulas
wb.refreshDynamicArrayFormulas(true);

wb.calculateFormula();
wb.save("out.xlsx");
```

Çıktı anlık görüntüsü:  
<br>  
<image src="4.png" width="70%" />  

