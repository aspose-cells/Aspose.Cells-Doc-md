---
title: Excel veya OpenOffice e C++ kullanarak Bağlantılar Ekleyin
linktitle: Hyperlinkleri Yönetme
type: docs
weight: 45
url: /tr/cpp/insert-hyperlinks-to-excel/
description: MS Excel kullanmadan Aspose.Cells kütüphanesi ile Excel dosyasına nasıl bağlantı eklenir.
keywords: Excel e Hyperlink Ekleme, Bağlantı Ekleme, URL ye Bağlantı Ekleme, Bir Hücreye Bağlantı Ekleme, Bir Dış Dosyaya Bağlantı Ekleme
---

{{% alert color="primary" %}} 

Bir bağlantı, iki varlık arasında bir bağlantı oluşturmak için kullanılır. Herkes, özellikle web sitelerinde bağlantıların kullanımı hakkında bilgilidir.
Aspose.Cells kullanarak, geliştiriciler Microsoft Excel dosyalarında farklı türde bağlantılar oluşturabilir. Bu konu, Aspose.Cells tarafından desteklenen bağlantı türlerini ve bunların Excel dosyalarımızda nasıl kullanılabileceğini tartışmaktadır.

{{% /alert %}} 

## **Hyperlinkler Ekleme**
Aspose.Cells, geliştiricilerin hem API kullanarak hem de tasarımcı tabloları (manuel olarak bağlantıların oluşturulduğu ve Aspose.Cells'in diğer tablolara aktarım için kullanıldığı tablolar) ile bağlantılar eklemesine olanak tanır.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her sayfaya erişim sağlayan [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) içerir. Bir sayfa [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, Excel dosyalarına farklı bağlantılar eklemek için çeşitli yöntemler sağlar.

## **URL'ye Bağlantı Ekleme**
[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, bir [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/) koleksiyonunu içerir. [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/) koleksiyonundaki her öğe, bir [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/) ile temsil edilir. URL'lere bağlantılar eklemek için [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) koleksiyonunun [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) metodunu çağırın. [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) yöntemi aşağıdaki parametreleri alır.

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, URL adresi.

```cpp
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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a hyperlink to cell "A1"
    worksheet.GetHyperlinks().Add(u"A1", 1, 1, u"http://www.aspose.com");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Yukarıdaki örnekte, bir hiper bağlantı boş bir hücre olan **A1**'e eklenir. Bu tür durumlarda, hücre boşsa, URL adresi de boş hücreye değeri olarak eklenir. Hücre dolu değilse ve bir hiper bağlantı eklenmişse, hücrenin değeri düz metin olarak görünür. Onu bir hiper bağlantı gibi görünmesini sağlamak için o hücreye uygun biçimlendirme ayarlarını uygulayın.

{{% /alert %}} 

## **Aynı Dosyadaki Bir Hücreye Bağlantı Ekleme**
Aynı Excel dosyasındaki hücrelere bağlantılar eklemek için [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) koleksiyonunun [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) metodunu çağırabilirsiniz. [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) yöntemi hem dahili hem de harici bağlantılar için çalışır. Aşırı yüklenmiş yöntemin bir sürümü aşağıdaki parametreleri alır.

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef hücrenin adresi.

```cpp
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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in
    // The same Excel file
    worksheet.GetHyperlinks().Add(u"B3", 1, 1, u"Sheet2!B9");

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Harici Bir Dosyaya Bağlantı Ekleme**
Harici Excel dosyalarına bağlantılar eklemek için [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) koleksiyonunun [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) metodunu çağırabilirsiniz. [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) yöntemi aşağıdaki parametreleri alır.

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef harici Excel dosyasının adresi.

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Add an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
    worksheet.GetHyperlinks().Add(U16String(u"A5"), 1, 1, srcDir + U16String(u"book1.xls"));

    // Save the Excel file
    workbook.Save(outDir + U16String(u"output.out.xls"));

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Görüntü Bağlantılarını Eklemek](/cells/tr/cpp/add-image-hyperlinks/)
- [Bağlantı Türünü Algılamak](/cells/tr/cpp/detect-hyperlink-type/)
- [Çalışma Sayfasının Bağlantılarını Düzenleme](/cells/tr/cpp/editing-hyperlinks-of-worksheet/)
- [Aralıktaki Bağlantıları Al](/cells/tr/cpp/get-hyperlinks-in-range/)
