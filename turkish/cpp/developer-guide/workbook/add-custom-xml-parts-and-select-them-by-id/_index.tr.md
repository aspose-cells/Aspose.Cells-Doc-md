---
title: C++ kullanarak Özel XML Parçaları Ekleyin ve Kimlik ile Seçin
linktitle: Özel XML Parçalarını Ekleyin ve ID leri ile Seçin
type: docs
weight: 70
url: /tr/cpp/add-custom-xml-parts-and-select-them-by-id/
description: Aspose.Cells ile C++ kullanarak Excel dosyalarında özel XML parçalarını eklemeyi ve seçmeyi öğrenin.
---

## **Olası Kullanım Senaryoları**

Özel XML Parçaları, Microsoft Excel belgeleri içinde depolanan XML verileridir ve bunlarla etkileşimde bulunan uygulamalar tarafından kullanılır. Şu anda bunları eklemenin doğrudan bir yolu Microsoft Excel UI kullanılarak yoktur. Ancak, bunları programlı olarak, VSTO veya Aspose.Cells kullanarak çeşitli yollarla ekleyebilirsiniz. Aspose.Cells API'sini kullanarak bir Özel XML Parçası eklemek için [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/) metodunu kullanın. Ayrıca, kimliğini [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/) özelliğiyle ayarlayabilirsiniz. Benzer şekilde, bir XML Parçasını Kimlik ile seçmek için [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/) metodunu kullanabilirsiniz.

## **Özel XML Parçalarını ekleyin ve ID'leri ile seçin**

Aşağıdaki örnek kod öncelikle [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/) yöntemiyle dört Özel XML Parçası ekler. Ardından, kimliklerini [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/) özelliğiyle ayarlar. Son olarak, eklenen Özel XML Parçalarından birini bulur veya seçer. Lütfen aşağıdaki kodun konsol çıkışını referans olarak inceleyin.

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Markup;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Some data in the form of byte array
    // Please use correct XML and Schema instead
    Vector<uint8_t> btsData = { 1, 2, 3 };
    Vector<uint8_t> btsSchema = { 1, 2, 3 };

    // Create four custom xml parts
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);

    // Assign ids to custom xml parts
    wb.GetCustomXmlParts().Get(0).SetID(u"Fruit");
    wb.GetCustomXmlParts().Get(1).SetID(u"Color");
    wb.GetCustomXmlParts().Get(2).SetID(u"Sport");
    wb.GetCustomXmlParts().Get(3).SetID(u"Shape");

    // Specify search custom xml part id
    U16String srchID = u"Fruit";
    srchID = u"Color";
    srchID = u"Sport";

    // Search custom xml part by the search id
    CustomXmlPart cxp = wb.GetCustomXmlParts().SelectByID(srchID);

    // Print the found or not found message on console
    if (cxp.IsNull())
    {
        std::cout << "Not Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }
    else
    {
        std::cout << "Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }

    std::cout << "AddCustomXMLPartsAndSelectThemByID executed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsol Çıktısı**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
