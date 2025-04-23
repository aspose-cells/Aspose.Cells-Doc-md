---
title: C++を使ったコメントのテキスト方向変更方法
linktitle: コメントのテキスト方向を変更する
type: docs
weight: 10
url: /ja/cpp/change-text-direction-of-the-comment/
description: Excelのコメントのテキスト方向を変更する方法をAspose.Cells for C++を使用して学びましょう。
---

{{% alert color="primary" %}}

Microsoft Excelでは、セルにコメントを追加して追加情報を表示し、データを強調表示することができます。開発者は、コメントをカスタマイズして配置設定やテキスト方向を指定する必要があります。Aspose.Cellsは、このタスクを実行するためのAPIを提供しています。

{{% /alert %}}

Aspose.Cellsはコメントのテキスト方向を設定するための[**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/)プロパティを提供します。以下のサンプルコードは、[**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/)プロパティを使用してコメントのテキスト方向を設定する方法を示しています。

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

    // Instantiate a new Workbook
    Workbook wb;

    // Get the first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Add a comment to A1 cell
    int commentIndex = sheet.GetComments().Add(u"A1");
    Comment comment = sheet.GetComments().Get(commentIndex);

    // Set its vertical alignment setting
    comment.GetCommentShape().SetTextVerticalAlignment(TextAlignmentType::Center);

    // Set its horizontal alignment setting
    comment.GetCommentShape().SetTextHorizontalAlignment(TextAlignmentType::Right);

    // Set the Text Direction - Right-to-Left
    comment.GetCommentShape().SetTextDirection(TextDirectionType::RightToLeft);

    // Set the Comment note
    comment.SetNote(u"This is my Comment Text. This is test");

    // Save the Excel file
    U16String outputPath = outDir + u"OutCommentShape.out.xlsx";
    wb.Save(outputPath);

    std::cout << "Comment shape created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
