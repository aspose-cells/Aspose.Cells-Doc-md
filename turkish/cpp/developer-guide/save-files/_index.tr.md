---
title: C++ ile Dosyaları Farklı Formatlarda Kaydetme Yöntemleri
linktitle: Dosyaları Kaydet
type: docs
weight: 40
url: /tr/cpp/different-ways-to-save-files/
description: Aspose.Cells for C++, dosyaları farklı formatlara kaydedebilir. PDF olarak kaydet. HTML olarak kaydet. DOCX olarak kaydet. PPTX olarak kaydet. JSON olarak kaydet. MHTML olarak kaydet.
keywords: Aspose.Cells, C++ kullanarak Excel i PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML ve diğer formatlara kaydetmenize veya dönüştürmenize olanak tanır; Çalışma kitabını PDF, HTML, JSON, TXT veya SQL e kaydedin veya dönüştürün.
---

{{% alert color="primary" %}}

Aspose.Cells, dosyalar oluşturmayı ve kaydetmeyi mümkün kılar. Bu makalede dosyaların kaydedilebileceği çeşitli yollar açıklanmaktadır.

{{% /alert %}}

## **Dosyaları Kaydetmenin Farklı Yolları**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden ve Excel dosyalarıyla çalışmak için gerekli özellikleri ve yöntemleri sağlayan [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sunar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyalarını kaydetmek için kullanılan [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemini sağlar. [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemi, farklı şekillerde dosyaları kaydetmek için kullanılan birçok aşırı yüklemeye sahiptir.

Dosyanın kaydedildiği dosya biçimi, [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) numaralandırmasına göre belirlenir

|**Dosya Biçimi Türleri**|**Açıklama**|
| :- | :- |
|CSV|CSV dosyasını temsil eder|
|Excel97To2003|Excel 97 - 2003 dosyasını temsil eder|
|Xlsx|Excel 2007 XLSX dosyasını temsil eder|
|Xlsm|Excel 2007 XLSM dosyasını temsil eder|
|Xltx|Excel 2007 şablonu XLTX dosyasını temsil eder|
|Xltm|Excel 2007 makro etkin XLTM dosyasını temsil eder|
|Xlsb|Excel 2007 ikili XLSB dosyasını temsil eder|
|SpreadsheetML|Yaygın Çalışma Kitabı XML dosyasını temsil eder|
|TSV|Tab boşluklu değerler dosyasını temsil eder|
|TabDelimited|Tab Delimited metin dosyasını temsil eder|
|ODS|ODS dosyasını temsil eder|
|Html|HTML dosya(lar)ını temsil eder|
|MHtml|MHTML dosya(lar)ını temsil eder|
|Pdf|PDF dosyasını temsil eder|
|XPS|XPS belgesini temsil eder|
|TIFF|Etiketli Görüntü Dosya Biçimi (TIFF)ni temsil eder|

## **Farklı Biçimlere Dosya Kaydetme Yöntemleri**

