---
title: Excel dosyalarının formüllerini yönetmek
linktitle: Formüller
type: docs
weight: 122
url: /tr/python-net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells for Python via .NET, basitçe Excel dosyalarının formüllerini alabilir, ayarlayabilir ve hesaplayabilir.
description: Aspose.Cells for Python via .NET kullanarak Excel dosyalarının formüllerini nasıl yöneteceğinizi öğrenin.
keywords: Python da formülleri nasıl hesaplarım, Python ile Formüller ve Fonksiyonlar, Python da Yerleşik Fonksiyonları nasıl yönetilir, Python ile Eklenti Fonksiyonları nasıl kullanılır, Python aracılığıyla Dizi Formülü nasıl kullanılır, Python da R1C1 Formülü nasıl kullanılır.
---

## **Giriş**

Microsoft Excel'in etkileyici özelliklerinden biri, verileri formüller ve fonksiyonlar kullanarak işleyebilme yeteneğidir. Microsoft Excel, kullanıcılara karmaşık hesaplamaları hızlıca yapmalarını sağlayan yerleşik fonksiyonlar ve formüller sunar. Aspose.Cells for Python via .NET de, geliştiricilerin kolayca hesaplama yapabilmesine yardımcı olan büyük bir yerleşik fonksiyon ve formül seti sağlar. Ayrıca, Aspose.Cells for Python via .NET, eklenti fonksiyonlarını da destekler. Dahası, Aspose.Cells for Python via .NET dizi ve R1C1 formüllerini de destekler.

## **Formüller ve Fonksiyonları Nasıl Kullanılır**

Aspose.Cells for Python via .NET, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ise [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonu sağlar. Cells koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfı nesnesini temsil eder.

Aşağıda daha detaylı olarak tartışılan [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfının özellikleri ve metotları kullanılarak hücrelere formül uygulamak mümkündür.

- Yerleşik fonksiyonları kullanarak.
- Eklenti fonksiyonlarını kullanarak.
- Dizi formülleri ile çalışma.
- Bir R1C1 formülü oluşturma.

## **Yerleşik Fonksiyonları Nasıl Kullanılır**

Yerleşik fonksiyonlar veya formüller, geliştiricilerin çaba ve zamanını azaltmak için hazır olarak sağlanmıştır. Aspose.Cells for Python via .NET tarafından desteklenen yerleşik fonksiyonların [listesine](/cells/tr/python-net/supported-formula-functions/) bakın. Fonksiyonlar alfabetik sırayla listelenmiştir. Gelecekte daha fazla fonksiyon desteklenecektir.

Aspose.Cells for Python via .NET, Microsoft Excel tarafından sunulan çoğu formül veya fonksiyonu destekler. Geliştiriciler bu formülleri API veya [tasarımcı elektronik tablosu](/cells/tr/net/what-is-a-designer-spreadsheet/) aracılığıyla kullanabilir. Aspose.Cells for Python via .NET, geniş matematiksel, dize, Mantıksal, tarih/saat, istatistik, veritabanı, arama ve referans formüllerini destekler.

[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfının [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula) özelliğini kullanarak hücreye formül ekleyin. Örneğin **Karmaşık formüller**

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, Aspose.Cells for Python via .NET'de de desteklenir. Bir hücreye formül uygularken, her zaman formül oluştururken yaptığınız gibi dizgiyi eşittir işareti (=) ile başlayın ve fonksiyon parametrelerini ayırmak için virgül (,) kullanın.

Aşağıdaki örnekte, karmaşık bir formül, bir çalışma sayfasının [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonunun ilk hücresine uygulanır. Formül, Aspose.Cells for Python via .NET tarafından sağlanan yerleşik **IF** fonksiyonunu kullanır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingBuiltinfunction-1.py" >}}

## **Eklenti Fonksiyonlarını Nasıl Kullanılır**

Excel'e dahil etmek istediğimiz bazı kullanıcı tanımlı formüllere excel eklentisi olarak eklemek istiyoruz. Hücre.Formül işlevi yerleşik fonksiyonları kullanırken sorunsuz çalışır, ancak eklenti fonksiyonlarını veya formülleri ayarlamak için bir ihtiyaç vardır.

Aspose.Cells for Python via .NET, [**worksheets.register_add_in_function()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/register_add_in_function) kullanarak eklenti fonksiyonlarını kaydetme özellikleri sağlar. Daha sonra cell.Formula = herhangiBirFonksiyon, eklenti fonksiyonundan alınan hesaplanan değeri içeren çıktı Excel dosyasına yazar.

Aşağıdaki örnek kodda, eklenti fonksiyonunu kaydetmek için aşağıdaki XLAM dosyası indirilmelidir. Benzer şekilde, çıktı dosyası olan "test_udf.xlsx"yi indirerek çıktıyı kontrol edebilirsiniz.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-RegisterAndCallFuncFromAddIn-1.py" >}}

## **Dizi Formülü Nasıl Kullanılır**

Dizi formüller, formülün bileşenlerine argüman olarak tek sayılar yerine dizileri alan formüllerdir. Dizi formülü gösterildiğinde, süslü parantezlerle ({}) çevrilidir.

Bazı Microsoft Excel fonksiyonları değerler dizileri döndürür. Bir dizi formülü ile birden çok sonucu hesaplamak için, diziyi formül argümanları olarak kullanarak aynı satır ve sütun sayısına sahip bir hücre aralığına girin.

Bir dizi formülünü, [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfının [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) yöntemini çağırarak bir hücreye uygulamak mümkündür. [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) yöntemi aşağıdaki parametreleri alır:

- **Dizi Formülü**, dizi formülü.
- **Satır Sayısı**, dizi formülünün sonucunu doldurmak için satır sayısı.
- **Sütun Sayısı**, dizi formülünün sonuçlarını doldurmak için sütun sayısı.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingArrayFunction-1.py" >}}

## **R1C1 Formülünü Nasıl Kullanılır**

Bir **R1C1** referans stili formülünü, [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfının [**r1c1_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/r1c1_formula) özelliği ile bir hücreye ekleyin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingR1C1-1.py" >}}

## **Gelişmiş Konular**
- [Öncüler ve Bağımlılar](/cells/tr/python-net/precedents-and-dependents/)
- [Formüllerde Harici Bağlantıları Ayarla](/cells/tr/python-net/set-external-links-in-formulas/)
- [Yeni satırlara veri girilirken Tablo veya List Objesinde Formülü otomatik olarak çoğaltın](/cells/tr/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Adlandırılmış Aralık için Formül Ayarlama](/cells/tr/python-net/setting-formula-for-named-range/)
- [Formülleri Ayarlama - Diğer Dilleri Kullanan Kullanıcılar İçin Uyarı](/cells/tr/python-net/setting-formulas-notice-for-non-english-users/)
- [Paylaşılan Formülü Ayarlama](/cells/tr/python-net/setting-shared-formula/)
- [Paylaşılan Formülün Maksimum Satırlarını Belirtme](/cells/tr/python-net/specify-maximum-rows-of-shared-formula/)
- [Desteklenen Excel İşlevleri](/cells/tr/python-net/supported-formula-functions/)


