---
title: Yorum ve Notları C++ ile Yönetme
linktitle: Yorumlar ve Notlar
type: docs
weight: 128
url: /tr/cpp/comments-and-notes/
description: Aspose.Cells for C++ ile yorum veya notlar ekleyip yönetme
keywords: yorum ekle, not ekle
---

## **Giriş**

Yorumlar, hücrelere ek bilgi eklemek için kullanılır. Aspose.Cells, hücrelere yorum eklemek için iki yöntem sağlar. İlk yöntem, tasarımcı dosyasında manuel olarak yorumlar oluşturmaktır. Bu yorumlar daha sonra Aspose.Cells kullanılarak içe aktarılır. İkinci yöntem, Aspose.Cells API'sını kullanarak çalışma zamanında yorum eklemektir. Bu konu, Aspose.Cells API'sını kullanarak hücrelere yorum eklemeyi tartışmaktadır. Yorumları biçimlendirmek de açıklanacaktır.

## **Yorum Ekleme**

Yorum koleksiyonunun Add metodu (encapsulated in the CommentAttribute object) çağrılarak bir hücreye yorum eklenir. Yeni CommentAttribute nesnesine, yorum dizinine geçilerek ulaşılabilir. CommentAttribute nesnesine erişildikten sonra, yorum notunu Customize edebilirsiniz.

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

## **Yorum Biçimlendirme**

Yorumların görünümünü yükseklik, genişlik ve yazı tipi ayarlarıyla biçimlendirmek de mümkündür.

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

## **Yoruma Resim Ekle**

Microsoft Excel 2007 ile, bir hücre yorumuna arka plan olarak bir resim eklemek de mümkündür. Excel 2007'de bunu aşağıdaki adımları takip ederek başarabilirsiniz. (Zaten bir hücre yorumu eklediğinizi varsayarlar.)

1. Yorum içeren hücreye sağ tıklayın.
1. **Yorumları Göster/Gizle**'yi seçin ve yorumdan herhangi bir metni temizleyin.
1. Yorumun kenarına tıklayın.
1. **Biçim**, ardından **Yorum**'u seçin.
1. **Renk ve Çizgiler** sekmesinde, **Renk** listesini genişletin.
1. **Dolgu Efektleri**'ni tıklayın.
1. **Resim** sekmesinde, **Resim Seç**'i tıklayın.
1. Resmi bulun ve seçin.
1. Tüm iletiler kapatılıncaya kadar **Tamam**'ı tıklayın.

Aspose.Cells ayrıca bu özelliği sağlar. Aşağıda, sıfırdan XLSX dosyası oluşturan ve "A1" hücresine resimli bir arka plan ekleyen bir kod örneği bulunmaktadır.

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

## **Gelişmiş Konular**
- [Yorumun Yazı Yönünü Değiştirme](/cells/tr/cpp/change-text-direction-of-the-comment/)
- [Yorum Yazı Tipi Rengini Nasıl Değiştirilir](/cells/tr/cpp/how-to-change-the-comment-font-color/)
- [Yorum arka planını nasıl ayarlarım](/cells/tr/cpp/how-to-set-comment-background/)
- [İz bırakan Yorumlar](/cells/tr/cpp/threaded-comments/)
{{< app/cells/assistant language="cpp" >}}
