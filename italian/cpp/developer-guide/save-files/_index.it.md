---
title: Diversi modi per salvare file con C++
linktitle: Salva file
type: docs
weight: 40
url: /it/cpp/different-ways-to-save-files/
description: Aspose.Cells for C++ può salvare file in diversi formati. Salva in PDF. Salva in HTML. Salva in DOCX. Salva in PPTX. Salva in JSON. Salva in MHTML.
keywords: Aspose.Cells salva Excel in PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML e altri usando C++, salva o converte workbook in PDF, HTML, JSON, TXT, SQL in C++.
---

{{% alert color="primary" %}}

Aspose.Cells rende possibile creare e salvare file. Questo articolo spiega i vari modi in cui i file possono essere salvati.

{{% /alert %}}

## **Diversi modi per salvare i file**

Aspose.Cells fornisce il [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file di Microsoft Excel e fornisce le proprietà e i metodi necessari per lavorare con i file di Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) fornisce il metodo [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) utilizzato per salvare i file di Excel. Il metodo [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) ha molte sovraccarichi che vengono utilizzati per salvare file in modi diversi.

Il formato del file in cui il file viene salvato è deciso dall'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)

|**Tipi di formato file**|**Descrizione**|
| :- | :- |
| CSV | Rappresenta un file CSV |
|Excel97To2003| Rappresenta un file Excel 97 - 2003 |
|Xlsx| Rappresenta un file Excel 2007 XLSX |
|Xlsm| Rappresenta un file Excel 2007 XLSM |
|Xltx| Rappresenta un modello di Excel 2007 XLTX |
|Xltm|Rappresenta un file XLTM abilitato per macro di Excel 2007|
|Xlsb|Rappresenta un file XLSB binario di Excel 2007|
|SpreadsheetML|Rappresenta un file XML di fogli di calcolo|
|TSV|Rappresenta un file di valori separati da tabulazione|
|TabDelimited|Rappresenta un file di testo delimitato da tabulazioni|
|ODS|Rappresenta un file ODS|
|Html|Rappresenta file HTML|
|MHtml|Rappresenta file MHTML|
|Pdf|Rappresenta un file PDF|
|XPS|Rappresenta un documento XPS|
|TIFF|Rappresenta il formato di file immagine TIFF (Tagged Image File Format)|

## **Come Salvare File in Diversi Formati**

Per salvare i file in una posizione di archiviazione, specificare il nome del file (completo di percorso di archiviazione) e il formato desiderato del file (dall'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)) durante la chiamata del metodo [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) dell'oggetto [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).

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

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xls";

    // Load your source workbook
    Workbook workbook(filePath);

    // Save in Excel 97 to 2003 format
    workbook.Save(outDir + u".output.xls");
    // OR
    XlsSaveOptions xlsSaveOptions;
    workbook.Save(outDir + u".output.xls", xlsSaveOptions);

    // Save in Excel2007 xlsx format
    workbook.Save(outDir + u".output.xlsx", SaveFormat::Xlsx);

    // Save in Excel2007 xlsb format
    workbook.Save(outDir + u".output.xlsb", SaveFormat::Xlsb);

    // Save in ODS format
    workbook.Save(outDir + u".output.ods", SaveFormat::Ods);

    // Save in Pdf format
    workbook.Save(outDir + u".output.pdf", SaveFormat::Pdf);

    // Save in Html format
    workbook.Save(outDir + u".output.html", SaveFormat::Html);

    // Save in SpreadsheetML format
    workbook.Save(outDir + u".output.xml", SaveFormat::SpreadsheetML);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Come Salvare un Workbook in Pdf**
Il formato di file Portable Document Format (PDF) è un tipo di documento creato da Adobe negli anni '90. Lo scopo di questo formato di file era introdurre uno standard per la rappresentazione di documenti e di altro materiale di riferimento in un formato indipendente dal software dell'applicazione, dall'hardware e dal Sistema Operativo. Il formato di file PDF ha la piena capacità di contenere informazioni come testo, immagini, collegamenti ipertestuali, campi modulo, media ricca, firme digitali, allegati, metadati, funzionalità geospaziali e oggetti 3D che possono diventare parte del documento di origine.

I seguenti codici mostrano come salvare il workbook in formato pdf con Aspose.Cells:
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the Workbook object
    Workbook workbook;

    // Set value to Cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"Hello World!");

    // Save the workbook to PDF
    workbook.Save(u"pdf1.pdf");

    // Save as Pdf format compatible with PDFA-1a
    PdfSaveOptions saveOptions;
    saveOptions.SetCompliance(PdfCompliance::PdfA1a);

    workbook.Save(u"pdfa1a.pdf", saveOptions);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Come Salvare un Workbook in Formato Testo o CSV**

A volte si desidera convertire o salvare un workbook con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV, ecc.), sia Microsoft Excel che Aspose.Cells di default salvano solo i contenuti del foglio di lavoro attivo.

