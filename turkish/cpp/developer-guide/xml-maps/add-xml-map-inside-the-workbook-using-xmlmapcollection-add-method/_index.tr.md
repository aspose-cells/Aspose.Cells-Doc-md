---
title: XmlMapCollection.Add yöntemiyle Çalışma kitabı içine XML Haritası ekleyin (C++)
linktitle: XmlMapCollection.Add Yöntemi Kullanarak Çalışma Kitabının İçine XML Haritası Ekle
type: docs
weight: 10
url: /tr/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/
description: Çalışma kitabı içine XmlMapCollection.Add yöntemiyle XML Haritası ekleyin (C++)
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, XML Haritasını kitap içine eklemek için kullanabileceğiniz [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) yöntemi sağlar.

## **XmlMapCollection.Add yöntemini kullanarak İçine 'XmlMap' ekleyin**

Aşağıdaki örnek kod, Kitap içine XML Haritası ekler ve [çıktı excel dosyasını](5115434.xlsx) olarak kaydeder. Ekran görüntüsü, [örnek.xml](5115433.xml) içinden alınan XML Haritasını gösterir.

![add-xml-map](add-xml-map.png)

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

    // Path of input XML file
    U16String inputXmlMap = srcDir + u"sample.xml";

    // Create workbook object
    Workbook workbook;

    // Add XML map found inside the sample.xml inside the workbook
    workbook.GetWorksheets().GetXmlMaps().Add(inputXmlMap);

    // Save the workbook in xlsx format
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully as xlsx format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
