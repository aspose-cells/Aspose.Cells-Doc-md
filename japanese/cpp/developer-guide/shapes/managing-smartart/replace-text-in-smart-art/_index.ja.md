---
title: SmartArt内のテキストをC++で置換
linktitle: スマートアート内のテキストの置換
type: docs
weight: 1200
url: /ja/cpp/replace-text-in-smart-art/
description: Aspose.Cells for C++を使用してShape.Textプロパティを設定し、スマートアートのテキストを更新する方法を学びます。
---

## **可能な使用シナリオ**

スマートアートはワークブックの主要なオブジェクトの一つです。多くの場合、スマートアートのテキストを更新する必要があります。Aspose.Cellsはこの機能を[**Shape.Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/)プロパティを設定することで提供します。

次のリンクからサンプルソースファイルをダウンロードできます:

[SmartArt.xlsx](77496338.xlsx)

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"SmartArt.xlsx";
    U16String outputFilePath = outDir + u"outputSmartArt.xlsx";

    Workbook workbook(inputFilePath);

    WorksheetCollection worksheets = workbook.GetWorksheets();
    for (int i = 0; i < worksheets.GetCount(); ++i)
    {
        Worksheet worksheet = worksheets.Get(i);
        ShapeCollection shapes = worksheet.GetShapes();

        for (int j = 0; j < shapes.GetCount(); ++j)
        {
            Shape shape = shapes.Get(j);
            shape.SetAlternativeText(u"ReplacedAlternativeText");

            if (shape.IsSmartArt())
            {
                GroupShape smartArtGroup = shape.GetResultOfSmartArt();
                auto groupedShapes = smartArtGroup.GetGroupedShapes();

                for (int k = 0; k < groupedShapes.GetLength(); ++k)
                {
                    Shape smartArtShape = groupedShapes[k];
                    smartArtShape.SetText(u"ReplacedText");
                }
            }
        }
    }

    OoxmlSaveOptions options;
    options.SetUpdateSmartArt(true);

    workbook.Save(outputFilePath, options);

    std::cout << "SmartArt updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
