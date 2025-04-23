---
title: C++ ile Konsolidasyon Fonksiyonu
linktitle: Konsolidasyon Fonksiyonu
type: docs
weight: 20
url: /tr/cpp/consolidation-function/
description: Aspose.Cells kullanarak C++ ile bir pivot tablosunun veri alanlarına Konsolidasyon Fonksiyonunu nasıl uygulayacağınızı öğrenin.
---

## **Konsolidasyon fonksiyonu**

Aspose.Cells, Pivot tablosunun veri alanlarına (veya değer alanlarına) KonsolidasyonFonksiyonu uygulamak için kullanılabilir. Microsoft Excel'de, değer alanına sağ tıkladıktan sonra **Değer Alanı Ayarları...** seçeneğini seçebilir ve ardından **Değerleri Nasıl Özetleyeceğinizi Seçin** sekmesini seçebilirsiniz. Oradan, Sum, Count, Average, Max, Min, Product, DistinctCount vb. gibi istediğiniz herhangi bir KonsolidasyonFonksiyonunu seçebilirsiniz.

Aspose.Cells, aşağıdaki konsolidasyon işlevlerini desteklemek için [**ConsolidationFunction**](https://reference.aspose.com/cells/cpp/aspose.cells/consolidationfunction/) numaralı sıralamayı sağlamaktadır.

- ConsolidationFunction::Ortalama
- ConsolidationFunction::Say
- ConsolidationFunction::SayNumaraları
- ConsolidationFunction::FarklıSayım
- ConsolidationFunction::Maksimum
- ConsolidationFunction::Minimum
- ConsolidationFunction::Çarpım
- ConsolidationFunction::StdSapma
- ConsolidationFunction::StdSapp
- ConsolidationFunction::Toplam
- ConsolidationFunction::Varyans
- ConsolidationFunction::Varyansp

### **Döndürme Tablosunun Veri Alanlarına Konsolidasyon İşlevi Uygulama**

Aşağıdaki kod **Ortalama** konsolidasyon fonksiyonunu birinci veri alanına (veya değer alanına) ve ikinci veri alanına (veya değer alanına) **FarklıSayıyıSay** konsolidasyon fonksiyonunu uygular.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table of the worksheet
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Apply Average consolidation function to first data field
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Average);

    // Apply DistinctCount consolidation function to second data field
    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::DistinctCount);

    // Calculate the data to make changes affect
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Farklı Sayı Sayımı konsolidasyon işlevi sadece Microsoft Excel 2013 tarafından desteklenmektedir.

{{% /alert %}}
