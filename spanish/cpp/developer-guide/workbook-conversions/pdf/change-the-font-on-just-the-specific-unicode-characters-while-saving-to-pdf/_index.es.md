---
title: Cambiar la fuente en caracteres Unicode específicos al guardar en PDF con C++
linktitle: Cambiar la fuente en caracteres Unicode
type: docs
weight: 260
url: /es/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Aprende cómo cambiar la fuente de caracteres Unicode específicos al guardar en PDF usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Algunos caracteres Unicode no se pueden mostrar con la fuente especificada por el usuario. Uno de estos caracteres Unicode es **Guión no separable** (U+2011) y su número Unicode es 8209. Este carácter no se puede mostrar con **Times New Roman**, pero se puede mostrar con otras fuentes como **Arial Unicode MS**.

 Cuando un carácter así aparece dentro de una palabra o frase que está en una fuente específica como Times New Roman, Aspose.Cells cambia toda la fuente de la palabra o frase a una fuente que pueda mostrar ese carácter, como Arial Unicode MS.

 Sin embargo, este comportamiento no es deseado para algunos usuarios, y solo quieren cambiar la fuente de ese carácter específico, en lugar de cambiar toda la fuente de la palabra o frase.

 Para abordar este problema, Aspose.Cells ofrece la propiedad `PdfSaveOptions.IsFontSubstitutionCharGranularity`, que debe establecerse en `true` para que solo se cambie la fuente del carácter que no se puede mostrar a una fuente visible, mientras que el resto de la palabra o frase permanecen en la fuente original.

{{% /alert %}}

## **Ejemplo**

La siguiente captura de pantalla compara los dos PDF generados por el código de muestra a continuación.

 Uno se genera sin configurar la propiedad `PdfSaveOptions.IsFontSubstitutionCharGranularity`, y el otro se genera después de configurarla en `true`.

 Como puedes ver en el primer PDF, la fuente de toda la oración cambió de Times New Roman a Arial Unicode MS a causa del guion no cortante. Mientras que en el segundo PDF, solo cambió la fuente del guion no cortante.

|**Archivo PDF primero**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**Archivo PDF segundo**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **Código de muestra**

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

    // Create workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style style = cell1.GetStyle();
    style.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(style);
    cell2.SetStyle(style);

    // Put the values inside the cell
    cell1.PutValue(u"Hello without Non-Breaking Hyphen");
    cell2.PutValue(u"Hello\u2011 with Non-Breaking Hyphen");

    // Autofit the columns
    worksheet.AutoFitColumns();

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.pdf");

    // Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
    PdfSaveOptions opts;
    opts.SetIsFontSubstitutionCharGranularity(true);
    workbook.Save(outDir + u"SampleOutput2_out.pdf", opts);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
