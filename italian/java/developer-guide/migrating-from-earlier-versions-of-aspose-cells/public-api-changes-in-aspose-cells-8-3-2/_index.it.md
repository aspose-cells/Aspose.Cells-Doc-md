---
title: Modifiche all'API pubblica in Aspose.Cells 8.3.2
type: docs
weight: 130
url: /it/java/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

 Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.3.1 alla 8.3.2 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati,[classi aggiunte ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-3-2/) e[classi rimosse ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-3-2/), ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo per impostare la posizione assoluta di PivotItem**
 Al fine di fornire la funzionalità[Posizionamento assoluto di PivotItem](/cells/it/java/specifying-the-absolute-position-of-the-pivot-item/), Aspose.Cells for Java 8.3.2 ha esposto una serie di proprietà e un metodo come elencato di seguito.

- PivotItem.setPosition può essere utilizzato per impostare l'indice di posizione in tutti i PivotItem indipendentemente dal nodo padre.
- PivotItem.setPositionInSameParentNode può essere utilizzato per impostare l'indice di posizione nei PivotItems sotto lo stesso nodo padre.
- Il metodo PivotItem.move(int count, bool isSameParent) può essere utilizzato per spostare l'elemento verso l'alto o verso il basso in base al valore del conteggio, dove count è il numero di posizioni per spostare l'oggetto PivotItem verso l'alto o verso il basso. Se il valore del conteggio è minore di zero, l'elemento verrà spostato verso l'alto dove, come se il valore del conteggio fosse maggiore di zero, il PivotItem si sposterà verso il basso, il parametro di tipo booleano isSameParent specifica se l'operazione di spostamento deve essere eseguita nello stesso nodo padre o no.

{{% alert color="primary" %}} 

Si noti che è necessario chiamare i metodi PivotTable.refreshData e PivotTable.calculateData prima di utilizzare le proprietà PivotItem.setPosition, PivotItem.setPositionInSameParentNode e il metodo PivotItem.move(int count, bool isSameParent).

{{% /alert %}} 
### **Classe SignatureLine Aggiunta**
Aspose.Cells 8.3.2 fornisce il supporto per la linea della firma per imitare la funzionalità equivalente di MS Excel. Questa versione ha esposto la classe SignatureLine e la proprietà Picture.SignatureLine per questo scopo.

Il codice di esempio seguente aggiunge una riga della firma utilizzando la proprietà Picture.SignatureLine alla cartella di lavoro.

**Giava**

{{< highlight "csharp" >}}

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
### **Metodo Chart.hasAxis aggiunto**
Con il rilascio della versione v8.3.2, l'API Aspose.Cells ha fornito il metodo Chart.hasAxis(AxisType axisType, bool isPrimary) per determinare se il grafico dispone o meno di un determinato asse.

Il seguente codice di esempio mostra l'utilizzo del metodo Chart.hasAxis per determinare se il grafico di esempio ha l'asse Primario, Secondario e Valore.

**Giava**

{{< highlight "csharp" >}}

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
### **Metodo WorkbookSettings.checkWriteProtectedPassword Aggiunto**
Metodo WorkbookSettings.checkWriteProtectedPassword consente agli sviluppatori di verificare se una determinata password per modificare il foglio di calcolo è corretta o meno.

**Giava**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **Metodi di sovraccarico WorkbookRender.toPrinter e SheetRender.toPrinter Aggiunto**
Aspose.Cells 8.3.2 ha fornito i metodi WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) e SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) per stampare rispettivamente l'intervallo di pagine della cartella di lavoro e del foglio di lavoro.

Il seguente codice di esempio illustra l'utilizzo dei metodi suddetti per stampare le pagine 2-5 della cartella di lavoro e del foglio di lavoro.

**Giava**

{{< highlight "csharp" >}}

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
### **Metodo Worksheet.refreshPivotTables Aggiunto**
Il metodo appena aggiunto Worksheet.refreshPivotTables consente di aggiornare tutte le tabelle pivot in un determinato foglio di calcolo in una singola chiamata.

