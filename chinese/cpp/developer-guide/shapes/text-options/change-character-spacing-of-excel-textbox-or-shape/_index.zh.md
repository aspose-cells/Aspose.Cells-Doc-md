---
title: 用C++改变Excel文本框或形状的字符间距
linktitle: 更改 Excel 文本框或形状的字符间距
type: docs
weight: 280
url: /zh/cpp/change-character-spacing-of-excel-textbox-or-shape/
description: 学习如何用Aspose.Cells和C++改变Excel文本框或形状的字符间距。
---

{{% alert color="primary" %}}

你可以用[**TextOptions.GetSpacing()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getspacing/)属性改变Excel文本框或形状的字符间距。

{{% /alert %}}

以下示例代码将Excel文件中某文本框的字符间距改为4点，并保存到磁盘。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your excel file inside a workbook object
    Workbook wb(srcDir + u"sampleChangeTextBoxOrShapeCharacterSpacing.xlsx");

    // Access your text box which is also a shape object from shapes collection
    Shape shape = wb.GetWorksheets().Get(0).GetShapes().Get(0);

    // Access the first font setting object via GetCharacters() method
    FontSetting fs = shape.GetRichFormattings()[0];

    // Set the character spacing to point 4
    fs.GetTextOptions().SetSpacing(4);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputChangeTextBoxOrShapeCharacterSpacing.xlsx", SaveFormat::Xlsx);

    std::cout << "Character spacing changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
