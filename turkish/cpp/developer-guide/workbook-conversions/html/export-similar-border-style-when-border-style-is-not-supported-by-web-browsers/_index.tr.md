---
title: Web Tarayıcılar Tarafından Desteklenmeyen Sınır Stiliyle Benzer Sınır Stili Dışa Aktarımı C++ ile
linktitle: Web Tarayıcıları tarafından Desteklenmeyen Kenar Stili Benzeri Kenar Stilini Dışa Aktar
type: docs
weight: 70
url: /tr/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Aspose.Cells kullanarak web tarayıcıları tarafından desteklenmeyen benzer sınır stillerinin nasıl dışa aktarılacağı öğrenin.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel, web tarayıcıları tarafından desteklenmeyen bazı çizgili sınır türlerini destekler. Böyle bir Excel dosyasını Aspose.Cells kullanarak HTML'ye dönüştürürken, bu sınırlar kaldırılır. Ancak, Aspose.Cells `[**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/)` özelliği ile bu sınırların da gösterilmesini destekleyebilir. Lütfen değeri **true** olarak ayarlayın ve desteklenmeyen sınırlar da HTML dosyasına dışa aktarılacaktır.

## **CrossHideRight ile Üzerine Binme Content'ini HTML'şe kaydederken Gizle**

Aşağıdaki örnek kod, desteklenmeyen bazı sınırları içeren [örnek Excel dosyasını](64716806.xlsx) yükler ve aşağıdaki ekran görüntüsünde gösterildiği gibi, `[**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/)` özelliğinin etkisini gösterir. Ayrıca ekran görüntüsü, [çıkış HTML'sinde](64716804.zip) `[**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/)` özelliğinin etkisini detaylandırır.

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the sample Excel file
    U16String inputFilePath(u"sampleExportSimilarBorderStyle.xlsx");
    Workbook workbook(inputFilePath);

    // Specify Html Save Options - Export Similar Border Style
    HtmlSaveOptions opts;
    opts.SetExportSimilarBorderStyle(true);

    // Save the workbook in Html format with specified Html Save Options
    U16String outputFilePath(u"outputExportSimilarBorderStyle.html");
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully in HTML format with similar border styles!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
