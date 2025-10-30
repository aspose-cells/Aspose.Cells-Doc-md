---
title: C++でタイムラインをレンダリング
type: docs
weight: 40
url: /ja/cpp/rendering-timeline/
description: Aspose.Cellsを使用してC++でExcelファイルのタイムラインを管理します。
keywords: Office 2013、Office 2016、Office 2019、Office 365を使用せずにタイムラインをレンダリング
---

## **可能な使用シナリオ**
Aspose.Cellsは、Office 2013、Office 2016、Office 2019、Office 365を使用せずにタイムラインの形状をレンダリングすることをサポートしています。ワークシートを画像に変換したり、ワークブックをPDFやHTML形式で保存すると、タイムラインが適切にレンダリングされます。

## **タイムラインのレンダリング**
以下のサンプルコードは、既存のタイムラインを含む[サンプルExcelファイル](input.xlsx)をロードします。その後、タイムラインの名前に応じてシェイプオブジェクトを取得し、Shape.ToImage()メソッドを使用して画像にレンダリングします。以下の画像は、レンダリングされたタイムラインを示す[出力画像](out.png)です。タイムラインが適切にレンダリングされており、サンプルExcelファイルと同じように見えます。

![todo:image_alt_text](out.png)
### **サンプルコード**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing timeline.
    Workbook workbook(u"input.xlsx");

    // Access second worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(1);

    // Access the first Timeline inside the worksheet.
    Timeline timeline = sheet.GetTimelines().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    // Get timeline shape object by timeline's name
    Shape timeLineShape = sheet.GetShapes().Get(timeline.GetName());

    // Save the timeline as an image
    timeLineShape.ToImage(u"out.png", options);

    std::cout << "Timeline image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
