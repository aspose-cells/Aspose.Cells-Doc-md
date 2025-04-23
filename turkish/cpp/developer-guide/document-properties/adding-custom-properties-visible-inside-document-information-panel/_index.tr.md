---
title: Belge Bilgileri Panelinde Görünen Özelleştirilmiş Özellikler Ekleme C++ ile
linktitle: Belge Bilgi Paneli içinde görülebilen Özel Özellikler eklemek
type: docs
weight: 300
url: /tr/cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Aspose.Cells ile C++ kullanarak Belge Bilgisi Panelinde görünür olan özelleştirilmiş özellikleri nasıl ekleyeceğinizi öğrenin.
---

## **Belge Bilgi Paneli içinde görülebilen Özel Özellikler eklemek**

Aspose.Cells, Belge Bilgi Paneli'nde görünen çalışma kitabı nesnesi içine özel özellikler eklemek için kullanılabilir. Microsoft Excel'de Belge Bilgi Paneli'ni Aç > Bilgi > Özellikler > Belgeyi Göster menü komutlarını kullanarak açabilirsiniz.

Lütfen belge bilgisi panelinde görünür olacak özelleştirilmiş özellik eklemek için [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) yöntemini kullanın.

Aşağıdaki örnek kod, iki özelleştirilmiş özellik ekler. Birinci özellik herhangi bir tipe sahip değildir, ikinci özellik ise tarih/zaman tipi taşır. Bu kodla oluşturulan çıktı Excel dosyasını açtığınızda, bu iki özelliği Belge Bilgisi Panelinde göreceksiniz.

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

    // Create workbook object with specified format
    Workbook workbook(FileFormatType::Xlsx);

    // Add simple property without any type
    workbook.GetContentTypeProperties().Add(u"MK31", u"Simple Data");

    // Add date time property with type
    workbook.GetContentTypeProperties().Add(u"MK32", u"04-Mar-2015", u"DateTime");

    // Save the workbook
    workbook.Save(srcDir + u"AddingCustomPropertiesVisible_out.xlsx");

    std::cout << "Custom properties added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **İlgili Makale**

{{% alert color="primary" %}}

- [Aspose.Cells'te Özel XML Parçalarını Kullanma](/cells/tr/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
