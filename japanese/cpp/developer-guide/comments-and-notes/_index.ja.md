---
title: C++でコメントやノートを管理する
linktitle: コメントとノート
type: docs
weight: 128
url: /ja/cpp/comments-and-notes/
description: Aspose.Cells for C++を使ったコメントやノートの挿入と管理。
keywords: コメントを挿入、ノートを挿入
---

## **紹介**

コメントはセルに追加情報を追加するために使用されます。Aspose.Cellsでは、セルにコメントを追加するための2つの方法が提供されます。最初の方法は、デザイナーファイルで手動でコメントを作成することです。これらのコメントはその後、Aspose.Cellsを使用してインポートされます。2番目は、Aspose.Cells APIを使用してランタイムでコメントを追加することです。このトピックでは、Aspose.Cells APIを使用してセルにコメントを追加する方法について説明します。コメントの書式設定についても説明します。

## **コメントの追加**

[**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/)コレクションの[**Add**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/add/)メソッド（[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)オブジェクト内にカプセル化）を呼び出すことによって、セルにコメントを追加します。新しい[**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/)オブジェクトは、コメントインデックスを渡して[**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/)コレクションからアクセスできます。[**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/)オブジェクトにアクセスした後、[**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/)オブジェクトの[**GetNote()**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/getnote/)プロパティを使用してコメントノートをカスタマイズします。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int32_t sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add a comment to cell "F5"
    int32_t commentIndex = worksheet.GetComments().Add(u"F5");

    // Access the newly added comment
    Comment comment = worksheet.GetComments().Get(commentIndex);

    // Set the comment note
    comment.SetNote(u"Hello Aspose!");

    // Save the Excel file
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **コメントの書式設定**

コメントの高さ、幅、フォント設定を構成することで、コメントの外観を書式設定することも可能です。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int32_t sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding a comment to "F5" cell
    int32_t commentIndex = worksheet.GetComments().Add(u"F5");

    // Accessing the newly added comment
    Comment comment = worksheet.GetComments().Get(commentIndex);

    // Setting the comment note
    comment.SetNote(u"Hello Aspose!");

    // Setting the font size of a comment to 14
    comment.GetFont().SetSize(14);

    // Setting the font of a comment to bold
    comment.GetFont().SetIsBold(true);

    // Setting the height of the font to 10
    comment.SetHeightCM(10);

    // Setting the width of the font to 2
    comment.SetWidthCM(2);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **コメントに画像を追加する**

Microsoft Excel 2007では、セルコメントの背景として画像を使用することもできます。Excel 2007では、次の手順を実行することでこれが実現されます。（すでにセルにコメントを追加していることを前提とします。）

1. コメントを含むセルを右クリックします。
1. **表示/非表示**を選択し、コメント内のテキストをクリアします。
1. コメントの境界線をクリックして選択します。
1. **書式**、次に**コメント**を選択します。
1. **色と線**タブで、**色**リストを展開します。
1. **塗りつぶしの効果**をクリックします。
1. **図**タブで、**ピクチャを選択**をクリックします。
1. 画像を探し、選択します。
1. すべてのダイアログが閉じるまで**OK**をクリックします。

Aspose.Cellsもこの機能を提供します。以下は、セル"A1"に画像を背景として設定したコメントを追加し、からXLSXファイルをスクラッチから作成するコードサンプルです。

```c++
#include <Aspose.Cells.h>
#include <fstream>
#include <vector>
#include <iostream>

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);
    CommentCollection comments = sheet.GetComments();

    int32_t commentIndex = comments.Add(0, 0);
    Comment comment = comments.Get(commentIndex);
    comment.SetNote(u"First note.");

    Font commentFont = comment.GetFont();
    commentFont.SetName(u"Times New Roman");

    U16String imagePath = srcDir + u"logo.jpg";
    std::vector<uint8_t> imageData;
    std::ifstream file(imagePath.ToUtf8(), std::ios::binary | std::ios::ate);
    if (file)
    {
        std::streamsize size = file.tellg();
        file.seekg(0, std::ios::beg);
        imageData.resize(size);
        file.read(reinterpret_cast<char*>(imageData.data()), size);
    }
    Vector<uint8_t> data(imageData.data(), static_cast<int32_t>(imageData.size()));

    CommentShape shape = comment.GetCommentShape();
    shape.GetFill().SetImageData(data);

    U16String outputPath = outDir + u"book1.out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    std::cout << "Workbook with image comment created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **高度なトピック**
- [コメントのテキスト方向を変更する](/cells/ja/cpp/change-text-direction-of-the-comment/)
- [コメントのフォント色を変更する方法](/cells/ja/cpp/how-to-change-the-comment-font-color/)
- [コメントの背景を設定する方法](/cells/ja/cpp/how-to-set-comment-background/)
- [スレッド化されたコメント](/cells/ja/cpp/threaded-comments/)
{{< app/cells/assistant language="cpp" >}}
