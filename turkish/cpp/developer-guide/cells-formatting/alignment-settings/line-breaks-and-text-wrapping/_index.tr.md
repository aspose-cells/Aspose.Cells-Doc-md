---
title: Çizgi Sonları ve Metin Sarma C++ ile
description: C++ dilinde Aspose.Cells kütüphanesini kullanarak metin sarma ve kelime kaydırma nasıl uygulanır. Aspose.Cells kütüphanesini kullanarak hücrelere metin ekleyebilir ve metin sarma yöntemini ayarlayabilirsiniz, örneğin manuel kelime kaydırma, kelime kaydırma vb. Bu belge, bu özellikleri nasıl uygulayacağınızı detaylandırmakta ve örnek kodlar sunmaktadır.
keywords: Aspose.Cells, satır sonları, metin kaydırma, metin düzeni
type: docs
weight: 60
url: /tr/cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Hücredeki metnin okunabilmesi için, açık satır sonları ve metin kaydırma uygulanabilir. Metin kaydırma, hücredeki bir satırı birden fazla satıra dönüştürür, açık satır sonları istediğiniz yerde kesmek için kullanılır.

{{% /alert %}}

## **Hücrede Metin Kaydırma**

Bir hücrede metni sarmak için, [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) özelliğini kullanın.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create Workbook Object
    Workbook wb;

    // Open first Worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Cells cell = ws.GetCells();

    // Increase the width of the first column
    cell.SetColumnWidth(0, 35);

    // Increase the height of the first row
    cell.SetRowHeight(0, 36);

    // Add text to the first cell
    cell.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make the cell's text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    wb.Save(srcDir + u"WrappingText.out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Açık Satır Sonları Kullanımı**

C++'ta hücrede açık satır sonları eklemek için '\n' kullanabilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create Workbook Object
    Workbook workbook;

    // Open first Worksheet in the workbook
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Aspose::Cells::Cells cell = ws.GetCells();

    // Increase the width of First Column Width
    cell.SetColumnWidth(0, 35);

    // Increase the height of first row
    cell.SetRowHeight(0, 65);

    // Add Text to the First Cell with Explicit Line Breaks
    cell.Get(0, 0).PutValue(u"I am using\nthe latest version of \nAspose.Cells to \ntest this functionality");

    // Make Cell's Text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    U16String outputFilePath = u"WrappingText.out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
