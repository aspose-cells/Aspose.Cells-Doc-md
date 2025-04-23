---
title: Kullanıcı Tanımlı Aralıklar Oluşturma, Erişme ve Kopyalama C++ ile
linktitle: Kullanıcı Tanımlı Aralıklar Oluşturma, Erişme ve Kopyalama
type: docs
weight: 200
url: /tr/cpp/create-access-and-copy-named-ranges/
description: Aspose.Cells kullanarak Excel dosyalarında kullanıcı tanımlı aralıklar nasıl oluşturulur, erişilir ve kopyalanır öğrenin.
---

## **Giriş**

Genellikle, sütun ve satır etiketleri, bireysel hücrelere referans göstermek için kullanılır. Hücreleri, hücre aralıklarını, formülleri veya sabit değerleri temsil eden açıklayıcı isimler oluşturmak mümkündür. **İsim** kelimesi, hücreleri, hücre aralıklarını, formülleri veya sabit değerleri temsil eden bir karakter dizisini ifade edebilir. Bir aralığa isim atamak, bu hücre aralığının ad ile referans edilmesini sağlar. Anlaşılması kolay isimler kullanın, örneğin Sales!C20:C30 gibi, anlaması güç aralıklar için Products gibi. Etiketler, aynı çalışma sayfasındaki verileri referans alan formüllerde kullanılabilir; başka çalışma sayfasındaki bir aralığı temsil etmek istiyorsanız, isim kullanabilirsiniz. *İsimlendirilmiş aralıklar, özellikle liste kontrolleri, özet tablolar, grafikler gibi kaynak aralıkları olarak kullanıldığında Microsoft Excel’in en güçlü özelliklerinden biridir.

## **Microsoft Excel Kullanarak Adlandırılmış Aralık İle Çalışma**

### **Adlandırılmış Aralık Oluştur**

Aşağıdaki adımlar, **MS Excel** kullanarak hücre veya hücre aralığını nasıl adlandıracağınızı açıklar. Bu yöntem, **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000**, ve **2002** için geçerlidir.

1. Adlandırmak istediğiniz hücre veya hücre aralığını seçin.
2. Formül çubuğunun sol ucundaki **Ad Kutusu'nu** tıklayın.
1. Hücrelerin adını yazın.
1. ENTER tuşuna basın.

{{% alert color="primary" %}}

Hücre içeriğini değiştirirken hücreye ad veremezsiniz.

{{% /alert %}}

## **Aspose.Cells Kullanarak Adlandırılmış Aralık İle Çalışma**

