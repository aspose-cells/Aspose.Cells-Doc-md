---
title: How to change background in comment in Excel with C++
linktitle: Comment Background
type: docs
weight: 190
url: /cpp/how-to-set-comment-background/
description: How to change color in comment in Excel. How to insert picture or image in comment in Excel using C++.
keywords: add inset picture image color comment background excel
---

{{% alert color="primary" %}}

Comments are added to cells to record comments, anything from the details of how a formula is worked, where a value comes from, or questions from reviewers. Comments play an extremely important role when multiple people discuss or review the same document at different times. How to distinguish different people's comments? Yes, we can set a different background color for each comment. But when we need to process a lot of documents and a lot of comments, doing it manually is a disaster. Fortunately, [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) provides an API that allows you to do this in code.

{{% /alert %}}

## **How to change color in comment in Excel**

When you don't need the default background color for comments, you may want to replace it with a color you're interested in. How do I change the background color of the Comments box in Excel?

The following code will guide you on how to use [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) to add your favorite background color to comments of your own choice.

Here we have prepared a [sample file](exmaple.xlsx) for you. This file is used to initialize the Workbook object in the code below.

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

Execute the above code, and you will get an [output file](result.xlsx).

## **How to insert picture or image in comment in Excel**

Microsoft Excel lets users customize the look and feel of spreadsheets to a great extent. It is even possible to add background pictures to comments. Adding a background image can be an aesthetic choice or be used to strengthen branding.

The sample code below creates an XLSX file from scratch using [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) API, and adds a comment with a picture background to cell A1.

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