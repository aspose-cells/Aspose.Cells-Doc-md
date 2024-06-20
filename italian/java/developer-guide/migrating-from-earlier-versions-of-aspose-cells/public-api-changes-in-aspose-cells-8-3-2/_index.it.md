---
title: Modifiche alle API pubbliche in Aspose.Cells 8.3.2
type: docs
weight: 130
url: /it/java/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche alle API di Aspose.Cells dalla versione 8.3.1 alla 8.3.2 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, [classi aggiunte ecc.](/cells/it/java/le-modifiche-dell-api-pubblica-in-aspose-cells-8-3-2/) e [classi rimosse ecc.](/cells/it/java/le-modifiche-dell-api-pubblica-in-aspose-cells-8-3-2/), ma anche una descrizione di eventuali cambiamenti nel comportamento nei bastimenti di Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo per impostare la posizione assoluta della PivotItem**
Al fine di fornire la funzionalità [Posizionamento Assoluto di PivotItem](/cells/it/java/specificare-la-posizione-assoluta-dell-elemento-pivot/), il Aspose.Cells for Java 8.3.2 ha esposto una serie di proprietà e un metodo come elencato di seguito.

- PivotItem.setPosition può essere utilizzato per impostare l'indice di posizione in tutti i PivotItems indipendentemente dal nodo padre.
- PivotItem.setPositionInSameParentNode può essere utilizzato per impostare l'indice di posizione nei PivotItems sotto lo stesso nodo padre.
- il metodo PivotItem.move(int count, bool isSameParent) può essere utilizzato per spostare l'elemento su o giù in base al valore del conteggio, in cui il conteggio è il numero di posizioni per spostare il PivotItem su o giù. Se il valore del conteggio è inferiore a zero, l'elemento verrà spostato su, mentre se il valore del conteggio è maggiore di zero, il PivotItem verrà spostato giù, il parametro Booleano isSameParent specifica se l'operazione di spostamento deve essere eseguita allo stesso nodo padre o no.

{{% alert color="primary" %}} 

Si prega di notare, è necessario chiamare i metodi PivotTable.refreshData e PivotTable.calculateData prima di utilizzare le proprietà PivotItem.setPosition, PivotItem.setPositionInSameParentNode e il metodo PivotItem.move(int count, bool isSameParent).

{{% /alert %}} 
### **Firma di classe SignatureLine aggiunta**
Aspose.Cells 8.3.2 fornisce il supporto per la Linea di Firma per simulare la funzionalità equivalente di MS Excel. Questo rilascio ha esposto la classe SignatureLine e la proprietà Picture.SignatureLine a questo scopo.

Il seguente codice di esempio aggiunge una Signature Line utilizzando la proprietà Picture.SignatureLine al workbook.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.getWorksheets().get(0).getPictures().add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.getWorksheets().get(0).getPictures().get(index);

//Create signature line object

SignatureLine s = new SignatureLine();

s.setSigner("John Doe");

s.setTitle("Development Lead");

s.setEmail("john.doe@aspose.com");

//Assign the signature line object to Picture.SignatureLine property

pic.setSignatureLine(s);

{{< /highlight >}}
### **Metodo Aggiunto Chart.hasAxis**
Con il rilascio di v8.3.2, Aspose.Cells API ha fornito il metodo Chart.hasAxis (AxisType axisType, bool isPrimary) per determinare se il grafico ha un particolare asse o meno.

Il codice di esempio seguente dimostra l'uso del metodo Chart.hasAxis per determinare se il grafico di esempio ha l'asse Primario, Secondario e dei Valori.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart

Chart chart = worksheet.getCharts().get(0);

//Determine which axis exists in chart

boolean ret = chart.hasAxis(AxisType.CATEGORY, true);

