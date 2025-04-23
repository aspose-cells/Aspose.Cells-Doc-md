---
title: Verileri İşlemek İçin Formüller veya Fonksiyonlar Kullanma
type: docs
weight: 5
url: /tr/java/get-and-set-formula/
---

{{% alert color="primary" %}}

Microsoft Excel'in etkileyici özelliklerinden biri, kullanıcıların karmaşık hesaplamaları hızlı bir şekilde gerçekleştirmesine yardımcı olan yerleşik fonksiyonlar ve formüllerini kullanma yeteneğidir. Aspose.Cells aynı zamanda geliştiricilerin değerleri kolayca hesaplamalarına yardımcı olan geniş bir yerleşik fonksiyonlar ve formüller kümesini sunar. Aspose.Cells ayrıca eklenti fonksiyonları da destekler. Ayrıca Aspose.Cells, Aspose.Cells'te dizi ve R1C1 formüllerini destekler.

{{% /alert %}}

## **Formülleri ve Fonksiyonları Kullanma**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf içerisinde, Excel dosyasındaki her çalışma sayfasına erişime izin veren bir [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) koleksiyonu bulunmaktadır. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, bir [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) koleksiyonundaki her bir öğe, [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının bir nesnesini temsil eder.

Aşağıdaki örnekte, bir çalışma sayfasının [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) koleksiyonunun ilk hücresine karmaşık bir formül uygulanmaktadır. Formül, Aspose.Cells tarafından sağlanan yerleşik bir **IF** fonksiyonunu kullanmaktadır.

- [Yerleşik fonksiyonları kullanma](/cells/tr/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [Eklenti fonksiyonları kullanma](/cells/tr/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [Dizi formülleriyle çalışma](/cells/tr/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [Bir R1C1 formülü oluşturma](/cells/tr/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **Yerleşik Fonksiyonları Kullanma**

Yerleşik fonksiyonlar veya formüller, geliştiricilerin çabalarını ve zamanını azaltmak için hazır fonksiyonlar olarak sunulur. [Yerleşik fonksiyonların listesini](/cells/tr/java/supported-formula-functions/) görün. Fonksiyonlar alfabetik sırayla listelenmiştir. Daha fazla fonksiyon gelecekte desteklenecektir.

Aspose.Cells, Microsoft Excel tarafından sunulan çoğu formül veya fonksiyonu destekler. Geliştiriciler, bu formülleri API veya [tasarımcı elektronik tablosu](/cells/tr/java/what-is-a-designer-spreadsheet/) aracılığıyla kullanabilirler. Aspose.Cells, matematiksel, dize, Boole, tarih/saat, istatistiksel, veri tabanı, arama, ve referans formüllerinin geniş bir yelpazesini destekler.

Bir hücreye formül eklemek için [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) sınıfının [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) özelliğini kullanın. Örneğin, **Karmaşık formüller**

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, Aspose.Cells'te de desteklenir. Bir hücreye formül uygularken, her zaman dizeye bir eşitlik işareti (=) ile başlayın (Microsoft Excel'de formül oluştururken olduğu gibi) ve bir virgül (,) kullanarak fonksiyon parametrelerini ayırın.

Aşağıdaki örnekte, bir çalışma sayfasının [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) koleksiyonunun ilk hücresine karmaşık bir formül uygulanmaktadır. Formül, Aspose.Cells tarafından sağlanan yerleşik bir **IF** fonksiyonunu kullanmaktadır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **Eklenti Fonksiyonlarını Kullanma**

Bir excel eklentisi olarak dahil etmek istediğimiz bazı kullanıcı tanımlı formüllere sahip olabiliriz. [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) işlevini ayarladığımızda yerleşik fonksiyonlar düzgün çalışır ancak eklenti fonksiyonlarını kullanarak özel işlevleri veya formülleri ayarlamak gerekmektedir.

Aspose.Cells, [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction-java.lang.String-java.lang.String-boolean-) kullanarak eklenti fonksiyonlarını kaydetme özellikleri sağlar. Daha sonra [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) = anyFunctionFromAddIn ayarlandığında, çıktı Excel dosyası, AddIn fonksiyonundan hesaplanan değeri içerir.

Aşağıdaki örnek kod için aşağıdaki XLAM dosyası indirilmelidir (Bir eklenmiş fonksiyon için kaydetme işlemi). Benzer şekilde, çıktı dosyası "test_udf.xlsx" indirilip çıktı kontrol edilebilir.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **Dizi Formülü Kullanma**

Dizi formüller, formülü oluşturan fonksiyonlara bağımsız sayılar yerine dizilerle çalışan formüllerdir. Bir dizi formülü görüntülendiğinde aşağıdaki gibi süslü parantezlerle ({}) çevrelenmiş olacaktır.

**G2 hücresine bir dizi formül ayarlama** 

![todo:image_alt_text](using-formulas-or-functions-to-process-data_1.png)

Bazı Microsoft Excel fonksiyonları değerler dizileri döndürür. Bir dizi formülü ile birden çok sonucu hesaplamak için, diziyi formül argümanları olarak kullanarak aynı satır ve sütun sayısına sahip bir hücre aralığına girin.

Bir dizi formülü uygulamak mümkündür, bunun için [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula-java.lang.String-int-int-) metodunu çağırmak gereklidir. [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula-java.lang.String-int-int-) metodu şu parametreleri alır:

- **Dizi Formülü**, dizi formülü.
- **Satır Sayısı**, dizi formülünün sonucunu doldurmak için satır sayısı.
- **Sütun Sayısı**, dizi formülünün sonucunu doldurmak için sütun sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **R1C1 Formülü Kullanma**

[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının [**setR1C1Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula) özelliği ile bir hücreye R1C1 başvuru stili formül uygula.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

{{< app/cells/assistant language="java" >}}
