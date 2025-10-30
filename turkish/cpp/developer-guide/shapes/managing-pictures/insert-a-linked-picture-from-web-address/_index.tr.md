---
title: Web Adresinden Bağlantılı Resim Ekleme C++ ile
linktitle: Web Adresinden Bağlantılı Bir Resim Eklemek
type: docs
weight: 450
url: /tr/cpp/insert-a-linked-picture-from-web-address/
description: Bir web adresinden bağlı resmi bir çalışma sayfasına nasıl ekleyeceğinizi öğrenin Aspose.Cells for C++ kullanarak.
---

{{% alert color="primary" %}}

Bazen bir elektronik tabloya (http://) web'den bir resim eklemeniz gerekebilir. Bunu yapmak için resmin URL'sini belirtin ve resim, Microsoft Excel'de her açıldığında indirilir. Resim fiziksel olarak Excel belgesine gömülmez, ancak bir web kaynağına işaret eder.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de (örneğin 2007):

1. **Ekle** menüsünü tıklayın ve **Resim**'i seçin.
1. Resim Ekle iletişim kutusunda resmin web adresini belirtin.

## **Aspose.Cells for C++ Kullanarak**

Aspose.Cells for C++, [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlinkedpicture/) metodunu kullanarak bağlı bir resim eklemeyi destekler. Metod, bir [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) nesnesi döndürür.

Aşağıdaki örnek, bir web adresinden bağlı bir resmi çalışma sayfasına nasıl ekleyeceğinizi gösterir.

```cpp
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
    Workbook workbook;

    // Insert a linked picture (from Web Address) to B2 Cell
    U16String imageUrl(u"http://www.aspose.com/Images/aspose-logo.jpg");
    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddLinkedPicture(1, 1, 100, 100, imageUrl);

    // Set the height and width of the inserted image
    pic.SetHeightInch(1.04);
    pic.SetWidthInch(2.6);

    // Save the Excel file
    U16String outputPath = outDir + u"outLinkedPicture.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Linked picture inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
