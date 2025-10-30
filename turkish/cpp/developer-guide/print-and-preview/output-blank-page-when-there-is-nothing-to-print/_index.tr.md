---  
title: Yazdırılacak hiçbir şey yoksa Boş Sayfa göster (C++)  
linktitle: Hiçbir şey Yazdırılacak Değilken Boş Sayfa Çıktısı  
type: docs  
weight: 90  
url: /tr/cpp/output-blank-page-when-there-is-nothing-to-print/  
description: Boş çalışma sayfalarını ve yazdırmak için boş sayfalar gösterimi ile Aspose.Cells kullanarak C++ ile nasıl yapılacağını öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Eğer sayfa boşsa, Aspose.Cells hiçbir şey yazdırmaz; çalışma sayfasını görüntüye dışa aktarırken bu davranışı değiştirmek için [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/) özelliğini kullanabilirsiniz. Bu özelliği **true** olarak ayarlarsanız, boş sayfa yazdırılır.  

## **Hiçbir şey Yazdırılacak Değilken Boş Sayfa Çıktısı**  

Aşağıdaki örnek kod, boş bir sayfa ile boş bir çalışma kitabı oluşturur ve [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/) özelliği **true** olarak ayarlandıktan sonra boş sayfayı bir resme dönüştürür. Sonuç olarak, yazdırılacak hiçbir şey olmadığından, aşağıdaki resimde görebileceğiniz boş bir sayfa oluşturur.  

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)  

## **Örnek Kod**  

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Output directory
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook wb;

    // Access first worksheet - it is an empty sheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify image or print options
    // Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
    // So that an empty page gets printed
    ImageOrPrintOptions opts;
    opts.SetImageType(Drawing::ImageType::Png);
    opts.SetOutputBlankPageWhenNothingToPrint(true);

    // Render empty sheet to png image
    SheetRender sr(ws, opts);
    sr.ToImage(0, outputDir + u"OutputBlankPageWhenNothingToPrint.png");

    std::cout << "Blank page rendered to PNG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  
{{< app/cells/assistant language="cpp" >}}
