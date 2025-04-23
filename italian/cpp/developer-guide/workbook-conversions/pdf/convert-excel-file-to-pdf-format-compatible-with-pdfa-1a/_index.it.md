---
title: Convertire il file Excel in formato PDF compatibile con PDFA 1a con C++
linktitle: Converti il file Excel nel formato PDF compatibile con PDFA 1a
type: docs
weight: 130
url: /it/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Impara come convertire i file Excel in formato PDF/A 1a utilizzando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**

PDF/A è una versione unica di PDF progettata per la preservazione a lungo termine dei documenti. PDF/A è una versione standardizzata ISO del formato Portable Document Format (PDF) che include tutti i font utilizzati nel documento all’interno del file PDF. PDF/A si differenzia dal PDF proibendo funzionalità come il collegamento di font (anziché l’incorporamento dei font) e la crittografia. Aspose.Cells ti permette di salvare i file Excel in file PDF conformi a PDF/A (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab, e PDF/A-3u sono supportati). Questo argomento descrive come salvare il workbook Excel in un file PDF conforme a PDF/A (PDF/A-1a).

## **Convertire file Excel nel formato PDF compatibile con PDF/A-1a**

Gli sviluppatori possono usare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) per impostare attributi diversi per la conversione. Impostare proprietà diverse della classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) ti dà il controllo su impostazioni di stampa, font, sicurezza e compressione per il PDF di output. La proprietà più importante è [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/) che permette di salvare i file Excel come file PDF conformi a PDF/A.

Il seguente codice di esempio spiega come convertire un file Excel nel formato PDF compatibile con PDF/A-1a. Consulta il suo [output PDF](outputCompliancePdfA1a.pdf) e uno screenshot a scopo di riferimento.

## **Screenshot**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and add some message inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This PDF format is compatible with PDFA-1a.");

    // Create pdf save options and set its compliance to PDFA-1a
    PdfSaveOptions opts;
    opts.SetCompliance(PdfCompliance::PdfA1a);

    // Save the output pdf
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputCompliancePdfA1a.pdf", opts);

    std::cout << "PDF created successfully with PDFA-1a compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
