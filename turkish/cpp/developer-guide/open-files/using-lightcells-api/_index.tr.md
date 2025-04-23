---
title: LightCells API ile C++ kullanımı
linktitle: LightCells API sını Kullanma
type: docs
weight: 160
url: /tr/cpp/using-lightcells-api/
description: LightCells API yi C++ kullanarak büyük Excel dosyalarını düşük bellek kullanımıyla verimli bir şekilde okuma ve yazma yöntemlerini öğrenin.
---

{{% alert color="primary" %}} 

Bazen büyük bir veri veya içeriğe sahip büyük Microsoft Excel dosyalarını okumak ve yazmak isteyebilirsiniz. Hafif Hücreler API'sı, bu iş için kullanışlıdır: daha az bellek kullanarak daha iyi performans ve verimlilik elde edersiniz.

{{% /alert %}} 

# Olay Tabanlı Mimari
Aspose.Cells, özellikle bellekte bir veri modeli bloğu oluşturmadan hücre verilerini bir bir işlemek için tasarlanmış olan LightCells API'sını sağlar (Hücre koleksiyonu vb. kullanılmadan). Olay temelli modda çalışır.

Çalışma kitaplarını kaydetmek için kaydederken hücre içeriğini hücre hücre sağlayın ve bileşen bunu doğrudan çıktı dosyasına kaydeder.

Şablon dosyalarını okurken bileşen her hücreyi ayrı ayrı ayrıştırır ve değerlerini tek tek sağlar.

Her iki süreçte de bir Cell nesnesi işlenir ve ardından atılır, Workbook nesnesi koleksiyonu tutmaz. Bu modda, dolayısıyla, çok miktarda bellek kullanan büyük veri kümesi barındıran Microsoft Excel dosyasının içe aktarımı ve dışa aktarımı sırasında bellek kaydedilir.

LightCells API, XLSX ve XLS dosyaları için hücreleri aynı şekilde işlemesine rağmen (bütün hücreleri belleğe yüklemez ama bir hücreyi işler ve ardından atar), XLSX dosyaları için XLS dosyalarına göre belleği daha etkili bir şekilde saklar çünkü iki formatın farklı veri modelleri ve yapıları vardır.

Ancak, **XLS dosyaları için**, geliştiriciler kayıt işlemi sırasında oluşturulan geçici veri için bir geçici konum belirtebilirler. Genellikle **LightCells API'nin kullanılması XLSX dosyası için% 50 veya daha fazla bellek tasarrufu sağlayabilirken**, **XLS için kullanılması% 20-40'a kadar bellek tasarrufu sağlayabilir**.

## Büyük Bir Excel Dosyası Yazma
Aspose.Cells, programınızda uygulanması gereken `LightCellsDataProvider` arayüzü sağlar. Bu arayüz, hafif modda büyük hesap tablosu dosyalarını kaydetmek için veri sağlayıcıyı temsil eder.

Bu modda bir çalışma kitabı kaydederken, `StartSheet(int)` her çalışma sayfası kaydedilirken kontrol edilir. Bir sayfa için, eğer `StartSheet(int)` doğruysa, kaydedilecek bu sayfanın satırları ve hücreleri ile ilgili tüm veri ve özellikler bu uygulama tarafından sağlanır. Öncelikle, kaydedilecek bir sonraki satır indeksini almak için `NextRow()` çağrılır. Geçerli bir satır indeksi döndürülürse (satır indeksi artan sıralamada olmalıdır), bu satırı temsil eden bir `Row` nesnesi sağlayıcıya `StartRow(Row)` ile özelliklerini ayarlama imkanı sağlar.

Bir satır için, önce `NextCell()` kontrol edilir. Geçerli bir sütun indeksi döndürülürse (sütun indeksi artan sıralamada olmalıdır), o hücreyi temsil eden bir `Cell` nesnesi sağlayıcıya `StartCell(Cell)` ile veri ve özelliklerini ayarlama imkanı sağlar. Hücrenin verisi ayarlandıktan sonra, hücre doğrudan oluşturulan elektronik tablo dosyasına kaydedilir ve bir sonraki hücre kontrol edilir ve işlenir.

### Büyük Bir Excel Dosyasını Yazmak: Örnek
Lütfen LightCells API'nin çalışmasını görmek için aşağıdaki örnek kodu inceleyin. Kod segmentlerini ihtiyacınıza göre ekleyin, kaldırın veya güncelleyin.

