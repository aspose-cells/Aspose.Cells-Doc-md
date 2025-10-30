---
title: Golang ile C++ kullanarak Formülleri Hesapla
linktitle: Formülleri Hesapla
description: Bu makale, Golang ile C++ kullanarak Microsoft Excel’de formülleri hesaplamak için Aspose.Cells kütüphanesinin nasıl kullanılacağını anlatmaktadır. Mevcut bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanabilir ve formülü hesaplayabiliriz. Son olarak, değiştirilen Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, formüller, hesaplamalar, Doğrudan Formül Hesaplaması, Formülleri Tekrarlı Hesapla, formül ekleme.
type: docs
weight: 125
url: /tr/go-cpp/calculate-formulas/
---

## **Formüller Ekleyin ve Sonuçlarını Hesaplayın**

Aspose.Cells gömülü bir formül hesaplama motoruna sahiptir. Tasarımcı şablonlarından ithal edilen formülleri tekrar hesaplamanın yanı sıra, çalışma zamanında eklenen formüllerin sonuçlarını da hesaplamayı destekler.

Aspose.Cells, Microsoft Excel'in (desteklenen fonksiyonların listesini [kullanılabilen fonksiyonların listesine göz at](/cells/tr/cpp/supported-formula-functions/)) parçası olan çoğu formülü veya fonksiyonu destekler. Bu fonksiyonlar API'ler veya tasarımcı elektronik tablolar aracılığıyla kullanılabilir. Aspose.Cells, büyük bir matematiksel, dize, mantıksal, tarih/zaman, istatistiksel, veritabanı, arama ve referans formülleri kümesine destek sağlar.

Bir hücreye formül eklemek için [**GetFormula**](https://reference.aspose.com/cells/go-cpp/cell/getformula/) sınıfının [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/) özelliği veya [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) metodunu kullanın. Bir formül uygularken, her zaman Microsoft Excel'de formül oluştururken yaptığınız gibi eşittir (=) ile başlayın ve fonksiyon parametrelerini ayırmak için virgül (,) kullanın.

Formüllerin sonuçlarını hesaplamak için, kullanıcı [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfının [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) yöntemini çağırabilir, bu tüm Excel dosyasına gömülü formülleri işler. Alternatif olarak, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) yöntemini çağırabilir, bu da bir sayfadaki tüm formülleri işler. Ya da, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/) yöntemini çağırabilir, bu da bir Hücre'nin formülünü işler:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas.go" >}}
### **Formüller İçin Bilinmesi Gerekenler**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) sınıfının **GetFormula** özelliği ve **SetFormula(...)** yöntemleri, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) ve [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) sınıflarının **Calculate** yöntemlerinden farklı çalışır. **GetFormula** özelliği ve **SetFormula(...)** yöntemleri, sadece formülü hücreye ekler ancak çalışma zamanında sonucu hesaplamaz. Formüllerin sonucunu almak için lütfen **Calculate** yöntemlerini çağırın.

{{% /alert %}}

## **Formülün Doğrudan Hesaplanması**

Aspose.Cells, gömülü bir formül hesaplama motoruna sahiptir. Bir tasarımcı dosyasından içe aktarılmış formülleri hesaplamanın yanı sıra, Aspose.Cells, formül sonuçlarını doğrudan hesaplamayı da destekler.

B sometimes, doğrudan formül sonuçlarını hesaplamanız gerekebilir, ve bu sonuçları çalışma sayfasına eklemeden de yapabilirsiniz. Formülde kullanılan hücrelerin değerleri zaten bir çalışma sayfasında mevcuttur ve sizin yapmanız gereken, bu değerlerin sonucunu Microsoft Excel formülleri kullanarak bulmaktır, formülü çalışma sayfasına ekmeden.

Aspose.Cells’ın formül hesaplama motoru API’lerini kullanarak, [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) ile [**calculate**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula/) arasındaki formüllerin sonuçlarını, bunları çalışma sayfasına eklemeden alabilirsiniz:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-1.go" >}}
Formülleri Tekrarlı Hesaplamak İçin Nasıl
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Formülleri Tekrar Hesaplama Yöntemleri**

Çok sayıda formül olduğunda ve kullanıcının sadece küçük bir kısmını değiştirerek tekrar tekrar hesaplaması gerekirse, performans için formül hesaplama zincirini etkinleştirmek faydalı olabilir: [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getenablecalculationchain/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-2.go" >}}
### **Bilinmesi Gerekenler**

{{% alert color="primary" %}}

Varsayılan olarak, hesaplama zinciri devre dışıdır. Çünkü zinciri oluşturmak ek zaman gerektirir, formülleri ilk kez ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)) hesaplamak, zincir olmadan hesaplamaya kıyasla daha fazla CPU işlem süresi ve bellek kullanabilir. Kullanıcı formülleri tekrar tekrar hesaplamaya gerek duymuyorsa, varsayılan davranış (hesaplama zinciri oluşturmadan doğrudan formül hesaplama) daha uygun olmalıdır.

{{% /alert %}}

## **Gelişmiş Konular**
- [Microsoft Excel Formül İzleme Penceresine Hücreler Ekleme](/cells/tr/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells ile IFNA işlevinin hesaplanması](/cells/tr/cpp/calculating-ifna-function-using-aspose-cells/)
- [Veri Tablolarının Dizi Formül Hesaplama](/cells/tr/cpp/calculation-of-array-formula-of-data-tables/)
- [Excel 2016 MINIFS ve MAXIFS işlevlerinin hesaplanması](/cells/tr/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Hücre.Calculate yönteminin Hesaplama Süresini Azaltma](/cells/tr/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Özel işlevin çalışma tablosuna yazılmadan doğrudan hesaplanması](/cells/tr/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Aspose.Cells'in Varsayılan Hesaplama Motorunu Genişletmek için Özel Hesaplama Motoru Uygulamak](/cells/tr/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [AbstractCalculationEngine Kullanarak Bir Değer Aralığı Döndürme](/cells/tr/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Çalışma Kitabının Formül Hesaplama Modunu Ayarlama](/cells/tr/cpp/setting-formula-calculation-mode-of-workbook/)
- [Aspose.Cells'te FormulaText Fonksiyonu Kullanma](/cells/tr/cpp/using-formulatext-function-in-aspose-cells/)
