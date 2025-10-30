---
title: C++ ile Hücre Değerinin Genişliğini ve Yüksekliğini Piksel Birimiyle Ölçün
linktitle: Boyutu Ölçün
type: docs
weight: 260
url: /tr/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Aspose.Cells for C++ API kullanarak Hücre değeri genişliği ve yüksekliğini nasıl ölçeceğinizi öğrenin.
keywords: Hücre Değerinin Genişliğini Piksel Birimiyle Ölçün, Hücre Değerinin Yüksekliğini Piksel Birimiyle Ölçün, Hücre Değerinin Genişliğini Piksel Birimiyle Alın, Hücre Değerinin Yüksekliğini Piksel Birimiyle Alın.
---

{{% alert color="primary" %}}

Bazen hücre değerinin genişliğini ve yüksekliğini, hücre içine hücre değerini sığdırmak için hesaplamanız gerekir. Aspose.Cells bu amaçla [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) ve [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) yöntemlerini sağlar. Bu yöntemleri kullanarak hücre değerinin genişliğini ve yüksekliğini hesaplayabilir, ardından o hücrenin sütun genişliğini ve satır yüksekliğini ayarlayabilirsiniz ve bu, hücre değerini hücrenin içine otomatik olarak ayarlar veya sığdırır.

Alternatif olarak, [hücre ya da hücre aralığının otomatik uyumunu sağlama]( /cells/tr/cpp/autofit-rows-and-columns/) Aspose.Cells API'larını kullanarak yapabilirsiniz.

{{% /alert %}}

Aşağıdaki kod, [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) ve [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) yöntemlerinin kullanımını açıklar.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell B2 and add some value inside it
    Cell cell = worksheet.GetCells().Get(u"B2");
    cell.PutValue(u"Welcome to Aspose!");

    // Enlarge its font to size 16
    Style style = cell.GetStyle();
    style.GetFont().SetSize(16);
    cell.SetStyle(style);

    // Calculate the width and height of the cell value in unit of pixels
    int32_t widthOfValue = cell.GetWidthOfValue();
    int32_t heightOfValue = cell.GetHeightOfValue();

    // Print both values
    std::wcout << u"Width of Cell Value: " << widthOfValue << std::endl;
    std::wcout << u"Height of Cell Value: " << heightOfValue << std::endl;

    // Set the row height and column width to adjust/fit the cell value inside cell
    worksheet.GetCells().SetColumnWidthPixel(1, widthOfValue);
    worksheet.GetCells().SetRowHeightPixel(1, heightOfValue);

    // Save the output excel file
    U16String outFilePath = u"output_out.xlsx";
    workbook.Save(outFilePath);

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Hücre Değeri Metnin Genişliğini Alma](/cells/tr/cpp/get-text-width-of-cell-value/)
{{< app/cells/assistant language="cpp" >}}
