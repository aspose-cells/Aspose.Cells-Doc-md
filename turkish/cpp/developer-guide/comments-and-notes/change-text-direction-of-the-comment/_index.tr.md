---
title: C++ kullanarak Yorumun Metin Yönünü Değiştirin
linktitle: Yorumun Metin Yönünü Değiştir
type: docs
weight: 10
url: /tr/cpp/change-text-direction-of-the-comment/
description: Excel de yorumların metin yönünü değiştirmeyi öğrenin, Aspose.Cells for C++ kullanarak.
---

{{% alert color="primary" %}}

Microsoft Excel, kullanıcılara ek bilgi eklemek ve verileri vurgulamak için hücrelere yorum eklemelerine izin verir. Geliştiriciler, hücreye özel hizalama ayarlarını ve metin yönünü belirtmek için yorumu özelleştirmek isteyebilir. Aspose.Cells, görevi başarmak için API'lar sağlar.

{{% /alert %}}

Aspose.Cells, yorumların metin yönünü ayarlamak için [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/) özelliği sağlar. Aşağıdaki örnek kod, [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/) özelliğinin kullanımını gösterir, böylece yorumların metin yönü değiştirilebilir.

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