System.out.println("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.CATEGORY, false);

System.out.println("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, true);

System.out.println("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, false);

System.out.println("Has Seconary Value Axis: " + ret);

{{< /highlight >}}
### **Metodo Aggiunto WorkbookSettings.checkWriteProtectedPassword**
Il metodo WorkbookSettings.checkWriteProtectedPassword consente agli sviluppatori di verificare se una password fornita per modificare il foglio di calcolo è corretta o meno.

**Java**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **Sovraccarico Metodi WorkbookRender.toPrinter & SheetRender.toPrinter Aggiunto**
Aspose.Cells 8.3.2 ha fornito i metodi WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) e SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) per stampare il range di pagine del foglio di lavoro e del foglio di lavoro rispettivamente.

Il seguente codice di esempio illustra l'uso dei suddetti metodi per stampare le pagine 2-5 del workbook e del foglio di calcolo.

**Java**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.toPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.toPrinter(printerName, 1, 4);

{{< /highlight >}}
### **Metodo Aggiunto Worksheet.refreshPivotTables**
Il metodo appena aggiunto Worksheet.refreshPivotTables consente di aggiornare tutte le tabelle pivot presenti in un foglio di calcolo dato in una sola chiamata.

**Java**

{{< highlight csharp >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **Metodo Aggiunto Workbook.getNamedStyle**
Aspose.Cells 8.3.2 ha esposto il metodo Workbook.getNamedStyle che accetta una stringa come parametro e recupera l'oggetto Style basato sul parametro passato.
### **Aggiunto il metodo Cells.importTwoDimensionArray**
Aspose.Cells API ha reso possibile l'importazione di array bidimensionali nelle celle del foglio di calcolo esponendo il metodo Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). Il metodo suddetto importa un array bidimensionale di dati in un foglio di calcolo con opzioni più flessibili definite in TxtLoadOptions.
### **Proprietà OnePagePerSheet, PageIndex e PageCount aggiunte**
Aspose.Cells for Java 8.3.2 ha esposto le proprietà OnePagePerSheet, PageIndex e PageCount per la classe XpsSaveOptions. L'utente può adattare tutti i contenuti di un foglio di calcolo su una singola pagina di XPS utilizzando la proprietà OnePagePerSheet e/o recuperare il numero di pagine da stampare utilizzando la proprietà PageCount. La proprietà PageIndex ottiene/imposta l'indice a base 0 della prima pagina da salvare.
### **Proprietà NumberDecimalSeparator e NumberGroupSeparator aggiunte**
Aspose.Cells for Java 8.3.2 ha introdotto le proprietà NumberDecimalSeparator e NumberGroupSeparator che possono ottenere/impostare i separatori personalizzati utilizzati per formattare e analizzare i valori numerici nei fogli di calcolo.

Il seguente codice di esempio illustra come specificare i separatori personalizzati utilizzando l'API di Aspose.Cells. Il codice seguente specifica i separatori personalizzati Decimal e Group rispettivamente come punto e spazio.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **Aggiunta la proprietà PdfSaveOptions.setFontSubstitutionCharGranularity**
Aspose.Cells for Java 8.3.2 ha esposto la proprietà PdfSaveOptions.setFontSubstitutionCharGranularity al fine di ovviare al problema in cui alcuni caratteri Unicode non possono essere visualizzati utilizzando una famiglia di caratteri specifica. Quando la proprietà PdfSaveOptions.setFontSubstitutionCharGranularity è impostata su true, solo il carattere specifico non visualizzabile verrà cambiato nel carattere visualizzabile e il resto della parola o frase dovrebbe rimanere nel carattere originale.

**Java**

{{< highlight csharp >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **API rimosse**
### **Metodi obsoleti rimossi**
I seguenti metodi sono stati rimossi dall'API pubblica.

- Metodi Workbook.open e Workbook.save.
- Metodo Workbook.setOleSize.
- Metodo Workbook.loadData.
- Metodi WorkbookDesigner.open e WorkbookDesigner.save.
- Metodo WorksheetCollection.deleteName.
### **Proprietà obsolette rimosse**
Le seguenti proprietà sono state rimosse dall'API pubblica.

- Proprietà Workbook.isProtected.
- Proprietà Workbook.Language.
- Proprietà Workbook.Region.
- Proprietà WorkbookSettings.ReCalcOnOpen.
- Proprietà WorkbookSettings.Language.
- Proprietà WorkbookSettings.Encoding.
- Proprietà WorkbookSettings.ConvertNumericData.
- Proprietà WorksheetCollection.HidePivotFieldList.
- Proprietà WorksheetCollection.EnableHTTPCompression.
- Proprietà WorksheetCollection.isMinimized.
- Proprietà WorksheetCollection.isHidden.
- Proprietà WorksheetCollection.SheetTabBarWidth.
- Proprietà WorksheetCollection.WindowLeft.
- Proprietà WorksheetCollection.WindowLeftInch.
- Proprietà WorksheetCollection.WindowLeftCM.
- Proprietà WorksheetCollection.WindowTop.
- Proprietà WorksheetCollection.WindowTopInch.
- Proprietà WorksheetCollection.WindowTopCM.
- Proprietà WorksheetCollection.WindowWidth.
- Proprietà WorksheetCollection.WindowWidthInch.
- Proprietà WorksheetCollection.WindowWidthCM.
- Proprietà WorksheetCollection.WindowHeight.
- Proprietà WorksheetCollection.WindowHeightInch.
- Proprietà WorksheetCollection.WindowHeightCM.
- Proprietà Worksheet.HPageBreaks.
- Proprietà Worksheet.VPageBreaks.
- Proprietà HtmlSaveOptions.DisplayHTMLCrossString.
- Proprietà HtmlSaveOptions.ExportChartImageFormat.
- Proprietà SaveOptions.ExpCellNameToXLSX.
- Proprietà SaveOptions.DefaultFont.
- Proprietà SaveOptions.Compliance.
- Proprietà SaveOptions.PdfBookmark.
- Proprietà SaveOptions.PdfImageCompression.
- Proprietà TxtSaveOptions.AlwaysQuoted.
## **API obsolete**
### **Proprietà Workbook.saveOptions È stata deprecata**
Un oggetto di tipo SaveOptions deve essere passato al metodo Workbook.Save dopo aver impostato correttamente le proprietà di SaveOptions. 
### **Proprietà Workbook.Styles e Classe StyleCollection sono state deprecate**
Si consiglia di utilizzare il metodo Workbook.createStyle per creare e manipolare lo stile per l'istanza di Workbook anziché creare uno stile con il metodo StyleCollection.add. Inoltre, si può utilizzare il metodo Workbook.getNamedStyle(string) per ottenere uno stile nominato invece di  StyleCollection.get(string).
### **Il metodo PivotItem.move(int count) è stato deprecato**
Con il rilascio di Aspose.Cells 8.3.2, l'API ha introdotto un'altra sovraccarica del metodo PivotItem.move che accetta il parametro intero per il conteggio e il parametro booleano per spostare un PivotItem all'interno del nodo genitore. 
