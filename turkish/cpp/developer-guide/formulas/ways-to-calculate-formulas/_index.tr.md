---
title: Formülleri Hesaplama Yolları
type: docs
weight: 30
url: /tr/cpp/ways-to-calculate-formulas/
---
## **giriiş**
Aspose.Cells yerleşik bir formül hesaplama motoruna sahiptir. Yalnızca tasarımcı şablonlarından içe aktarılan formülleri yeniden hesaplamakla kalmaz, aynı zamanda çalışma zamanında eklenen formüllerin sonuçlarının hesaplanmasını da destekler.
## **Formül Ekleme ve Sonuçları Hesaplama**
Aspose.Cells, Microsoft Excel'in parçası olan formüllerin veya işlevlerin çoğunu destekler. API aracılığıyla veya tasarımcı elektronik tabloları kullanılarak kullanılabilirler. Aspose.Cells, çok sayıda matematiksel, dizi, boole, tarih/saat, istatistik, arama ve referans formüllerini destekler.

Bir hücreye formül eklemek için Cell.Formula yöntemini kullanın. Bir hücreye formül uygularken, Microsoft Excel'de formül oluştururken yaptığınız gibi dizeye her zaman eşittir işaretiyle (=) başlayın. İşlev parametrelerini ayırmak için virgül (,) kullanın.

Formüllerin sonuçlarını hesaplamak için, bir Excel dosyasına katıştırılmış tüm formülleri işleyen Workbook.CalculateFormula() yöntemini çağırın. Lütfen formülü ekleyen ve sonuçlarını hesaplayan aşağıdaki örnek koda bakın. lütfen kontrol ediniz[çıktı excel dosyası](38109185.xlsx) bu kod ile oluşturulmuştur.

**Basit kod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults.cpp" >}}
## **Formülün Doğrudan Hesaplanması**
Bazen, formül sonuçlarını bir çalışma sayfasına eklemeden doğrudan hesaplamanız gerekir. Formülde kullanılan hücrelerin değerleri bir çalışma sayfasında zaten var ve ihtiyacınız olan tek şey, formülü bir çalışma sayfasına eklemeden bazı Microsoft Excel formüllerine dayalı olarak bu değerlerin sonucunu bulmak.

Bu tür formüllerin sonuçlarını çalışma sayfasına eklemeden hesaplamak için Worksheet.CalculateFormula(String formula) yöntemini kullanabilirsiniz.

Aşağıdaki kod aşağıdaki çıktıyı üretir.

{{< highlight "java" >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Basit kod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}
## **Formülleri Yalnızca Bir Kez Hesaplama**
Bir çalışma kitabı şablonundaki formüllerin değerlerini hesaplamak için Workbook.CalculateFormula() çağrıldığında, Aspose.Cells bir hesaplama zinciri oluşturur. Formüller ikinci veya üçüncü kez hesaplandığında performansı artırır.

Bununla birlikte, şablon çok sayıda formül içeriyorsa, formülün ilk kez hesaplanması çok fazla CPU işlem süresi ve bellek tüketebilir.

Aspose.Cells, formülleri yalnızca bir kez hesaplamak istediğinizde kullanışlı olan bir hesaplama zinciri oluşturmayı kapatmanıza olanak tanır.

 Lütfen Workbook.GetISettings().SetCreateCalcChain() öğesini false parametresiyle çağırın. kullanabilirsiniz[sağlanan excel dosyası](38109186.xlsx) Bu kodu test etmek için.

**Basit kod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly.cpp" >}}
