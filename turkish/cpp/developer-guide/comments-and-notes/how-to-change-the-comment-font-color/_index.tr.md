---
title: Yorumun Yazı Tipi Rengini C++ ile Nasıl Değiştiririz
linktitle: Yorum Metin Rengini Nasıl Değiştirilir
type: docs
weight: 180
url: /tr/cpp/how-to-change-the-comment-font-color/
description: Aspose.Cells kullanarak Excel de yorumların yazı tipi rengini nasıl özelleştireceğinizi C++ diliyle öğrenin.
---

{{% alert color="primary" %}} 

Microsoft Excel, kullanıcılara ek bilgi eklemek ve verileri vurgulamak için hücrelere yorum eklemelerine izin verir. Geliştiriciler, yorumu özelleştirmek, hizalama ayarlarını belirtmek, metin yönü Font Rengi gibi işlemler yapmak isteyebilirler. Aspose.Cells, görevi başarmak için API'lar sağlar.

{{% /alert %}} 

Aspose.Cells, Yorumu yazı tipi rengi ayarlamak için [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) özelliği sağlar. Aşağıdaki örnek kod, [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) özelliğinin kullanımıyla yorum için metin yönünü ayarlar.

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

Yukarıdaki kod tarafından oluşturulan çıktı dosyası, referansınız için ekte bulunmaktadır.
{{< app/cells/assistant language="cpp" >}}
