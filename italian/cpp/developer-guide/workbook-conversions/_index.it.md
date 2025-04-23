---
title: Converti Excel in Pdf, Immagine e altri formati con C++
linktitle: Conversione di cartelle di lavoro
type: docs
weight: 65
url: /it/cpp/convert-workbook-to-different-formats/
description: Converti file Excel in Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML e altro ancora usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione tra molti formati.Tecnicamente, la conversione significa caricare un workbook in un formato di file e salvarlo in un altro.

{{% /alert %}}

## **Converti il foglio di lavoro di Excel in PDF**

I file PDF sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e gli sviluppatori di software spesso devono trovare un modo per convertire i file Microsoft Excel in documenti PDF.

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Instantiate the Workbook object and open an Excel file
    Workbook workbook(u"Book1.xlsx");

    // Save the document in PDF format
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    std::cout << "Excel file converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Converti cartella di lavoro Excel in JPG**
Aspose.Cells supporta la conversione dei file Excel in JPG.
L'esempio di codice qui sotto mostra come salvare una cartella di lavoro come JPG.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"Book1.xlsx");
    Workbook book(inputFilePath);

    U16String outputFilePath(u"Image1.jpg");
    book.Save(outputFilePath, SaveFormat::Jpg);

    std::cout << "Workbook converted to JPG image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Converti cartella di lavoro Excel in immagine**
Aspose.Cells supporta la conversione dei file Excel in immagini.
L'esempio di codice qui sotto mostra come salvare una cartella di lavoro come immagini.

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook(srcDir + u"Book1.xlsx");

    workbook.Save(outDir + u"Image1.bmp", SaveFormat::Bmp);
    workbook.Save(outDir + u"Image1.jpg", SaveFormat::Jpg);
    workbook.Save(outDir + u"Image1.png", SaveFormat::Png);
    workbook.Save(outDir + u"Image1.emf", SaveFormat::Emf);
    workbook.Save(outDir + u"Image1.gif", SaveFormat::Gif);

    std::cout << "Workbook converted to images successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Conversione della cartella di lavoro Excel in XPS**

Il formato del documento XPS consiste in markup XML strutturato che definisce la disposizione di un documento e l'aspetto visuale di ogni pagina, insieme alle regole di rendering per distribuire, archiviare, rendere, elaborare e stampare documenti.

Il linguaggio di markup per XPS è un sottoinsieme di XAML, che consente di incorporare elementi grafici vettoriali nei documenti, usando XAML per contrassegnare le primitive di Windows Presentation Foundation (WPF). Gli elementi utilizzati sono descritti in termini di percorsi e altre primitive geometriche.

Un file XPS è, in effetti, un archivio ZIP Unicode che utilizza le Open Packaging Conventions, contenente i file che compongono il documento. Questi includono un file di markup XML per ogni pagina, testo, font incorporati, immagini raster, grafica vettoriale 2D e informazioni di gestione dei diritti digitali. Il contenuto di un file XPS può essere esaminato semplicemente aprendolo in un’applicazione che supporta ZIP.

A partire da Aspose.Cells 6.0.0, è supportata la conversione di Microsoft Excel in XPS.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xls";
    Workbook workbook(inputFilePath);

    Worksheet sheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    SheetRender sr(sheet, options);
    sr.ToImage(0, outDir + u"out_image.png");

    XpsSaveOptions xpsOptions;
    workbook.Save(outDir + u"out_whole_printingxps.out.xps", xpsOptions);

    std::cout << "Files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Converti Excel in Ods, Sxc e Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells supporta la conversione di file Excel in file Ods, Sxc e Fods. L'esempio di codice seguente mostra come convertire il [modello](book1.xlsx) in file Ods, Sxc e Fods.

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

## **Conversione della cartella di lavoro Excel in file MHTML**

MHTML combina HTML normale con risorse esterne (cioè contenuti che di solito sono collegati, come immagini, animazioni, audio, e così via) in un unico file. Sono utilizzati per le email con l'estensione del file .mht.

Aspose.Cells supporta la lettura e la scrittura dei file MHTML.

L'esempio di codice sotto mostra come salvare un workbook come file MHTML.