Burada görevi yapmak için Aspose.Cells API'sını kullanıyoruz.
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı ise bir [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu sunar.

### **İsimlendirilmiş Aralık Oluştur**

Bir isimlendirilmiş aralık oluşturmak için, [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) sınıfının [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunun aşırı yüklenmiş [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) metodunu çağırabilirsiniz. Tipik olarak, [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) metodunun aldığı parametreler şunlardır:

- Sol üst hücrenin adı, aralıktaki sol üst hücrenin adı.
- Sağ alt hücrenin adı, aralıktaki sağ alt hücrenin adı.

[**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) yöntemi çağrıldığında, yeni oluşturulan aralık, [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) sınıfının bir örneği olarak döner. Bu [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) nesnesini, isimlendirilmiş aralığı yapılandırmak için kullanın. Örneğin, [**GetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getname/) özelliğini kullanarak aralığın adını ayarlayın. Aşağıdaki örnek, B4:G14 üzerine uzanan hücrelerin adlandırılmış bir aralık oluşturmak için nasıl yapılacağını göstermektedir.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating a named range
    Range range = worksheet.GetCells().CreateRange(u"B4", u"G14");

    // Setting the name of the named range
    range.SetName(u"TestRange");

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Named range created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Adı Verilen Aralıktaki Hücrelere Veri Girişi**

Bir aralıktaki bireysel hücrelere veri ekleyebilirsiniz. İzlenecek desen aşağıdaki gibidir:

- **C++**: Aralık(satır, sütun)

A1:C4 aralığında bir isimlendirilmiş aralık olduğunu varsayalım. Matris 4 * 3 = 12 hücre yapar. Bu hücreler sıralı diziliştir: Range(0, 0), Range(0, 1), Range(0, 2), Range(1, 0), Range(1, 1), Range(1, 2), Range(2, 0), Range(2, 1), Range(2, 2), Range(3, 0), Range(3, 1), Range(3, 2).

Aralıktaki hücreleri tanımlamak için aşağıdaki özellikleri kullanın:

- FirstRow, isimlendirilmiş aralıktaki ilk satırın indisini döndürür.
- FirstColumn, isimlendirilmiş aralıktaki ilk sütunun indisini döndürür.
- RowCount, isimlendirilmiş aralıktaki toplam satır sayısını döndürür.
- ColumnCount, isimlendirilmiş aralıktaki toplam sütun sayısını döndürür.

Aşağıdaki örnek, belirtilen bir aralıktaki hücrelere bazı değerler girmeyi gösterir.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Create a range of cells based on H1:J4
    Range range = worksheet1.GetCells().CreateRange(u"H1", u"J4");

    // Name the range
    range.SetName(u"MyRange");

    // Input some data into cells in the range
    range.Get(0, 0).PutValue(u"USA");
    range.Get(0, 1).PutValue(u"SA");
    range.Get(0, 2).PutValue(u"Israel");
    range.Get(1, 0).PutValue(u"UK");
    range.Get(1, 1).PutValue(u"AUS");
    range.Get(1, 2).PutValue(u"Canada");
    range.Get(2, 0).PutValue(u"France");
    range.Get(2, 1).PutValue(u"India");
    range.Get(2, 2).PutValue(u"Egypt");
    range.Get(3, 0).PutValue(u"China");
    range.Get(3, 1).PutValue(u"Philipine");
    range.Get(3, 2).PutValue(u"Brazil");

    // Save the excel file
    workbook.Save(outDir + u"rangecells.out.xls");

    std::cout << "Range cells created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **İsimlendirilmiş Aralıktaki Hücreleri Tanımlama**

Bir aralıktaki bireysel hücrelere veri ekleyebilirsiniz. İzlenecek desen aşağıdaki gibidir:

- **C++**: Aralık(satır, sütun)

Bir A1:C4 uzanıp giden adlandırılmış aralığınız varsa. Matris 4 * 3 = 12 hücre yapar. Bireysel aralık hücreleri sıralı şekilde dizilmiştir: Aralık(0, 0), Aralık(0, 1), Aralık(0, 2), Aralık(1, 0), Aralık(1, 1), Aralık(1, 2), Aralık(2, 0), Aralık(2, 1), Aralık(2, 2), Aralık(3, 0), Aralık(3, 1), Aralık(3, 2).

Aralıktaki hücreleri tanımlamak için aşağıdaki özellikleri kullanın:

- FirstRow, isimlendirilmiş aralıktaki ilk satırın indisini döndürür.
- FirstColumn, isimlendirilmiş aralıktaki ilk sütunun indisini döndürür.
- RowCount, isimlendirilmiş aralıktaki toplam satır sayısını döndürür.
- ColumnCount, isimlendirilmiş aralıktaki toplam sütun sayısını döndürür.

Aşağıdaki örnek, belirtilen bir aralıktaki hücrelere bazı değerler girmeyi gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    // Identify range cells
    std::cout << "First Row : " << range.GetFirstRow() << std::endl;
    std::cout << "First Column : " << range.GetFirstColumn() << std::endl;
    std::cout << "Row Count : " << range.GetRowCount() << std::endl;
    std::cout << "Column Count : " << range.GetColumnCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **İsimlendirilmiş Aralıklara Eriş**

#### **Belirli Bir Adlandırılmış Aralığa Erişme**

Belirli bir adlandırılmış aralığa erişmek için [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunun [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) yöntemini çağırın. Tipik bir [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) yöntemi, adlandırılmış aralığın adını alır ve belirtilen adlandırılmış aralığı [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) sınıfının bir örneği olarak döndürür. Aşağıdaki örnek, adına göre belirtilen bir aralığa nasıl erişileceğini göstermektedir.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Getting the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    if (range)
    {
        std::cout << "Named Range : " << range.GetRefersTo().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

#### **Bir Elektronik Tablodaki Tüm İsimlendirilmiş Aralıklara Eriş**

Bir elektronik tabloda tüm adlandırılmış aralıkları almak için [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunun [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) metodunu çağırın. [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) metodu, [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonundaki tüm adlandırılmış aralıkların dizisini döndürür.

Aşağıdaki örnek, bir çalışma kitabındaki tüm adlandırılmış aralıklara erişmeyi gösterir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    WorksheetCollection sheets = workbook.GetWorksheets();
    Vector<Range> ranges = sheets.GetNamedRanges();

    std::cout << "Total Number of Named Ranges: " << ranges.GetLength() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **İsimlendirilmiş Aralıkları Kopyala**

Aspose.Cells, başka bir aralığa biçimlendirmeyle birlikte hücreleri kopyalamak için [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/) metodunu sağlar.

Aşağıdaki örnek, kaynak hücre aralığını başka adlandırılmış bir aralığa kopyalamanın nasıl yapıldığını göstermektedir.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Range range1 = worksheet.GetCells().CreateRange(u"E12", u"I12");
    range1.SetName(u"MyRange");

	Color borderColor = Color{ 0,0, 0, 128 };
    range1.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Medium, borderColor);

    range1.Get(0, 0).PutValue(u"Test");
    range1.Get(0, 4).PutValue(u"123");

    Range range2 = worksheet.GetCells().CreateRange(u"B3", u"F3");
    range2.SetName(u"testrange");
    range2.Copy(range1);

    workbook.Save(outDir + u"copyranges.out.xls");

    std::cout << "Ranges copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
