---
title: C++ ile HTML ye Kaydederken Gizli Çalışma Sayfası İçeriğinin Dışa Aktarılmasını Engelle
linktitle: Gizli Çalışma Sayfası İçeriğinin Dışa Aktarılmasını Önle
type: docs
weight: 210
url: /tr/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Aspose.Cells for C++ kullanarak Excel çalışma kitablarını HTML ye kaydederken gizli çalışma sayfası içeriğinin dışa aktarımını engellemeyi öğrenin.
---

{{% alert color="primary" %}}

Excel çalışma kitaplarını HTML olarak kaydedebilirsiniz. Ancak, çalışma kitabı gizli çalışma sayfalarını içeriyorsa, Aspose.Cells varsayılan olarak gizli çalışma sayfası içeriğini (_files) dizinine dışa aktarır. Bu dizin, çalışma sayfaları, resimler, tabstrip.htm, stylesheet.css gibi dosyalar içerir. Bazı durumlarda, gizli çalışma sayfalarının bu şekilde içeriğinin dışa aktarılması uygun olmayabilir. Örneğin, gizli çalışma sayfası dışa aktarılmaması gereken resimler içeriyorsa.

{{% /alert %}}

Aspose.Cells, [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexporthiddenworksheet/) özelliğini sağlar. Varsayılan olarak **true** olarak ayarlanmıştır ve gizli çalışma sayfaları HTML'e dışa aktarılır. Eğer **false** olarak ayarlarsanız, Aspose.Cells gizli çalışma sayfa içeriğini dışa aktarmaz.

```c++
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
    U16String inputFilePath = srcDir + u"WorkbookWithHiddenContent.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"HtmlWithoutHiddenContent_out.html";

    // Create workbook object
    Workbook workbook(inputFilePath);

    // Create HTML save options
    HtmlSaveOptions options;

    // Do not export hidden worksheet contents
    options.SetExportHiddenWorksheet(false);

    // Save the workbook
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully without hidden content!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
