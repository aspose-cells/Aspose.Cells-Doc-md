---
title: Excel de Yorumda Arka Plan Nasıl Değiştirilir C++ ile
linktitle: Yorum Arka Planı
type: docs
weight: 190
url: /tr/cpp/how-to-set-comment-background/
description: Excel de yoruma renk nasıl değiştirilir. C++ kullanarak Excel de yoruma resim veya görüntü nasıl eklenir.
keywords: Yorum arkaplan rengi ekle, resim ekle, yorum gölgeleme excel
---

{{% alert color="primary" %}}

 Yorumlar, hücrelere eklenen ve yorumları kaydetmek için kullanılan yorumlardır, formülün nasıl çalıştığı, değerlerin nereden geldiği veya inceleyenlerin soruları gibi detayları içerir. Yorumlar, birden fazla kişinin aynı belgeyi farklı zamanlarda tartışması veya gözden geçirmesi sırasında son derece önemli rol oynar. Farklı kişilerin yorumlarını nasıl ayırt edebilirim? Evet, her yorum için farklı bir arkaplan rengi ayarlayabiliriz. Ancak, çok sayıda belge ve yorum işlemeniz gerektiğinde, bu manuel olarak yapmak bir felakettir. Neyse ki, [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) bir API sağlar ve bunu koda uygun şekilde yapmanıza imkan tanır.

{{% /alert %}}

## **Excel'de yorumda renk nasıl değiştirilir**

Varsayılan yorum arkaplan rengini kullanmak istemiyorsanız, onu ilgilendiğiniz bir renk ile değiştirmek isteyebilirsiniz. Excel'de Yorum kutusunun arkaplan rengini nasıl değiştiririm?

 Aşağıdaki kod, [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) kullanarak kendi seçtiğiniz yorumlara favori arkaplan renginizi eklemenize nasıl yardımcı olacağını gösterecek.

 Size bir [örnek dosya](exmaple.xlsx) hazırladık. Bu dosya, aşağıdaki kodda Workbook nesnesini başlatmak için kullanılır.

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

 Yukarıdaki kodu çalıştırın ve bir [sonuç dosyası](result.xlsx) alın.

## **Excel'de yorumlara resim veya görüntü eklemek**

 Microsoft Excel, kullanıcıların elektronik tabloların görünümünü ve hissini büyük ölçüde özelleştirmesine olanak tanır. Yorumlara arkaplan resmi eklemek bile mümkündür. Bir arkaplan resmi eklemek estetik bir tercih olabilir veya markalaşmayı güçlendirmek için kullanılabilir.

 Aşağıdaki örnek kod, [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) API kullanarak sıfırdan bir XLSX dosyası oluşturur ve hücre A1'e resimli arkaplan ile bir yorum ekler.

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
