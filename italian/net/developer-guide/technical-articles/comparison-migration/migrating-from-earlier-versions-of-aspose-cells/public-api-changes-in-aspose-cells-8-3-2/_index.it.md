---
title: Pubblico API Modifiche Aspose.Cells 8.3.2
type: docs
weight: 120
url: /it/net/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

 Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.3.1 alla 8.3.2 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati,[classi aggiunte ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-3-2/) e[classi rimosse ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-3-2/), ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo per impostare la posizione assoluta di PivotItem**
 Al fine di fornire la funzionalità[Posizionamento assoluto di PivotItem](/cells/it/net/specifying-the-absolute-position-of-the-pivot-item/)Aspose.Cells for .NET 8.3.2 ha esposto una serie di proprietà e metodi di supporto elencati di seguito.

- La proprietà PivotItem.Position può essere utilizzata per specificare l'indice di posizione in tutti i PivotItem indipendentemente dal nodo padre.
- La proprietà PivotItem.PositionInSameParentNode può essere utilizzata per specificare l'indice di posizione nei PivotItems sotto lo stesso nodo padre.
- Il metodo PivotItem.Move(int count, bool isSameParent) può essere usato per spostare l'elemento verso l'alto o verso il basso in base al valore del conteggio, dove count è il numero della posizione per spostare l'oggetto PivotItem verso l'alto o verso il basso. Se il valore del conteggio è minore di zero, l'elemento verrà spostato verso l'alto dove, come se il valore del conteggio fosse maggiore di zero, il PivotItem si sposterà verso il basso, il parametro di tipo booleano isSameParent specifica se l'operazione di spostamento deve essere eseguita nello stesso nodo padre o no.

{{% alert color="primary" %}} 

Si noti che è necessario chiamare i metodi PivotTable.RefreshData e PivotTable.CalculateData prima di utilizzare le proprietà PivotItem.Position, PivotItem.PositionInSameParentNode e il metodo PivotItem.Move(int count, bool isSameParent).

{{% /alert %}} 
### **Classe SignatureLine Aggiunta**
Aspose.Cells for .NET 8.3.2 fornisce il supporto per la riga della firma per imitare la funzionalità equivalente di MS Excel. Questa versione di Aspose.Cells for .NET ha esposto la classe SignatureLine e la proprietà Picture.SignatureLine per questo scopo.

Il codice di esempio seguente aggiunge una riga della firma utilizzando la proprietà Picture.SignatureLine alla cartella di lavoro.

**C#**

{{< highlight "csharp" >}}

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


### **Metodo Chart.HasAxis Aggiunto**
Con il rilascio di v8.3.2, il Aspose.Cells API ha fornito il metodo Chart.HasAxis(AxisType axisType, bool isPrimary) per determinare se il grafico ha o meno un asse particolare.

Il seguente codice di esempio illustra l'utilizzo del metodo Chart.HasAxis per determinare se il grafico di esempio ha l'asse Primario, Secondario e Valore.

**C#**

{{< highlight "csharp" >}}

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


### **Metodo WorkbookSettings.CheckWriteProtectedPassword aggiunto**
Metodo WorkbookSettings.CheckWriteProtectedPassword consente agli sviluppatori di verificare se una determinata password per modificare il foglio di calcolo è corretta o meno.

**C#**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **Metodi di sovraccarico WorkbookRender.ToPrinter e SheetRender.ToPrinter aggiunti**
Aspose.Cells for .NET 8.3.2 ha fornito i metodi WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) e SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) per stampare rispettivamente l'intervallo di pagine della cartella di lavoro e del foglio di lavoro.

Il seguente codice di esempio illustra l'utilizzo dei metodi suddetti per stampare le pagine 2-5 della cartella di lavoro e del foglio di lavoro.

**C#**

{{< highlight "csharp" >}}

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


### **Metodo Worksheet.RefreshPivotTables Aggiunto**
Il metodo appena aggiunto Worksheet.RefreshPivotTables consente di aggiornare tutte le tabelle pivot in un determinato foglio di calcolo in una singola chiamata.

