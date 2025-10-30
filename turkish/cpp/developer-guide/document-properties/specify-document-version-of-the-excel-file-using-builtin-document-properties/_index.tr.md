---
title: Uygulamalı olarak Excel Dosyasının Belge Sürümünü Belge Özellikleri ile Belirtin (C++ ile)
linktitle: Belge Sürümünü Belirt
type: docs
weight: 20
url: /tr/cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Aspose.Cells for C++ kullanarak yerleşik belge özellikleriyle bir Excel dosyasının belge sürümünü nasıl belirteceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Bir Excel dosyasının **Sürüm numarasını** sağ tıklayıp özellikler > ayrıntılar menüsünden değiştirebilirsiniz ve ardından **Sürüm numarası** alanını düzenleyin. Programatik olarak değiştirmek için Lütfen [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/) özelliğini kullanın.

## **Aspose.Cells kullanarak Excel Dosyasının Belge Sürümünü Belirtme**

 Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve başlık, Yazarlar ve Sürüm numarası gibi yerleşik belge özelliklerini değiştirir. Lütfen kodla oluşturulan [çıktı Excel dosyasını](64716811.xlsx) ve değiştirilmiş Sürüm numarasını gösteren ekran görüntüsünü inceleyin.

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Properties;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access built-in document property collection
    BuiltInDocumentPropertyCollection bdpc = wb.GetBuiltInDocumentProperties();

    // Set the title
    bdpc.SetTitle(u"Aspose File Format APIs");

    // Set the author
    bdpc.SetAuthor(u"Aspose APIs Developers");

    // Set the document version
    bdpc.SetDocumentVersion(u"Aspose.Cells Version - 18.3");

    // Save the workbook in xlsx format
    wb.Save(u"outputSpecifyDocumentVersionOfExcelFile.xlsx", SaveFormat::Xlsx);

    std::cout << "Document properties set and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
