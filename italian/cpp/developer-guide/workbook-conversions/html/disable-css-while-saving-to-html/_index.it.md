---
title: Disabilita CSS durante il salvataggio in HTML con C++
linktitle: Disabilitare CSS durante il salvataggio in HTML
type: docs
weight: 320
url: /it/cpp/disable-css-while-saving-to-html/
description: Impara come disattivare il CSS durante il salvataggio di file Excel in HTML usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Quando salvi il tuo file Excel come HTML a pagina singola, di solito gli elementi CSS saranno incorporati nel file HTML e si troveranno nella sezione HEAD. Se allegi questo file come contenuto/corpo di un'email, gli elementi CSS saranno rimossi dalla maggior parte dei client di posta elettronica, causando rendering scorretto. La versione 24.12 di Aspose.Cells introduce un’opzione che permette di disabilitare opzionalmente il CSS, consentendo di applicare gli stili direttamente agli elementi HTML stessi. Se vuoi impostare l’HTML come contenuto/corpo dell’email, utilizza la proprietà [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/) e impostala su **true**.

## **Disabilita CSS durante il salvataggio in HTML**

Il seguente esempio di codice mostra l'uso della proprietà [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/).

## **Codice di Esempio**

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

    // Load sample workbook
    Workbook wb(srcDir + u"sampleDisableCss.xlsx");

    // Disable CSS
    HtmlSaveOptions opts;
    opts.SetDisableCss(true);

    // Save the workbook in HTML
    wb.Save(outDir + u"outputDisable.html", opts);

    std::cout << "Workbook saved with CSS disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