**C#**

{{< highlight "csharp" >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Metodo Workbook.GetNamedStyle Aggiunto**
Aspose.Cells for .NET API ha esposto il metodo Workbook.GetNamedStyle che accetta la stringa come parametro e recupera l'oggetto Style in base al parametro passato.
### **Metodo Cells.ImportTwoDimensionArray aggiunto**
Aspose.Cells for .NET API ha reso possibile l'importazione di array bidimensionali nelle celle del foglio di calcolo esponendo il metodo Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). Il suddetto metodo importa una matrice di dati a due dimensioni in un foglio di lavoro con opzioni più flessibili definite in TxtLoadOptions.
### **Proprietà OnePagePerSheet, PageIndex e PageCount aggiunto**
Aspose.Cells for .NET 8.3.2 ha esposto le proprietà OnePagePerSheet, PageIndex e PageCount per la classe XpsSaveOptions. L'utente può inserire tutti i contenuti di un foglio di calcolo in una singola pagina di XPS utilizzando la proprietà OnePagePerSheet e/o recuperare il numero di pagine da stampare utilizzando la proprietà PageCount. La proprietà PageIndex ottiene/imposta l'indice in base 0 della prima pagina da salvare.
### **Proprietà NumberDecimalSeparator e NumberGroupSeparator aggiunte**
Aspose.Cells for .NET 8.3.2 ha introdotto le proprietà NumberDecimalSeparator e NumberGroupSeparator che possono ottenere/impostare i separatori personalizzati utilizzati per la formattazione e l'analisi dei valori numerici nei fogli di calcolo.

Il codice di esempio seguente illustra come specificare i separatori personalizzati utilizzando Aspose.Cells API. Il codice seguente specifica i separatori decimali e di gruppo personalizzati rispettivamente come punto e spazio.

**C#**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **Proprietà PdfSaveOptions.IsFontSubstitutionCharGranularity aggiunta**
Aspose.Cells for .NET 8.3.2 ha esposto la proprietà PdfSaveOptions.IsFontSubstitutionCharGranularity per ovviare al problema per cui alcuni caratteri Unicode non possono essere visualizzati utilizzando una specifica famiglia di font. Quando la proprietà PdfSaveOptions.IsFontSubstitutionCharGranularity è impostata su true, solo il carattere di un carattere specifico che non è visualizzabile verrà modificato in carattere visualizzabile e il resto della parola o della frase deve rimanere nel carattere originale.

**C#**

{{< highlight "csharp" >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **API rimosse**
### **Metodi obsoleti rimossi**
seguenti metodi sono stati rimossi dal pubblico API.

- Metodi Workbook.Open e Workbook.Save.
- Metodo Workbook.SetOleSize.
- Metodo Workbook.LoadData.
- Metodi WorkbookDesigner.Open e WorkbookDesigner.Save.
- Metodo WorksheetCollection.DeleteName.
### **Proprietà obsolete rimosse**
Le seguenti proprietà sono state rimosse dal pubblico API.

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
- Proprietà Worksheet.HPPageBreaks.
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
### **Proprietà Workbook.SaveOptions Obsoleto**
Un oggetto di SaveOptions deve essere passato al metodo Workbook.Save dopo aver impostato le proprietà SaveOptions appropriate.
### **Property Workbook.Styles & Class StyleCollection Obsoleto**
Si consiglia di usare il metodo Workbook.CreateStyle per creare e modificare lo stile per l'istanza di Workbook invece di creare uno Style con il metodo StyleCollection.Add. Inoltre, il metodo Workbook.GetNamedStyle(string) può essere utilizzato per ottenere uno stile con nome invece di StyleCollection[string].
### **Metodo PivotItem.Move(int count) Obsoleto**
Con il rilascio di Aspose.Cells 8.3.2, API ha introdotto un altro overload del metodo PivotItem.Move che accetta il parametro integer per il conteggio e il parametro booleano per spostare un PivotItem all'interno del nodo padre.
