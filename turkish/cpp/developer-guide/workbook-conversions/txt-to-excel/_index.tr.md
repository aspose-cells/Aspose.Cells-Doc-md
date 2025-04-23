---
title: CSV, TSV ve TXT yi Excel e dönüştür
linktitle: CSV, TSV ve TXT yi Excel e dönüştür
type: docs
weight: 30
url: /tr/cpp/convert-csv-tsv-and-txt-to-excel/
description: CSV, TSV ve TXT dosyalarını Excel e dönüştürmenin yollarını Aspose.Cells for C++ kullanarak öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ kullanılarak, CSV, OpenOffice, PDF, JSON ve diğer birçok formata dönüştürülebilir.

{{% /alert %}}

## **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerlerin virgüllerle ayrıldığı kayıtlar içerir. Veriler, her sütunun virgül karakteriyle ayrıldığı ve çift tırnak karakteriyle alıntılanmış bir tabloda saklanır. Bir alan değeri çift tırnak karakteri içeriyorsa, çift tırnak karakteriyle kaçış yapılır. Ayrıca, Excel'i kullanarak elektronik tablo verilerinizi CSV'ye dışa aktarabilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions4(LoadFormat::Csv);

    // Create a Workbook object and open the file from its path
    Workbook wbCSV(srcDir + u"Book_CSV.csv", loadOptions4);

    std::cout << "CSV file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **CSV Dosyalarını Açma ve Geçersiz Karakterleri Değiştirme**

Excel'de, özel karakterler içeren bir CSV dosyası açıldığında, karakterler otomatik olarak değiştirilir. Aynı işlemi Aspose.Cells API'si de yapar, aşağıdaki kod örneğinde gösterildiği gibi.

```c++
// Fix BOM issue
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filename = srcDir + u"[20180220142533][ASPOSE_CELLS_TEST].csv";

    TxtLoadOptions options;
    options.SetSeparator(u';');
    options.SetCheckExcelRestriction(false);
    options.SetConvertNumericData(false);
    options.SetConvertDateTimeData(false);

    LoadFilter* filter = new LoadFilter(LoadDataFilterOptions::CellData);
    options.SetLoadFilter(filter);

    Workbook workbook(filename, options);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::cout << worksheet.GetName().ToUtf8() << std::endl;
    std::cout << worksheet.GetName().GetLength() << std::endl;
    std::cout << "CSV file opened successfully!" << std::endl;

    delete filter;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Tercih Edilen Ayrıştırıcı Kullanma**

CSV dosyaları açmak için varsayılan ayrıştırıcı ayarlarını her zaman kullanmak gerekmez. Bazen, bir CSV dosyasını ithal etmek beklenen çıktıyı oluşturmaz, örneğin tarih formatı beklenildiği gibi değilse veya boş alanlar farklı şekilde işleniyorsa. Bu amaçla, **TxtLoadOptions.PreferredParsers** kullanılarak ihtiyaçlarınıza uygun kendi tercihinize göre ayırıcılar belirlenebilir. Aşağıdaki örnek kod, tercihi ayrıştırıcı kullanımını göstermektedir.

Bu özelliği test etmek için örnek kaynak dosya ve çıktı dosyalarını aşağıdaki bağlantılardan indirebilirsiniz.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
	Aspose::Cells::Startup();

	U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
	U16String outDir(u"..\\Data\\02_OutputDirectory\\");

	TxtLoadOptions loadOptions(LoadFormat::Csv);
	loadOptions.SetSeparator(u',');
	loadOptions.SetConvertDateTimeData(true);

	Workbook workbook(srcDir + u"sample.csv", loadOptions);

	Worksheet worksheet = workbook.GetWorksheets().Get(0);
	Cells cells = worksheet.GetCells();

	Cell cell = cells.Get(u"A1");
	std::cout << "A1: " << static_cast<int>(cell.GetType())
		<< " - " << cell.GetDisplayStringValue().ToUtf8() << std::endl;

	cell = cells.Get(u"B1");
	std::cout << "B1: " << static_cast<int>(cell.GetType())
		<< " - " << cell.GetDisplayStringValue().ToUtf8() << std::endl;

	workbook.Save(outDir + u"outputsample.xlsx");

	std::cout << "OpeningCSVFilesWith executed successfully." << std::endl;

	Aspose::Cells::Cleanup();
	return 0;
}
```

### **Özel Ayraçlı Metin Dosyalarını Açma**

Metin dosyaları biçimlendirme olmadan elektronik tablo verilerini tutmak için kullanılır. Dosya, özelleştirilmiş ayraçlar içerebilen bir tür düz metin dosyasıdır.

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

    // Path of input CSV file
    U16String filePath = srcDir + u"Book11.csv";

    // Instantiate Text File's LoadOptions
    TxtLoadOptions txtLoadOptions;

    // Specify the separator
    txtLoadOptions.SetSeparator(u',');

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath, txtLoadOptions);

    // Save file
    wb.Save(outDir + u"output.txt");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Sekmeli Ayrılmış Dosyaları Açma**

Sekmeli ayraçlı (Metin) dosyalar tablo verisi içerir, ancak biçimlendirme içermez. Veri, tablolar ve elektronik tablolar gibi satır ve sütunlar halinde düzenlenmiştir. Temelde, sekmeli ayraçlı dosya, her sütunun arasına bir sekme konmuş özel bir düz metin dosyasıdır.

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

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions(LoadFormat::TabDelimited);

    // Create a Workbook object and open the file from its path
    Workbook wbTabDelimited(srcDir + u"Book1TabDelimited.txt", loadOptions);

    std::cout << "Tab delimited file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Sekmeyle Ayrılmış Değerler (TSV) Dosyalarını Açma**

Sekmeli Ayrılmış Değerler (TSV) dosyaları, biçimlendirme olmadan elektronik tablo verisi içerir. Bu, verilerin tablolar ve elektronik tablolar gibi satır ve sütunlar halinde düzenlendiği sekmeli ayraçlı dosyayla aynıdır.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions(LoadFormat::Tsv);

    // Create a Workbook object and open the file from its path
    Workbook workbook(srcDir + u"SampleTSVFile.tsv", loadOptions);

    // Using the Sheet 1 in Workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing a cell using its name
    Cell cell = worksheet.GetCells().Get(u"C3");

    // Output the cell name and value
    std::cout << "Cell Name: " << cell.GetName().ToUtf8() << " Value: " << cell.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Gelişmiş Konular**
- [Formüller ile CSV Dosyası Yükle veya İçe Aktar](/cells/tr/cpp/load-or-import-csv-file-with-formulas/)
- [Çeşitli Kodlamalarla CSV Dosyası Okuma](/cells/tr/cpp/reading-csv-file-with-multiple-encodings/)
