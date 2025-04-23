---
title: C++ ile Excel Dosyalarının Verilerini Yönetme
linktitle: Hücre Verileri
type: docs
weight: 110
url: /tr/cpp/view-and-edit-excel-data/
description: Bu makale, Aspose.Cells kütüphanesi kullanarak C++ ile Excel dosyalarının verilerini nasıl görüntüleyip düzenleyeceğinizi açıklamaktadır.
keywords: Aspose.Cells C++ ile Excel dosyasının verilerini yönetme, Excel dosyasına veri ekleme, Excel dosyasından veri alma, Veri ekleme verimliliğini artırma, hücre verilerini yönetme, hücreleri güncelleme, hücreleri alma, hücreleri ekleme
---

{{% alert color="primary" %}}

[Bir Çalışma Sayfasının Hücrelerine Erişim](/cells/tr/cpp/accessing-cells-of-a-worksheet/) bölümünde, bir çalışma sayfasındaki hücrelere erişim için temel yaklaşımları tartıştık. Bu makale, bu yaklaşımlardan birini kullanarak hücrelere farklı türde veri eklemeyi ele almaktadır.

{{% /alert %}}

## **Hücrelere Veri Ekleme**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı bir [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfından bir nesneyi temsil eder.

Aspose.Cells, geliştiricilere hücrelere farklı türde veri eklemelerine izin veren bir [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) yöntemini çağırarak çalışma sayfalarındaki hücrelere veri eklemelerini sağlar. Aspose.Cells, geliştiricilere hücrelere farklı türde veri eklemelerine izin veren [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) yönteminin aşırı yüklenmiş sürümlerini sağlar. Bu aşırı yüklenmiş [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) yöntemlerini kullanarak, bir mantıksal, dize, çift, tamsayı veya tarih/saat vb. değerleri hücreye eklemek mümkündür.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);


    worksheet.GetCells().Get(U16String(u"A1")).PutValue(U16String(u"Hello World"));
    worksheet.GetCells().Get(U16String(u"A2")).PutValue(20.5);
    worksheet.GetCells().Get(U16String(u"A3")).PutValue((int32_t)15);
    worksheet.GetCells().Get(U16String(u"A4")).PutValue(true);

    Cell cellA1 = worksheet.GetCells().Get(U16String(u"A4"));
    Style style = cellA1.GetStyle();
    style.SetNumber(15);
    cellA1.SetStyle(style);

    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Data inserted and workbook saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Verimliliği Nasıl Arttırılır**

[**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) yöntemini bir çalışma sayfasına büyük miktarda veri eklemek için kullanıyorsanız, uygulamalarınızın verimliliğini artırmak için öncelikle satır ve sonra sütunlar olarak hücrelere değer eklemelisiniz. Bu yaklaşım, uygulamalarınızın verimliliğini büyük ölçüde artırır.

## **Hücrelerden Veri Almak**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, dosyadaki çalışma sayfalarına erişime izin veren bir [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı bir [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfından bir nesneyi temsil eder.

