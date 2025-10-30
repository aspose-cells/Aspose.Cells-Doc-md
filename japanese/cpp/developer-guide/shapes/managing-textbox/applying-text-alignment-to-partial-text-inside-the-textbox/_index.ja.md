---
title: ### C++を使用したテキストボックスへのテキスト位置設定/適用方法
linktitle: テキストボックスにテキストの配置を行う
type: docs
weight: 20
url: /ja/cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Aspose.Cellsでテキストボックスのテキスト位置を設定/適用する方法（C++）
keywords: Excelのワークシートテキストボックスに配置/設定を行うAspose
---

TextBoxは、私たちの文書や図表の表現力を向上させることができ、TextBoxの異なる部分に異なる配置を適用することで、読者に強調したいポイントを際立たせることができます。しかし、デフォルトの配置ではすべてのニーズを満たしません。これには、それぞれのTextBoxを調整して目標要件を満たす必要があります。調整すべきTextBoxオブジェクトがたくさんなければ幸運です。多くのTextBoxを調整しなければならない場合、問題になるかもしれません。心配はいりません、[Aspose.Cells](https://products.aspose.com/cells/)は、そのためのAPIインターフェイスを提供しています。

次のサンプルコードは、テキストボックスにテキストの配置を適用します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the shapes collection from the first worksheet
    ShapeCollection shapes = workbook.GetWorksheets().Get(0).GetShapes();

    // Add a TextBox to the worksheet
    Shape shape = shapes.AddTextBox(2, 0, 2, 0, 50, 120);

    // Set the text of the TextBox
    shape.SetText(u"This is a test.");

    // Set the horizontal and vertical alignment of the text
    shape.SetTextHorizontalAlignment(TextAlignmentType::Center);
    shape.SetTextVerticalAlignment(TextAlignmentType::Center);

    // Save the workbook to the output directory
    workbook.Save(outDir + u"result.xlsx");

    std::cout << "TextBox added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

適切なHTMLテキストを使って、TextBox内の一部のテキストのテキスト配置を変更することも可能です。以下のサンプルコードは、部分的なテキストに対してテキスト配置を適用します。

[ソースファイル](SampleTextboxExcel2016.xlsx)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleTextboxExcel2016.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output.xlsx";

    // Initialize an object of the Workbook class to load template file
    Workbook sourceWb(inputFilePath);

    // Access the target textbox whose text is to be aligned
    auto sourceTextBox = sourceWb.GetWorksheets().Get(0).GetShapes().Get(0);

    // Create an object of the target workbook
    Workbook destWb;

    // Access first worksheet from the collection
    auto sheet = destWb.GetWorksheets().Get(0);

    // Create new textbox
    TextBox textBox = sheet.GetShapes().AddShape(MsoDrawingType::TextBox, 1, 0, 1, 0, 200, 200);

    // Alternatively text box can be added using following line as well
    // TextBox textBox = sheet.GetShapes().AddTextBox(1, 0, 1, 0, 200, 200);

    // Use Html string from a template file textbox
    textBox.SetHtmlText(sourceTextBox.GetHtmlText());

    // Save the workbook on disc
    destWb.Save(outputFilePath);

    std::cout << "Textbox copied and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
