---
title: Excel dosyalarının formüllerini yönetme
linktitle: formüller
type: docs
weight: 122
url: /tr/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells, excel dosyalarının formüllerini kolayca alabilir, ayarlayabilir ve hesaplayabilir.
---
## **Giriş**

Microsoft Excel'in ilgi çekici özelliklerinden biri, verileri formüller ve işlevlerle işleyebilmesidir. Microsoft Excel, kullanıcıların karmaşık hesaplamaları hızla gerçekleştirmesine yardımcı olan bir dizi yerleşik işlev ve formül sağlar. Aspose.Cells ayrıca, geliştiricilerin değerleri kolayca hesaplamasına yardımcı olan çok sayıda yerleşik işlev ve formül sağlar. Aspose.Cells ayrıca eklenti işlevlerini de destekler. Ayrıca Aspose.Cells, Aspose.Cells'deki dizi ve R1C1 formüllerini destekler.

## **Formülleri ve İşlevleri Kullanma**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. Cells koleksiyonundaki her öğe, bir nesneyi temsil eder.[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf.

 tarafından sunulan özellikler ve yöntemler kullanılarak hücrelere formüller uygulamak mümkündür.[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf, aşağıda daha ayrıntılı olarak ele alınmıştır.

- Yerleşik işlevleri kullanma.
- Eklenti işlevlerini kullanma.
- Dizi formülleriyle çalışma.
- R1C1 formülü oluşturma.

## **Yerleşik İşlevleri Kullanma**

 Yerleşik işlevler veya formüller, geliştiricilerin çabalarını ve zamanını azaltmak için hazır işlevler olarak sağlanır. Görmek[yerleşik işlevlerin bir listesi](/cells/tr/net/supported-formula-functions/) Aspose.Cells tarafından desteklenmektedir. Fonksiyonlar alfabetik sırayla listelenmiştir. Gelecekte daha fazla işlev desteklenecektir.

 Aspose.Cells, Microsoft Excel tarafından sunulan formüllerin veya işlevlerin çoğunu destekler. Geliştiriciler bu formülleri API veya[tasarımcı elektronik tablosu](/cells/tr/net/what-is-a-designer-spreadsheet/). Aspose.Cells, çok sayıda matematiksel, dizi, Boolean, tarih/saat, istatistik, veritabanı, arama ve referans formüllerini destekler.

 Kullan[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf'[**formül**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)hücreye formül ekleme özelliği.**karmaşık formüller**, örneğin

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, Aspose.Cells'de de desteklenir. Bir hücreye formül uygularken, Microsoft Excel'de formül oluştururken yaptığınız gibi dizeye her zaman eşittir işaretiyle (=) başlayın ve işlev parametrelerini ayırmak için virgül (,) kullanın.

 Aşağıdaki örnekte, bir çalışma sayfasının ilk hücresine karmaşık bir formül uygulanmıştır.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Toplamak. Formül yerleşik bir kullanır**EĞER** Aspose.Cells tarafından sağlanan işlev.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Eklenti İşlevlerini Kullanma**

Excel eklentisi olarak dahil etmek istediğimiz bazı kullanıcı tanımlı formüllerimiz olabilir. Cell.Formula işlevini ayarlarken yerleşik işlevler iyi çalışır, ancak eklenti işlevleri kullanarak özel işlevleri veya formülleri ayarlamaya ihtiyaç vardır.

 Aspose.Cells, kullanarak eklenti işlevlerini kaydetmek için özellikler sağlar[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Daha sonra cell.Formula=anyFunctionFromAddIn ayarını yaptığımızda çıktı Excel dosyası AddIn fonksiyonundan hesaplanan değeri içermektedir.

Aşağıdaki örnek kodda eklenti işlevinin kaydedilmesi için aşağıdaki XLAM dosyası indirilmelidir. Benzer şekilde çıktıyı kontrol etmek için "test_udf.xlsx" çıktı dosyası indirilebilir.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Dizi Formülünü Kullanma**

Dizi formülleri, formülü oluşturan işlevlerin bağımsız değişkenleri olarak tek tek sayılar yerine dizileri alan formüllerdir. Bir dizi formülü görüntülendiğinde, parantezler ({}) içine alınır.

Bazı Microsoft Excel işlevleri, değer dizileri döndürür. Bir dizi formülüyle birden çok sonucu hesaplamak için diziyi, dizi bağımsız değişkenleriyle aynı sayıda satır ve sütuna sahip bir hücre aralığına girin.

 çağırarak bir hücreye dizi formülü uygulamak mümkündür.[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf'[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) yöntem. bu[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) yöntem aşağıdaki parametreleri alır:

- **Dizi Formülü**dizi formülü.
- **Satır sayısı**, dizi formülünün sonucu doldurulacak satır sayısı.
- **Sütun sayısı**dizi formülünün sonucu doldurulacak sütun sayısı.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **R1C1 Formülünü Kullanma**

 ekle**R1C1** ile bir hücreye başvuru stili formülü[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf'[**R1C1Formülü**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) Emlak.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **ileri konular**
- [Emsaller ve Bağımlı Kişiler](/cells/tr/net/precedents-and-dependents/)
- [Formüllerde Dış Bağlantıları Ayarlama](/cells/tr/net/set-external-links-in-formulas/)
- [Yeni satırlara veri girerken Formülü Tablo veya Liste Nesnesinde otomatik olarak yay](/cells/tr/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Adlandırılmış Aralık için Ayar Formülü](/cells/tr/net/setting-formula-for-named-range/)
- [Ayar Formülleri - İngilizce Dışı Kullanıcılar İçin Uyarı](/cells/tr/net/setting-formulas-notice-for-non-english-users/)
- [Paylaşılan Formülü Ayarlama](/cells/tr/net/setting-shared-formula/)
- [Paylaşılan Formülün Maksimum Satırını Belirtin](/cells/tr/net/specify-maximum-rows-of-shared-formula/)
- [Desteklenen Excel İşlevleri](/cells/tr/net/supported-formula-functions/)

