---
title: Excel i Pdf, Görüntü ve diğer formatlara C++ ile dönüştürün
linktitle: Çalışma Kitabı Dönüşümleri
type: docs
weight: 65
url: /tr/cpp/convert-workbook-to-different-formats/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML ve daha fazlasına dönüştürün.
---

{{% alert color="primary" %}}

Aspose.Cells, birçok format arasında dönüşüm desteği sağlar. Teknik olarak, dönüşüm, bir dosya formatında bir çalışma kitabı yükleme ve başka bir formatta kaydetme anlamına gelir.

{{% /alert %}}

## **Excel Çalışma Kitabını PDF'e Dönüştür**

PDF dosyaları, belge alışverişinde yaygın olarak kullanılmaktadır; hem organizasyonlar, hükümet sektörleri hem de bireyler arasında. Standart bir belge formatıdır ve yazılım geliştiricilerden, Microsoft Excel dosyalarını PDF belgelerine dönüştürmenin yollarını bulmaları istenir.

Aspose.Cells, Excel dosyalarını PDF'ye dönüştürmeyi destekler ve dönüşümde yüksek görsel sadakati korur.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Instantiate the Workbook object and open an Excel file
    Workbook workbook(u"Book1.xlsx");

    // Save the document in PDF format
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    std::cout << "Excel file converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel Çalışma Kitabını JPG'e Dönüştür**
Aspose.Cells, Excel dosyalarını JPG'ye dönüştürmeyi destekler.
Aşağıdaki kod örneği, bir çalışma kitabını JPG olarak kaydetmenin nasıl yapıldığını göstermektedir.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"Book1.xlsx");
    Workbook book(inputFilePath);

    U16String outputFilePath(u"Image1.jpg");
    book.Save(outputFilePath, SaveFormat::Jpg);

    std::cout << "Workbook converted to JPG image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel Çalışma Kitabını Görüntüye Dönüştür**
Aspose.Cells, Excel dosyalarını görüntülere dönüştürmeyi destekler.
Aşağıdaki kod örneği, bir çalışma kitabını resim olarak kaydetme yöntemini gösterir.

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook(srcDir + u"Book1.xlsx");

    workbook.Save(outDir + u"Image1.bmp", SaveFormat::Bmp);
    workbook.Save(outDir + u"Image1.jpg", SaveFormat::Jpg);
    workbook.Save(outDir + u"Image1.png", SaveFormat::Png);
    workbook.Save(outDir + u"Image1.emf", SaveFormat::Emf);
    workbook.Save(outDir + u"Image1.gif", SaveFormat::Gif);

    std::cout << "Workbook converted to images successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel Çalışma Kitabını XPS'ye Dönüştürme**

XPS belge formatı, her bir sayfanın düzenini ve her bir sayfanın görsel görünümünü tanımlayan yapılandırılmış XML işaretleme ve belgelerin dağıtımı, arşivleme, işleme ve yazdırma kurallarıyla birlikte renderleme kurallarından oluşur.

XPS işaretleme dili, XAML'in bir alt kümesidir ve dokümanlarda vektör grafik öğelerini içermesine olanak tanır, Windows Sunum Temeli (WPF) temel öğelerini işaretlemek için XAML kullanılır. Kullanılan öğeler yol ve diğer geometrik temel öğeler olarak tanımlanır.

Bir XPS dosyası, aslında Open Packaging Conventions kullanarak Unicode ZIP arşividir ve dokümanı oluşturan dosyaları içerir. Bunlar arasında her sayfa için XML işaretleme dosyası, metin, gömülü fontlar, raster görüntüler, 2D vektör grafikler ve dijital haklar yönetimi bilgisi bulunur. Bir XPS dosyasının içeriği, ZIP dosyalarını destekleyen bir uygulama ile açılarak incelenebilir.

Aspose.Cells 6.0.0'dan itibaren Microsoft Excel'den XPS dönüşümü desteklenmektedir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xls";
    Workbook workbook(inputFilePath);

    Worksheet sheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    SheetRender sr(sheet, options);
    sr.ToImage(0, outDir + u"out_image.png");

    XpsSaveOptions xpsOptions;
    workbook.Save(outDir + u"out_whole_printingxps.out.xps", xpsOptions);

    std::cout << "Files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel'i Ods, Sxc ve Fods (OpenOffice / LibreOffice Calc) biçimlerine dönüştürün**
Aspose.Cells, Excel dosyalarını Ods, Sxc ve Fods dosyalarına dönüştürme desteği sağlar. Aşağıdaki kod örneği, [şablon](book1.xlsx) dosyasını Ods, Sxc ve Fods dosyalarına nasıl dönüştüreceğinizi gösterir.

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

## **Excel Çalışma Kitabını MHTML Dosyalarına Dönüştürme**

MHTML, normal HTML'yi dış kaynaklarla (genellikle bağlantılı olarak bulunan, resimler, animasyonlar, sesler vb.) tek bir dosyaya birleştirir. Bunlar, .mht dosya uzantılı e-postalar için kullanılır.

