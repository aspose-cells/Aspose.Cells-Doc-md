---
title: Hücre Referansı ile Resim Ekleme C++ ile
linktitle: Hücre Referansına Dayalı Bir Resim Eklemek
type: docs
weight: 150
url: /tr/cpp/insert-a-picture-based-on-cell-reference/
description: Aspose.Cells for C++ kullanarak hücre referansına göre nasıl resim eklenir öğrenin.
---

{{% alert color="primary" %}}

Bazen boş bir resminiz vardır ve resimde verileri veya içeriği bir hücre referansı belirleyerek göstermek istersiniz. Aspose.Cells bu özelliği destekler (Microsoft Excel 2010).

{{% /alert %}}

## Hücre Referansına Dayalı Bir Resim Eklemek

Aspose.Cells, bir resim şeklinde bir çalışma sayfası hücresindeki içeriği görüntülemenin destekler. Resmi, istemci tarafı uygulamasında kullanılan kolay Aspose.Cells API'sinin bir yöntemi olan [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) yöntemini çağırarak çalışma sayfasına ekleyebilirsiniz. Hücre aralığını, [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) nesnesinin [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) özelliğini kullanarak belirtin.

### Kod Örneği

```cpp
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    cells.Get(U16String(u"A1")).PutValue(U16String(u"A1"));
    cells.Get(U16String(u"C10")).PutValue(U16String(u"C10"));

    Aspose::Cells::Vector<uint8_t> imagedata = ConditionalFormattingIcon::GetIconImageData(IconSetType::TrafficLights31, 0);

    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddPicture(0, 3, imagedata, 10, 10);
    pic.SetFormula(U16String(u"A1:C10"));

    workbook.GetWorksheets().Get(0).GetShapes().UpdateSelectedValue();
    workbook.Save(outDir + u"referencedpicture.out.xlsx");

    std::cout << "Referenced picture added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
