---
title: Formülleri Hesapla
description: Bu makale, Aspose.Cells kütüphanesini kullanarak Microsoft Excel de formülleri hesaplamayı nasıl yapacağınızı tanıtır. Varolan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanarak formülü hesaplayabilir ve sonucu alabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, formüller, hesaplamalar, Doğrudan Formül Hesaplaması, Formülleri Tekrarlı Hesapla, formül ekleme.
type: docs
weight: 125
url: /tr/net/calculate-formulas/
---

## **Formüller Ekleyin ve Sonuçlarını Hesaplayın**

Aspose.Cells, yerleşik bir formül hesaplama motoruna sahiptir. Sadece tasarımcı şablonlarından içe aktarılan formülleri yeniden hesaplayabileceği gibi, çalışma zamanında eklenen formül sonuçlarını da hesaplama desteği sağlar.

Aspose.Cells, Microsoft Excel'in bir parçası olan çoğu formül veya işlevi destekler (Okumak için [hesaplama motoru tarafından desteklenen fonksiyonların listesi](/cells/tr/net/supported-formula-functions/)). Bu işlevler API'ler veya tasarımcı elektronik tablolar aracılığıyla kullanılabilir. Aspose.Cells, matematiksel, dize, mantıksal, tarih/saat, istatistiksel, veritabanı, arama ve referans formüllerinin büyük bir setini destekler.

Bir hücreye formül eklemek için [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) özelliğini veya [**SetFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) yöntemlerini kullanın. Bir formül uygularken, her zaman bir eşittir işareti ile ( = ) başlayın, Microsoft Excel'de bir formül oluştururken yaptığınız gibi ve bir virgül ( , ) kullanarak fonksiyon parametrelerini sınırlayın.

Formüllerin sonuçlarını hesaplamak için, kullanıcı, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) yöntemini çağırabilir, bir Excel dosyasına gömülü olan tüm formülleri işleyen. Veya, kullanıcı, [**Worsheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) yöntemini çağırabilir, bir sayfaya gömülü olan tüm formülleri işleyen. Ya da, kullanıcı, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının [**Calculate**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) yöntemini çağırabilir, bir Hücrenin formülünü işleyen:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **Formüller İçin Bilinmesi Gerekenler**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının **Formül** özelliği ve **SetFormula(...)** yöntemleri, **[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) ve [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)** sınıflarının **Hesapla** yöntemlerinden farklı çalışır. **Formül** özelliği ve **SetFormula(...)** yöntemleri, sadece bir formülü bir hücreye ekler ancak çalışma zamanında sonucu hesaplamaz. Formüllerin sonucunu elde etmek için lütfen **Hesapla** yöntemlerini çağırın.

{{% /alert %}}

## **Formülün Doğrudan Hesaplanması**

Aspose.Cells, gömülü bir formül hesaplama motoruna sahiptir. Bir tasarımcı dosyasından içe aktarılmış formülleri hesaplamanın yanı sıra, Aspose.Cells, formül sonuçlarını doğrudan hesaplamayı da destekler.

Bazen, bir elektronik tabloya formül eklemadan, formülde kullanılan hücre değerlerinin sonuçlarını, Microsoft Excel formülüne dayalı olarak bulmanız gerekebilir. Formülde kullanılan hücrelerin değerleri zaten bir elektronik tabloda mevcutsa ve ihtiyacınız olan tek şey bir elektronik tabloya formül eklemek değilse, Aspose.Cells'in formül hesaplama motoru API'lerini kullanarak bu tür formüllerin sonuçlarını {0} için {1} hesaplayabilirsiniz.

Yukarıdaki kod aşağıdaki çıktıyı üretir:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

Formülleri Tekrarlı Hesaplamak İçin Nasıl
{{< highlight net >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Formülleri tekrar tekrar hesaplama**

Çalışma kitabında çok sayıda formül bulunduğunda ve kullanıcının bunların bir kısmını tekrarlanacak şekilde sık sık hesaplaması gerektiğinde, formül hesaplama zincirini etkinleştirmek, yalnızca bir elektronik tablo kısmını değiştirerek tekrarlamak için formül hesaplama zincirini etkinleştirmek performans için yararlı olabilir: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **Bilinmesi Gerekenler**

{{% alert color="primary" %}}

Varsayılan olarak hesaplama zinciri devre dışıdır. Zinciri oluşturmak da ekstra zaman gerektirdiğinden, formülleri hesaplamanın ilk kez yapılması ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) zincir oluşturmadan formülleri hesaplama ile karşılaştırıldığında daha fazla CPU işleme zamanı ve bellek tüketebilir. Kullanıcı formülleri tekrar tekrar hesaplamak istemiyorsa, varsayılan davranış (hesaplama zinciri oluşturmadan doğrudan formül hesaplama) daha iyi bir yol olmalıdır.

{{% /alert %}}


## **Gelişmiş Konular**
- [Microsoft Excel Formül İzleme Penceresine Hücreler Ekleme](/cells/tr/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells ile IFNA işlevinin hesaplanması](/cells/tr/net/calculating-ifna-function-using-aspose-cells/)
- [Veri Tablolarının Dizi Formül Hesaplama](/cells/tr/net/calculation-of-array-formula-of-data-tables/)
- [Excel 2016 MINIFS ve MAXIFS işlevlerinin hesaplanması](/cells/tr/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Hücre.Calculate yönteminin Hesaplama Süresini Azaltma](/cells/tr/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Dairesel Referansı Algılama](/cells/tr/net/detecting-circular-reference/)
- [Özel işlevin çalışma tablosuna yazılmadan doğrudan hesaplanması](/cells/tr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Aspose.Cells'in Varsayılan Hesaplama Motorunu Genişletmek için Özel Hesaplama Motoru Uygulamak](/cells/tr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Çalışma Kitabının Formül Hesaplamasını Kesmek veya İptal Etmek](/cells/tr/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [AbstractCalculationEngine Kullanarak Bir Değer Aralığı Döndürme](/cells/tr/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [ICustomFunction Kullanarak Bir Değer Aralığı Döndürme](/cells/tr/net/returning-a-range-of-values-using-icustomfunction/)
- [Çalışma Kitabının Formül Hesaplama Modunu Ayarlama](/cells/tr/net/setting-formula-calculation-mode-of-workbook/)
- [Aspose.Cells'te FormulaText Fonksiyonu Kullanma](/cells/tr/net/using-formulatext-function-in-aspose-cells/)
- [ICustomFunction Özelliğinin Kullanımı](/cells/tr/net/using-icustomfunction-feature/)
{{< app/cells/assistant language="csharp" >}}
