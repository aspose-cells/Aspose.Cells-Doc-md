---
title: Microsoft Excel ile OLE nesnesini otomatik yenilemeyi C++ kullanarak sağlayın
linktitle: Otomatik olarak OLE nesnesini yenile
type: docs
weight: 270
url: /tr/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Aspose.Cells kullanarak Microsoft Excel de OLE nesnelerini otomatik yenileme yöntemini öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel'de Excel dosyası açılırken OLE nesnesini yenilemek için [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getautoload/) özelliğini sağlar. Bu özellik sayesinde, OLE nesnesi Microsoft Excel tarafından oluşturulan doğru OLE görüntüsünü gösterecektir.

{{% /alert %}}

Aşağıdaki örnek kod, gerçek olmayan bir OLE görüntüsü içeren [örnek Excel dosyasını](5115231.xlsx) yükler. OLE nesnesi aslında bir Microsoft Word belgesidir, ancak örnek Excel dosyası, Microsoft Word görüntüsü yerine hayvan resmi gösterir. Ancak, [çıktı Excel dosyasını](5115225.xlsx) açarsanız, Microsoft Excel'in doğru OLE görüntüsünü gösterdiğini görürsünüz.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object from your sample excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Set auto load property of first ole object to true
    sheet.GetOleObjects().Get(0).SetAutoLoad(true);

    // Save the workbook in xlsx format
    wb.Save(srcDir + u"RefreshOLEObjects_out.xlsx", SaveFormat::Xlsx);

    std::cout << "OLE object refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
