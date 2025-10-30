---
title: Hücre Değeri Metninin Genişliğini C++ ile alın
linktitle: Hücre Değeri Metnin Genişliğini Alma
type: docs
weight: 50
url: /tr/cpp/get-text-width-of-cell-value/
description: Aspose.Cells for C++ API kullanarak Hücre Değeri Metninin genişliğini nasıl alacağınızı öğrenin.
keywords: Hücre Değerinin Metin Genişliğini Alın, Hücre Değerinin Metin Genişliğini Elde Edin
---

## **Hücre Değeri Metnin Genişliğini Alma**

Bazen geliştiriciler, veriyi düzenlemek için hücrenin değerinin genişliğini hesaplamaları gerekebilir. Aspose.Cells, geliştiricilerin hücrenin değerinin metin genişliğini almalarına olanak tanıyan [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/) metodunu sağlar. Aşağıdaki örnek kod, [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/) kullanarak hücrenin metin genişliğine nasıl erişileceğini gösterir.

Aşağıdaki kod parçasında kullanılan Kaynak dosyası, referansınız için ekte bulunmaktadır.

[Kaynak Dosya](96928090.xlsx)

## Örnek Kod

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory path for source files
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook from the specified Excel file
    Workbook workbook(sourceDir + u"GetTextWidthSample.xlsx");

    // Calculate the text width for the string value of cell A1
    double textWidth = CellsHelper::GetTextWidth(workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue(), workbook.GetDefaultStyle().GetFont(), 1);

    // Output the text width
    std::wcout << u"Text width: " << textWidth << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
