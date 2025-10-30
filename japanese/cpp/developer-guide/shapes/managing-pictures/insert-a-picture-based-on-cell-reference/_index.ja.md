---
title: セル参照に基づいて画像を挿入する C++で
linktitle: セル参照に基づいて画像を挿入する
type: docs
weight: 150
url: /ja/cpp/insert-a-picture-based-on-cell-reference/
description: Aspose.Cells for C++を使った、セル参照に基づいて画像を挿入する方法を学びます。
---

{{% alert color="primary" %}}

時々、空の画像があり、Formula Barでセル参照を設定して画像内のデータや内容を表示する必要があります。 Aspose.Cellsはこの機能（Microsoft Excel 2010）をサポートしています。

{{% /alert %}}

## セル参照に基づいて画像を挿入する

Aspose.Cellsは、ワークシートのセルの内容を画像形状で表示する機能をサポートしています。指定のセルまたはセル範囲をリンクして、データを表示したい画像に紐付けることができます。セルまたはセル範囲がグラフィックオブジェクトにリンクされているため、そのセルまたはセル範囲のデータを変更すると、自動的にグラフィックオブジェクトにも反映されます。[**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/)メソッドを呼び出してワークシートに画像を追加します。このメソッドは[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)コレクションの[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)オブジェクトでカプセル化されています。[**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/)属性を使用してセル範囲を指定します。この属性は[**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)オブジェクトのものです。

### コード例

```cpp
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    cells.Get(U16String(u"A1")).PutValue(U16String(u"A1"));
    cells.Get(U16String(u"C10")).PutValue(U16String(u"C10"));

    Aspose::Cells::Vector<uint8_t> imagedata = ConditionalFormattingIcon::GetIconImageData(IconSetType::TrafficLights31, 0);

    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddPicture(0, 3, imagedata, 10, 10);
    pic.SetFormula(U16String(u"A1:C10"));

    workbook.GetWorksheets().Get(0).GetShapes().UpdateSelectedValue();
    workbook.Save(outDir + u"referencedpicture.out.xlsx");

    std::cout << "Referenced picture added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
