---
title: Modifiche alle API pubbliche in Aspose.Cells 8.3.2
type: docs
weight: 120
url: /it/net/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche apportate all'API Aspose.Cells dalla versione 8.3.1 alla 8.3.2 che possono interessare gli sviluppatori di moduli/applicazioni. Include non solo nuovi metodi pubblici e aggiornati, [classi aggiunte ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-3-2/) e [classi rimosse ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-3-2/), ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo per impostare la posizione assoluta della PivotItem**
Al fine di fornire la funzione [Posizionamento assoluto di PivotItem](/cells/it/net/specifying-the-absolute-position-of-the-pivot-item/), il Aspose.Cells for .NET 8.3.2 ha esposto una serie di proprietà e metodi di aiuto come elencato di seguito.

- La proprietà PivotItem.Position può essere utilizzata per specificare l'indice di posizione in tutti i PivotItem indipendentemente dal nodo genitore.
- La proprietà PivotItem.PositionInSameParentNode può essere utilizzata per specificare l'indice di posizione nei PivotItem sotto lo stesso nodo genitore.
- Il metodo PivotItem.Move(int count, bool isSameParent) può essere utilizzato per spostare l'elemento su o giù in base al valore del conteggio, dove il conteggio è il numero di posizioni per spostare il PivotItem su o giù. Se il valore del conteggio è inferiore a zero, l'elemento verrà spostato su di posizione, mentre se il valore del conteggio è maggiore di zero, il PivotItem si sposterà in basso; il parametro di tipo booleano isSameParent specifica se l'operazione di spostamento deve essere eseguita nello stesso nodo genitore o no.

{{% alert color="primary" %}} 

Si noti che è necessario chiamare i metodi PivotTable.RefreshData e PivotTable.CalculateData prima di utilizzare le proprietà PivotItem.Position, PivotItem.PositionInSameParentNode e il metodo PivotItem.Move(int count, bool isSameParent).

{{% /alert %}} 
### **Firma di classe SignatureLine aggiunta**
Aspose.Cells for .NET 8.3.2 fornisce il supporto per la Signature Line per emulare la funzione equivalente di MS Excel. Questa versione di Aspose.Cells for .NET ha esposto la classe SignatureLine e la proprietà Picture.SignatureLine a tale scopo.

Il seguente codice di esempio aggiunge una Signature Line utilizzando la proprietà Picture.SignatureLine al workbook.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.Worksheets[0].Pictures.Add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.Worksheets[0].Pictures[index];

//Create signature line object

SignatureLine s = new SignatureLine();

s.Signer = "John Doe";

s.Title = "Development Lead";

s.Email = "john.doe@aspose.com";

//Assign the signature line object to Picture.SignatureLine property

pic.SignatureLine = s;

{{< /highlight >}}


### **Aggiunto il metodo Chart.HasAxis**
Con il rilascio della v8.3.2, l'API Aspose.Cells ha fornito il metodo Chart.HasAxis(AxisType axisType, bool isPrimary) per determinare se il grafico ha un particolare asse o no.

Il seguente codice di esempio dimostra l'uso del metodo Chart.HasAxis per determinare se il grafico di esempio ha un asse primario, secondario e del valore.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart

Chart chart = worksheet.Charts[0];

//Determine which axis exists in chart

bool ret = chart.HasAxis(AxisType.Category, true);

