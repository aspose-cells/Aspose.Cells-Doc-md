---
title: Çalışma Sayfası CSS sini Ayrı Olarak Çıktıya Dışa Aktar C++ ile
linktitle: Çıktı HTML sindeki Sayfa CSS sini Ayrı Ayrı Dışa Aktarma
type: docs
weight: 80
url: /tr/cpp/export-worksheet-css-separately-in-output/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını HTML ye dönüştürürken çalışma sayfası CSS lerini ayrı olarak ihraç etmeyi öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, Excel dosyanızı HTML'ye dönüştürürken çalışma sayfası CSS'sini ayrı olarak dışa aktarma özelliği sağlar. Lütfen bu amaçla [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/) özelliğini kullanın ve Excel dosyasını HTML formatına kaydederken **true** olarak ayarlayın.

## **Çıktı HTML'sindeki Sayfa CSS'sini Ayrı Ayrı Dışa Aktarma**

Aşağıdaki örnek kod, bir Excel dosyası oluşturur, **B5** hücresine **kırmızı** renkte bir metin ekler ve ardından [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/) özelliğini kullanarak HTML formatında kaydeder. Referans için kod tarafından oluşturulan [çıktı HTML'si](60489766.zip)'nı inceleyin. Örnek kodun bir çıktısı olarak içinde **stylesheet.css** bulacaksınız.

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and put value inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This is some text.");

    // Set the style of the cell - font color is Red
    Style st = cell.GetStyle();
    st.GetFont().SetColor(Color::Red());
    cell.SetStyle(st);

    // Specify html save options - export worksheet css separately
    HtmlSaveOptions opts;
    opts.SetExportWorksheetCSSSeparately(true);

    // Save the workbook in html
    wb.Save(u"outputExportWorksheetCSSSeparately.html", opts);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Tek Sayfa Çalışma Kitabını HTML'ye Dışa Aktar**

Birden fazla çalışma sayfası içeren bir çalışma kitabı Aspose.Cells kullanılarak HTML'ye dönüştürüldüğünde, CSS ve çoklu HTML dosyalarını içeren bir klasörle birlikte bir HTML dosyası oluşturur. Bu HTML dosyası tarayıcıda açıldığında sekmeler görülür. Aynı davranış, tek sayfalık çalışma kitabı HTML'ye dönüştürülürken de istenir. Önceden, tek sayfalık çalışma kitapları için ayrı bir klasör oluşturulmazdı ve yalnızca bir HTML dosyası oluşturulurdu. Böyle bir HTML dosyası tarayıcıda açıldığında sekme göstermez. MS Excel, tek sayfalık çalışma kitabı için de uygun bir klasör ve HTML oluşturur ve bu nedenle aynı davranış Aspose.Cells API'leri kullanılarak uygulanmıştır. Aşağıdaki bağlantıdan örnek dosya indirilebilir ve aşağıdaki örnek kodda kullanılabilir:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Örnek Kod**

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
    U16String inputFilePath = srcDir + u"sampleSingleSheet.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputSampleSingleSheet.htm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify HTML save options
    HtmlSaveOptions options;

    // Set optional settings
    options.SetEncoding(EncodingType::UTF8);
    options.SetExportImagesAsBase64(true);
    options.SetExportGridLines(true);
    options.SetExportSimilarBorderStyle(true);
    options.SetExportBogusRowData(true);
    options.SetExcludeUnusedStyles(true);
    options.SetExportHiddenWorksheet(true);

    // Save the workbook in HTML format with specified HTML save options
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