```cpp
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

    // Specify the HTML Saving Options
    HtmlSaveOptions sv(SaveFormat::MHtml);

    // Instantiate a workbook and open the template XLSX file
    Workbook wb(filePath);

    // Save the MHT file
    wb.Save(filePath + u".out.mht", sv);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Conversione di un Workbook Excel in HTML**

L’API Aspose.Cells supporta l’esportazione di fogli di calcolo in formato HTML. Per questo scopo, Aspose.Cells utilizza la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) per fornire la flessibilità di controllare vari aspetti dell’HTML di output.

L'esempio di codice sotto mostra come salvare un workbook come file HTML.

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

    // Path of output HTML file
    U16String outputFilePath = outDir + u"ConvertingToHTMLFiles_out.html";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in HTML format
    wb.Save(outputFilePath, SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Impostazione delle Preferenze Immagine per HTML**

A partire dalla versione 8.0.2, Aspose.Cells ha esposto [**GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) per la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/), consentendo agli sviluppatori di specificare le preferenze di immagine durante il salvataggio dei fogli di calcolo in formato HTML.

Di seguito sono riportati alcuni dettagli delle impostazioni di immagine che possono essere applicate:

- [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/): Specifica il tipo di immagine. Si noti che tutte le forme, inclusi grafici, vengono rappresentati come immagini nell'HTML di output.
- [**GetQuality()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getquality/): Specifica la qualità dell’immagine tra 0 e 100 quando [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) è specificato come Jpeg.
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/): Ottiene o imposta la risoluzione verticale dell'immagine in punti per pollice.
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/): Ottiene o imposta la risoluzione orizzontale dell'immagine in punti per pollice.
- [**TiffCompression**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/): Ottiene o imposta il tipo di compressione per le immagini quando [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) è specificato come Tiff.
- [**GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/): Indica se lo sfondo di un'immagine deve essere trasparente quando ImageFormat è specificato come Png.

Il codice seguente dimostra come utilizzare [**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) per specificare diverse preferenze.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"Book1.xlsx";

    Workbook book(filePath);
    HtmlSaveOptions saveOptions(SaveFormat::Html);

    saveOptions.GetImageOptions().SetImageType(ImageType::Png);

    book.Save(outDir + u"output.html", saveOptions);

    std::cout << "Spreadsheet converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Converti Workbook Excel in Markdown**

L’API Aspose.Cells supporta l’esportazione di fogli di calcolo in formato Markdown. Per esportare il foglio attivo in Markdown, passare [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). È inoltre possibile utilizzare la classe [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) per specificare impostazioni aggiuntive per l’esportazione del foglio in Markdown.

Il seguente esempio di codice dimostra come esportare il foglio attivo in Markdown usando il membro di enumerazione [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). Consultare il [file Markdown di output](md_sample.txt) generato dal codice come riferimento.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Markdown file
    U16String outputFilePath = outDir + u"Book1.md";

    // Create workbook from the input Excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as Markdown
    workbook.Save(outputFilePath, SaveFormat::Markdown);

    std::cout << "Workbook saved as Markdown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Converti Workbook Excel in JSON**

Aspose.Cells supporta la conversione di un workbook in JSON (JavaScript Object Notation).

Il seguente esempio di codice dimostra come esportare il foglio attivo in JSON usando il membro di enumerazione [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). Consultare il codice per convertire il [file sorgente](Book1.xlsx) nel [file JSON di output](Book1.Json) generato dal codice come riferimento.

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

## **Converti Excel in XML**
Aspose.Cells supporta la conversione di un workbook in Excel 2003 Spreadsheet XML e dati XML semplici.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save as Excel 2003 Spreadsheet XML
    U16String outputFilePath1 = u"Spreadsheet.xml";
    workbook.Save(outputFilePath1);

    // Save as plain XML data
    U16String outputFilePath2 = u"data.xml";
    XmlSaveOptions xmlSaveOptions;
    workbook.Save(outputFilePath2, xmlSaveOptions);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Converti Workbook di Excel in TIFF**
Aspose.Cells supporta la conversione di un workbook in file TIFF.

Il frammento di codice seguente mostra come convertire Excel in TIFF:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open a template excel file
    U16String inputFilePath(u"Book1.xlsx");
    Workbook book(inputFilePath);

    // Save file to TIFF
    U16String outputFilePath(u"out.tiff");
    book.Save(outputFilePath);

    std::cout << "File saved successfully to TIFF format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Converti Workbook di Excel in DOCX**

L’API Aspose.Cells supporta la conversione di fogli di calcolo in formato DOCX. Per esportare il workbook in DOCX, passare [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). È inoltre possibile utilizzare la classe [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) per specificare impostazioni aggiuntive per l’esportazione del foglio in DOCX.

Il seguente esempio di codice dimostra come esportare il foglio attivo in DOCX usando il membro di enumerazione [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). Consultare il [file DOCX di output](Book1.docx) generato dal codice come riferimento.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output docx file
    U16String outputFilePath = outDir + u"Book1.docx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save as DOCX
    workbook.Save(outputFilePath, SaveFormat::Docx);

    std::cout << "File saved successfully as DOCX!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Converti Workbook di Excel in PPTX**

L’API Aspose.Cells supporta la conversione di fogli di calcolo in formato PPTX. Per esportare il workbook in PPTX, passare [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). È inoltre possibile utilizzare la classe [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) per specificare impostazioni aggiuntive per l’esportazione del foglio in PPTX.

Il seguente esempio di codice dimostra l'esportazione del foglio di lavoro attivo in PPTX utilizzando [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) membro dell'enumerazione. Si veda il [file PPTX generato](Book1.pptx) come riferimento.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output PowerPoint file
    U16String outputFilePath = outDir + u"Book1.pptx";

    // Create workbook from the input Excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as a PowerPoint file
    workbook.Save(outputFilePath, SaveFormat::Pptx);

    std::cout << "Workbook saved as PowerPoint successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Converti cartella di lavoro Excel in EPUB**

L'API Aspose.Cells supporta la conversione di fogli di calcolo in formato EPUB. Per esportare la cartella di lavoro in EPUB, passare [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). È inoltre possibile utilizzare la classe [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) per specificare impostazioni aggiuntive per l'esportazione del foglio di lavoro in EPUB.

Il seguente esempio di codice dimostra l'esportazione del foglio di lavoro attivo in EPUB utilizzando [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) membro dell'enumerazione.

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

    // Path of output EPUB file
    U16String outputFilePath = outDir + u"ConvertingToEPUBFiles_out.epub";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in EPUB format
    wb.Save(outputFilePath, SaveFormat::Epub);

    std::cout << "File converted to EPUB format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Converti cartella di lavoro Excel in AZW3**

L'API Aspose.Cells supporta la conversione di fogli di calcolo in formato AZW3. Per esportare la cartella di lavoro in AZW3, passare [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). È inoltre possibile utilizzare la classe [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) per specificare impostazioni aggiuntive per l'esportazione del foglio di lavoro in AZW3.

Il seguente esempio di codice dimostra l'esportazione del foglio di lavoro attivo in AZW3 utilizzando [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) membro dell'enumerazione.

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
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output AZW3 file
    U16String outputFilePath = outDir + u"ConvertingToEPUBFiles_out.azw3";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in AZW3 format
    wb.Save(outputFilePath, SaveFormat::Azw3);

    std::cout << "File converted to AZW3 format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Converti la revisione di XLSB in XLSM](/cells/it/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/it/cpp/convert-excel-to-html/)
- [Immagine](/cells/it/cpp/convert-excel-to-image/)
- [Json](/cells/it/cpp/convert-workbook-to-json/)
- [Converti cartella di lavoro Excel in Ods, Sxc e Fods (OpenOffice / LibreOffice calc).](/cells/it/cpp/convert-excel-to-ods/)
- [Pdf](/cells/it/cpp/convert-excel-workbook-to-pdf/)
- [Converti Excel in CSV, TSV e Txt](/cells/it/cpp/convert-excel-to-csv-tsv-and-txt/)
- [Monitorare il progresso della conversione dei documenti](/cells/it/cpp/track-document-conversion-progress/)
- [Converti CSV, TSV e TXT in Excel](/cells/it/cpp/convert-csv-tsv-and-txt-to-excel/)
