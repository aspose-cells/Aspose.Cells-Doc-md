---
title: Excel dosyası yüklerken VBA Projesini filtreleme (Meta) verilerinin yüklenmesi sırasında Aspose.Cells kullanarak nasıl filtreleneceğini öğrenin.
linktitle: Çalışma kitabı yüklenirken VBA Projesini filtrele
type: docs
weight: 140
url: /tr/cpp/filter-vba-project-while-loading-a-workbook/
description: Aspose.Cells kullanarak Excel dosyası yüklerken VBA projelerini nasıl filtreleyeceğinizi öğrenin.
---

## **Excel dosyası yüklerken VBA Projesini C++ ile filtreleme**

Bazı .xlsm/.xlsb dosyalarında aşırı büyük makrolar (veya çok uzun makrolar) bulunabilir. Aspose.Cells, bu tür çalışma kitapları açılırken bu (meta) verileri kayıtsız şartsız yükler. Ancak, yalnızca çok sayıda çalışma sayfası ismi çıkarmak istiyorsanız, ve bu gereksiz içeriği atlamak istiyorsanız, bu filtreyi [**LoadDataFilterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions) kullanarak kontrol edebilirsiniz. Bu yeni seçenek, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions) ile eklenmiştir.

## **Örnek Kod**

Aşağıdaki örnek kod, yalnızca VBA'nın filtrelenerek bir çalışma kitabı yükler. Bu özelliği test etmek için kullanılabilecek bir örnek dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Set the load options, we do not want to load VBA
    LoadOptions loadOptions(LoadFormat::Auto);
    LoadFilter loadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::VBA);
    loadOptions.SetLoadFilter(&loadFilter);

    // Create workbook object from sample excel file using load options
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleMacroEnabledWorkbook.xlsm";
    Workbook book(inputFilePath, loadOptions);

    // Save the output in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    U16String outputFilePath = outputDir + u"OutputSampleMacroEnabledWorkbook.xlsm";
    book.Save(outputFilePath, SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
