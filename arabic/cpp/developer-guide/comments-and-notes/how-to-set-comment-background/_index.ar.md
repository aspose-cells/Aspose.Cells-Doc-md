---
title: كيفية تغيير خلفية التعليق في Excel باستخدام C++
linktitle: خلفية التعليق
type: docs
weight: 190
url: /ar/cpp/how-to-set-comment-background/
description: كيفية تغيير اللون في تعليق في Excel. كيفية إدراج صورة أو صورة في تعليق في Excel باستخدام C++.
keywords: إضافة صورة داخلية لملصق خلفية تعليق في Excel
---

{{% alert color="primary" %}}

يتم إضافة التعليقات إلى الخلايا لتسجيل الملاحظات، سواء كانت تفاصيل حول كيفية عمل صيغة، مصدر قيمة، أو أسئلة من المراجعين. تلعب التعليقات دورًا مهمًا جدًا عندما يناقش عدة أشخاص أو يراجعون نفس المستند في أوقات مختلفة. كيف يمكن تمييز تعليقات الأشخاص المختلفين؟ نعم، يمكننا ضبط لون خلفية مختلف لكل تعليق. ولكن عند الحاجة لمعالجة العديد من المستندات والكثير من التعليقات، فإن القيام بذلك يدويًا يمثل كارثة. لحسن الحظ، توفر [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) API تتيح لك تنفيذ ذلك برمز.

{{% /alert %}}

## **كيفية تغيير اللون في التعليق في إكسل**

عندما لا تحتاج إلى لون خلفية افتراضي للتعليقات، قد ترغب في استبداله بلون تهتم به. كيف أغير لون خلفية صندوق التعليقات في Excel؟

سيوجهك الكود التالي حول كيفية استخدام [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) لإضافة لون خلفية مفضل لديك لتعليقاتك الخاصة.

لقد أعددنا لك [ملف نموذجي](exmaple.xlsx). يُستخدم هذا الملف لتهيئة كائن Workbook في الشيفرة أدناه.

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

نفذ الكود أعلاه، وستحصل على ملف [الإخراج](result.xlsx).

## **كيفية إدراج صورة أو صورة في التعليق في إكسل**

يتيح Microsoft Excel للمستخدمين تخصيص مظهر وأسلوب جداول البيانات إلى حد كبير. من الممكن أيضًا إضافة صور خلفية إلى التعليقات. يمكن أن يكون إضافة صورة خلفية اختيارًا جماليًا أو يُستخدم لتعزيز العلامة التجارية.

ينشئ الكود أدناه ملف XLSX من الصفر باستخدام API [**Aspose.Cells**](https://products.aspose.com/cells/cpp/)، ويضيف تعليقًا بخلفية صورة إلى الخلية A1.

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
