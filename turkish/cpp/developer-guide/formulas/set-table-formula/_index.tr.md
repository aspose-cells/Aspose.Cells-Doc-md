---
title: C++ kullanarak yeni satırlara veri girerken tablo veya liste nesnesinde formülü otomatik olarak yaygınlaştırma
linktitle: Tablo Formülünü Ayarlar
type: docs
weight: 260
url: /tr/cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Aspose.Cells for C++ kullanarak yeni veri girerken tablolar veya liste nesnelerinde formülleri otomatik olarak yaygınlaştırmayı öğrenin.
---

## **Olası Kullanım Senaryoları**
Bazen, Tablo veya Liste Nesnenizdeki bir formülün yeni veriler girilirken otomatik olarak yayılmasını istersiniz. Bu, Microsoft Excel'in varsayılan davranışıdır. Aynı işlevselliği Aspose.Cells ile sağlamak için, [ListColumn::GetFormula](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listcolumn/getformula/) metodunu kullanın.

## **Yeni satırlara veri girilirken Tablo veya List Objesinde Formülü otomatik olarak çoğaltın**
Aşağıdaki örnek kod, B sütunundaki formülün yeni veriler girildiğinde otomatik olarak yeni satırlara yayılacak şekilde bir Tablo veya Liste Nesnesi oluşturur. Bu kodla üretilen [çıktı excel dosyasını](5115469.xlsx) kontrol edin. A3 hücresine herhangi bir sayı girerseniz, B2 hücresindeki formülün otomatik olarak B3 hücresine yayıldığını göreceksiniz.

```c++
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

    // Create workbook object
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add column headings in cell A1 and B1
    sheet.GetCells().Get(0, 0).PutValue(u"Column A");
    sheet.GetCells().Get(0, 1).PutValue(u"Column B");

    // Add list object, set its name and style
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(0, 0, 1, sheet.GetCells().GetMaxColumn(), true));
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium2);
    listObject.SetDisplayName(u"Table");

    // Set the formula of second column so that it propagates to new rows automatically while entering data
    listObject.GetListColumns().Get(1).SetFormula(u"=[Column A] + 1");

    // Save the workbook in xlsx format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
