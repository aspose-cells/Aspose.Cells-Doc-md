---
title: Çıktı HTML ye Yazdırma Alanı Aralığını C++ ile Dışa Aktar
linktitle: Yazdırma Alanı Aralığını HTML ye Dışa Aktar
type: docs
weight: 60
url: /tr/cpp/export-print-area-range-to/
description: Aspose.Cells for C++ kullanarak yazdırma alanı aralığını HTML ye nasıl dışa aktarmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Bu, genellikle tüm sayfa yerine yalnızca yazdırma alanını, yani seçili hücre aralığını HTML'ye dışa aktarmamız gerektiğinde karşılaşılan yaygın bir senaryodur. Bu özellik halihazırda PDF renderlama için kullanılabilir durumda; ancak artık bu işlemi HTML için de gerçekleştirebilirsiniz. İlk olarak, çalışma sayfasının sayfa düzeni nesnesinde yazdırma alanını ayarlayın. Daha sonra, yalnızca seçilen aralığı dışa aktarmak için [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportprintareaonly/) bayrağını kullanın.

## **Örnek Kod**

Aşağıdaki örnek kod, bir çalışma kitabını yükler ve ardından yazdırma alanını HTML'ye dışa aktarır. Bu özelliği test etmek için kullanılacak örnek dosya aşağıdaki bağlantıdan indirilebilir:

[sampleInlineCharts.xlsx](79527946.xlsx)

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleInlineCharts.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputInlineCharts.html";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area
    worksheet.GetPageSetup().SetPrintArea(u"D2:M20");

    // Initialize HtmlSaveOptions
    HtmlSaveOptions options;

    // Set flag to export print area only
    options.SetExportPrintAreaOnly(true);

    // Save to HTML format
    workbook.Save(outputFilePath, options);

    std::cout << "HTML file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
