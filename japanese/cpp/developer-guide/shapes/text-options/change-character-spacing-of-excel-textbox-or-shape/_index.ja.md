---
title: ExcelのTextBoxまたはShapeの文字間隔をC++で変更する方法
linktitle: Excelテキストボックスまたは図形の文字間隔を変更する
type: docs
weight: 280
url: /ja/cpp/change-character-spacing-of-excel-textbox-or-shape/
description: Aspose.Cellsを使用してC++でExcelのテキストボックスや図形の文字間隔を変更する方法を学びます。
---

{{% alert color="primary" %}}

[**TextOptions.GetSpacing()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getspacing/)プロパティを使用してExcelのテキストボックスや図形の文字間隔を変更できます。

{{% /alert %}}

次のサンプルコードは、Excelファイル内のテキストボックスの文字間隔をポイント4に設定し、ディスクに保存します。

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
{{< app/cells/assistant language="cpp" >}}