Aspose.Cells, MHTML dosyalarını okuma ve yazma desteği sağlamaktadır.

Aşağıdaki kod örneği, bir çalışma kitabını MHTML dosyası olarak kaydetmenin nasıl yapıldığını göstermektedir.

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
    U16String filePath = srcDir + u"Book1.xlsx";

    // Specify the HTML Saving Options
    HtmlSaveOptions sv(SaveFormat::MHtml);

    // Instantiate a workbook and open the template XLSX file
    Workbook wb(filePath);

    // Save the MHT file
    wb.Save(filePath + u".out.mht", sv);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel Çalışma Kitabını HTML'ye Dönüştürme**

Aspose.Cells API, elektronik tabloyu HTML formatına aktarmayı destekler. Bu amaçla, Aspose.Cells [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) sınıfını kullanarak çıktı HTML'sinin çeşitli yönlerini kontrol etme esnekliği sağlar.

Aşağıdaki kod örneği, bir çalışma kitabını HTML dosyası olarak kaydetme yöntemini gösterir.

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
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"ConvertingToHTMLFiles_out.html";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in HTML format
    wb.Save(outputFilePath, SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **HTML için Görüntü Tercihlerini Ayarlama**

8.0.2 sürümünden itibaren, Aspose.Cells [**GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) sınıfı için [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) sınıfını açtı ve geliştiricilerin, elektronik tabloları HTML formatına kaydederken resim tercihini belirtmelerine olanak tanıdı.

İşte uygulanabilecek bazı resim ayarlarının detayları:

- [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/): Görüntü türünü belirtir. Lütfen not edin, tüm şekiller, grafikler de dahil olmak üzere çıktı HTML'de resim olarak oluşturulur.
- [**GetQuality()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getquality/): [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) Jpeg olarak ayarlandığında, resmin kalitesini 0 ile 100 arasında belirtir.
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/): Görselin dikey düzeyde inç başına nokta cinsinden çözünürlüğünü alır veya ayarlar.
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/): Görselin yatay düzeyde inç başına nokta cinsinden çözünürlüğünü alır veya ayarlar.
- [**TiffCompression**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/): [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) parametresi TIFF olarak belirtildiğinde, görüntülerin sıkıştırma türünü alır veya ayarlar.
- [**GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/): Görüntü biçimi Png olarak belirtildiğinde bir görüntünün arka planının saydam olup olmayacağını belirtir.

Aşağıdaki kod, farklı tercihleri belirtmek için [**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) kullanımını gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"Book1.xlsx";

    Workbook book(filePath);
    HtmlSaveOptions saveOptions(SaveFormat::Html);

    saveOptions.GetImageOptions().SetImageType(ImageType::Png);

    book.Save(outDir + u"output.html", saveOptions);

    std::cout << "Spreadsheet converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel Çalışma Kitabını Markdown'a Dönüştür**

Aspose.Cells API, elektronik tabloları Markdown formatına dışa aktarma desteği sağlar. Aktif çalışma sayfasını Markdown'a dışa aktarmak için, [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yönteminin ikinci parametresi olarak [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) değeri geçin. Ayrıca, çalışma sayfasını Markdown'a dışa aktarmak için ek ayarları belirtmek üzere [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) sınıfını kullanabilirsiniz.