L'esempio di codice seguente spiega come salvare un intero workbook in formato testo. Carica il workbook di origine che potrebbe essere un file di fogli di calcolo Microsoft Excel o OpenOffice (quindi XLS, XLSX, XLSM, XLSB, ODS e così via) con un qualsiasi numero di fogli di lavoro.

Quando il codice viene eseguito, converte i dati di tutti i fogli nel workbook nel formato TXT.

Puoi modificare lo stesso esempio per salvare il tuo file in CSV. Per impostazione predefinita, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) è la virgola, quindi non specificare un separatore se salvi in formato CSV. Nota: Se usi la versione di valutazione e anche se la proprietà [**TxtSaveOptions.GetExportAllSheets()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getexportallsheets/) è impostata su true, il programma exporterà ancora solo un foglio di lavoro.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output text file
    U16String outputFilePath = outDir + u"out.txt";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook data saved to text file successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Come salvare un file in file di testo con un separatore personalizzato**

I file di testo contengono dati del foglio di calcolo senza formattazione. Il file è una sorta di file di testo semplice che può avere alcuni delimitatori personalizzati tra i suoi dati.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';');

    // Save the file with the options
    wb.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Come salvare un file in uno stream**

Per salvare i file in uno stream, creare un oggetto *MemoryStream* o *FileStream* e salvare il file su quell'oggetto stream chiamando il metodo [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) dell'oggetto [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Specificare il formato del file desiderato utilizzando l'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) al momento della chiamata del metodo [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```

## **Come salvare un file di Excel in file Html e Mht**
Aspose.Cells può semplicemente salvare un file di Excel, JSON, CSV o altri file che potrebbero essere caricati da Aspose.Cells come file .html e .mht.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    Workbook workbook(inputFilePath);

    // Save file to MHTML format
    U16String outputFilePath(u"out.mht");
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully to MHTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **Come salvare un file di Excel in OpenOffice (ODS, SXC, FODS, OTS)**
Possiamo salvare i file in formato open office: ODS, SXC, FODS, OTS ecc.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file
    workbook.Save(u"Out.ods");

    // Save as sxc file
    workbook.Save(u"Out.sxc");

    // Save as fods file
    workbook.Save(u"Out.fods");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Come salvare un file di Excel in JSON o XML**

JSON (JavaScript Object Notation) è un formato file standard aperto per la condivisione di dati che utilizza testo leggibile dall'uomo per memorizzare e trasmettere dati. I file JSON sono memorizzati con l'estensione .json. JSON richiede meno formattazione ed è una buona alternativa per XML. JSON deriva da JavaScript, ma è un formato di dati indipendente dal linguaggio. La generazione e l'analisi di JSON sono supportate da molti linguaggi di programmazione moderni. application/json è il tipo di supporto usato per JSON.

Aspose.Cells supporta il salvataggio dei file in JSON o XML.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output json file
    U16String outputFilePath = outDir + u"book1.json";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **Argomenti avanzati**
- [Regola il livello di compressione del workbook](/cells/it/cpp/adjust-workbook-compression-level/)
- [Salva il foglio di lavoro nel formato Strict Open XML Spreadsheet](/cells/it/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Salvataggio del file nell'oggetto di risposta](/cells/it/cpp/saving-file-to-response-object/)
