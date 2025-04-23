---
title: C++ kullanarak Çalışma Kitabı ve Sayfa kapsamlı Tanımlı Aralıklar oluşturma
linktitle: Adlandırılmış Aralık
type: docs
weight: 40
url: /tr/cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Aspose.Cells kullanarak C++ ile çalışma kitabı ve sayfa kapsamlı tanımlı aralıklar oluşturmayı öğrenin.
---

{{% alert color="primary" %}} 

Microsoft Excel, kullanıcılara çalışma kitabı (aynı zamanda genel kapsam olarak da bilinir) ve çalışma sayfası olmak üzere iki farklı kapsamla adlandırılmış aralıkları tanımlama imkanı tanır.

- Bir çalışma kitabı kapsamına sahip adlandırılmış aralıklar, sadece isimlerini kullanarak o çalışma kitabındaki herhangi bir çalışma sayfasından erişilebilir.
- Çalışma sayfası kapsamlı adlandırılmış aralıklar, oluşturulduğu belirli çalışma sayfasına referansla erişilir.

Aspose.Cells, çalışma kitabı ve çalışma sayfası kapsamlı adlandırılmış aralıklar eklemek için Microsoft Excel ile aynı işlevselliği sağlar. Bir çalışma sayfası kapsamlı adlandırılmış aralık oluşturulurken, adlandırılmış aralıkta çalışma sayfası referansı kullanılmalıdır.

{{% /alert %}} 

## **Çalışma Kitabı Kapsamlı Adlandırılmış Aralık Ekleme**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells from Cell A1 to C10
    Range workbookScope = cells.CreateRange(u"A1", u"C10");

    // Assign the name to workbook scope named range
    workbookScope.SetName(u"workbookScope");

    // Save the workbook
    workbook.Save(srcDir + u"WorkbookScope.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Çalışma Sayfası Kapsamlı Adlandırılmış Aralık Ekleme**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells
    Range localRange = cells.CreateRange(u"A1", u"C10");

    // Assign name to range with sheet reference
    localRange.SetName(u"Sheet1!local");

    // Save the workbook
    U16String outputFilePath = u"..\\Data\\02_OutputDirectory\\output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Erişim Oluştur ve Adlandırılmış Aralıkları Kopyala](/cells/tr/cpp/create-access-and-copy-named-ranges/)
- [Biçimlendir ve Adlandırılmış Aralıkları Değiştir](/cells/tr/cpp/format-and-modify-named-ranges/)
- [Harici Bağlantıları Olan Aralığı Al](/cells/tr/cpp/get-range-with-external-links/)
- [Sıralı Olmayan Aralıkları Uygulama](/cells/tr/cpp/implementing-non-sequential-ranges/)

