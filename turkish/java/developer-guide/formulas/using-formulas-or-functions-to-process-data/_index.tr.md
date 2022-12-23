---
title: Verileri İşlemek İçin Formülleri veya İşlevleri Kullanma
type: docs
weight: 5
url: /tr/java/get-and-set-formula/
---
{{% alert color="primary" %}}

Microsoft Excel'in ilgi çekici özelliklerinden biri, verileri formüller ve işlevlerle işleyebilmesidir. Microsoft Excel, kullanıcıların karmaşık hesaplamaları hızla gerçekleştirmesine yardımcı olan bir dizi yerleşik işlev ve formül sağlar. Aspose.Cells ayrıca, geliştiricilerin değerleri kolayca hesaplamasına yardımcı olan çok sayıda yerleşik işlev ve formül sağlar. Aspose.Cells ayrıca eklenti işlevlerini de destekler. Ayrıca Aspose.Cells, Aspose.Cells'deki dizi ve R1C1 formüllerini destekler.

{{% /alert %}}

## **Formülleri ve İşlevleri Kullanma**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)sınıf.

 tarafından sunulan özellikler ve yöntemler kullanılarak hücrelere formüller uygulamak mümkündür.[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)sınıf, aşağıda daha ayrıntılı olarak ele alınmıştır.

- [Yerleşik işlevleri kullanma](/cells/tr/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [Eklenti işlevlerini kullanma](/cells/tr/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [Dizi formülleriyle çalışma](/cells/tr/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [R1C1 formülü oluşturma](/cells/tr/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **Yerleşik İşlevleri Kullanma**

 Yerleşik işlevler veya formüller, geliştiricilerin çabalarını ve zamanını azaltmak için hazır işlevler olarak sağlanır. Görmek[yerleşik işlevlerin bir listesi](/cells/tr/java/supported-formula-functions/). Fonksiyonlar alfabetik sırayla listelenmiştir. Gelecekte daha fazla işlev desteklenecektir.

 Aspose.Cells, Microsoft Excel tarafından sunulan formüllerin veya işlevlerin çoğunu destekler. Geliştiriciler bu formülleri API veya[tasarımcı elektronik tablosu](/cells/tr/java/what-is-a-designer-spreadsheet/). Aspose.Cells, çok sayıda matematiksel, dizi, Boole, tarih/saat, istatistik, veritabanı, arama ve referans formüllerini destekler.

 Kullan[**formül**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)mülkiyeti[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) hücreye formül eklemek için sınıf.**karmaşık formüller**, örneğin

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, Aspose.Cells'de de desteklenir. Bir hücreye formül uygularken, Microsoft Excel'de formül oluştururken yaptığınız gibi dizeye her zaman eşittir işaretiyle (=) başlayın ve işlev parametrelerini ayırmak için virgül (,) kullanın.

 Aşağıdaki örnekte, bir çalışma sayfasının ilk hücresine karmaşık bir formül uygulanmıştır.[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) Toplamak. Formül yerleşik bir kullanır**EĞER** Aspose.Cells tarafından sağlanan işlev.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **Eklenti İşlevlerini Kullanma**

 Excel eklentisi olarak dahil etmek istediğimiz bazı kullanıcı tanımlı formüllerimiz olabilir. ayarlarken[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) yerleşik işlevler iyi çalışır, ancak eklenti işlevleri kullanarak özel işlevleri veya formülleri ayarlamaya ihtiyaç vardır.

 Aspose.Cells, kullanarak eklenti işlevlerini kaydetmek için özellikler sağlar[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean)). Daha sonra ayarladığımızda[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) anyFunctionFromAddIn, çıktı Excel dosyası AddIn işlevinden hesaplanan değeri içerir.

Aşağıdaki örnek kodda eklenti fonksiyonunun kaydedilmesi için XLAM dosyası indirilmelidir. Benzer şekilde, çıktıyı kontrol etmek için "test_udf.xlsx" çıktı dosyası indirilebilir.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **Dizi Formülünü Kullanma**

Dizi formülleri, formülü oluşturan işlevlerin bağımsız değişkenleri olarak tek tek sayılar yerine dizilerle çalışan formüllerdir. Bir dizi formülü görüntülendiğinde, aşağıda gösterildiği gibi köşeli parantezler ({}) içine alınır.

**G2 hücresinde bir dizi formülü ayarlama** 

![yapılacaklar:resim_alternatif_metin](using-formulas-or-functions-to-process-data_1.png)

Bazı Microsoft Excel işlevleri, değer dizileri döndürür. Bir dizi formülüyle birden çok sonucu hesaplamak için diziyi, dizi bağımsız değişkenleriyle aynı sayıda satır ve sütuna sahip bir hücre aralığına girin.

 çağırarak bir hücreye dizi formülü uygulamak mümkündür.[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıf'[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int) ) yöntem. bu[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)) yöntemi aşağıdaki parametreleri alır:

- **Dizi Formülü**dizi formülü.
- **Satır sayısı**, dizi formülünün sonucu doldurulacak satır sayısı.
- **Sütun sayısı**, dizi formülünün sonucunu dolduracak sütun sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **R1C1 Formülünü Kullanma**

 Uygula**R1C1** ile bir hücreye başvuru stili formülü[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıf'[**setR1C1Formül**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula)Emlak.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

