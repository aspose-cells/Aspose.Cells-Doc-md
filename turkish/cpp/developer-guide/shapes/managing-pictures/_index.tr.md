---
title: C++ ile Resimleri Yönetmek
linktitle: Resim Yönetimi
type: docs
weight: 10
url: /tr/cpp/managing-pictures/
description: API kullanarak çalışma sayfalarında resimleri ekleyin, konumlandırın ve yönetin. Aspose.Cells for C++.
---

Aspose.Cells, geliştiricilere çalışma zamanında elektron mikroskobu resimlerini elektron mikroskobuna eklemelerine olanak tanır. Dahası, bu resimlerin konumu çalışma zamanında kontrol edilebilir, bu daha sonra detaylı olarak tartışılacaktır.

Bu makale, resim eklemenin ve belirli hücrelerin içeriğini gösteren bir resmin nasıl eklenmesinin açıklamasını içerir.

## **Resim Ekleme**

Bir elektron mikroskobuna resim eklemek çok kolaydır. Sadece birkaç satır kod gerektirir:
Sadece, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) nesnesinde kapsüllenmiş [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) nesnesinin [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) metodunu çağırın. [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) metodunun aşağıdaki parametreleri alır:

- **Sol üst satır dizini**, sol üst sütunun dizini.
- **Sol üst sütun dizini**, sol üst sütunun dizini.
- **Resim dosya adı**, yol bilgisi ile birlikte resim dosyasının adı.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Add worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add image to worksheet at F6 (row 5, column 5)
    U16String imagePath = srcDir + u"logo.jpg";
    worksheet.GetPictures().Add(5, 5, imagePath);

    // Save workbook
    U16String outputPath = outDir + u"output.xls";
    workbook.Save(outputPath);

    std::cout << "Worksheet with image created successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Resim Konumlandırma**

Aspose.Cells kullanarak resimlerin konumlandırılmasını kontrol etmek için iki olası yol bulunmaktadır:

- Oransal konumlandırma: satır yüksekliği ve genişliğine oranla bir konum tanımlayın.
- Mutlak konumlandırma: resmi ekleyeceğiniz sayfa üzerindeki tam konumu tanımlayın, örneğin, hücrenin solundan 40 piksel ve altından 20 piksel.

### **Oransal Konumlandırma**

Geliştiriciler, [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) nesnesinin [**UpperDeltaX**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltax/) ve [**UpperDeltaY**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltay/) özelliklerini kullanarak resimleri satır yüksekliğine ve sütun genişliğine orantılı olarak konumlandırabilirler. Bir [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) nesnesi, [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) nesnesinden görüntü indeksini geçirerek elde edilebilir. Bu örnek, F6 hücresine bir görüntü yerleştirir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Add new worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add picture to worksheet at (5,5) position
    U16String imagePath = outDir + u"logo.jpg";
    int pictureIndex = worksheet.GetPictures().Add(5, 5, imagePath);

    // Access added picture and set positioning
    Drawing::Picture picture = worksheet.GetPictures().Get(pictureIndex);
    picture.SetUpperDeltaX(200);
    picture.SetUpperDeltaY(200);

    // Save modified workbook
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Picture added and positioned successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Mutlak Konumlandırma**

Geliştiriciler, resimleri [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) nesnesinin [**Left**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getleft/) ve [**Top**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettop/) özelliklerini kullanarak mutlak olarak da konumlandırabilirler. Bu örnek, resmi F6 hücresine sol üstten 60 piksel ve üstten 10 piksel uzaklığa yerleştirir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access worksheet collection and add new sheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    int sheetIndex = worksheets.Add();

    // Get reference to newly added worksheet
    Worksheet worksheet = worksheets.Get(sheetIndex);

    // Add picture to worksheet at row 5, column 5 (cell F6)
    PictureCollection pictures = worksheet.GetPictures();
    int pictureIndex = pictures.Add(5, 5, srcDir + u"logo.jpg");

    // Access added picture and set position
    Picture picture = pictures.Get(pictureIndex);
    picture.SetLeft(60);
    picture.SetTop(10);

    // Save modified workbook
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Workbook with inserted picture saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Hücre Referansına Dayalı Resim Ekleme**

Aspose.Cells, bir çalışma sayfası hücresinin içeriğini bir görüntü şeklinde görüntülemenizi sağlar. Verilerin görüntülenmesini istediğiniz hücreye bağlayabilirsiniz. Hücre veya hücre aralığı grafik nesnesine bağlandığından, o hücre veya hücre aralığındaki değişiklikler otomatik olarak grafik nesnesinde görünür.

Bir resmi, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) nesnesinde kapsüllenmiş [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) metodunu çağırarak çalışma sayfasına ekleyin. Hücre aralığını [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) nesnesinin [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) özelliği ile belirtin.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access first worksheet and cells collection
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    Cells cells = worksheet.GetCells();

    // Set cell values
    cells.Get(u"A1").PutValue(U16String(u"A1"));
    cells.Get(u"C10").PutValue(U16String(u"C10"));

    // Add picture to worksheet
    auto shapes = worksheet.GetShapes();
    Picture pic = shapes.AddPicture(0, 3, 10, 6, Vector<uint8_t>());

    // Set picture formula and update values
    pic.SetFormula(u"A1:C10");
    shapes.UpdateSelectedValue();

    // Save workbook
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Hücre Metni ile Koşullu İkon Takımı Ekle](/cells/tr/cpp/add-conditional-icons-set-with-the-cell-text/)
- [Web Adresinden Bağlantılı Resim Ekle](/cells/tr/cpp/insert-a-linked-picture-from-web-address/)
- [Hücre Referansına Dayalı Resim Ekle](/cells/tr/cpp/insert-a-picture-based-on-cell-reference/)
- [Bir URL'den Web Resmi Yükleyerek Excel Çalışma Sayfasına Ekleyin](/cells/tr/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
