---
title: Formülleri Hesapla
type: docs
weight: 110
url: /tr/java/calculate-formulas/
---
## **Formül Ekleme ve Sonuçları Hesaplama**

Aspose.Cells yerleşik bir formül hesaplama motoruna sahiptir. Yalnızca tasarımcı şablonlarından içe aktarılan formülleri yeniden hesaplamakla kalmaz, aynı zamanda çalışma zamanında eklenen formüllerin sonuçlarını hesaplamayı da destekler.

 Aspose.Cells, Microsoft Excel'in parçası olan formüllerin veya işlevlerin çoğunu destekler (Oku[hesaplama motoru tarafından desteklenen işlevlerin bir listesi](/cells/tr/java/supported-formula-functions/)). Bu işlevler, API'ler veya tasarımcı elektronik tabloları aracılığıyla kullanılabilir. Aspose.Cells, çok sayıda matematiksel, dizi, boole, tarih/saat, istatistik, veritabanı, arama ve referans formüllerini destekler.

 Kullan[**formül**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) mülk veya[**Formülü Ayarla(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula(java.lang.String,%20com.aspose.cells.FormulaParseOptions,%20java.lang.Object) ) yöntemleri[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)hücreye formül eklemek için sınıf. Bir formülü uygularken, Microsoft Excel'de formül oluştururken yaptığınız gibi dizeye her zaman eşittir işaretiyle (=) başlayın ve işlev parametrelerini ayırmak için virgül (,) kullanın.

 Formüllerin sonuçlarını hesaplamak için kullanıcı[**HesaplaFormül**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) yöntemi[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)bir Excel dosyasına katıştırılmış tüm formülleri işleyen sınıf. Veya, kullanıcı arayabilir[**HesaplaFormül**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(com.aspose.cells.CalculationOptions,%20boolean)) yöntemi[**Worsheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) bir sayfaya katıştırılmış tüm formülleri işleyen sınıf. Veya kullanıcı ayrıca[**Hesaplamak**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate(com.aspose.cells.CalculationOptions)) yöntemi[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)bir Cell formülünü işleyen sınıf:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Bilmeniz Önemli**

{{% alert color="primary" %}}

 bu**formül** mülkiyet ve**Formülü Ayarla(...)** yöntemleri[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)sınıftan farklı çalışır**Hesaplamak** yöntemleri[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) ve[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) sınıflar. bu**formül** mülkiyet ve**Formülü Ayarla(...)** yöntemler yalnızca formülü bir hücreye ekler ancak çalışma zamanında sonucu hesaplamaz. Formüllerin sonucunu almak için lütfen arayınız.**Hesaplamak** yöntemler.

{{% /alert %}}

## **Formülün Doğrudan Hesaplanması**

Aspose.Cells yerleşik bir formül hesaplama motoruna sahiptir. Aspose.Cells, bir tasarımcı dosyasından içe aktarılan formülleri hesaplamanın yanı sıra, formül sonuçlarını doğrudan hesaplayabilir.

Bazen, formül sonuçlarını bir çalışma sayfasına eklemeden doğrudan hesaplamanız gerekir. Formülde kullanılan hücrelerin değerleri bir çalışma sayfasında zaten var ve ihtiyacınız olan tek şey, formülü bir çalışma sayfasına eklemeden bazı Microsoft Excel formüllerine dayalı olarak bu değerlerin sonucunu bulmak.

 Aspose.Cells' formül hesaplama motoru API'lerini aşağıdakiler için kullanabilirsiniz:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) ile[**hesaplamak**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(java.lang.String,%20com.aspose.cells.CalculationOptions)) çalışma sayfasına eklemeden bu tür formüllerin sonuçları:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

Yukarıdaki kod aşağıdaki çıktıyı üretir:
{{< highlight "java" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Formülleri tekrar tekrar hesaplamak**

 Çalışma kitabında çok sayıda formül olduğunda ve kullanıcının bunları yalnızca küçük bir bölümünü değiştirerek tekrar tekrar hesaplaması gerektiğinde, formül hesaplama zincirini etkinleştirmek performans açısından yararlı olabilir:[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Bilmeniz Önemli**

{{% alert color="primary" %}}

Hesaplama zinciri varsayılan olarak devre dışıdır. Zinciri oluşturmak da ekstra zaman gerektirdiğinden, formülleri ilk kez hesaplarken ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions))) zincirsiz hesaplama formülleriyle karşılaştırıldığında daha fazla CPU işleme süresi ve bellek tüketebilir. Kullanıcının formülleri tekrar tekrar hesaplaması gerekmiyorsa, varsayılan davranış (hesaplama zinciri oluşturmadan formülü doğrudan hesaplama) daha iyi bir yol olmalıdır.

{{% /alert %}}

## **ileri konular**
- [Cells'i Microsoft'e ekleyin Excel Formül İzleme Penceresi](/cells/tr/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells Formül Hesaplama Motoru](/cells/tr/java/aspose-cells-formula-calculation-engine/)
- [Aspose.Cells kullanarak IFNA işlevini hesaplama](/cells/tr/java/calculating-ifna-function-using-aspose-cells/)
- [Veri Tablolarının Dizi Formülünün Hesaplanması](/cells/tr/java/calculation-of-array-formula-of-data-tables/)
- [Excel 2016 MINIFS ve MAXIFS işlevlerinin hesaplanması](/cells/tr/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Cell'in Hesaplama Süresini azaltın. Hesaplama yöntemi](/cells/tr/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [Döngüsel Referans Algılama](/cells/tr/java/detecting-circular-reference/)
- [Bir çalışma sayfasına yazmadan özel işlevin doğrudan hesaplanması](/cells/tr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Aspose.Cells Varsayılan Hesaplama Motorunu genişletmek için Özel Hesaplama Motorunu uygulayın](/cells/tr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Çalışma Kitabının Formül Hesaplamasını Durdurun veya İptal Edin](/cells/tr/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [AbstractCalculationEngine kullanarak bir Değer Aralığı Döndürme](/cells/tr/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [ICustomFunction kullanarak bir Değer Aralığı Döndürme](/cells/tr/java/returning-a-range-of-values-using-icustomfunction/)
- [ICustomFunction Özelliğini Kullanma](/cells/tr/java/using-icustomfunction-feature/)
