---
title: C++ ile Adlandırılmış Aralıkları Silme
linktitle: Adlandırılmış Aralıkları Sil
type: docs
weight: 90
url: /tr/cpp/delete-named-ranges/
description: Farklı isim veya adlandırılmış aralıkları Excel veya OpenOffice dosyalarından kaldırmak için Aspose.Cells for C++ kullanmayı öğrenin.
---

## **Giriş**
Eğer Excel dosyalarında çok fazla tanımlanmış isim veya adlandırılmış aralık varsa, tekrar atıfta bulunulmadığından bazılarını temizlememiz gerekebilir.

## **MS Excel'de Adlandırılmış Aralığı Kaldır**

Excel'den adlandırılmış bir aralığı kaldırmak için şu adımları izleyebilirsiniz:
1. Microsoft Excel'i açın ve adlandırılmış aralığı içeren çalışma kitabını açın.
2. Excel kurdelesindeki "Formüller" sekmesine gidin.
3. "Tanımlı İsimler" grubundaki "Ad Yöneticisi" düğmesini tıklayın. Bu, Ad Yöneticisi iletişim kutusunu açacaktır.
4. Ad Yöneticisi iletişim kutusunda, kaldırmak istediğiniz adlandırılmış aralığı seçin.
5. "Sil" düğmesine tıklayın. İstenildiğinde silme işlemini onaylayın.
6. Ad Yöneticisi iletişim kutusunu kapatmak için "Kapat" düğmesine tıklayın.
7. Değişiklikleri korumak için çalışma kitabını kaydedin.

## **Aspose.Cells for C++ kullanarak Adlandırılmış Aralıkları Silme**
Aspose.Cells for C++ ile listede [metin](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/remove/) veya [indeks](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/) kullanarak adlandırılmış aralıkları veya tanımlanmış isimleri kaldırabilirsiniz.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete a named range by text
    worksheets.GetNames().Remove(u"NamedRange");

    // Delete a defined name by index
    worksheets.GetNames().RemoveAt(0);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Not: Eğer tanımlanmış isim formüller tarafından referans gösteriliyorsa, kaldırılamaz. Sadece tanımlanmış ismin formülü kaldırabiliriz.

## **Bazı Adlandırılmış Aralıkları Kaldırma**
Bir tanımlı ismi kaldırdığımızda, dosyadaki tüm formüller tarafından kullanılıp kullanılmadığını kontrol etmeliyiz.
Adlandırılmış aralıkların kaldırılmasının performansını artırmak için bazılarını birlikte kaldırabiliriz.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    Vector<U16String> namesToRemove = { u"NamedRange1", u"NamedRange2" };
    worksheets.GetNames().Remove(namesToRemove);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Yinelenen Tanımlı İsimleri Kaldırma**
Bazı Excel dosyaları, aynı isimli tanımlanmış isimler nedeniyle bozulur. Bu yüzden bu yinelenen isimleri kaldırıp dosyayı onarabiliriz.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    worksheets.GetNames().RemoveDuplicateNames();

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully after removing duplicate names!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
