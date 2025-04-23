---
title: C++ kullanarak başka çalışma sayfalarındaki referansları güncelleyin, boş sütunları ve satırları silerken
linktitle: Diğer çalışma sayfalarındaki referansları güncelleyin
type: docs
weight: 5000
url: /tr/cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Aspose.Cells for C++ kullanarak bir çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları nasıl güncelleyeceğinizi öğrenin.
---

{{% alert color="primary" %}}

Bir çalışma sayfasında boş sütunları ve satırları sildiğinizde, diğer çalışma sayfalarındaki referanslar geçersiz hale gelir. Bu davranışı önlemek ve diğer çalışma sayfalarındaki geçerli çalışma sayfasına yapılan referansların da güncellenmesini sağlamak istiyorsanız, [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) özelliğini kullanın ve **true** olarak ayarlayın.

{{% /alert %}}

## **Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle**

Lütfen aşağıdaki örnek kodu ve konsol çıktısını inceleyin. İkinci çalışma sayfasındaki E3 hücresinde `=Sheet1!C3` formülü bulunmaktadır; bu, ilk çalışma sayfasındaki C3 hücresine referans verir. Eğer [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) özelliğini **true** yaparsanız, bu formül, ilk çalışma sayfasında boş sütunlar ve satırlar silindikten sonra `=Sheet1!A1` olarak güncellenecektir. Ancak, [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) özelliğini **false** yaparsanız, ikinci çalışma sayfasındaki E3 hücresindeki formül değişmeyecek ve geçersiz hale gelecektir.

### **Programlama Örneği**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Add second sheet with name Sheet2
    wb.GetWorksheets().Add(u"Sheet2");

    // Access first sheet and add some integer value in cell C1
    // Also add some value in any cell to increase the number of blank rows and columns
    Worksheet sht1 = wb.GetWorksheets().Get(0);
    sht1.GetCells().Get(u"C1").PutValue(4);
    sht1.GetCells().Get(u"K30").PutValue(4);

    // Access second sheet and add formula in cell E3 which refers to cell C1 in first sheet
    Worksheet sht2 = wb.GetWorksheets().Get(1);
    sht2.GetCells().Get(u"E3").SetFormula(u"'Sheet1'!C1");

    // Calculate formulas of workbook
    wb.CalculateFormula();

    // Print the formula and value of cell E3 in second sheet before deleting blank columns and rows in Sheet1.
    std::cout << "Cell E3 before deleting blank columns and rows in Sheet1." << std::endl;
    std::cout << "--------------------------------------------------------" << std::endl;
    std::cout << "Cell Formula: " << sht2.GetCells().Get(u"E3").GetFormula().ToUtf8() << std::endl;
    std::cout << "Cell Value: " << sht2.GetCells().Get(u"E3").GetStringValue().ToUtf8() << std::endl;

    // If you comment DeleteOptions.UpdateReference property below, then the formula in cell E3 in second sheet will not be updated
    DeleteOptions opts;
    opts.SetUpdateReference(true);

    // Delete all blank rows and columns with delete options
    sht1.GetCells().DeleteBlankColumns(opts);
    sht1.GetCells().DeleteBlankRows(opts);

    // Calculate formulas of workbook
    wb.CalculateFormula();

    // Print the formula and value of cell E3 in second sheet after deleting blank columns and rows in Sheet1.
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << "Cell E3 after deleting blank columns and rows in Sheet1." << std::endl;
    std::cout << "--------------------------------------------------------" << std::endl;
    std::cout << "Cell Formula: " << sht2.GetCells().Get(u"E3").GetFormula().ToUtf8() << std::endl;
    std::cout << "Cell Value: " << sht2.GetCells().Get(u"E3").GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Konsol Çıktısı**

Yukarıdaki örnek kodun, [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) özelliği **true** ayarlandığında ortaya çıkan konsol çıktısı.

{{< highlight java >}}

Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4

Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!A1
Cell Value: 4

{{< /highlight >}}

Yukarıdaki örnek kodun, [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) özelliği **false** ayarlandığında ortaya çıkan konsol çıktısı. Gördüğünüz gibi, ikinci çalışma sayfasındaki E3 hücresindeki formül güncellenmedi ve hücre değeri artık 4 yerine 0 oldu, bu da geçersizdir.

{{< highlight java >}}

Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4

Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 0

{{< /highlight >}}
