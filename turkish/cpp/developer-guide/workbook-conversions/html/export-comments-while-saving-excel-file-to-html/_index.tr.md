--- 
title: Excel dosyasını HTML ye kaydederken Yorumları Dışa Aktar C++ ile 
linktitle: Excel Dosyasını HTML ye Kaydederken Yorumları Dışa Aktar 
type: docs 
weight: 40 
url: /tr/cpp/export-comments-while-saving-excel-file-to/ 
description: Aspose.Cells kullanarak C++ ile Excel dosyalarını HTML ye kaydederken yorumları dışa aktarmayı öğrenin. 
--- 

## **Olası Kullanım Senaryoları**

Excel dosyanızı HTML'ye kaydederken yorumlar dışa aktarılmaz. Ancak, Aspose.Cells bu özelliği [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/) özelliği kullanarak sağlar. Bunu **true** olarak ayarlarsanız, HTML, Excel dosyanızdaki yorumları da gösterecektir.

## **Excel Dosyasını HTML'ye Kaydederken Yorumları Dışa Aktar**

Aşağıdaki örnek kod, [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/) özelliğinin kullanımını açıklar. Kodun etkisinin gösterildiği ekran görüntüsü, **true** ayarlandığında HTML üzerindedir. Referans olarak, lütfen [örnek Excel dosyasını](50528260.xlsx) ve [üretilen HTML'yi](5052826.txt) indirin.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleExportCommentsHTML.xlsx";
    Workbook workbook(inputFilePath);

    // Export comments - set IsExportComments property to true
    HtmlSaveOptions opts;
    opts.SetIsExportComments(true);

    // Save the Excel file to HTML
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outputDir + u"outputExportCommentsHTML.html", opts);

    std::cout << "Excel file exported to HTML with comments successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
