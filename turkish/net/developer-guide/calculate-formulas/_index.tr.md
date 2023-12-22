---
title: Formülleri Hesapla
description: Bu makalede, Microsoft Excel'deki formülleri hesaplamak için Aspose.Cells kitaplığının nasıl kullanılacağı anlatılmaktadır. Mevcut bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak Aspose.Cells'in sağladığı yöntemleri kullanarak formülü hesaplayıp sonuca ulaşabiliriz. Son olarak değiştirdiğimiz Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, formulas, calculations, Direct Calculation of Formula, Calculate Formulas repeatedly, add formulas.
type: docs
weight: 125
url: /tr/net/calculate-formulas/
---
##  **Formül Ekleme ve Sonuçları Hesaplama**

Aspose.Cells yerleşik bir formül hesaplama motoruna sahiptir. Yalnızca tasarımcı şablonlarından içe aktarılan formülleri yeniden hesaplamakla kalmaz, aynı zamanda çalışma zamanında eklenen formüllerin sonuçlarının hesaplanmasını da destekler.

 Aspose.Cells, Microsoft Excel'in parçası olan formüllerin veya işlevlerin çoğunu destekler(Oku[hesaplama motoru tarafından desteklenen işlevlerin listesi](/cells/tr/net/supported-formula-functions/)). Bu işlevler API'ler veya tasarımcı elektronik tabloları aracılığıyla kullanılabilir. Aspose.Cells çok sayıda matematik, dize, boole, tarih/saat, istatistik, veritabanı, arama ve referans formüllerini destekler.

 Kullan[**Formül**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) mülk veya[**Formülü Ayarla(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) yöntemleri[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Hücreye formül eklemek için sınıf. Formül uygularken, Microsoft Excel'de formül oluştururken yaptığınız gibi dizeye her zaman eşittir işaretiyle (=) başlayın ve işlev parametrelerini sınırlamak için virgül (,) kullanın.

 Formüllerin sonuçlarını hesaplamak için kullanıcı[**HesaplaFormül**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) yöntemi[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Bir Excel dosyasına gömülü tüm formülleri işleyen sınıf. Veya kullanıcı arayabilir[**HesaplaFormül**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) yöntemi[**Çalışma sayfası**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Bir sayfaya gömülü tüm formülleri işleyen sınıf. Veya kullanıcı ayrıca[**Hesaplamak**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) yöntemi[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Cell'in formülünü işleyen sınıf:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

###  **Formüller İçin Bilinmesi Gereken Önemli**

{{% alert color="primary" %}}

**Formül** mülkiyet ve**Formülü Ayarla(...)** yöntemleri[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf çalışması diğerlerinden farklı**Hesaplamak** yöntemleri[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Ve[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıflar.**Formül** mülkiyet ve**Formülü Ayarla(...)** yöntemler yalnızca formülü bir hücreye ekler ancak çalışma zamanında sonucu hesaplamaz. Formüllerin sonucunu öğrenmek için lütfen arayınız.**Hesaplamak** yöntemler.

{{% /alert %}}

##  **Formülün Doğrudan Hesaplanması**

Aspose.Cells yerleşik bir formül hesaplama motoruna sahiptir. Aspose.Cells, bir tasarımcı dosyasından içe aktarılan formülleri hesaplamanın yanı sıra formül sonuçlarını da doğrudan hesaplayabilir.

Bazen formül sonuçlarını bir çalışma sayfasına eklemeden doğrudan hesaplamanız gerekir. Formülde kullanılan hücrelerin değerleri bir çalışma sayfasında zaten mevcuttur ve ihtiyacınız olan tek şey, formülü bir çalışma sayfasına eklemeden Microsoft Excel formülüne dayalı olarak bu değerlerin sonucunu bulmaktır.

 Aspose.Cells' formül hesaplama motoru API'lerini aşağıdakiler için kullanabilirsiniz:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) ile[**hesaplamak**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) bu tür formüllerin sonuçlarını çalışma sayfasına eklemeden:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

Yukarıdaki kod aşağıdaki çıktıyı üretir:
{{< highlight "net" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

##  **Formüller Tekrar tekrar Nasıl Hesaplanır?**

Çalışma kitabında çok sayıda formül olduğunda ve kullanıcının yalnızca küçük bir kısmını değiştirerek bunları tekrar tekrar hesaplaması gerektiğinde, formül hesaplama zincirini etkinleştirmek performans açısından faydalı olabilir:[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

###  **Bilmeniz Önemli**

{{% alert color="primary" %}}

Varsayılan olarak hesaplama zinciri devre dışıdır. Zinciri oluşturmak da fazladan zaman gerektirdiğinden, formüllerin ilk kez hesaplanması ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)), zincirsiz formüllerin hesaplanmasıyla karşılaştırıldığında daha fazla CPU işlem süresi ve belleği tüketebilir. Kullanıcının formülleri tekrar tekrar hesaplaması gerekmiyorsa, varsayılan davranış (hesaplama zinciri oluşturmadan formülün doğrudan hesaplanması) daha iyi bir yol olmalıdır.

{{% /alert %}}


##  **İleri konular**
- [Cells'i Microsoft'e ekleyin Excel Formül İzleme Penceresi](/cells/tr/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells'i kullanarak IFNA işlevini hesaplama](/cells/tr/net/calculating-ifna-function-using-aspose-cells/)
- [Veri Tablolarının Dizi Formülünün Hesaplanması](/cells/tr/net/calculation-of-array-formula-of-data-tables/)
- [Excel 2016 MINIFS ve MAXIFS fonksiyonlarının hesaplanması](/cells/tr/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Cell'in Hesaplama Süresini azaltın. Hesaplama yöntemi](/cells/tr/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Dairesel Referansı Algılama](/cells/tr/net/detecting-circular-reference/)
- [Özel işlevin çalışma sayfasına yazmadan doğrudan hesaplanması](/cells/tr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Aspose.Cells Varsayılan Hesaplama Motorunu genişletmek için Özel Hesaplama Motorunu uygulayın](/cells/tr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Çalışma Kitabının Formül Hesaplamasını Durdurun veya İptal Edin](/cells/tr/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [AbstractCalculationEngine kullanarak bir Değer Aralığı Döndürme](/cells/tr/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [ICustomFunction kullanarak bir Değer Aralığı Döndürme](/cells/tr/net/returning-a-range-of-values-using-icustomfunction/)
- [Çalışma Kitabının Formül Hesaplama Modunu Ayarlama](/cells/tr/net/setting-formula-calculation-mode-of-workbook/)
- [Aspose.Cells'de FormulaText işlevini kullanma](/cells/tr/net/using-formulatext-function-in-aspose-cells/)
- [ICustomFunction Özelliğini Kullanma](/cells/tr/net/using-icustomfunction-feature/)
