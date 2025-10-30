---
title: Office Eklentilerini Excel den PDF ye dönüştürürken Render Etme  C++ ile
linktitle: Excel i PDF e dönüştürürken Office Eklentilerini Oluşturma
type: docs
weight: 100
url: /tr/cpp/render-office-add-ins-while-converting-excel-to-pdf/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını PDF ye dönüştürürken Office Eklentilerini render etme öğrenin.
---

## **Olası Kullanım Senaryoları**

Önceden, Aspose.Cells, Excel dosyası PDF'ye kaydedildiğinde Office Eklentilerini render edemiyordu. Şimdi, Aspose.Cells doğru şekilde render eder. Office Eklentilerini çıktı PDF'sinde görselleştirmek için herhangi bir özel yöntem veya özellik kullanmanıza gerek yoktur. Sadece Excel dosyanızı PDF formatında kaydedin ve Office Eklentilerini render edecektir.

## **Excel'i PDF'e dönüştürürken Office Eklentilerini renderla**

Aşağıdaki örnek kod, Office Eklentilerini içeren [örnek Excel dosyasını](60489769.xlsx) kaydeder. Lütfen önceki sürümle (örneğin 17.11) oluşturulan çıktı PDF'yi ve yeni sürümle (örneğin 17.12 ve sonrası) oluşturulan çıktı PDF'yi inceleyin. Önceki sürüm çıktı PDF'si boştur, ancak yeni sürüm çıktı PDF'si Office Eklentisi'ni gösterir.

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file containing Office Add-Ins
    U16String inputFilePath = u"sampleRenderOfficeAdd-Ins.xlsx";
    Workbook wb(inputFilePath);

    // Save it to Pdf format with version appended to the output filename
    U16String outputFilePath = u"output-" + CellsHelper::GetVersion() + u".pdf";
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "File saved successfully: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
