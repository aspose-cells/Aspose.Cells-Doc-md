---
title: Çalışma Sayfasından Senaryolar Oluşturun, Değiştirin veya Silin ve C++ ile Yönetin
linktitle: Senaryoları Yönetme
type: docs
weight: 190
url: /tr/cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Bu makalede, Aspose.Cells API ile C++ Kütüphanesini kullanarak Excel Çalışma Sayfalarından senaryolar nasıl oluşturulacağı, düzenleneceği veya kaldırılacağı anlatılacaktır.
keywords: çalışma sayfası senaryosu oluştur c++, çalışma sayfası senaryosunu kaldır c++, senaryo çalışma sayfasını düzenle c++
---

{{% alert color="primary" %}}

Bazen Elektronik Tablolarda senaryolar oluşturmanızı, manipüle etmenizi veya silmenizi gerekebilir. Senaryo, bir veya daha fazla formülle bağlı değişken giriş hücrelerini içeren adlandırılmış 'ne olurdu?' modelidir. Bir senaryo oluşturmadan önce, farklı değerlerin eklenebileceği en az bir formül içeren çalışma sayfasını tasarlayın. Aşağıdaki örnek, Aspose.Cells API'leri aracılığıyla bir iş kitabındaki bir çalışma sayfasından senaryolar oluşturmayı ve kaldırmayı gösterir.

{{% /alert %}}

Aspose.Cells, bazı kullanışlı sınıflar sağlar, örneğin [**ScenarioCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenariocollection/), [**Scenario**](https://reference.aspose.com/cells/cpp/aspose.cells/scenario/), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcellcollection/) ve [**ScenarioInputCell**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcell/) sınıfları. Ayrıca [**Worksheet.GetScenarios()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getscenarios/) özelliği de mevcuttur. Aşağıdaki örnek kod, bazı senaryolar içeren bir XLSX Excel dosyasını açar ve mevcut bir senaryoyu kaldırır. Ayrıca, Excel dosyasını kaydetmeden önce çalışma sayfasına yeni bir senaryo ekler. Bu örnek, çok basit bir şablon dosyası kullanır ve içinde bir senaryo bulunur.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load input Excel file
    Workbook workbook(srcDir + u"aspose-sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access scenarios collection
    ScenarioCollection scenarios = worksheet.GetScenarios();
    if (scenarios.GetCount() > 0)
    {
        // Create new scenario and configure
        int32_t scenarioIndex = scenarios.Add(u"MyScenario");
        Scenario scenario = scenarios.Get(scenarioIndex);
        scenario.SetComment(u"Test scenario is created.");

        // Add input cell to scenario
        ScenarioInputCellCollection inputCells = scenario.GetInputCells();
        inputCells.Add(3, 1, u"1100000"); // Cell B4 (0-based)

        // Save modified workbook
        U16String outputPath = outDir + u"outBk_scenarios1.out.xlsx";
        workbook.Save(outputPath);

        std::cout << "\nProcess completed successfully.\nFile saved at " << outputPath.ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
