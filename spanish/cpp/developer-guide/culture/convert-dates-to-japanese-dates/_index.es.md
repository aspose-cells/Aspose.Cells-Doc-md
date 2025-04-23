---
title: Convertir fechas a fechas japonesas con C++
linktitle: Convertir Fechas a Fechas Japonesas
type: docs
weight: 350
url: /es/cpp/convert-dates-to-japanese-dates/
description: Aprende cómo convertir fechas gregorianas a fechas japonesas usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

En el calendario japonés, una nueva era comienza con el reinado de un nuevo emperador. El 1 de mayo de 2019, un nuevo emperador asumió el poder, finalizando la era Heisei y comenzando la era Reiwa.

{{% /alert %}}

Aspose.Cells ofrece una forma de convertir fechas gregorianas a fechas japonesas. Durante esta conversión, también se consideran los cambios en la era. El siguiente fragmento de código convierte el archivo [Excel fuente](90112015.xlsx) que contiene fechas gregorianas a un [PDF de salida](90112016.pdf) con fechas japonesas, como se muestra en la imagen abajo.

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)

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

    // Create load options for XLSX format
    LoadOptions options(LoadFormat::Xlsx);

    // Set culture info to Japanese
    options.SetLanguageCode(CountryCode::Japan);

    // Load the workbook with Japanese dates
    Workbook workbook(srcDir + u"JapaneseDates.xlsx", options);

    // Save the workbook as PDF
    workbook.Save(outDir + u"JapaneseDates.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF with Japanese dates!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
