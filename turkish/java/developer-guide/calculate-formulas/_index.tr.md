---
title: Formülleri Hesapla
type: docs
weight: 110
url: /tr/java/calculate-formulas/
---

## **Formüller Ekleyin ve Sonuçlarını Hesaplayın**

Aspose.Cells, yerleşik bir formül hesaplama motoruna sahiptir. Sadece tasarımcı şablonlarından içe aktarılan formülleri yeniden hesaplayabileceği gibi, çalışma zamanında eklenen formül sonuçlarını da hesaplama desteği sağlar.

Aspose.Cells, Microsoft Excel'in bir parçası olan çoğu formülü veya işlevi destekler (Formül Motoru tarafından desteklenen işlevlerin bir listesini okuyun). Bu işlevler, API'ler veya tasarımcı elektronik tabloları aracılığıyla kullanılabilir. Aspose.Cells, matematiksel, dize, mantıksal, tarih/saat, istatistiksel, veritabanı, arama ve referans formüllerinin geniş bir setini destekler.

Bir hücreye formül eklemek için [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) sınıfının [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) özelliğini veya [**SetFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula-java.lang.String-com.aspose.cells.FormulaParseOptions-java.lang.Object-) yöntemlerini kullanın. Bir formül uygularken, her zaman bir eşittir işareti ile ( = ) başlayın, Microsoft Excel'de bir formül oluştururken yaptığınız gibi ve bir virgül ( , ) kullanarak fonksiyon parametrelerini sınırlayın.

Formüllerin sonuçlarını hesaplamak için, kullanıcı [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--) metodunu [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfında çağırabilir. Bu metod, bir Excel dosyasına gömülü tüm formülleri işler. Ayrıca, kullanıcı [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-com.aspose.cells.CalculationOptions-boolean-) metodunu [**Worsheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfında çağırabilir veya [**Calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate-com.aspose.cells.CalculationOptions-) metodunu çağırabilir, bu metodlar da gömülü tüm formülleri işler veya sadece bir hücrenin formülünü işler:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Bilinmesi Gerekenler**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) sınıfının **Formül** özelliği ve **SetFormula(...)** yöntemleri, **[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) ve [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)** sınıflarının **Hesapla** yöntemlerinden farklı çalışır. **Formül** özelliği ve **SetFormula(...)** yöntemleri, sadece bir formülü bir hücreye ekler ancak çalışma zamanında sonucu hesaplamaz. Formüllerin sonucunu elde etmek için lütfen **Hesapla** yöntemlerini çağırın.

{{% /alert %}}

## **Formülün Doğrudan Hesaplanması**

Aspose.Cells, gömülü bir formül hesaplama motoruna sahiptir. Bir tasarımcı dosyasından içe aktarılmış formülleri hesaplamanın yanı sıra, Aspose.Cells, formül sonuçlarını doğrudan hesaplamayı da destekler.

Bazen, bir elektronik tabloya formül eklemadan, formülde kullanılan hücre değerlerinin sonuçlarını, Microsoft Excel formülüne dayalı olarak bulmanız gerekebilir. Formülde kullanılan hücrelerin değerleri zaten bir elektronik tabloda mevcutsa ve ihtiyacınız olan tek şey bir elektronik tabloya formül eklemek değilse, Aspose.Cells'in formül hesaplama motoru API'lerini kullanarak bu tür formüllerin sonuçlarını {0} için {1} hesaplayabilirsiniz.

Yukarıdaki kod aşağıdaki çıktıyı üretir:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

Formülleri Tekrarlı Hesaplamak İçin Nasıl
{{< highlight java >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Formüllerin Tekrarlayarak Hesaplanması**

Çalışma kitabında çok sayıda formül bulunduğunda ve kullanıcının bunların bir kısmını tekrarlanacak şekilde sık sık hesaplaması gerektiğinde, formül hesaplama zincirini etkinleştirmek, yalnızca bir elektronik tablo kısmını değiştirerek tekrarlamak için formül hesaplama zincirini etkinleştirmek performans için yararlı olabilir: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Bilinmesi Gerekenler**

{{% alert color="primary" %}}

Varsayılan olarak hesaplama zinciri devre dışıdır. Çünkü zincir oluşturmak fazladan zaman alır; formülleri ilk kez hesaplamak ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--) daha fazla CPU işlemi ve bellek kullanabilir, zincirsiz hesaplamaya göre). Eğer kullanıcı tekrar tekrar formülleri hesaplamıyorsa, varsayılan davranış (doğrudan formülü hesaplamak, zincir oluşturmadan) daha uygun olur.

{{% /alert %}}

## **Gelişmiş Konular**
- [Microsoft Excel Formül İzleme Penceresine Hücreler Ekleme](/cells/tr/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells Formül Hesaplama Motoru](/cells/tr/java/aspose-cells-formula-calculation-engine/)
- [Aspose.Cells ile IFNA işlevinin hesaplanması](/cells/tr/java/calculating-ifna-function-using-aspose-cells/)
- [Veri Tablolarının Dizi Formül Hesaplama](/cells/tr/java/calculation-of-array-formula-of-data-tables/)
- [Excel 2016 MINIFS ve MAXIFS işlevlerinin hesaplanması](/cells/tr/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Hücre.Calculate yönteminin Hesaplama Süresini Azaltma](/cells/tr/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [Dairesel Referansı Algılama](/cells/tr/java/detecting-circular-reference/)
- [Özel işlevin çalışma tablosuna yazılmadan doğrudan hesaplanması](/cells/tr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Aspose.Cells'in Varsayılan Hesaplama Motorunu Genişletmek için Özel Hesaplama Motoru Uygulamak](/cells/tr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Çalışma Kitabının Formül Hesaplamasını Kesmek veya İptal Etmek](/cells/tr/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [AbstractCalculationEngine Kullanarak Bir Değer Aralığı Döndürme](/cells/tr/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [ICustomFunction Kullanarak Bir Değer Aralığı Döndürme](/cells/tr/java/returning-a-range-of-values-using-icustomfunction/)
- [ICustomFunction Özelliğinin Kullanımı](/cells/tr/java/using-icustomfunction-feature/)
{{< app/cells/assistant language="java" >}}
