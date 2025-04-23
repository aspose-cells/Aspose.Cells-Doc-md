---
title: Excel dosyalarının formüllerini yönetmek
linktitle: Formüller
type: docs
weight: 122
url: /tr/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells sadece Excel dosyalarının formüllerini alabilir, ayarlayabilir ve hesaplayabilir.
description: Aspose.Cells for NET API leri aracılığıyla Excel dosyalarının formüllerini nasıl yöneteceğinizi öğrenin.
keywords: C# da formülleri nasıl hesaplayacağınız, C# Kullanarak Formüller ve Fonksiyonlar, C# Kullanarak Yerleşik Fonksiyonları Yönetme, C# ile Eklenti Fonksiyonlarını Nasıl Kullanılır, C# ile Dizi Formülü Nasıl Kullanılır, C# ile R1C1 Formülü Nasıl Kullanılır.
---

## **Giriş**

Microsoft Excel'in etkileyici özelliklerinden biri, verileri formüller ve fonksiyonlar ile işleyebilme yeteneğidir. Microsoft Excel, karmaşık hesaplamaları hızlıca yapmaya yardımcı olan yerleşik fonksiyonlar ve formüller sunar. Aspose.Cells ayrıca, gelişmiş fonksiyon ve formüllerin büyük bir kümesini sağlar ve ayrıca eklenti fonksiyonlarını da destekler. Ayrıca, Aspose.Cells, dizi ve R1C1 formüllerini destekler.

## **Formüller ve Fonksiyonları Nasıl Kullanılır**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişime izin veren bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu sağlar. Hücreler koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfından bir nesneyi temsil eder.

Aşağıda daha detaylı olarak tartışılan [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının özellikleri ve metotları kullanılarak hücrelere formül uygulamak mümkündür.

- Yerleşik fonksiyonları kullanarak.
- Eklenti fonksiyonlarını kullanarak.
- Dizi formülleri ile çalışma.
- Bir R1C1 formülü oluşturma.

## **Yerleşik Fonksiyonları Nasıl Kullanılır**

Yerleşik fonksiyonlar veya formüller, geliştiricilerin çabalarını ve zamanını azaltmak için hazır işlevler olarak sunulur. Aspose.Cells tarafından desteklenen [yerleşik fonksiyonların listesine](/cells/tr/net/supported-formula-functions/) bakın. Fonksiyonlar alfabetik sırayla listelenir. Daha fazla fonksiyon gelecekte desteklenecektir.

Aspose.Cells, Microsoft Excel tarafından sunulan çoğu formülü veya fonksiyonu destekler. Geliştiriciler bu formülleri API veya [tasarımcı elektronik tablo](/cells/tr/net/what-is-a-designer-spreadsheet/) kullanarak kullanabilirler. Aspose.Cells, matematiksel, dize, Boolean, tarih/saat, istatistiksel, veritabanı, arama ve referans formüllerinin büyük bir kümesini destekler.

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) özelliğini kullanarak hücreye formül ekleyin. Örneğin **Karmaşık formüller**

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, Aspose.Cells'te de desteklenir. Bir hücreye formül uygularken, her zaman dizeye bir eşitlik işareti (=) ile başlayın (Microsoft Excel'de formül oluştururken olduğu gibi) ve bir virgül (,) kullanarak fonksiyon parametrelerini ayırın.

Aşağıdaki örnekte, bir çalışma sayfasının [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunun ilk hücresine karmaşık bir formül uygulanmıştır. Formül, Aspose.Cells tarafından sağlanan yerleşik bir **IF** fonksiyonunu kullanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Eklenti Fonksiyonlarını Nasıl Kullanılır**

Excel'e dahil etmek istediğimiz bazı kullanıcı tanımlı formüllere excel eklentisi olarak eklemek istiyoruz. Hücre.Formül işlevi yerleşik fonksiyonları kullanırken sorunsuz çalışır, ancak eklenti fonksiyonlarını veya formülleri ayarlamak için bir ihtiyaç vardır.

Aspose.Cells, [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index) kullanarak eklenti fonksiyonlarını kaydetme özellikleri sağlar. Daha sonra hücre.Formül = anyFunctionFromAddIn şeklinde ayarlandığında, çıktı Excel dosyası, AddIn fonksiyonundan hesaplanan değeri içerir.

Aşağıdaki örnek kodda, eklenti fonksiyonunu kaydetmek için aşağıdaki XLAM dosyası indirilmelidir. Benzer şekilde, çıktı dosyası olan "test_udf.xlsx"yi indirerek çıktıyı kontrol edebilirsiniz.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Dizi Formülü Nasıl Kullanılır**

Dizi formüller, formülün bileşenlerine argüman olarak tek sayılar yerine dizileri alan formüllerdir. Dizi formülü gösterildiğinde, süslü parantezlerle ({}) çevrilidir.

Bazı Microsoft Excel fonksiyonları değerler dizileri döndürür. Bir dizi formülü ile birden çok sonucu hesaplamak için, diziyi formül argümanları olarak kullanarak aynı satır ve sütun sayısına sahip bir hücre aralığına girin.

Bir dizi formülünü, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) yöntemini çağırarak bir hücreye uygulamak mümkündür. [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) yöntemi aşağıdaki parametreleri alır:

- **Dizi Formülü**, dizi formülü.
- **Satır Sayısı**, dizi formülünün sonucunu doldurmak için satır sayısı.
- **Sütun Sayısı**, dizi formülünün sonuçlarını doldurmak için sütun sayısı.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **R1C1 Formülünü Nasıl Kullanılır**

Bir **R1C1** referans stili formülünü, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının [**R1C1Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) özelliği ile bir hücreye ekleyin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **Gelişmiş Konular**
- [Öncüler ve Bağımlılar](/cells/tr/net/precedents-and-dependents/)
- [Formüllerde Harici Bağlantıları Ayarla](/cells/tr/net/set-external-links-in-formulas/)
- [Yeni satırlara veri girilirken Tablo veya List Objesinde Formülü otomatik olarak çoğaltın](/cells/tr/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Adlandırılmış Aralık için Formül Ayarlama](/cells/tr/net/setting-formula-for-named-range/)
- [Formülleri Ayarlama - Diğer Dilleri Kullanan Kullanıcılar İçin Uyarı](/cells/tr/net/setting-formulas-notice-for-non-english-users/)
- [Paylaşılan Formülü Ayarlama](/cells/tr/net/setting-shared-formula/)
- [Paylaşılan Formülün Maksimum Satırlarını Belirtme](/cells/tr/net/specify-maximum-rows-of-shared-formula/)
- [Desteklenen Excel İşlevleri](/cells/tr/net/supported-formula-functions/)

{{< app/cells/assistant language="csharp" >}}
