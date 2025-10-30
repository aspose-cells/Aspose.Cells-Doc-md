---
title: Abilita le Proprietà Personalizzate CSS durante il salvataggio in HTML con C++
linktitle: Abilita le Proprietà Personalizzate CSS durante il salvataggio in HTML
type: docs
weight: 320
url: /it/cpp/enable-css-custom-properties-while-saving-to-html/
description: Scopri come abilitare le proprietà personalizzate CSS durante il salvataggio di file Excel in HTML usando Aspose.Cells for C++. Migliora le performance riducendo i dati di immagine ridondanti.
---

## **Possibili Scenari di Utilizzo**

Quando salvi il tuo file Excel in HTML, nel caso in cui ci siano più occorrenze di un'immagine base64, con proprietà personalizzate i dati dell'immagine devono essere salvati una sola volta così da migliorare le performance dell'HTML risultante. Usa la proprietà [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/) e impostala su **true** durante il salvataggio in HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Abilita le Proprietà CSS Personalizzate durante il salvataggio in HTML**

Il seguente esempio di codice mostra l'uso della proprietà [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/). Lo screenshot mostra l'effetto di questa proprietà quando non è impostata su **true**. Scarica il [file Excel di esempio](50528260.xlsx) usato in questo codice e l'[HTML di output](50528261.zip) generato per riferimento.

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
    Workbook wb(srcDir + u"sampleEnableCssCustomProperties.xlsx");

    // Create HtmlSaveOptions object
    HtmlSaveOptions opts;

    // Set ExportImagesAsBase64 to true
    opts.SetExportImagesAsBase64(true);

    // Enable EnableCssCustomProperties
    opts.SetEnableCssCustomProperties(true);

    // Save the workbook in HTML format
    wb.Save(outDir + u"outputEnableCssCustomProperties.html", opts);

    std::cout << "Workbook saved successfully with CSS custom properties enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
