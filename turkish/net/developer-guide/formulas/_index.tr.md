---
title: Excel dosyalarının formüllerini yönetme
linktitle: Formüller
type: docs
weight: 122
url: /tr/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells excel dosyalarının formüllerini kolayca alabilir, ayarlayabilir ve hesaplayabilir.
description: NET API'leri için Aspose.Cells aracılığıyla Excel dosyalarının formüllerini nasıl yöneteceğinizi öğrenin.
keywords: How to calculate formulas in C#, Formulas and Functions using C#, C# Manage Built-in Functions, How to Use Add-in Functions with C#, How to Use Array Formula via C#, How to Use R1C1 Formula in C#.
---
##  **giriiş**

Microsoft Excel'in ilgi çekici özelliklerinden biri de verileri formüller ve işlevlerle işleyebilmesidir. Microsoft Excel, kullanıcıların karmaşık hesaplamaları hızla gerçekleştirmesine yardımcı olan bir dizi yerleşik işlev ve formül sağlar. Aspose.Cells ayrıca geliştiricilerin değerleri kolayca hesaplamasına yardımcı olan çok sayıda yerleşik işlev ve formül sağlar. Aspose.Cells ayrıca eklenti işlevlerini de destekler. Ayrıca Aspose.Cells, Aspose.Cells'deki diziyi ve R1C1 formüllerini destekler.

##  **Formüller ve İşlevler Nasıl Kullanılır?**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. Cells koleksiyonundaki her öğe, bir nesneyi temsil eder.[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf.

 Programın sunduğu özellik ve yöntemlerle formüllerin hücrelere uygulanması mümkündür.[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf, aşağıda daha ayrıntılı olarak tartışılmıştır.

- Yerleşik işlevleri kullanma.
- Eklenti işlevlerini kullanma.
- Dizi formülleriyle çalışma.
- R1C1 formülü oluşturma.

##  **Yerleşik İşlevler Nasıl Kullanılır**

Yerleşik işlevler veya formüller, geliştiricilerin çabalarını ve zamanını azaltmak için hazır işlevler olarak sağlanır. Görmek[yerleşik işlevlerin listesi](/cells/tr/net/supported-formula-functions/) Aspose.Cells tarafından desteklenmektedir. İşlevler alfabetik sıraya göre listelenmiştir. Gelecekte daha fazla fonksiyon desteklenecektir.

 Aspose.Cells, Microsoft Excel tarafından sunulan formüllerin veya işlevlerin çoğunu destekler. Geliştiriciler bu formülleri API veya[tasarımcı elektronik tablosu](/cells/tr/net/what-is-a-designer-spreadsheet/). Aspose.Cells çok sayıda matematik, dize, Boolean, tarih/saat, istatistik, veritabanı, arama ve referans formüllerini destekler.

 Kullan[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf'[**Formül**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) Hücreye formül ekleme özelliği. *Karmaşık formüller** örneğin

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, Aspose.Cells'de de desteklenir. Bir hücreye formül uygularken, Microsoft Excel'de formül oluştururken yaptığınız gibi dizeye her zaman eşittir işaretiyle (=) başlayın ve işlev parametrelerini sınırlamak için virgül (,) kullanın.

 Aşağıdaki örnekte, çalışma sayfasının ilk hücresine karmaşık bir formül uygulanmıştır.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Toplamak. Formül yerleşik bir formül kullanır**IF** Aspose.Cells tarafından sağlanan işlev.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

##  **Eklenti İşlevleri Nasıl Kullanılır**

Excel eklentisi olarak eklemek istediğimiz bazı kullanıcı tanımlı formüllerimiz olabilir. Cell.Formula işlevini ayarlarken yerleşik işlevler iyi çalışır ancak eklenti işlevlerini kullanarak özel işlevleri veya formülleri ayarlamaya ihtiyaç vardır.

 Aspose.Cells, eklenti işlevlerinin kaydedilmesi için özellikler sağlar.[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Daha sonra cell.Formula = anyFunctionFromAddIn ayarladığımızda çıktı Excel dosyası AddIn fonksiyonundan hesaplanan değeri içerir.

Aşağıdaki örnek koddaki eklenti fonksiyonunun kaydedilmesi için aşağıdaki XLAM numaralı dosya indirilecektir. Benzer şekilde, çıktıyı kontrol etmek için "test_udf.xlsx" çıktı dosyası indirilebilir.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

##  **Dizi Formülü Nasıl Kullanılır**

Dizi formülleri, formülü oluşturan işlevlere bağımsız değişken olarak tek tek sayılar yerine dizileri alan formüllerdir. Bir dizi formülü görüntülendiğinde, parantez ({}) ile çevrilidir.

Bazı Microsoft Excel işlevleri değer dizileri döndürür. Dizi formülüyle birden çok sonucu hesaplamak için diziyi, dizi bağımsız değişkenleriyle aynı sayıda satır ve sütuna sahip bir hücre aralığına girin.

 Çağrılarak bir hücreye dizi formülü uygulamak mümkündür.[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf'[**DiziFormülünü Ayarla**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) yöntem.[**DiziFormülünü Ayarla**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) yöntem aşağıdaki parametreleri alır:

- *Dizi Formülü**, dizi formülü.
- *Satır Sayısı**, dizi formülü sonucunun doldurulacağı satır sayısı.
- *Sütun Sayısı**, dizi formülü sonucunun doldurulacağı sütun sayısı.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

##  **R1C1 Formülü Nasıl Kullanılır**

 Ekle**R1C1** stil formülüne sahip bir hücreye başvuru[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf'[**R1C1Formülü**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) mülk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

##  **İleri konular**
- [Emsaller ve Bağımlılar](/cells/tr/net/precedents-and-dependents/)
- [Formüllerde Dış Bağlantıları Ayarlama](/cells/tr/net/set-external-links-in-formulas/)
- [Yeni satırlara veri girerken Formülü Tablo veya Liste Nesnesinde otomatik olarak yayma](/cells/tr/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Adlandırılmış Aralık için Formül Ayarlama](/cells/tr/net/setting-formula-for-named-range/)
- [Formülleri Ayarlama - İngilizce Bilmeyen Kullanıcılar için Uyarı](/cells/tr/net/setting-formulas-notice-for-non-english-users/)
- [Paylaşılan Formülü Ayarlama](/cells/tr/net/setting-shared-formula/)
- [Paylaşılan Formülün Maksimum Satırını Belirtin](/cells/tr/net/specify-maximum-rows-of-shared-formula/)
- [Desteklenen Excel İşlevleri](/cells/tr/net/supported-formula-functions/)