Dosyaları bir depolama konumuna kaydetmek için [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) numaralandırmasından istenen dosya biçimini belirterek [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) nesnesinin [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemini çağırdığınızda dosya adını (depolama yoluyla tamamlanmış) belirtin.

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

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xls";

    // Load your source workbook
    Workbook workbook(filePath);

    // Save in Excel 97 to 2003 format
    workbook.Save(outDir + u".output.xls");
    // OR
    XlsSaveOptions xlsSaveOptions;
    workbook.Save(outDir + u".output.xls", xlsSaveOptions);

    // Save in Excel2007 xlsx format
    workbook.Save(outDir + u".output.xlsx", SaveFormat::Xlsx);

    // Save in Excel2007 xlsb format
    workbook.Save(outDir + u".output.xlsb", SaveFormat::Xlsb);

    // Save in ODS format
    workbook.Save(outDir + u".output.ods", SaveFormat::Ods);

    // Save in Pdf format
    workbook.Save(outDir + u".output.pdf", SaveFormat::Pdf);

    // Save in Html format
    workbook.Save(outDir + u".output.html", SaveFormat::Html);

    // Save in SpreadsheetML format
    workbook.Save(outDir + u".output.xml", SaveFormat::SpreadsheetML);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Çalışma Kitabını Pdf'ye Nasıl Kaydedilir**
Taşınabilir Belge Biçimi (PDF), 1990'ların başında Adobe tarafından oluşturulan bir belge türüdür. Bu dosya biçiminin amacı, belgelerin ve diğer referans materyallerin, uygulama yazılımı, donanım ve İşletim Sistemi'nden bağımsız bir formatta temsil edilmesi için bir standart tanıtmaktır. PDF dosya biçimi, metin, görseller, hiperbağlantılar, form alanları, zengin medya, dijital imzalar, eklentiler, meta veriler, jeo uzamsal özellikler ve 3B objeler gibi bilgileri içerecek tam kapasiteye sahiptir ve bu bilgilerin kaynak belgenin bir parçası haline gelmesi mümkündür.

Aşağıdaki kodlar, Aspose.Cells ile çalışma kitabını pdf dosyası olarak nasıl kaydedeceğinizi gösterir:
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the Workbook object
    Workbook workbook;

    // Set value to Cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"Hello World!");

    // Save the workbook to PDF
    workbook.Save(u"pdf1.pdf");

    // Save as Pdf format compatible with PDFA-1a
    PdfSaveOptions saveOptions;
    saveOptions.SetCompliance(PdfCompliance::PdfA1a);

    workbook.Save(u"pdfa1a.pdf", saveOptions);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Çalışma Kitabını Metin veya CSV Formatına Nasıl Kaydedilir**

Bazen, birden fazla çalışma sayfası olan bir çalışma kitabını metin formatına dönüştürmek veya kaydetmek isteyebilirsiniz. Metin formatları (örneğin TXT, TabDelim, CSV, vb.) için, varsayılan olarak hem Microsoft Excel hem de Aspose.Cells sadece etkin çalışma sayfasının içeriğini kaydeder.

Aşağıdaki kod örneği, bir çalışma kitabını metin formatına kaydetmenin nasıl yapıldığını açıklar. Herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyasını (yani XLS, XLSX, XLSM, XLSB, ODS vb.) yükleyin ve içinde herhangi bir sayıda çalışsayfa olabilir.

Kod çalıştırıldığında, çalışma kitabındaki tüm sayfaların verilerini TXT formatına dönüştürür.

Aynı örneği, dosyanızı CSV'ye kaydetmek için değiştirebilirsiniz. Varsayılan olarak, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) virgüldür, bu yüzden CSV formatına kaydederken ayırıcı belirtmeyin. Lütfen dikkat edin: Değerlendirme sürümünü kullanıyorsanız ve hatta [**TxtSaveOptions.GetExportAllSheets()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getexportallsheets/) özelliği true olarak ayarlanmış olsa bile, program yalnızca bir çalışma sayfasını dışa aktaracaktır.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output text file
    U16String outputFilePath = outDir + u"out.txt";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook data saved to text file successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Özel Ayraçlı Metin Dosyalarına Nasıl Kaydedilir**

Metin dosyaları, biçimlendirme olmadan elektronik tablo verisi içerir. Dosya, verileri arasında özelleştirilmiş sınıflandırıcılara sahip bir düz metin dosyası türündedir.

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
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';');

    // Save the file with the options
    wb.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Bir Akışa Dosya Nasıl Kaydedilir**

Dosyaları bir akışa kaydetmek için *MemoryStream* veya *FileStream* nesnesi oluşturun ve [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) nesnesinin [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemini çağırarak dosyayı bu akış nesnesine kaydedin. [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemini çağırırken istenen dosya formatını [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) numaralı sıralama kullanarak belirtin.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```

## **Excel Dosyasını Html ve Mht Dosyalarına Nasıl Kaydedilir**
Aspose.Cells, Excel dosyasını, JSON, CSV veya diğer dosyaları .html ve .mht dosyaları olarak kolayca kaydedebilir.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    Workbook workbook(inputFilePath);

    // Save file to MHTML format
    U16String outputFilePath(u"out.mht");
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully to MHTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **Excel Dosyasını OpenOffice (ODS, SXC, FODS, OTS) Dosyalarına Nasıl Kaydedilir**
Dosyaları open office formatı olan ODS, SXC, FODS, OTS vb. olarak kaydetme

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file
    workbook.Save(u"Out.ods");

    // Save as sxc file
    workbook.Save(u"Out.sxc");

    // Save as fods file
    workbook.Save(u"Out.fods");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Excel Dosyasını JSON veya XML'e Nasıl Kaydedilir**

JSON (JavaScript Object Notation), veri paylaşımı için insan tarafından okunabilir metin kullanan açık standart bir dosya formatıdır. JSON dosyaları .json uzantısıyla saklanır. JSON, daha az biçimlendirme gerektirir ve XML için iyi bir alternatiftir. JSON, JavaScript'ten türetilmiş, ancak dilsiz bir veri formatıdır. JSON'un oluşturulması ve ayrıştırılması modern birçok programlama dilince desteklenmektedir. application/json, JSON için kullanılan medya türüdür.

Aspose.Cells, dosyaların JSON veya XML olarak kaydedilmesini destekler.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output json file
    U16String outputFilePath = outDir + u"book1.json";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **Gelişmiş Konular**
- [Çalışma kitabının sıkıştırma seviyesi ayarlanabilir.](/cells/tr/cpp/adjust-workbook-compression-level/)
- [Sıkı Açık XML Elektronik Tablo Biçimine Çalışma Kitabını Kaydet](/cells/tr/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Yanıt Nesnesine Dosya Kaydetme](/cells/tr/cpp/saving-file-to-response-object/)
