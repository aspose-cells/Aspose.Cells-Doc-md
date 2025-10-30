# Libreria C++ per formati di file Excel

![Versione 23.11.0](https://img.shields.io/badge/nuget-v23.11.0-blue) ![NuGet](https://img.shields.io/nuget/dt/Aspose.Cells.Cpp)

[![banner](https://raw.githubusercontent.com/Aspose/aspose.github.io/master/img/banners/aspose_cells-for-cpp-banner.png)](https://releases.aspose.com/cells/cpp/)

[Pagina del Prodotto](https://products.aspose.com/cells/cpp/) | [Docs](https://docs.aspose.com/cells/cpp/) | [Demos](https://products.aspose.app/cells/family) | [API Reference](https://reference.aspose.com/cells/cpp) | [Esempi](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Blog](https://blog.aspose.com/category/cells/) | [Rilasci](https://releases.aspose.com/cells/cpp/) | [Supporto Gratuito](https://forum.aspose.com/c/cells) | [Licenza Temporanea](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for C++](https://products.aspose.com/cells/cpp/) è una libreria nativa C++ per creare, manipolare, elaborare e convertire file Microsoft Excel senza necessità di Microsoft Office o Automazione. L'API Excel C++ supporta Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML e altri formati come CSV, TSV e altro ancora.

Consente agli sviluppatori di lavorare con righe, colonne, dati, formule, tabelle pivot, fogli di lavoro, tabelle, grafici e oggetti di disegno dalle proprie applicazioni C++.

## Cos'è Aspose.Cells for C++?

Aspose.Cells for C++ è un'API nativa C++ on premise per integrare funzionalità di creazione, manipolazione e conversione di fogli elettronici nelle applicazioni C++ personali. Supporta il lavoro con molti formati di file di fogli elettronici popolari di Microsoft Excel (XLS, XLSX, XLSB, CSV, ecc.) e OpenOffice/LibreOffice (ODS).

Puoi utilizzare Aspose.Cells for C++ per sviluppare applicazioni a 64 bit in qualsiasi ambiente di sviluppo che supporti C++, come Microsoft Visual Studio. Aspose.Cells for C++ è un'assembly nativa che può essere distribuita semplicemente copiandola. Non devi preoccuparti di altri servizi o moduli.

Aspose.Cells for C++ ti consente di lavorare con le proprietà del documento integrate e personalizzate in Microsoft Excel. Supporta la conversione di alta qualità di cartelle di lavoro di Excel in file conformi a PDF/A. Lavora con formule, tabelle pivot, fogli di lavoro, tabelle, intervalli, grafici, oggetti OLE e molto altro ancora.

## Funzionalità di elaborazione file Excel

- Aprire un file di foglio di calcolo senza Microsoft Excel.
- [Apri un file Excel](https://docs.aspose.com/cells/cpp/different-ways-to-open-files/) tramite un percorso sul computer locale o utilizzando uno stream.
- [Converti il foglio di lavoro](https://docs.aspose.com/cells/cpp/converting-worksheet-to-different-image-formats/) in diversi formati di immagine.
- [Applica formattazione condizionale](https://docs.aspose.com/cells/cpp/apply-conditional-formatting-in-worksheet/) secondo la tua scelta.
- [Manipola tabelle pivot](https://docs.aspose.com/cells/cpp/manipulate-pivot-table/) nei tuoi fogli di calcolo.
- [Converti tabella in intervallo](https://docs.aspose.com/cells/cpp/tables-and-ranges/) senza perdere la formattazione.
- Recupera il nome di una cella fornendo l'indice della riga e della colonna, allo stesso modo, [recupera l'indice della riga e della colonna della cella](https://docs.aspose.com/cells/cpp/names-and-indices/) dal suo nome.
- Crea [grafico a piramide, grafico a linee, grafico a bolle](https://docs.aspose.com/cells/cpp/creating-and-customizing-charts/), o un grafico personalizzato.
- [Rendi](https://docs.aspose.com/cells/cpp/chart-rendering/) supportati tipi di grafico in immagini o PDF.
- [Inserisci un oggetto OLE nel foglio di lavoro](https://docs.aspose.com/cells/cpp/inserting-ole-objects-into-the-worksheet/).
- Accedi a tutti gli oggetti OLE contenuti nel foglio di lavoro per [estrazione](https://docs.aspose.com/cells/cpp/extracting-ole-objects-from-worksheet/).

## Formati di lettura e scrittura supportati

**Microsoft Excel:** XLS, XLSX, XLSB, SpreadsheetML\
**Text:** CSV, TSV, TabDelimited\
**OpenDocument:** ODS\
**Altro:** HTML, MHTML

## Salva documenti di fogli di calcolo come

**Microsoft Excel:** XLSM, XLTX, XLTM, XLAM\
**Formato documento portatile:** PDF, XPS
**Text:** CSV, TSV, TabDelimited\
**Immagini:** SVG, JPEG, PNG, BMP, GIF\
**Web:** HTML, MHTML\
**Metafile:** EMF\
**Altro** DIF

## Cominciare

Sei pronto a provare Aspose.Cells for C++? Esegui semplicemente `Install-Package Aspose.Cells.Cpp` dalla Console del Gestore dei pacchetti in Visual Studio per ottenere il pacchetto NuGet. Se hai già Aspose.Cells for C++ e vuoi aggiornare la versione, esegui `Update-Package Aspose.Cells.Cpp` per ottenere l'ultima versione.

### Converti XLS in XLSX, XLSB & CSV usando C++

Prova a eseguire il frammento sottostante per vedere come funziona l'API nel tuo ambiente o controlla il [Repository GitHub](https://github.com/aspose-cells/Aspose.Cells-for-C) per altri scenari di utilizzo comuni.

```c++
U16String dir(u"your path");
// load the file to be converted
Workbook book(dir + u"template.xls");
// save in different formats
book.Save(dir + u"output.xlsx", SaveFormat::Xlsx);
book.Save(dir + u"output.xlsb", SaveFormat::Xlsb);
book.Save(dir + u"output.csv", SaveFormat::CSV);
book.Save(dir + u"output.json", SaveFormat::Json);
```

### Crea un grafico Excel personalizzato con C++

```c++
// create a new workbook
Workbook workbook;

// get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// add sample data
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"A4").PutValue(110);
worksheet.GetCells().Get(u"B1").PutValue(260);
worksheet.GetCells().Get(u"B2").PutValue(12);
worksheet.GetCells().Get(u"B3").PutValue(50);
worksheet.GetCells().Get(u"B4").PutValue(100);

// add a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// access the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// add SeriesCollection (chart data source) to the chart ranging from A1 to B4
chart.GetNSeries().Add(u"A1:B4", true);

// set the chart type of 2nd NSeries to display as line chart
chart.GetNSeries().Get(1).SetType(
	Aspose::Cells::Charts::ChartType::Line);

// save the Excel file
workbook.Save(u"output.xlsx");
```

[Pagina del Prodotto](https://products.aspose.com/cells/cpp/) | [Docs](https://docs.aspose.com/cells/cpp/) | [Demos](https://products.aspose.app/cells/family) | [API Reference](https://reference.aspose.com/cells/cpp) | [Esempi](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Blog](https://blog.aspose.com/category/cells/) | [Rilasci](https://releases.aspose.com/cells/cpp/) | [Supporto Gratuito](https://forum.aspose.com/c/cells) | [Licenza Temporanea](https://purchase.aspose.com/temporary-license/)
{{< app/cells/assistant language="cpp" >}}
