---
title: Converti date in date giapponesi con C++
linktitle: Convertire le date in date giapponesi
type: docs
weight: 350
url: /it/cpp/convert-dates-to-japanese-dates/
description: Impara come convertire date Gregoriana in date giapponesi usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Nel Calendario Giapponese, una nuova era inizia con il regno di un nuovo imperatore. Il 1° maggio 2019, un nuovo imperatore ha preso il potere, con cui l'era Heisei è terminata e l'era Reiwa è iniziata.

{{% /alert %}}

Aspose.Cells fornisce un metodo per convertire le date Gregoriane in date giapponesi. Durante questa conversione, vengono considerate anche le variazioni dell'epoca. Il seguente frammento di codice converte il file [Excel di origine](90112015.xlsx) contenente date Gregoriane in un [PDF di output](90112016.pdf) con date giapponesi come mostrato nell'immagine sotto.

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
{{< app/cells/assistant language="cpp" >}}
