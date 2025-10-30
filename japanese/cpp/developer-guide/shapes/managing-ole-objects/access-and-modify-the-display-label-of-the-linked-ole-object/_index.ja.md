---
title: C++でリンクされたOleオブジェクトの表示ラベルにアクセス・変更する方法
linktitle: リンクされたオブジェクトの表示ラベルへのアクセスと変更
type: docs
weight: 100
url: /ja/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Aspose.Cells for C++を使用してExcelファイルのリンクされたOleオブジェクトの表示ラベルにアクセスおよび変更する方法を学ぶ。
---

## **可能な使用シナリオ**

Microsoft Excelでは、次のスクリーンショットのようにOleオブジェクトの表示ラベルを変更できます。Aspose.Cells APIの [**GetLabel()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getlabel/) と [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/) メソッドを使用してOleオブジェクトの表示ラベルにアクセスまたは変更することも可能です。

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **リンクされたオブジェクトの表示ラベルへのアクセスと変更**

次のサンプルコードを参照してください。Ole Objectを含む[sample Excel file](64716810.xlsx)を読み込みます。コードはOle Objectにアクセスし、そのラベルをサンプルAPIからAspose APIに変更します。下記のコンソール出力を参照してください。これはサンプルコードのサンプルExcelファイルへの効果を示しています。

## **サンプルコード**

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file
    U16String inputFilePath = u"sampleAccessAndModifyLabelOfOleObject.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    OleObject oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object
    std::cout << "Ole Object Label - Before: " << oleObject.GetLabel().ToUtf8() << std::endl;

    // Modify the Label of the Ole Object
    oleObject.SetLabel(u"Aspose APIs");

    // Save workbook to memory stream
    auto ms = wb.SaveToStream();

    // Set the workbook reference to null
    wb = Workbook();

    // Load workbook from memory stream
    wb = Workbook(ms);

    // Access first worksheet
    ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object that has been modified earlier
    std::cout << "Ole Object Label - After: " << oleObject.GetLabel().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **コンソール出力**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
