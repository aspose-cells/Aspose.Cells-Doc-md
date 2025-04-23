--- 
title: Excel olmadan C++ ile Dondurulmuş Durumu Nasıl Kontrol Ederim 
linktitle: Dondurulmuş Durum 
type: docs 
weight: 190 
url: /tr/cpp/how-to-check-frozen-state-of-excel-worksheet 
description: Bu makalede, Aspose.Cells API ile C++ kullanarak bir Excel çalışma sayfasının dondurma durumunu programlı olarak nasıl kontrol edeceğinizi öğreneceksiniz. 
--- 

## **Giriş** 

Bu makalede, bir Excel çalışma sayfasının donmuş durumunu programatik olarak nasıl kontrol edeceğimizi öğreneceğiz. MS Excel'de çalışma sayfasının donmuş veya bölünmüş olup olmadığını basitçe bulabiliriz. Ama C++ ile donmuş mu yoksa bölünmüş mü olduğunu bulmanın bir yolu var mı? Bunu Aspose.Cells for C++ ile yapabiliriz. 

## **Pencereler Dondurulmuş mu** 
Aspose.Cells for C++ ile pencerenin donmuş olup olmadığını ve kaç satır ve sütunun kilitli olduğunu kontrol edebiliriz. 

Lütfen [**GetPaneState()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getpanestate/) özelliğini kullanarak pencere bölmelerinin durumunu kontrol edin ve [**Worksheet::GetFreezedPanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getfreezedpanes/) yöntemiyle kilitli satır ve sütunları alın. 
1. Dosyayı açmak için Workbook'u oluşturun. 
2. Çalışma sayfasının dondurulup dondurulmadığını kontrol edin. 
3. Kilitli satır ve sütunları alın. 

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create the workbook from the specified file
    Workbook workbook(u"Frozen.xlsx");

    // Get the first worksheet from the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Check whether the worksheet is frozen
    if (sheet.GetPaneState() == PaneStateType::Frozen || sheet.GetPaneState() == PaneStateType::FrozenSplit)
    {
        int32_t row = 0, column = 0;
        int32_t rows = 0, columns = 0;

        // Get the locked rows and columns
        sheet.GetFreezedPanes(row, column, rows, columns);

        // Output the details if needed (just for demonstration)
        std::cout << "Frozen panes at Row: " << row << ", Column: " << column << ", Total Frozen Rows: " 
                  << rows << ", Total Frozen Columns: " << columns << std::endl;
    }

    Aspose::Cells::Cleanup();
}
``` 

