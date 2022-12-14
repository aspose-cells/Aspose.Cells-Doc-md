---
title: Formülleri Hesapla
type: docs
weight: 125
url: /tr/net/calculate-formulas/
---
## **Formül Ekleme ve Sonuçları Hesaplama**

Aspose.Cells yerleşik bir formül hesaplama motoruna sahiptir. Yalnızca tasarımcı şablonlarından içe aktarılan formülleri yeniden hesaplamakla kalmaz, aynı zamanda çalışma zamanında eklenen formüllerin sonuçlarını hesaplamayı da destekler.

 Aspose.Cells, Microsoft Excel'in parçası olan formüllerin veya işlevlerin çoğunu destekler (Oku[hesaplama motoru tarafından desteklenen işlevlerin bir listesi](/cells/tr/net/supported-formula-functions/)). Bu işlevler, API'ler veya tasarımcı elektronik tabloları aracılığıyla kullanılabilir. Aspose.Cells, çok sayıda matematiksel, dizi, boole, tarih/saat, istatistik, veritabanı, arama ve referans formüllerini destekler.

 Kullan[**formül**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) mülk veya[**Formülü Ayarla(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) yöntemleri[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)hücreye formül eklemek için sınıf. Bir formülü uygularken, Microsoft Excel'de formül oluştururken yaptığınız gibi dizeye her zaman eşittir işaretiyle (=) başlayın ve işlev parametrelerini ayırmak için virgül (,) kullanın.

 Formüllerin sonuçlarını hesaplamak için kullanıcı[**HesaplaFormül**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) yöntemi[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)bir Excel dosyasına katıştırılmış tüm formülleri işleyen sınıf. Veya, kullanıcı arayabilir[**HesaplaFormül**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) yöntemi[**Worsheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bir sayfaya katıştırılmış tüm formülleri işleyen sınıf. Veya kullanıcı ayrıca[**Hesaplamak**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) yöntemi[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)bir Cell formülünü işleyen sınıf:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **Bilmeniz Önemli**

{{% alert color="primary" %}}

 bu**formül** mülkiyet ve**Formülü Ayarla(...)** yöntemleri[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıftan farklı çalışır**Hesaplamak** yöntemleri[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) ve[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıflar. bu**formül** mülkiyet ve**Formülü Ayarla(...)** yöntemler yalnızca formülü bir hücreye ekler ancak çalışma zamanında sonucu hesaplamaz. Formüllerin sonucunu almak için lütfen arayınız.**Hesaplamak** yöntemler.

{{% /alert %}}

## **Formülün Doğrudan Hesaplanması**

Aspose.Cells yerleşik bir formül hesaplama motoruna sahiptir. Aspose.Cells, bir tasarımcı dosyasından içe aktarılan formülleri hesaplamanın yanı sıra, formül sonuçlarını doğrudan hesaplayabilir.

Bazen, formül sonuçlarını bir çalışma sayfasına eklemeden doğrudan hesaplamanız gerekir. Formülde kullanılan hücrelerin değerleri bir çalışma sayfasında zaten var ve ihtiyacınız olan tek şey, formülü bir çalışma sayfasına eklemeden bazı Microsoft Excel formüllerine dayalı olarak bu değerlerin sonucunu bulmak.

 Aspose.Cells' formül hesaplama motoru API'lerini aşağıdakiler için kullanabilirsiniz:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) ile[**hesaplamak**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) çalışma sayfasına eklemeden bu tür formüllerin sonuçları:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

Yukarıdaki kod aşağıdaki çıktıyı üretir:
{{< highlight "net" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Formülleri tekrar tekrar hesaplamak**

 Çalışma kitabında çok sayıda formül olduğunda ve kullanıcının bunları yalnızca küçük bir bölümünü değiştirerek tekrar tekrar hesaplaması gerektiğinde, formül hesaplama zincirini etkinleştirmek performans açısından yararlı olabilir:[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **Bilmeniz Önemli**

{{% alert color="primary" %}}

Hesaplama zinciri varsayılan olarak devre dışıdır. Zinciri oluşturmak da ekstra zaman gerektirdiğinden, formülleri ilk kez hesaplarken ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)), zincirsiz hesaplama formülleriyle karşılaştırıldığında daha fazla CPU işlem süresi ve bellek tüketebilir. Kullanıcının formülleri tekrar tekrar hesaplaması gerekmiyorsa, varsayılan davranış (hesaplama zinciri oluşturmadan formülü doğrudan hesaplama) daha iyi bir yol olmalıdır.

{{% /alert %}}


## **ileri konular**
- [Cells'i Microsoft'e ekleyin Excel Formül İzleme Penceresi](/cells/tr/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells kullanarak IFNA işlevini hesaplama](/cells/tr/net/calculating-ifna-function-using-aspose-cells/)
- [Veri Tablolarının Dizi Formülünün Hesaplanması](/cells/tr/net/calculation-of-array-formula-of-data-tables/)
- [Excel 2016 MINIFS ve MAXIFS işlevlerinin hesaplanması](/cells/tr/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Cell'in Hesaplama Süresini azaltın. Hesaplama yöntemi](/cells/tr/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Döngüsel Referans Algılama](/cells/tr/net/detecting-circular-reference/)
- [Bir çalışma sayfasına yazmadan özel işlevin doğrudan hesaplanması](/cells/tr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Aspose.Cells Varsayılan Hesaplama Motorunu genişletmek için Özel Hesaplama Motorunu uygulayın](/cells/tr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Çalışma Kitabının Formül Hesaplamasını Durdurun veya İptal Edin](/cells/tr/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [AbstractCalculationEngine kullanarak bir Değer Aralığı Döndürme](/cells/tr/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [ICustomFunction kullanarak bir Değer Aralığı Döndürme](/cells/tr/net/returning-a-range-of-values-using-icustomfunction/)
- [Çalışma Kitabının Formül Hesaplama Modunu Ayarlama](/cells/tr/net/setting-formula-calculation-mode-of-workbook/)
- [Aspose.Cells'de FormulaText işlevini kullanma](/cells/tr/net/using-formulatext-function-in-aspose-cells/)
- [ICustomFunction Özelliğini Kullanma](/cells/tr/net/using-icustomfunction-feature/)
