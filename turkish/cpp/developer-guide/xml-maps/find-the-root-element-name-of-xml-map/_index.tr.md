---
title: C++ kullanarak XML Haritasının Kök Eleman Adını Bulma
linktitle: XML Haritasının Kök Öğe Adını Bul
type: docs
weight: 30
url: /tr/cpp/find-the-root-element-name-of-xml-map/
description: Aspose.Cells for C++ kullanarak XML haritasının kök eleman adını nasıl bulunacağını öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells ile *Xml Haritasının Kök Öğe Adı* kullanarak [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/) özelliğini bulabilirsiniz. Aşağıdaki ekran görüntüsü, XML Haritasının Microsoft Excel içindeki kök öğe adını gösterir.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Örnek Kod**

Aşağıdaki örnek kod, [örnek Excel dosyasını](55541789.xlsx) yükler ve ilk XML Haritasına erişir ve [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/) özelliğini yazdırır. Lütfen aşağıda verilen örnek kodun konsol çıktısını görün.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleRootElementNameOfXmlMap.xlsx";

    // Load sample Excel file having Xml Map
    Workbook wb(inputFilePath);

    // Access first Xml Map inside the Workbook
    XmlMap xmap = wb.GetWorksheets().GetXmlMaps().Get(0);

    // Print Root Element Name of Xml Map on Console
    std::cout << "Root Element Name Of Xml Map: " << xmap.GetRootElementName().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsol Çıktısı**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
