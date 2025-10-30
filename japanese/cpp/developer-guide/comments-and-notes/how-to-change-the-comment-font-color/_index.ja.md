---
title: C++を使用したコメントのフォントカラー変更方法
linktitle: コメントのフォントの色を変更する方法
type: docs
weight: 180
url: /ja/cpp/how-to-change-the-comment-font-color/
description: Aspose.Cellsを使用してExcelのコメントのフォント色をカスタマイズする方法をC++で学びましょう。
---

{{% alert color="primary" %}} 

Microsoft Excelでは、ユーザーはセルにコメントを追加して追加情報を表示し、データを強調表示することができます。開発者は、コメントをカスタマイズして配置設定、テキスト方向のフォントカラーなどを指定する必要があります。Aspose.Cellsは、このタスクを実行するためのAPIを提供しています。

{{% /alert %}} 

Aspose.Cellsはコメントのフォント色を設定するための[**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/)プロパティを提供します。以下のサンプルコードは、[**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/)プロパティを使用してコメントのテキスト方向を設定する方法を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add some text in cell A1
    worksheet.GetCells().Get(u"A1").PutValue(u"Here");

    // Add a comment to A1 cell
    int commentIndex = worksheet.GetComments().Add(u"A1");
    Comment comment = worksheet.GetComments().Get(commentIndex);

    // Set its vertical alignment setting
    comment.GetCommentShape().SetTextVerticalAlignment(TextAlignmentType::Center);

    // Set the Comment note
    comment.SetNote(u"This is my Comment Text. This is Test.");

    // Get the comment shape
    Shape shape = comment.GetCommentShape();

    // Set the fill color of the shape to black
    shape.GetFill().GetSolidFill().SetColor(Color::Black());

    // Get the font of the shape
    Font font = shape.GetFont();

    // Set the font color to white
    font.SetColor(Color::White());

    // Create a StyleFlag to apply font color changes
    StyleFlag styleFlag;
    styleFlag.SetFontColor(true);

    // Apply the font color changes to the shape's text
    shape.GetTextBody().Format(0, shape.GetText().GetLength(), font, styleFlag);

    // Save the Excel file
    workbook.Save(outDir + u"outputChangeCommentFontColor.xlsx");

    Aspose::Cells::Cleanup();
}
```

上記のコードによって生成された[出力ファイル](102662195.xlsx)を参照してください。
{{< app/cells/assistant language="cpp" >}}
