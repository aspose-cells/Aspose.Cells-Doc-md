---
title: Yüklü Belge Özelliklerinin ScaleCrop ve LinksUpToDate Özelliklerini C++ ile Ayarlama
linktitle: ScaleCrop ve LinksUpToDate Özelliklerini Ayarlama
type: docs
weight: 320
url: /tr/cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Aspose.Cells for C++ kullanarak yerleşik belge özelliklerinin ScaleCrop ve LinksUpToDate özelliklerini nasıl ayarlayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**
[GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) ve [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) yerleşik belge özellikleri OpenXml formatında tanımlanmış iki genişletilmiş yerleşik özellik. Bu özelliklerin amacı şöyledir:

## **1) ScaleCrop**
Bu öğe, belge küçüğünün görüntüleme modunu gösterir. Belge küçüğünü ekranın uygun şekilde ölçeklendirmesi için bu öğeyi **TRUE** olarak ayarlayın. Yalnızca ekranın sığabileceği bölümleri göstermek için bu öğeyi **FALSE** olarak ayarlayın.

Bu öğe için olası değerler, W3C XML Şema boolean veri türü tarafından tanımlanır.

## **2) LinksUpToDate**
Bu öğe, bir belgedeki hiperbağlantıların güncel olup olmadığını gösterir. Hiperbağlantıların güncellendiğini belirtmek için bu öğeyi **TRUE** olarak ayarlayın. Hiperbağlantıların güncel olmadığını belirtmek için bu öğeyi **FALSE** olarak ayarlayın.

Bu öğe için olası değerler, W3C XML Şema boolean veri türü tarafından tanımlanır.

## **Bu özellikleri app.xml dosyası içinde gösteren ekran görüntüsü**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Yerleşik Belge Özelliklerinin ScaleCrop ve LinksUpToDate özelliklerini ayarlama**
 Aşağıdaki örnek kod, çalışma kitabının genişletilmiş yerleşik belge özellikleri olan GetScaleCrop() ve GetLinksUpToDate() ayarlamaktadır. Lütfen bu kodla oluşturulan çıktı excel dosyasını (.xlsx) kontrol edin, uzantısını .zip yapın ve içeriğini çıkarın, sonra app.xml'i yukarıdaki ekran görüntüsünde gösterildiği gibi görüntüleyin.

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

    // Instantiating a Workbook object.
    Workbook workbook;

    // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
    workbook.GetBuiltInDocumentProperties().SetScaleCrop(true);
    workbook.GetBuiltInDocumentProperties().SetLinksUpToDate(true);

    // Saving the Excel file.
    workbook.Save(outDir + u"output.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
