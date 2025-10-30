---
title: AbstractCalculationEngine Özelliği Kullanımı
type: docs
weight: 20
url: /tr/cpp/using-abstractcalculationengine-feature/
---


## **Giriş**
Bu makale, özel fonksiyonları uygulamak için [AbstractCalculationEngine](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) özelliğini nasıl kullanacağınızı anlamınızı sağlar.

AbstractCalculationEngine arayüzü, belirli gereksinimleri karşılamak için Aspose.Cells çekirdek hesaplama motorunu genişletmek amacıyla özel formül hesaplama fonksiyonları eklemenize olanak tanır. Bu özellik, belirli gereksinimleri karşılamak için özel (kullanıcı tanımlı) fonksiyonları tanımlamak ve Aspose.Cells API'lerini kullanarak Aspose.Cells çekirdek hesaplama motoru içinde herhangi diğer varsayılan Microsoft Excel fonksiyonu gibi uygulamak ve değerlendirmek için kullanışlıdır.

## **SoyutHesapMakinesi Özelliği Kullanımı - 1**

Aşağıdaki örnek kod, AbstractCalculationEngine arayüzünü uygular ve A1 ve A2 hücrelerinde yer alan MySampleFunc() ve YourSampleFunc() adlı iki özel fonksiyonun değerlerini değerlendirir ve döndürür. Daha sonra, Workbook.CalculateFormula(const CalculationOptions& options) yöntemini çağırarak AbstractCalculationEngine .Calculate(CalculationData& data) yöntemi uygulanır. Ardından, A1 ve A2'nin değerlerini konsola yazdırır. Daha fazla yardım için lütfen aşağıdaki örnek kodun Konsol Çıkışına bakın.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingAbstractCalculationEngine.cpp" >}}


## **Konsol Çıktısı**
{{< highlight java >}}

MySampleFunc-Test called successfully.
YourSampleFunc-Test called successfully.
Value of A1 is : 1
Value of A2 is : 2

{{< /highlight >}}

## **SoyutHesapMakinesi Özelliği Kullanımı - 2**

Aşağıdaki örnek kod, özel bir fonksiyonun örnek bir dosyadan okunması ve Workbook.CalculateFormula(const CalculationOptions& options) metodunun çağrılarak SoyutHesapMakinesi .Calculate(CalculationData& data) metodunun çağrılmasını gösterir.

Örnek dosya:[sample-file.xlsx](sample-file.xlsx)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingAbstractCalculationEngine2.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
