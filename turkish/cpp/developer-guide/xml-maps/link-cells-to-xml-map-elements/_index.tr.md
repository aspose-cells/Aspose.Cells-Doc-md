---
title: Hücreleri XML Haritası Elemanlarına Bağlama (C++)
linktitle: Hücreleri XML Haritası Öğelerine Bağla
type: docs
weight: 50
url: /tr/cpp/link-cells-to-xml-map-elements/
description: Hücreleri XML Haritası elemanlarına bağlamanın yollarını Aspose.Cells kullanarak C++ ile öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells kullanarak, hücrelerinizi XML Haritası öğelerine bağlayabilirsiniz. Bu amaçla lütfen [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/linktoxmlmap/) yöntemini kullanın.

## **Xml Haritasına Hücreleri Bağlama**

Aşağıdaki örnek kod, XML Haritası içeren [kaynak excel dosyasını](5115471.xlsx) yükler ve ardından A1, B2, C3, D4, E5 ve F6 hücrelerini sırasıyla XML Haritası öğeleri FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 ve FIELD8 ile bağlar ve daha sonra kitabı [çıktı excel dosyası](5115467.xlsx) olarak kaydeder.

[Çıktı excel dosyasını](5115467.xlsx) açarsanız ve Geliştirici > Kaynak düğmesine tıklarsanız, hücrelerin XML Haritası öğelerine bağlandığını ve bunların Microsoft Excel tarafından aşağıdaki gibi vurgulandığını göreceksiniz.

```cpp
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

    // Load sample workbook
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the Xml Map inside it
    XmlMap map = wb.GetWorksheets().GetXmlMaps().Get(0);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Map FIELD1 and FIELD2 to cell A1 and B2
    ws.GetCells().LinkToXmlMap(map.GetName(), 0, 0, u"/root/row/FIELD1");
    ws.GetCells().LinkToXmlMap(map.GetName(), 1, 1, u"/root/row/FIELD2");

    // Map FIELD4 and FIELD5 to cell C3 and D4
    ws.GetCells().LinkToXmlMap(map.GetName(), 2, 2, u"/root/row/FIELD4");
    ws.GetCells().LinkToXmlMap(map.GetName(), 3, 3, u"/root/row/FIELD5");

    // Map FIELD7 and FIELD8 to cell E5 and F6
    ws.GetCells().LinkToXmlMap(map.GetName(), 4, 4, u"/root/row/FIELD7");
    ws.GetCells().LinkToXmlMap(map.GetName(), 5, 5, u"/root/row/FIELD8");

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