Program, bir çalışma sayfasında **10.000 (10000x30 matris) kayıt** içeren devasa bir dosya oluşturur ve bunları sahte verilerle doldurur. `Main()` metodundaki `rowsCount` ve `colsCount` değişkenlerini değiştirerek kendi matrisinizi belirtebilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestDataProvider : public LightCellsDataProvider {
private:
    int _row = -1;
    int _column = -1;
    int maxRows;
    int maxColumns;
    Workbook _workbook;

public:
    TestDataProvider(Workbook workbook, int maxRows, int maxColumns)
        : _workbook(workbook), maxRows(maxRows), maxColumns(maxColumns) {}

    bool IsGatherString() override {
        return false;
    }

    int NextCell() override {
        ++_column;
        if (_column < this->maxColumns)
            return _column;
        else {
            _column = -1;
            return -1;
        }
    }

    int NextRow() override {
        ++_row;
        if (_row < this->maxRows) {
            _column = -1;
            return _row;
        }
        else
            return -1;
    }

    void StartCell(Cell& cell) override {
        cell.PutValue(_row + _column);
        if (_row != 1) {
            cell.SetFormula(u"=Rand() + A2");
        }
    }

    void StartRow(Row& row) override {}

    bool StartSheet(int sheetIndex) override {
        return sheetIndex == 0;
    }
};

void WriteUsingLightCellsAPI() {
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    int rowsCount = 10000;
    int colsCount = 30;

    Workbook workbook;
    OoxmlSaveOptions ooxmlSaveOptions;

    TestDataProvider dataProvider(workbook, rowsCount, colsCount);
    ooxmlSaveOptions.SetLightCellsDataProvider(&dataProvider);

    workbook.Save(outDir + u"output.out.xlsx", ooxmlSaveOptions);

    std::cout << "File saved successfully using LightCells API!" << std::endl;
}

int main() {
    Aspose::Cells::Startup();
    WriteUsingLightCellsAPI();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Büyük Excel Dosyalarını Okuma
Aspose.Cells, uygulamanızda uygulanması gereken `LightCellsDataHandler` adlı bir arayüz sağlar. Bu arayüz, büyük elektronik tablo dosyalarını hafif modda okuma veri sağlayıcısını temsil eder.

Bu modda bir çalışma kitabı okunurken, `StartSheet` her çalışma sayfası okunurken kontrol edilir. Bir sayfa için, `StartSheet` doğruysa, sayfadaki satırların ve sütunların hücrelerinin tüm verileri ve özellikleri bu arayüzün uygulaması tarafından kontrol edilip işlenir. Her satır için, `StartRow` çağrılır ve işlem gerek olup olmadığını kontrol eder. İşlem gerekiyorsa, önce özellikleri okunur ve geliştirici `ProcessRow` ile erişebilir. Eğer satırın hücreleri de işlenecekse, `ProcessRow` doğru döner ve her hücre için `StartCell` çağrılır. İşlenmesi gereken hücreler varsa, ardından `ProcessCell` çağrılır.

### Büyük Excel Dosyalarını Okuma: Örnek
Lütfen LightCells API'nin çalışmasını görmek için aşağıdaki örnek kodu inceleyin. Kod segmentlerini ihtiyacınıza göre ekleyin, kaldırın veya güncelleyin.

Program, bir çalışma kitabında milyonlarca kayıt içeren büyük bir dosyayı okur. Her çalışma sayfasını okumak biraz zaman alır. Örnek kod, dosyayı okur ve her çalışma sayfasında toplam hücre sayısını, dize sayısını ve formül sayısını alır.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class LightCellsDataHandlerVisitCells : public LightCellsDataHandler
{
private:
    int cellCount;
    int formulaCount;
    int stringCount;

public:
    LightCellsDataHandlerVisitCells() : cellCount(0), formulaCount(0), stringCount(0) {}

    int GetCellCount() const { return cellCount; }
    int GetFormulaCount() const { return formulaCount; }
    int GetStringCount() const { return stringCount; }

    bool StartSheet(Worksheet& sheet) override
    {
        std::cout << "Processing sheet[" << sheet.GetName().ToUtf8() << "]" << std::endl;
        return true;
    }

    bool StartRow(int32_t rowIndex) override
    {
        return true;
    }

    bool ProcessRow(Row& row) override
    {
        return true;
    }

    bool StartCell(int32_t columnIndex) override
    {
        return true;
    }

    bool ProcessCell(Cell& cell) override
    {
        cellCount++;
        if (cell.IsFormula())
        {
            formulaCount++;
        }
        else if (cell.GetType() == CellValueType::IsString)
        {
            stringCount++;
        }
        return false;
    }
};

void Run()
{
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create load options and set the light cells data handler
    LoadOptions opts;
    auto handler = std::make_shared<LightCellsDataHandlerVisitCells>();
    opts.SetLightCellsDataHandler(handler.get());

    // Load the workbook with the specified options
    Workbook wb(srcDir + u"LargeBook1.xlsx", opts);

    // Get the total number of sheets
    int sheetCount = wb.GetWorksheets().GetCount();

    // Output the results
    std::cout << "Total sheets: " << sheetCount << ", cells: " << handler->GetCellCount()
              << ", strings: " << handler->GetStringCount() << ", formulas: " << handler->GetFormulaCount() << std::endl;
}

int main()
{
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```
