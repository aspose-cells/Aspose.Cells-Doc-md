---
title: Esporta DataBar, ColorScale e IconSet di formattazione condizionale durante la conversione di Excel in HTML con C++
linktitle: Esporta formattazione condizionale in HTML
type: docs
weight: 30
url: /it/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
description: Scopri come esportare DataBar, ColorScale e IconSet di formattazione condizionale durante la conversione di file Excel in HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Puoi esportare la formattazione condizionale DataBar, ColorScale e IconSet mentre converti il tuo file Excel in HTML. Questa funzione è parzialmente supportata da Microsoft Excel ma Aspose.Cells for C++ la supporta completamente.

{{% /alert %}} 

## **Esporta DataBar, ColorScale e IconSet di formattazione condizionale durante la Conversione da Excel in HTML**
La schermata successiva mostra il [file excel di esempio](5115558.xlsx) con Formattazione condizionale DataBar, ColorScale e IconSet. Puoi scaricare il [file excel di esempio](5115558.xlsx) dal link fornito.

![todo:image_alt_text](conversion_1.png)

La schermata successiva mostra il file HTML di output di Aspose.Cells con Formattazione condizionale DataBar, ColorScale e IconSet. Come puoi vedere, è identico al [file excel di esempio](5115558.xlsx).

![todo:image_alt_text](conversion_2.png)

### **Codice di Esempio**
Il seguente esempio di codice converte il file excel di esempio in HTML, che rappresenta una semplice [conversione da Excel a HTML](/cells/it/cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).

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

    // Load your sample excel file in a workbook object
    Workbook wb(filePath);

    // Save it in HTML format
    wb.Save(outDir + u"ConvertingToHTMLFiles_out.html", SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