Aşağıdaki kod örneği, aktif çalışma sayfasını [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enum öğesini kullanarak dışa aktarmayı gösterir. Lütfen kod ile oluşturulan [çıktı Markdown dosyasını](md_sample.txt) referans alın.

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

    // Path of output Markdown file
    U16String outputFilePath = outDir + u"Book1.md";

    // Create workbook from the input Excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as Markdown
    workbook.Save(outputFilePath, SaveFormat::Markdown);

    std::cout << "Workbook saved as Markdown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel Çalışma Kitabını JSON'a Dönüştür**

Aspose.Cells, çalışma kitabını JSON (JavaScript Nesne Gösterimi) dosyasına dönüştürme desteği sağlar.

Aşağıdaki kod örneği, aktif çalışma sayfasını [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enum öğesini kullanarak JSON'a dışa aktarmayı gösterir. Lütfen kodu, [kaynak dosyayı](Book1.xlsx) JSON [çıktı dosyasına](Book1.Json) dönüştürmek için kullanın.

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

## **Excel'i XML'e Dönüştür**
Aspose.Cells, bir çalışma kitabını Excel 2003 Elektronik Tablo XML ve düz XML veriye dönüştürmeyi destekler.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save as Excel 2003 Spreadsheet XML
    U16String outputFilePath1 = u"Spreadsheet.xml";
    workbook.Save(outputFilePath1);

    // Save as plain XML data
    U16String outputFilePath2 = u"data.xml";
    XmlSaveOptions xmlSaveOptions;
    workbook.Save(outputFilePath2, xmlSaveOptions);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel Çalışma Kitabını TIFF'e Dönüştür**
Aspose.Cells, bir çalışma kitabını TIFF dosyasına dönüştürmeyi destekler.

Aşağıdaki kod parçası, Excel'i TIFF'e dönüştürmeyi göstermektedir:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open a template excel file
    U16String inputFilePath(u"Book1.xlsx");
    Workbook book(inputFilePath);

    // Save file to TIFF
    U16String outputFilePath(u"out.tiff");
    book.Save(outputFilePath);

    std::cout << "File saved successfully to TIFF format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel Çalışma Kitabını DOCX'e Dönüştür**

Aspose.Cells API, çalışma sayfalarını DOCX formatına dönüştürme desteği sağlar. Çalışma kitabını DOCX'e aktarmak için, [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yönteminin ikinci parametresi olarak [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) değeri geçin. Ayrıca, çalışma sayfasını DOCX'e dışa aktarmak için [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) sınıfını kullanabilirsiniz.

Aşağıdaki kod örneği, aktif çalışma sayfasını [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enum öğesini kullanarak DOCX’e dışa aktarmayı gösterir. Lütfen kod ile oluşturulan [çıktı DOCX dosyasını](Book1.docx) referans alın.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output docx file
    U16String outputFilePath = outDir + u"Book1.docx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save as DOCX
    workbook.Save(outputFilePath, SaveFormat::Docx);

    std::cout << "File saved successfully as DOCX!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel Çalışma Kitabını PPTX'e Dönüştür**

Aspose.Cells API, çalışma sayfalarını PPTX formatına dönüştürme desteği sağlar. Çalışma kitabını PPTX'e aktarmak için, [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yönteminin ikinci parametresi olarak [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) değeri geçin. Ayrıca, çalışma sayfasını PPTX’e dışa aktarmak için [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) sınıfını kullanabilirsiniz.

Aşağıdaki kod örneği, [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumerasyon üyesini kullanarak aktif çalışma sayfasını PPTX formatına dışa aktarmayı gösterir. Referans için kod tarafından oluşturulan [çıktı PPTX dosyasını](Book1.pptx) inceleyiniz.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output PowerPoint file
    U16String outputFilePath = outDir + u"Book1.pptx";

    // Create workbook from the input Excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as a PowerPoint file
    workbook.Save(outputFilePath, SaveFormat::Pptx);

    std::cout << "Workbook saved as PowerPoint successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel Çalışma Kitabını EPUB'a dönüştür**

Aspose.Cells API, elektronik tabloyu EPUB formatına dönüştürmeyi destekler. Çalışma kitabını EPUB'a dışa aktarmak için, [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metodunun ikinci parametresi olarak [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) kullanın. Ayrıca, çalışma sayfasını EPUB'a dışa aktarmak için ek ayarlar belirlemek üzere [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) sınıfını da kullanabilirsiniz.

Aşağıdaki kod örneği, [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumerasyon üyesini kullanarak aktif çalışma sayfasını EPUB formatına dışa aktarmayı gösterir.

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
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output EPUB file
    U16String outputFilePath = outDir + u"ConvertingToEPUBFiles_out.epub";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in EPUB format
    wb.Save(outputFilePath, SaveFormat::Epub);

    std::cout << "File converted to EPUB format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel Çalışma Dosyasını AZW3'e dönüştür**

Aspose.Cells API, elektronik tabloyu AZW3 formatına dönüştürmeyi destekler. Çalışma kitabını AZW3'e dışa aktarmak için, [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metodunun ikinci parametresi olarak [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) kullanın. Ayrıca, çalışma sayfasını AZW3'e dışa aktarmak için ek ayarları belirlemek üzere [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) sınıfını da kullanabilirsiniz.

Aşağıdaki kod örneği, [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumerasyon üyesini kullanarak aktif çalışma sayfasını AZW3 formatına dışa aktarmayı gösterir.

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
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output AZW3 file
    U16String outputFilePath = outDir + u"ConvertingToEPUBFiles_out.azw3";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in AZW3 format
    wb.Save(outputFilePath, SaveFormat::Azw3);

    std::cout << "File converted to AZW3 format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [XLSB Revizyonunu XLSM'ye Dönüştür](/cells/tr/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/tr/cpp/convert-excel-to-html/)
- [Görüntü](/cells/tr/cpp/convert-excel-to-image/)
- [Json](/cells/tr/cpp/convert-workbook-to-json/)
- [Excel çalışma kitabını Ods, Sxc ve Fods (OpenOffice / LibreOffice calc) formatlarına dönüştür.](/cells/tr/cpp/convert-excel-to-ods/)
- [Pdf](/cells/tr/cpp/convert-excel-workbook-to-pdf/)
- [Excel'i CSV, TSV ve Txt formatlarına dönüştür](/cells/tr/cpp/convert-excel-to-csv-tsv-and-txt/)
- [Belge Dönüşüm İlerlemesini İzle](/cells/tr/cpp/track-document-conversion-progress/)
- [CSV, TSV ve TXT'yi Excel'e dönüştür](/cells/tr/cpp/convert-csv-tsv-and-txt-to-excel/)
{{< app/cells/assistant language="cpp" >}}
