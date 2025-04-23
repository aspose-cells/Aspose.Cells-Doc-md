---
title: Formüller Hesaplama Yolları
type: docs
weight: 30
url: /tr/go-cpp/ways-to-calculate-formulas/
---

## **Giriş**

Aspose.Cells, gömülü bir formül hesaplama motoruna sahiptir. Sadece tasarımcı şablonlarından alınan formülleri yeniden hesaplamakla kalmaz, aynı zamanda çalışma zamanında eklenen formüllerin sonuçlarını hesaplama konusunda da destek sağlar.

## **Formüller Ekleyin ve Sonuçlarını Hesaplayın**

Aspose.Cells, Microsoft Excel'in bir parçası olan çoğu formül veya işlevi destekler. Bunlar API aracılığıyla veya tasarımcı elektronik tabloları kullanarak kullanılabilir. Aspose.Cells, matematiksel, dize, mantıksal, tarih/saat, istatistiksel, arama ve başvuru formüllerinin geniş bir kümesini destekler.

Bir hücreye formül eklemek için Cell.SetFormula yöntemini kullanın. Bir hücreye formül uygularken, formülü her zaman bir eşitlik işareti (=) ile başlatın, Microsoft Excel'de formül oluştururken yaptığınız gibi. Bir virgül (,) kullanarak işlev parametrelerini ayırın.

Formüllerin sonuçlarını hesaplamak için Workbook.CalculateFormula() yöntemini çağırın, bu yöntem bir Excel dosyasına gömülü tüm formülleri işler. Lütfen bu kod ile oluşturulan [çıktı excel dosyasını](38109185.xlsx) kontrol edin.

**Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingFormulasAndCalculatingResults.go" >}}

## **Formülleri Yalnızca Bir Kez Hesaplayın**

Workbook.CalculateFormula() çağrıldığında, Aspose.Cells, bir hesaplama zinciri oluşturur. Bu, formüller ikinci veya üçüncü kez hesaplandığında performansı artırır.

Ancak, eğer şablon çok sayıda formül içeriyorsa, formülün ilk kez hesaplanması, çok miktarda CPU işlem zamanı ve bellek tüketebilir.

Aspose.Cells, formüllerin yalnızca bir kez hesaplanmak istendiğinde yararlı olan bir hesaplama zinciri oluşturmayı kapatmanıza olanak tanır.

Lütfen Workbook.GetISettings().SetCreateCalcChain() yöntemini false parametre ile çağırın. Bu kodu test etmek için [sunulan excel dosyasını](38109186.xlsx) kullanabilirsiniz.

**Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculatingFormulasOnceOnly.go" >}}
