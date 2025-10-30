---
title: C++ ile ContentTypeProperties ile Çalışmak
linktitle: ContentTypeProperties ile Çalışma
type: docs
weight: 150
url: /tr/cpp/working-with-contenttypeproperties/
description: Aspose.Cells kullanarak bir Excel dosyasına özel ContentTypeProperties ekleyin.
---

Aspose.Cells, Excel dosyasına özel ContentTypeProperties eklemek için [**Workbook.ContentTypeProperties.Add**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) yöntemini sağlar. Ayrıca, [**ContentTypeProperty.IsNillable**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypeproperty/isnillable/) özelliğini **true** olarak ayarlayarak özelliği isteğe bağlı hale getirebilirsiniz. Aşağıdaki kod örneği, isteğe bağlı özel ContentTypeProperties'lerin bir Excel dosyasına nasıl ekleneceğini gösterir. Aşağıdaki resim, örnek kod tarafından eklenen her iki özelliği de göstermektedir.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Örnek kod tarafından oluşturulan çıktı dosyası referans için ekte bulunmaktadır.

[Çıkış Dosyası](95584314.xlsx)

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook with XLSX format
    Workbook workbook(FileFormatType::Xlsx);

    // Add content type properties
    int index = workbook.GetContentTypeProperties().Add(u"MK31", u"Simple Data");
    workbook.GetContentTypeProperties().Get(index).SetIsNillable(false);

    // Get current date and time
    time_t now = time(nullptr);
    char buffer[80];
    strftime(buffer, sizeof(buffer), "%Y-%m-%dT%H:%M:%S", localtime(&now));
    U16String dateTime(buffer);

    // Add another content type property with current date and time
    index = workbook.GetContentTypeProperties().Add(u"MK32", dateTime, u"DateTime");
    workbook.GetContentTypeProperties().Get(index).SetIsNillable(true);

    // Save the workbook
    workbook.Save(outDir + u"WorkingWithContentTypeProperties_out.xlsx");

    std::cout << "Content type properties added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