**Giava**

{{< highlight "csharp" >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **Metodo Workbook.getNamedStyle Aggiunto**
Aspose.Cells 8.3.2 ha esposto il metodo Workbook.getNamedStyle che accetta la stringa come parametro e recupera l'oggetto Style in base al parametro passato.
### **Metodo Cells.importTwoDimensionArray aggiunto**
L'API Aspose.Cells ha reso possibile l'importazione di array bidimensionali nelle celle del foglio di calcolo esponendo il metodo Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). Il suddetto metodo importa una matrice di dati a due dimensioni in un foglio di lavoro con opzioni più flessibili definite in TxtLoadOptions.
### **Proprietà OnePagePerSheet, PageIndex e PageCount aggiunto**
Aspose.Cells for Java 8.3.2 ha esposto le proprietà OnePagePerSheet, PageIndex e PageCount per la classe XpsSaveOptions. L'utente può inserire tutti i contenuti di un foglio di calcolo in una singola pagina di XPS utilizzando la proprietà OnePagePerSheet e/o recuperare il numero di pagine da stampare utilizzando la proprietà PageCount. La proprietà PageIndex ottiene/imposta l'indice in base 0 della prima pagina da salvare.
### **Proprietà NumberDecimalSeparator e NumberGroupSeparator aggiunti**
Aspose.Cells for Java 8.3.2 ha introdotto le proprietà NumberDecimalSeparator e NumberGroupSeparator che possono ottenere/impostare i separatori personalizzati utilizzati per la formattazione e l'analisi dei valori numerici nei fogli di calcolo.

Il seguente codice di esempio illustra come specificare i separatori personalizzati utilizzando l'API Aspose.Cells. Il codice seguente specifica i separatori decimali e di gruppo personalizzati rispettivamente come punto e spazio.

**Giava**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **Proprietà PdfSaveOptions.setFontSubstitutionCharGranularity Aggiunta**
Aspose.Cells for Java 8.3.2 ha esposto la proprietà PdfSaveOptions.setFontSubstitutionCharGranularity per ovviare al problema per cui alcuni caratteri Unicode non possono essere visualizzati utilizzando una specifica famiglia di font. Quando la proprietà PdfSaveOptions.setFontSubstitutionCharGranularity è impostata su true, solo il carattere di un carattere specifico che non è visualizzabile verrà modificato in carattere visualizzabile e il resto della parola o della frase dovrebbe rimanere nel carattere originale.

**Giava**

{{< highlight "csharp" >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **API rimosse**
### **Metodi obsoleti rimossi**
seguenti metodi sono stati rimossi dall'API pubblica.

- Metodi Workbook.open e Workbook.save.
- Metodo Workbook.setOleSize.
- Metodo Workbook.loadData.
- Metodi WorkbookDesigner.open e WorkbookDesigner.save.
- Metodo WorksheetCollection.deleteName.
### **Proprietà obsolete rimosse**
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
### **Proprietà Workbook.saveOptions Obsoleto**
 Un oggetto di SaveOptions deve essere passato al metodo Workbook.Save dopo aver impostato le proprietà SaveOptions appropriate.
### **Property Workbook.Styles & Class StyleCollection Obsoleto**
Si consiglia di utilizzare il metodo Workbook.createStyle per creare e modificare lo stile per l'istanza di Workbook invece di creare uno Style con il metodo StyleCollection.add. Inoltre, il metodo Workbook.getNamedStyle(string) può essere utilizzato per ottenere uno stile con nome invece di StyleCollection.get(string).
### **Metodo PivotItem.move(int count) Obsoleto**
 Con il rilascio di Aspose.Cells 8.3.2, l'API ha introdotto un altro overload del metodo PivotItem.move che accetta il parametro integer per il conteggio e il parametro booleano per spostare un PivotItem all'interno del nodo padre.