Console.WriteLine("Has Primary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Category, false);

Console.WriteLine("Has Secondary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, true);

Console.WriteLine("Has Primary Value Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, false);

Console.WriteLine("Has Secondary Value Axis: " + ret);

{{< /highlight >}}


### **Aggiunto il metodo WorkbookSettings.CheckWriteProtectedPassword**
Il metodo WorkbookSettings.CheckWriteProtectedPassword consente agli sviluppatori di verificare se una password fornita per modificare il foglio di calcolo è corretta o meno.

**C#**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **Sovraccarico dei metodi WorkbookRender.ToPrinter e SheetRender.ToPrinter Aggiunti**
Aspose.Cells for .NET 8.3.2 ha fornito i metodi WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) e SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) per stampare la gamma di pagine del workbook e del foglio di calcolo rispettivamente.

Il seguente codice di esempio illustra l'uso dei suddetti metodi per stampare le pagine 2-5 del workbook e del foglio di calcolo.

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.ToPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.ToPrinter(printerName, 1, 4);

{{< /highlight >}}


### **Aggiunto il metodo Worksheet.RefreshPivotTables**
Il metodo appena aggiunto Worksheet.RefreshPivotTables consente di aggiornare tutte le tabelle pivot in un foglio di calcolo specifico in un'unica chiamata.

**C#**

{{< highlight csharp >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Metodo Workbook.GetNamedStyle aggiunto**
L'API Aspose.Cells for .NET ha esposto il metodo Workbook.GetNamedStyle che accetta la stringa come parametro e recupera l'oggetto Style in base al parametro passato.
### **Metodo Cells.ImportTwoDimensionArray aggiunto**
L'API Aspose.Cells for .NET ha reso possibile l'importazione di matrici bidimensionali nelle celle del foglio di calcolo esponendo il metodo Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). Il suddetto metodo importa una matrice bidimensionale di dati in un foglio di lavoro con opzioni più flessibili definite in TxtLoadOptions.
### **Proprietà OnePagePerSheet, PageIndex e PageCount aggiunte**
L'API Aspose.Cells for .NET 8.3.2 ha esposto le proprietà OnePagePerSheet, PageIndex e PageCount per la classe XpsSaveOptions. L'utente può adattare tutti i contenuti di un foglio di calcolo su una singola pagina di XPS utilizzando la proprietà OnePagePerSheet e/o recuperare il numero di pagine da stampare utilizzando la proprietà PageCount. La proprietà PageIndex ottiene/imposta l'indice a base 0 della prima pagina da salvare.
### **Proprietà NumberDecimalSeparator e NumberGroupSeparator aggiunte**
L'API Aspose.Cells for .NET 8.3.2 ha introdotto le proprietà NumberDecimalSeparator e NumberGroupSeparator che possono ottenere/impostare i separatori personalizzati utilizzati per formattare e analizzare i valori numerici nei fogli di calcolo.

Il seguente codice di esempio illustra come specificare i separatori personalizzati utilizzando l'API Aspose.Cells. Il codice seguente specifica i separatori Decimal e Group personalizzati come rispettivamente punto e spazio.

**C#**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **Proprietà PdfSaveOptions.IsFontSubstitutionCharGranularity aggiunta**
L'API Aspose.Cells for .NET 8.3.2 ha esposto la proprietà PdfSaveOptions.IsFontSubstitutionCharGranularity per superare il problema in cui alcuni caratteri Unicode non possono essere visualizzati utilizzando una famiglia di caratteri specifica. Quando la proprietà PdfSaveOptions.IsFontSubstitutionCharGranularity è impostata su true, solo il carattere specifico che non è visualizzabile cambierà il font in un font visualizzabile e il resto della parola o della frase dovrebbe rimanere nel font originale.

**C#**

{{< highlight csharp >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **API rimosse**
### **Metodi obsoleti rimossi**
I seguenti metodi sono stati rimossi dall'API pubblica.

- Metodi Workbook.Open e Workbook.Save.
- Metodo Workbook.SetOleSize.
- Metodo Workbook.LoadData.
- Metodi WorkbookDesigner.Open e WorkbookDesigner.Save.
- Metodo WorksheetCollection.DeleteName.
### **Proprietà obsolette rimosse**
Le seguenti proprietà sono state rimosse dall'API pubblica.

- Proprietà Workbook.IsProtected.
- Proprietà Workbook.Language.
- Proprietà Workbook.Region.
- Proprietà WorkbookSettings.ReCalcOnOpen.
- Proprietà WorkbookSettings.Language.
- Proprietà WorkbookSettings.Encoding.
- Proprietà WorkbookSettings.ConvertNumericData.
- Proprietà WorksheetCollection.HidePivotFieldList.
- Proprietà WorksheetCollection.EnableHTTPCompression.
- Proprietà WorksheetCollection.IsMinimized.
- Proprietà WorksheetCollection.IsHidden.
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
### **Proprietà Workbook.SaveOptions obsoleta**
Un oggetto di tipo SaveOptions deve essere passato al metodo Workbook.Save dopo aver impostato correttamente le proprietà di SaveOptions.
### **Proprietà Workbook.Styles e classe StyleCollection obsoleti**
È consigliabile utilizzare il metodo Workbook.CreateStyle per creare e manipolare uno stile per un'istanza di Workbook anziché creare uno stile con il metodo StyleCollection.Add. Inoltre, è possibile utilizzare il metodo Workbook.GetNamedStyle(string) per ottenere uno stile nominato anziché StyleCollection[string].
### **Metodo PivotItem.Move(int count) obsoleto**
Con il rilascio di Aspose.Cells 8.3.2, l'API ha introdotto un'altra sovraccarica del metodo PivotItem.Move che accetta il parametro integer per il conteggio e il parametro booleano per spostare un PivotItem all'interno del nodo padre.
{{< app/cells/assistant language="csharp" >}}
