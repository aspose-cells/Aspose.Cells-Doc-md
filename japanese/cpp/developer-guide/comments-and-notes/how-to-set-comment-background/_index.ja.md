---
title: C++を使用したExcelのコメントの背景変更方法
linktitle: コメント背景
type: docs
weight: 190
url: /ja/cpp/how-to-set-comment-background/
description: Excelのコメントの色を変更する方法。C++を使用してExcelのコメントに画像や写真を挿入する方法。
keywords: 挿入画像、色付きコメント背景、Excel
---

{{% alert color="primary" %}}

コメントはセルに追加され、コメントの詳細、数式の仕組みや値の出所、レビュアーの質問などを記録します。複数人が同じドキュメントを異なる時間に議論やレビューを行う際に非常に重要な役割を果たします。異なる人のコメントを区別するにはどうすればよいですか？はい、それぞれのコメントに異なる背景色を設定できます。しかし、多くのドキュメントや多くのコメントを処理する必要がある場合、手動で行うのは大変です。幸い、[**Aspose.Cells**](https://products.aspose.com/cells/cpp/)はこれをコードで実行できるAPIを提供します。

{{% /alert %}}

## **Excel でコメントの色を変更する方法**

コメントのデフォルト背景色が不要な場合は、お好きな色に置き換えることもできます。Excelのコメントボックスの背景色を変更するにはどうすればよいですか？

以下のコードは、[**Aspose.Cells**](https://products.aspose.com/cells/cpp/)を使用して、自分の好きな背景色をコメントに追加する方法を案内します。

こちらに[サンプルファイル](exmaple.xlsx)を用意しました。このファイルは、以下のコードでWorkbookオブジェクトを初期化するために使われます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"exmaple.xlsx";
    Workbook book(inputPath);

    Worksheet worksheet = book.GetWorksheets().Get(0);
    Comment comment = worksheet.GetComments().Get(0);

    CommentShape shape = comment.GetCommentShape();
    shape.GetFill().GetSolidFill().SetColor(Color::Red());

    U16String outputPath = outDir + u"result.xlsx";
    book.Save(outputPath);

    std::cout << "Comment color changed successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

上記のコードを実行すると、[出力ファイル](result.xlsx)が得られます。

## **Excel でコメントに画像を挿入する方法**

Microsoft Excelは、スプレッドシートの外観と感触を大きくカスタマイズ可能です。コメントに背景画像を追加することも可能です。背景画像の追加は、見た目の工夫やブランディング強化に役立ちます。

以下のサンプルコードは、[**Aspose.Cells**](https://products.aspose.com/cells/cpp/) APIを使用して、好きな背景色を持つコメントを作成し、セルA1に追加する方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include <vector>
#include <cstdint>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a Workbook
    Workbook workbook;

    // Get a reference of comments collection with the first sheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    CommentCollection comments = worksheet.GetComments();

    // Add a comment to cell A1
    int32_t commentIndex = comments.Add(0, 0);
    Comment comment = comments.Get(commentIndex);
    comment.SetNote(u"First note.");
    Font font = comment.GetFont();
    font.SetName(u"Times New Roman");

    // Load an image into stream
    U16String imagePath = srcDir + u"image2.jpg";
    std::vector<uint8_t> imageData;
    // Assume image loading logic here
    // For simplicity, we assume imageData is populated with the image bytes

    // Set image data to the shape associated with the comment
    CommentShape commentShape = comment.GetCommentShape();
    commentShape.GetFill().SetImageData(Aspose::Cells::Vector<uint8_t>(imageData.data(), imageData.size()));

    // Save the workbook
    U16String outputPath = outDir + u"commentwithpicture1.out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with comment and image!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
