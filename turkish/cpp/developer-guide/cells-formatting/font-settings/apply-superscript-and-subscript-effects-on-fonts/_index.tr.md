---
title: Üst simge ve Alt simge efektleri uygulama C++ ile
linktitle: Fontlarda Üstsimge ve Altsimge Efektleri Uygulama
type: docs
weight: 80
url: /tr/cpp/apply-superscript-and-subscript-effects-on-fonts/
description: Aspose.Cells for C++ API kullanılarak Excel de üst simge ve alt simge efektleri uygulayan C++ kodu.
keywords: excel üst simge c++, excel alt simge c++, excel üst ve alt simge c++, excel e alt ve üst simge ekleme c++, excel de alt ve üst simge ekleme, excel e üst ve alt simge ekleme, excel de üst simge ve alt simge ekleme, excel de üst ve alt simge ekleme
---

{{% alert color="primary" %}}

Aspose.Cells, metne üstsimge (metnin taban çizgisinin üstünde) ve altsimge (metnin taban çizgisinin altında) efektlerini uygulama işlevselliği sağlar.

{{% /alert %}}

## **Üstsimge ve Altsimge ile Çalışma**

Üstsimge efektini **true** olarak ayarlayarak [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) nesnesinin [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) özelliğini ayarlayarak uygulayabilirsiniz. Altsimge uygulamak için, [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) nesnesinin [**IsSubscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) özelliğini **true** olarak ayarlayın.

Aşağıdaki kod örnekleri, metne üst simge ve altsimge uygulamanın nasıl yapılacağını göstermektedir.

### C++ ile Üst Simge Efekti Uygulama Kodu

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Setting the font Superscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSuperscript(true);
    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"Superscript_out.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully with superscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### C++ ile Alt Simge Efekti Uygulama Kodu

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Set the font Subscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSubscript(true);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"Subscript_out.xls", SaveFormat::Auto);

    std::cout << "File saved successfully with subscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