[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfı, geliştiricilere verileri hücrelerden türlerine göre almak için birkaç özellik sağlar. Bu özellikler şunları içerir:

- [**StringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/): hücrenin dize değerini döndürür.
- [**DoubleValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/): hücrenin ondalık değerini döndürür.
- [**BoolValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/): hücrenin mantıksal değerini döndürür.
- [**DateTimeValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/): hücrenin tarih/saat değerini döndürür.
- [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/): hücrenin ondalık değerini döndürür.
- [**IntValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/): hücrenin tam sayı değerini döndürür.

Bir alan doldurulmadığında, [**DoubleValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) veya [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) ile başlayan hücreler bir istisna fırlatır.

Hücrede bulunan veri türü ayrıca [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının [**Type**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) özelliği kullanılarak kontrol edilebilir. Aslında, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının [**Type**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) özelliği, önceden tanımlanmış değerleri listelenen [**CellValueType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/) numaralı numaralandırmaya dayanan bir özelliktir:

|**Hücre Değer Türleri**|**Açıklama**|
| :- | :- |
|IsBool| Hücre değerinin Boolean olduğunu belirtir.
|IsDateTime| Hücre değerinin tarih/saat olduğunu belirtir.
|IsNull| Boş bir hücreyi temsil eder.
|IsNumeric| Hücre değerinin sayısal olduğunu belirtir.
|IsString| Hücre değerinin bir dize olduğunu belirtir.
|IsUnknown| Hücre değerinin bilinmeyen olduğunu belirtir.

Yukarıda tanımlanan hücre değeri tiplerini aynı zamanda her hücrede bulunan veri türüyle karşılaştırmak için de kullanabilirsiniz.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    int maxRow = worksheet.GetCells().GetMaxDataRow();
    int maxCol = worksheet.GetCells().GetMaxDataColumn();

    for (int row = 0; row <= maxRow; row++)
    {
        for (int col = 0; col <= maxCol; col++)
        {
            Cell cell = worksheet.GetCells().Get(row, col);

            U16String stringValue;
            double doubleValue = 0.0;
            bool boolValue = false;

            switch (cell.GetType())
            {
                case CellValueType::IsString:
                    stringValue = cell.GetStringValue();
                    std::cout << "String Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsNumeric:
                    doubleValue = cell.GetDoubleValue();
                    std::cout << "Double Value: " << doubleValue << std::endl;
                    break;

                case CellValueType::IsBool:
                    boolValue = cell.GetBoolValue();
                    std::cout << "Bool Value: " << boolValue << std::endl;
                    break;

                case CellValueType::IsDateTime:
                    stringValue = cell.GetStringValue();
                    std::cout << "DateTime Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsUnknown:
                    stringValue = cell.GetStringValue();
                    std::cout << "Unknown Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsNull:
                    break;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Çalışma sayfalarında çalışırken, kullanıcılar hücrelere farklı veri türleri ekleyebilir. Bu veri tipleri, Boolean, tam sayı, kayan nokta, metin veya tarih/saat değerlerini içerebilir. Aspose.Cells ile, hücrelerden uygun değerleri alabilirsiniz, bunlar veri tiplerine göre.

{{% /alert %}}

## **Gelişmiş Konular**
- [Bir Çalışma Sayfasının Hücrelerine Erişme](/cells/tr/cpp/accessing-cells-of-a-worksheet/)
- [Metin Sayı Değerini Sayıya Dönüştürme](/cells/tr/cpp/convert-text-numeric-data-to-number/)
- [Alt Toplamlar Oluşturma](/cells/tr/cpp/creating-subtotals/)
- [Veri Filtreleme](/cells/tr/cpp/data-filtering/)
- [Veri Sıralama](/cells/tr/cpp/sort-data-of-excel/)
- [Veri Doğrulama](/cells/tr/cpp/data-validation/)
- [Veri Bulma veya Arama](/cells/tr/cpp/find-or-search-data/)
- [Biçimlendirmeyle ve biçimlendirme olmadan Hücre Dize Değerini Alın](/cells/tr/cpp/get-cell-string-value-with-and-without-formatting/)
- [Hücre İçinde HTML Zengin Metin Ekleme](/cells/tr/cpp/adding-html-rich-text-inside-the-cell/)
- [Excel veya OpenOffice'de Hyperlinkler Eklemek](/cells/tr/cpp/insert-hyperlinks-to-excel/)
- [Numaralandırıcıları Nerede ve Nasıl Kullanılır](/cells/tr/cpp/how-and-where-to-use-enumerators/)
- [Hücre Değeri Genişliğini ve Yüksekliğini Piksel Birimiyle Ölçme](/cells/tr/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Birden Fazla İş Parçacığında Aynı Anda Hücre Değerleri Okuma](/cells/tr/cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Hücre adı ve satır/sütun indeksi arasında dönüşüm](/cells/tr/cpp/names-and-indices/)
- [Veri İlk Olarak Satır, Sonra Sütun Olarak Doldurma](/cells/tr/cpp/populate-data-first-by-row-then-by-column/)
- [Hücre Değerinin veya Aralığın Ön Eklemesini Koruma](/cells/tr/cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Zengin Metnin Kısımlarına Erişme ve Güncelleme](/cells/tr/cpp/access-and-update-the-portions-of-rich-text-of-cell/)
