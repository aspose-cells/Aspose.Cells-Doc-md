---
title: Formülleri Hesaplamanın Yolları
type: docs
weight: 30
url: /tr/cpp/ways-to-calculate-formulas/
---
##  **giriiş**
Aspose.Cells yerleşik bir formül hesaplama motoruna sahiptir. Yalnızca tasarımcı şablonlarından içe aktarılan formülleri yeniden hesaplamakla kalmaz, aynı zamanda çalışma zamanında eklenen formüllerin sonuçlarının hesaplanmasını da destekler.
##  **Formül Ekleme ve Sonuçları Hesaplama**
Aspose.Cells, Microsoft Excel'in parçası olan formüllerin veya işlevlerin çoğunu destekler. API numaralı telefondan veya tasarımcı e-tabloları kullanılarak kullanılabilirler. Aspose.Cells çok sayıda matematik, dize, boole, tarih/saat, istatistiksel, arama ve referans formüllerini destekler.

Hücreye formül eklemek için Cell.SetFormula yöntemini kullanın. Bir hücreye formül uygularken, Microsoft Excel'de formül oluştururken yaptığınız gibi dizeye her zaman eşittir işaretiyle (=) başlayın. İşlev parametrelerini sınırlamak için virgül (,) kullanın.

Formüllerin sonuçlarını hesaplamak için, bir Excel dosyasına katıştırılmış tüm formülleri işleyen Workbook.CalculateFormula() yöntemini çağırın. Lütfen formülü ekleyen ve sonuçlarını hesaplayan aşağıdaki örnek koda bakın. lütfen kontrol ediniz[excel dosyasının çıktısını almak](38109185.xlsx) bu kodla oluşturuldu.

**Basit kod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults-new.cpp" >}}
<!---## **Direct Calculation of Formula**
Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Worksheet.CalculateFormula(String formula) method to calculate the results of such formulas without adding them to worksheet.

The code below produces the following output.

{{< highlight java >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Sample Code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}   --->
##  **Formüllerin Yalnızca Bir Kez Hesaplanması**
Bir çalışma kitabı şablonundaki formüllerin değerlerini hesaplamak için Workbook.CalculateFormula() çağrıldığında, Aspose.Cells bir hesaplama zinciri oluşturur. Formüllerin ikinci veya üçüncü kez hesaplanması performansı artırır.

Bununla birlikte, şablon çok sayıda formül içeriyorsa, formülün ilk kez hesaplanması, çok fazla CPU işlem süresi ve belleği tüketebilir.

Aspose.Cells, formülleri yalnızca bir kez hesaplamak istediğinizde yararlı olan bir hesaplama zinciri oluşturmayı kapatmanıza olanak tanır.

 Lütfen false parametresiyle Workbook.GetISettings().SetCreateCalcChain() öğesini çağırın. Şunu kullanabilirsiniz:[sağlanan excel dosyası](38109186.xlsx) Bu kodu test etmek için.

**Basit kod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly-new.cpp" >}}
