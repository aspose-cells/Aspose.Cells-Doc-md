---  
title: Çalışma Sayfası İçinde Yorum veya Şeklin Kenar Boşluklarını C++ ile Ayarlama  
linktitle: Çalışma Sayfası İçindeki Yorum veya Şeklin Kenar Boşluklarını Ayarlama  
type: docs  
weight: 1500  
url: /tr/cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Aspose.Cells kullanarak çalışma sayfası içindeki yorumların veya şekillerin kenar boşluklarını nasıl ayarlayacağınızı öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Aspose.Cells, [**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/gettextalignment/) özelliği kullanılarak herhangi bir şeklin veya yorumun kenar boşluklarını ayarlamanıza izin verir. Bu özellik, [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment) sınıfının nesnesini döndürür ve farklı özelliklere sahiptir örn. [**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/), [**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/), [**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/), [**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/) gibi, bunlar üst, sol, alt ve sağ kenar boşluklarını ayarlamak için kullanılabilir.  

## **Çalışma Sayfası İçindeki Yorum veya Şeklin Kenar Boşluklarını Ayarlama**  

Aşağıdaki örnek kod, iki şekil içeren bir çalışma kitabı yükler. Kod, şekillere birer birer erişerek üst, sol, alt ve sağ kenar boşluklarını ayarlar. Kod tarafından oluşturulan [çıktı Excel dosyasını](61767852.xlsx) ve kodun etkisini gösteren ekran görüntüsünü görebilirsiniz.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Örnek Kod**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the sample Excel file
    Workbook workbook(u"sampleSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Iterate through each shape in the worksheet
    for (int32_t i = 0; i < ws.GetShapes().GetCount(); i++)
    {
        Shape sh = ws.GetShapes().Get(i);

        // Access the text alignment
        ShapeTextAlignment txtAlign = sh.GetTextBody().GetTextAlignment();

        // Set auto margin false
        txtAlign.SetIsAutoMargin(false);

        // Set the top, left, bottom and right margins
        txtAlign.SetTopMarginPt(10);
        txtAlign.SetLeftMarginPt(10);
        txtAlign.SetBottomMarginPt(10);
        txtAlign.SetRightMarginPt(10);
    }

    // Save the output Excel file
    workbook.Save(u"outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");

    std::cout << "Margins set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  

