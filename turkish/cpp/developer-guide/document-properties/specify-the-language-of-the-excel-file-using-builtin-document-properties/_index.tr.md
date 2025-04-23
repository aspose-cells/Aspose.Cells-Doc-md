---
title: Excel Dosyasının Dilini Yerleşik Belge Özellikleri ile Belirtme (C++ ile)
linktitle: Excel Dosyasının Dilini Belirtme
type: docs
weight: 30
url: /tr/cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
description: Aspose.Cells for C++ kullanarak bir Excel dosyasının dilini programlama yoluyla nasıl değiştireceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

 Bir Excel dosyasının dilini değiştirmek için dosyaya sağ tıklayın ve özellikler > ayrıntılar menüsünü seçin, sonra Dil alanını düzenleyin. Programatik olarak değiştirmek için [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/) özelliğini kullanın.

## **Dahili Belge Özelliklerini Kullanarak Excel Dosyasının Dilini Belirtme**

 Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve içindeki Dil adlı yerleşik belge özelliğini değiştirir. Lütfen bu kodla oluşturulan [çıktı Excel dosyasını](64716891.xlsx) ve değiştirilmiş Dil alanını gösteren ekran görüntüsünü inceleyin.

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Örnek Kod**

```c++
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

    // Set the language of the Excel file
    bdpc.SetLanguage(u"German, French");

    // Save the workbook in xlsx format
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx", SaveFormat::Xlsx);

    std::cout << "Language set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
