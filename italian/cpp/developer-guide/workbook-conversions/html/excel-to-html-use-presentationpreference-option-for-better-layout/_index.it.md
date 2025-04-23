---
title: Excel in HTML  Utilizza l Opzione PresentationPreference per un layout migliore con C++
linktitle: Excel to HTML  Utilizzare l Opzione PresentationPreference per una Migliore Layout
type: docs
weight: 220
url: /it/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
description: Impara a rendere un layout migliore quando salvi file Excel in HTML con C++.
---

{{% alert color="primary" %}} 

Aspose.Cells fornisce una utile proprietà HtmlSaveOptions.PresentationPreference per gli sviluppatori che necessitano di un layout migliore durante il salvataggio di un file Microsoft Excel in formato HTML o MHT. Il valore predefinito della proprietà è false. Consigliamo di impostare questa proprietà su true per ottenere una presentazione più attraente dei report Excel.

{{% /alert %}} 

Si prega di vedere il codice di esempio di seguito che dimostra come renderizzare un file HTML da un report Excel con preferenza di presentazione attiva.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Instantiate the Workbook and load an Excel file
    Workbook workbook(inputFilePath);

    // Create HtmlSaveOptions object
    HtmlSaveOptions options;

    // Set the Presentation preference option
    options.SetPresentationPreference(true);

    // Save the Excel file to HTML with specified option
    U16String outputFilePath = srcDir + u"outPresentationlayout1.out.html";
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file saved as HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
