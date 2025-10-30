---
title: C++ kullanarak Excel den HTML ye Dönüşümde Belge Çalışma Kitabı ve Çalışma Sayfası Özelliklerini Dışa Aktar
linktitle: Excel den HTML ye Dönüştürme sırasında Belge Çalışma Kitabı ve Çalışma Sayfası Özelliklerini İhraç Et
type: docs
weight: 50
url: /tr/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını HTML ye dönüştürürken Belge, Çalışma Kitabı ve Çalışma Sayfası özelliklerini dışa aktarmayı veya aktarmamayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Bir Microsoft Excel dosyası, Microsoft Excel veya Aspose.Cells kullanılarak HTML'ye aktarıldığında, aşağıdaki ekran görüntüsünde gösterildiği gibi çeşitli Belge, Çalışma Kitabı ve Çalışma Sayfası özellikleri de dışa aktarılır. Bu özellikleri dışa aktarmamayı sağlayabilirsiniz; [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportdocumentproperties/), [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/) ve [**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) değerlerini **false** olarak ayarlayarak. Bu özelliklerin varsayılan değeri **true**'dur. Aşağıdaki ekran görüntüsü, bu özelliklerin dışa aktarılan HTML'de nasıl göründüğünü gösterir.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Excel'de HTML'ye Belge, Çalışma Kitabı ve Çalışma Sayfası Özellikleri Dışa Aktarma**

Aşağıdaki örnek kod, [örnek Excel dosyasını](61767776.xlsx) yükler ve Belge, Çalışma Kitabı ve Çalışma Sayfası özelliklerini dışa aktarmadan HTML'ye dönüştürür [çıktı HTML'si](61767779.zip).

## **Örnek Kod**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html";

    // Load the sample Excel file
    Workbook workbook(inputFilePath);

    // Specify Html Save Options
    HtmlSaveOptions options;

    // We do not want to export document, workbook and worksheet properties
    options.SetExportDocumentProperties(false);
    options.SetExportWorkbookProperties(false);
    options.SetExportWorksheetProperties(false);

    // Export the Excel file to Html with Html Save Options
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file exported to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
