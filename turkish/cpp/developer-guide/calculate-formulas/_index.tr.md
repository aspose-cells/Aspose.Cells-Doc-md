---
title: Formülleri C++ ile Hesapla
linktitle: Formülleri Hesapla
description: Bu makale, Aspose.Cells kütüphanesini kullanarak Microsoft Excel de formülleri C++ ile nasıl hesaplayacağınızı anlatmaktadır. Varolan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanarak formülü hesaplayabilir ve sonucu alabilirsiniz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, formüller, hesaplamalar, Doğrudan Formül Hesaplaması, Formülleri Tekrarlı Hesapla, formül ekleme.
type: docs
weight: 125
url: /tr/cpp/calculate-formulas/
---

## **Formüller Ekleyin ve Sonuçlarını Hesaplayın**

Aspose.Cells gömülü bir formül hesaplama motoruna sahiptir. Tasarımcı şablonlarından ithal edilen formülleri tekrar hesaplamanın yanı sıra, çalışma zamanında eklenen formüllerin sonuçlarını da hesaplamayı destekler.

Aspose.Cells, Microsoft Excel'in (desteklenen fonksiyonların listesini [kullanılabilen fonksiyonların listesine göz at](/cells/tr/cpp/supported-formula-functions/)) parçası olan çoğu formülü veya fonksiyonu destekler. Bu fonksiyonlar API'ler veya tasarımcı elektronik tablolar aracılığıyla kullanılabilir. Aspose.Cells, büyük bir matematiksel, dize, mantıksal, tarih/zaman, istatistiksel, veritabanı, arama ve referans formülleri kümesine destek sağlar.

Bir hücreye formül eklemek için [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/) sınıfının [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/) özelliği veya [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) metodunu kullanın. Bir formül uygularken, her zaman Microsoft Excel'de formül oluştururken yaptığınız gibi eşittir (=) ile başlayın ve fonksiyon parametrelerini ayırmak için virgül (,) kullanın.

Formüllerin sonuçlarını hesaplamak için, kullanıcı [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfının [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) yöntemini çağırabilir, bu tüm Excel dosyasına gömülü formülleri işler. Alternatif olarak, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) yöntemini çağırabilir, bu da bir sayfadaki tüm formülleri işler. Ya da, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/) yöntemini çağırabilir, bu da bir Hücre'nin formülünü işler:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add values to cells
    worksheet.GetCells().Get(u"A1").PutValue(1);
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(3);

    // Add a SUM formula to cell A4
    worksheet.GetCells().Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Calculate the results of formulas
    workbook.CalculateFormula();

    // Get the calculated value of cell A4
    U16String value = worksheet.GetCells().Get(u"A4").GetStringValue();

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Formüller İçin Bilinmesi Gerekenler**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının **GetFormula** özelliği ve **SetFormula(...)** yöntemleri, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) ve [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıflarının **Calculate** yöntemlerinden farklı çalışır. **GetFormula** özelliği ve **SetFormula(...)** yöntemleri, sadece formülü hücreye ekler ancak çalışma zamanında sonucu hesaplamaz. Formüllerin sonucunu almak için lütfen **Calculate** yöntemlerini çağırın.

{{% /alert %}}

## **Formülün Doğrudan Hesaplanması**

Aspose.Cells, gömülü bir formül hesaplama motoruna sahiptir. Bir tasarımcı dosyasından içe aktarılmış formülleri hesaplamanın yanı sıra, Aspose.Cells, formül sonuçlarını doğrudan hesaplamayı da destekler.

B sometimes, doğrudan formül sonuçlarını hesaplamanız gerekebilir, ve bu sonuçları çalışma sayfasına eklemeden de yapabilirsiniz. Formülde kullanılan hücrelerin değerleri zaten bir çalışma sayfasında mevcuttur ve sizin yapmanız gereken, bu değerlerin sonucunu Microsoft Excel formülleri kullanarak bulmaktır, formülü çalışma sayfasına ekmeden.

Aspose.Cells’ın formül hesaplama motoru API’lerini kullanarak, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) ile [**calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) arasındaki formüllerin sonuçlarını, bunları çalışma sayfasına eklemeden alabilirsiniz:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put 20 in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.PutValue(20);

    // Put 30 in cell A2
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.PutValue(30);

    // Calculate the Sum of A1 and A2
    Aspose::Cells::Object results = worksheet.CalculateFormula(u"=Sum(A1:A2)");

    // Print the output
    std::cout << "Value of A1: " << cellA1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Value of A2: " << cellA2.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Result of Sum(A1:A2): " << results.ToString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

Formülleri Tekrarlı Hesaplamak İçin Nasıl
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Formülleri Tekrar Hesaplama Yöntemleri**

Çok sayıda formül olduğunda ve kullanıcının sadece küçük bir kısmını değiştirerek tekrar tekrar hesaplaması gerekirse, performans için formül hesaplama zincirini etkinleştirmek faydalı olabilir: [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/getenablecalculationchain/).

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the template workbook
    Workbook workbook(srcDir + u"book1.xls");

    // Print the time before formula calculation
    auto start = std::chrono::system_clock::now();
    std::time_t start_time = std::chrono::system_clock::to_time_t(start);
    std::cout << "Start time: " << std::ctime(&start_time);

    // Set the CreateCalcChain as true
    workbook.GetSettings().GetFormulaSettings().SetEnableCalculationChain(true);

    // Calculate the workbook formulas
    workbook.CalculateFormula();

    // Print the time after formula calculation
    auto end = std::chrono::system_clock::now();
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);
    std::cout << "End time: " << std::ctime(&end_time);

    // Change the value of one cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"newvalue");

    // Re-calculate those formulas which depend on cell A1
    workbook.CalculateFormula();

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Bilinmesi Gerekenler**

{{% alert color="primary" %}}

Varsayılan olarak, hesaplama zinciri devre dışıdır. Çünkü zinciri oluşturmak ek zaman gerektirir, formülleri ilk kez ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)) hesaplamak, zincir olmadan hesaplamaya kıyasla daha fazla CPU işlem süresi ve bellek kullanabilir. Kullanıcı formülleri tekrar tekrar hesaplamaya gerek duymuyorsa, varsayılan davranış (hesaplama zinciri oluşturmadan doğrudan formül hesaplama) daha uygun olmalıdır.

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
{{< app/cells/assistant language="cpp" >}}
