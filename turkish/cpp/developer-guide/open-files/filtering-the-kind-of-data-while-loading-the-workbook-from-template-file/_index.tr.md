---
title: C++ ile şablon dosyasından çalışma kitabı yüklerken veri türünü filtreleme
linktitle: Çalışma Kitabı Yüklerken Veri Filtreleme
type: docs
weight: 400
url: /tr/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Aspose.Cells kullanarak şablon dosyasından çalışma kitabı yüklerken belirli veri türlerini nasıl filtreleyeceğinizi öğrenin.
---

{{% alert color="primary" %}}

 Bazen, çalışma kitabını şablon dosyasından oluştururken hangi tür verinin yükleneceğini belirtmek istersiniz. Yüklenen veriyi filtrelemek, özellikle [LightCells API'leri](/cells/tr/cpp/using-lightcells-api/) kullanırken, performansı artırabilir. Bu amaçla [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) özelliğini kullanın.

{{% /alert %}}

Aşağıdaki örnek kod, şablon dosyasından çalışma kitabı yüklenirken yalnızca şekil nesnelerini yükler. Bu amaçla ayarladığınız [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) özelliği [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) olacağı için, kırmızı renkli ve sarı arka planlı verilerin yüklenmeyeceği şablon dosyasının içeriğini ve açıklamasını gösterir.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Aşağıdaki ekran görüntüsü, verilerin kırmızı renkli ve sarı arka planlı olmadığını, ancak tüm şekillerin olduğunu gösterir.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

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

    // Set the load options, we only want to load shapes and do not want to load data
    LoadOptions loadOptions(LoadFormat::Xlsx);
    loadOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Create workbook object from sample excel file using load options
    Workbook workbook(srcDir + u"sampleFilterChars.xlsx", loadOptions);

    // Save the output in pdf format
    workbook.Save(outDir + u"sampleFilterChars_out.pdf", SaveFormat::Pdf);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
