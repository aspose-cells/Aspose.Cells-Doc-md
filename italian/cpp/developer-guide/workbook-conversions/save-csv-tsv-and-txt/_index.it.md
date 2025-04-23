---
title: Converti Excel in CSV, TSV e Txt con C++
linktitle: Salva come CSV, TSV e Txt
type: docs
weight: 40
url: /it/cpp/convert-excel-to-csv-tsv-and-txt/
description: Converti facilmente file Excel in formati CSV, TSV e TXT usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells rende possibile convertire file Excel, ODS, JSON e altri formati in CSV, TSV e TXT.

{{% /alert %}}

## **Salvataggio Workbook in formato testo o CSV**

A volte si desidera convertire o salvare un workbook con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV, ecc.), sia Microsoft Excel che Aspose.Cells di default salvano solo i contenuti del foglio di lavoro attivo.

L'esempio di codice seguente spiega come salvare un intero workbook in formato testo. Carica il workbook di origine che potrebbe essere un file di fogli di calcolo Microsoft Excel o OpenOffice (quindi XLS, XLSX, XLSM, XLSB, ODS e così via) con un qualsiasi numero di fogli di lavoro.

Quando il codice viene eseguito, converte i dati di tutti i fogli nel workbook nel formato TXT.

Puoi modificare lo stesso esempio per salvare il file in formato CSV. Per impostazione predefinita, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) è una virgola, quindi non specificare un separatore se si salva in formato CSV.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/TxtSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    U16String outputFilePath = srcDir + u"out.txt";
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully as text file!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Salvataggio file di testo con separatore personalizzato**

I file di testo contengono dati del foglio di calcolo senza formattazione. Il file è una sorta di file di testo semplice che può avere alcuni delimitatori personalizzati tra i suoi dati.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/TxtSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and opening the file from its path
    Workbook workbook(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';'); // Using U16String for the char

    // Save the file with the options
    workbook.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Mantieni i separatori per le righe vuote durante l'esportazione di fogli di calcolo in formato CSV](/cells/it/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Taglia righe e colonne vuote iniziali durante l'esportazione di fogli di calcolo nel formato CSV](/cells/it/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
