---
title: Izgara çizgilerini ve Satır Sütun Başlıklarını Göster ve Gizle  C++ ile
linktitle: Izgara Çizgileri ve Satır Sütun Başlıklarını Gösterme ve Gizleme
type: docs
weight: 30
url: /tr/cpp/show-and-hide-gridlines-and-row-column-headers/
description: Bu makale, C++ API veya Kütüphanesini kullanarak bir Excel çalışma sayfasında ızgara çizgilerini, satır ve sütun başlıklarını programatik olarak gizlemek veya göstermek için örnek kodlar sağlar.
---

{{% alert color="primary" %}}

Aspose.Cells, varsayılan olarak görünür olan çalışma taşraflarının izgara çizgilerini gizleme ve göstermeyi destekler. Aynı zamanda çalışma taşraflarının Satır Sütun Başlıklarının görünürlüğünü kontrol etmeyi sağlar.

{{% /alert %}}

## **Izgara Çizgilerini Gösterme ve Gizleme**

Tüm Excel çalışma taşraları varsayılan olarak izgara çizgilerine sahiptir. Onlar, belirli hücrelere veri girmeyi kolaylaştırdığı için hücreleri çevreler. Izgara çizgileri, bir çalışma taşrasını hücre koleksiyonu olarak görüntülememizi sağlar, burada her hücre kolayca tanımlanabilir.

### **Izgaraların Görünürlüğünü Kontrol Etme**

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı ile bir Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine olanak tanıyan bir [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyon içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışma sayfasını yönetmek için çeşitli özellikler ve yöntemler sağlar. Izgara çizgilerinin görünürlüğünü kontrol etmek için [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) özelliğini kullanın. [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) bir Boolean özelliğidir, yani yalnızca doğru ya da yanlış değeri saklar.

#### **Izgaraları Görünür Yapma**

Izgara çizgilerini görünür yapmak için [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) özelliğini **true** yapın.

#### **Izgaraları Gizleme**

Izgara çizgilerini gizlemek için [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) özelliğini **false** yapın.

Aşağıda verilen tam örnek, [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) özelliğini kullanarak bir excel dosyasını (book1.xls) açmayı, ilk çalışma sayfasındaki ızgara çizgilerini gizlemeyi ve değiştirilmiş dosyayı output.xls olarak kaydetmeyi göstermektedir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the grid lines of the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Grid lines hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Satır Sütun Başlıklarını Göster ve Gizle**

Bir Excel dosyasındaki tüm çalışma sayfaları, satırlar ve sütunlarda düzenlenmiş hücrelerden oluşur. Tüm satırlar ve sütunlar benzersiz değerlere sahiptir ve bunları tanımlamak ve bireysel hücreleri tanımlamak için kullanılır. Örneğin, satırlar numaralandırılır - 1, 2, 3, 4, vb. - ve sütunlar alfabetik sıraya göre düzenlenir - A, B, C, D, vb. Satır ve sütun değerleri başlıklarda görüntülenir. Aspose.Cells kullanılarak, geliştiriciler bu satır ve sütun başlıklarının görünürlüğünü kontrol edebilir.

### **Çalışma sayfalarının görünürlüğünü kontrol etmek**

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı ile bir Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine olanak tanıyan bir [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyon içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışma sayfasını yönetmek için çeşitli özellikler ve yöntemler sağlar. Satır ve sütun başlıklarının görünürlüğünü kontrol etmek için [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) özelliğini kullanın. [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) bir Boolean özelliğidir, yani yalnızca doğru ya da yanlış değeri saklar.

#### **Satır/Sütun Başlıklarını Görünür Yapma**

Satır ve sütun başlıklarını görünür yapmak için [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) özelliğini **true** yapın.

#### **Satır/Sütun Başlıklarını Gizleme**

Boş hücreleri gizleyip göstermek için, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) özelliğini **false** olarak ayarlayınız.

Aşağıda, [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) özelliğinin nasıl kullanılacağını gösteren tam bir örnek verilmiştir; bir excel dosyası (book1.xls) açma, ilk çalışma sayfasındaki satır ve sütun başlıklarını gizleme ve değiştirilen dosyayı output.xls olarak kaydetme işlemleri yapılmaktadır.

```cpp
#include <iostream>
#include <memory>
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the headers of rows and columns
    worksheet.SetIsRowColumnHeadersVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Headers hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Ayrıca, [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) sınıfının [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) ve [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) metodlarını kullanarak birden fazla satır ve sütunu görünür hale getirmek de mümkündür.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
