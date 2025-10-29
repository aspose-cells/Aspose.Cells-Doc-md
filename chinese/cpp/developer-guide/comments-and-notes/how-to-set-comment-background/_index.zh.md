---
title: 在 Excel 中使用 C++ 更改批注背景色的方法
linktitle: 评论背景
type: docs
weight: 190
url: /zh/cpp/how-to-set-comment-background/
description: 如何更改 Excel 批注中的颜色。以及如何使用 C++ 在批注中插入图片或图像。
keywords: 在单元格中添加插入图片、颜色、批注背景的教程
---

{{% alert color="primary" %}}

批注被添加到单元格，用于记录评论，从公式的详细操作、数据来源到审阅者的提问。批注在多人讨论或定期审阅同一文档时起着极其重要的作用。如何区分不同人的评论？是的，我们可以为每个批注设置不同的背景色。但当需要处理大量文档和大量批注时，手动操作将变得很麻烦。幸运的是，[**Aspose.Cells**](https://products.aspose.com/cells/cpp/) 提供了支持用代码实现的 API。

{{% /alert %}}

## **如何在Excel中更改评论的颜色**

当你不需要批注的默认背景色时，可以用自己关注的颜色替换它。如何更改 Excel 中批注框的背景色？

以下代码将指导你如何使用 [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) 为你的批注添加你喜欢的背景色。

这里我们为你准备了一个[示例文件](exmaple.xlsx)。该文件用于初始化下面的代码中的 Workbook 对象。

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

执行上述代码，你会得到一个[输出文件](result.xlsx)。

## **如何在Excel中评论中插入图片或图像**

Microsoft Excel 允许用户极大程度地自定义电子表格的外观和感觉。甚至可以在评论中添加背景图片。添加背景图片可以是美观的选择，也可以用来强化品牌。

以下示例代码使用 [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) API 从零开始创建一个 XLSX 文件，并在单元格 A1 添加带有图片背景的评论。

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
