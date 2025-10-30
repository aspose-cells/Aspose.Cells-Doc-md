---
title: Cambia il font sui caratteri Unicode specifici durante il salvataggio in PDF con C++
linktitle: Cambia il font sui caratteri Unicode
type: docs
weight: 260
url: /it/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Impara come cambiare il font di caratteri Unicode specifici durante il salvataggio in PDF usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Alcuni caratteri Unicode non possono essere visualizzati dal font specificato dall'utente. Uno di questi caratteri Unicode è **Trattino Non-Rotoso** (U+2011) e il suo numero Unicode è 8209. Questo carattere non può essere visualizzato con **Times New Roman**, ma può essere visualizzato con altri font come **Arial Unicode MS**.

Quando un carattere di questo tipo compare all'interno di una parola o frase in un font specifico come Times New Roman, Aspose.Cells cambia il font dell'intera parola o frase in un font che può visualizzare questo carattere come Arial Unicode MS.

Tuttavia, questo comportamento è indesiderato per alcuni utenti, e desiderano che venga cambiato solo il font di quel carattere specifico invece di cambiare il font di tutta la parola o frase.

Per affrontare questo problema, Aspose.Cells fornisce la proprietà `PdfSaveOptions.IsFontSubstitutionCharGranularity`, che dovrebbe essere impostata su `true` per cambiare il font solo del carattere specifico che non può essere visualizzato, mantenendo invariato il font del resto della parola o frase.

{{% /alert %}}

## **Esempio**

Lo screenshot seguente confronta i due file PDF generati dal codice di esempio qui sotto.

Uno viene generato senza impostare la proprietà `PdfSaveOptions.IsFontSubstitutionCharGranularity`, e l'altro è stato generato dopo aver impostato la proprietà `PdfSaveOptions.IsFontSubstitutionCharGranularity` su `true`.

Come puoi vedere nel primo PDF, il carattere di tutta la frase è cambiato da Times New Roman a Arial Unicode MS a causa dell'Hypen Non Interrotto. Mentre nel secondo PDF, solo il font dell'Hypen Non Interrotto è cambiato.

|**Primo file PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**Secondo file PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **Codice di Esempio**

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
{{< app/cells/assistant language="cpp" >}}
