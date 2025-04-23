---
title: XLS ve XLSX formatlarının desteklediği Maksimum Satır ve Sütun Sayısını C++ ile Bulma
linktitle: Maksimum Satır ve Sütunları Bul
type: docs
weight: 20
url: /tr/cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: XLS ve XLSX formatlarının desteklediği maksimum satır ve sütunları bulmak için Aspose.Cells for C++ kullanmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Excel formatlarının desteklediği satır ve sütun sayıları farklıdır. Örneğin, XLS 65536 satır ve 256 sütun desteklerken, XLSX 1048576 satır ve 16384 sütun destekler. Belirli bir formatın kaç satır ve sütunu desteklediğini öğrenmek için [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) ve [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) özelliklerini kullanabilirsiniz.

## **XLS ve XLSX formatları tarafından desteklenen maksimum satır ve sütun sayısını bulun.**

Aşağıdaki örnek kod, ilk olarak XLS formatında, sonra XLSX formatında bir çalışma kitabı oluşturur. Oluşturulduktan sonra, [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) ve [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) özelliklerinin değerlerini yazdırır. Lütfen aşağıda verilen kodun konsol çıktılarına bakınız.

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Print message about XLS format.
    std::cout << "Maximum Rows and Columns supported by XLS format." << std::endl;

    // Create workbook in XLS format.
    Workbook wb(FileFormatType::Excel97To2003);

    // Print the maximum rows and columns supported by XLS format.
    int maxRows = wb.GetSettings().GetMaxRow() + 1;
    int maxCols = wb.GetSettings().GetMaxColumn() + 1;
    std::cout << "Maximum Rows: " << maxRows << std::endl;
    std::cout << "Maximum Columns: " << maxCols << std::endl;
    std::cout << std::endl;

    // Print message about XLSX format.
    std::cout << "Maximum Rows and Columns supported by XLSX format." << std::endl;

    // Create workbook in XLSX format.
    wb = Workbook(FileFormatType::Xlsx);

    // Print the maximum rows and columns supported by XLSX format.
    maxRows = wb.GetSettings().GetMaxRow() + 1;
    maxCols = wb.GetSettings().GetMaxColumn() + 1;
    std::cout << "Maximum Rows: " << maxRows << std::endl;
    std::cout << "Maximum Columns: " << maxCols << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsol Çıktısı**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
