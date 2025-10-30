---
title: GridLines ile Excel i HTML ye Dışa Aktar ve C++ ile
linktitle: Excel den HTML e Grid Çizgileri ile Dışa Aktar
type: docs
weight: 40
url: /tr/cpp/export-excel-to-html-with-gridlines/
description: Aspose.Cells for C++ kullanarak ızgaralar ile Excel dosyalarını HTML ye dışa aktarmayı öğrenin.
---

{{% alert color="primary" %}} 

HTML'ye GridLines ile Excel dosyasını dışa aktarmak istiyorsanız, lütfen [HtmlSaveOptions.GetExportGridLines()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportgridlines/) özelliğini kullanın ve **true** olarak ayarlayın.

{{% /alert %}} 

## **Excel'den HTML'e Grid Çizgileri ile Dışa Aktar**
Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve çalışma sayfasını bazı değerlerle doldurur, ardından [HtmlSaveOptions.GetExportGridLines()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportgridlines/) ayarlarını **true** olarak ayarlayarak HTML formatında kaydeder.

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

    // Create workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Fill worksheet with some integer values
    for (int r = 0; r < 10; r++)
    {
        for (int c = 0; c < 10; c++)
        {
            ws.GetCells().Get(r, c).PutValue(r * 1);
        }
    }

    // Save workbook in HTML format and export gridlines
    HtmlSaveOptions opts;
    opts.SetExportGridLines(true);
    wb.Save(outDir + u"ExportToHTMLWithGridLines_out.html", opts);

    std::cout << "Workbook exported to HTML with gridlines successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
