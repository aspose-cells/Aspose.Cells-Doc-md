---
title: Establecer fuente predeterminada al renderizar hoja de cálculo a HTML con C++
linktitle: Establecer la fuente predeterminada al renderizar la hoja de cálculo en HTML
type: docs
weight: 370
url: /es/cpp/set-default-font-while-rendering-spreadsheet-to/
description: Aprende cómo establecer la fuente predeterminada al renderizar hojas de cálculo a HTML utilizando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells te permite establecer la fuente predeterminada al renderizar una hoja de cálculo a HTML. Por favor, usa [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/) para este propósito. Esta propiedad es útil cuando hay celdas en una hoja de cálculo que tienen fuentes inválidas o no existentes. Entonces, esas celdas se renderizarán con la fuente especificada con la propiedad [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/).

{{% /alert %}}

## Establecer la fuente predeterminada al renderizar la hoja de cálculo en HTML

El siguiente código de ejemplo crea un libro de trabajo, agrega algo de texto en la celda B4 de la primera hoja de cálculo y establece su fuente en una fuente desconocida o inexistente. Luego guarda el libro en HTML estableciendo diferentes nombres de fuente predeterminada como Courier New, Arial, Times New Roman, etc.

La captura de pantalla muestra el efecto de establecer diferentes nombres de fuentes predeterminadas mediante la propiedad [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

El código genera el [archivo HTML de salida con Courier New](5115516), el [archivo HTML de salida con Arial](5115518), y el [archivo HTML de salida con Times New Roman](5115517).

## Código de Muestra

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

    // Create workbook object and access first worksheet
    Workbook wb;
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B4 and add some text inside it
    Cell cell = ws.GetCells().Get(u"B4");
    cell.PutValue(u"This text has some unknown or invalid font which does not exist.");

    // Set the font of cell B4 which is unknown
    Style st = cell.GetStyle();
    st.GetFont().SetName(u"UnknownNotExist");
    st.GetFont().SetSize(20);
    cell.SetStyle(st);

    // Now save the workbook in html format and set the default font to Courier New
    HtmlSaveOptions opts;
    opts.SetDefaultFontName(u"Courier New");
    wb.Save(outDir + u"out_courier_new_out.htm", opts);

    // Now save the workbook in html format once again but set the default font to Arial
    opts.SetDefaultFontName(u"Arial");
    wb.Save(outDir + u"out_arial_out.htm", opts);

    // Now save the workbook in html format once again but set the default font to Times New Roman
    opts.SetDefaultFontName(u"Times New Roman");
    wb.Save(outDir + u"times_new_roman_out.htm", opts);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
