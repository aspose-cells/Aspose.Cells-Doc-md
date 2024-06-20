---
title: Modifiche all API pubblica in Aspose.Cells 8.5.2
type: docs
weight: 180
url: /it/net/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche apportate all'API di Aspose.Cells dalla versione 8.5.1 alla 8.5.2 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, [classi aggiunte ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-5-2/), ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Renderizzare il foglio di lavoro al contesto grafico**
Con questo rilascio di Aspose.Cells for .NET, l'API ha esposte due nuove sovraccarichi del metodo SheetRender.ToImage che ora permettono di accettare un'istanza della classe System.Drawing.Graphics per [rendere nel contesto grafico](/cells/it/net/render-worksheet-to-graphic-context/). Le firme dei metodi appena aggiunti sono le seguenti.

1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Create empty Bitmap

Bitmap bmp = new Bitmap(800, 800);

//Create Graphics Context

Graphics g = Graphics.FromImage(bmp);

g.Clear(Color.Blue);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.OnePagePerSheet = true;

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.ToImage(0, g, 0, 0);

//Save the graphics context image in Png format

bmp.Save("test.png", ImageFormat.Png);

{{< /highlight >}}


### **Aggiunto il Metodo PivotTable.GetCellByDisplayName**
Aspose.Cells for .NET 8.5.2 ha esposto il metodo PivotTable.GetCellByDisplayName che può essere utilizzato per [recuperare l'oggetto Cell dal nome del campo pivot](/cells/it/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Questo metodo potrebbe essere utile in scenari in cui si desidera evidenziare o formattare l'intestazione del campo pivot.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.PivotTables[0];

//Access cell by display name of 2nd data field of the pivot table

Cell cell = pivotTable.GetCellByDisplayName(pivotTable.DataFields[1].DisplayName);

//Access cell style and set its fill color and font color

Style style = cell.GetStyle();

style.ForegroundColor = Color.LightBlue;

style.Font.Color = Color.Black;

//Set the style of the cell

pivotTable.Format(cell.Row, cell.Column, style);

//Save workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Aggiunta la Proprietà SaveOptions.MergeAreas**
Aspose.Cells for .NET 8.5.2 ha esposto la proprietà SaveOptions.MergeAreas che può accettare un valore di tipo Boolean. Il valore predefinito è false, tuttavia, se impostato su true, l'API Aspose.Cells for .NET cerca di unire le singole aree di cella prima di salvare il file.

{{% alert color="primary" %}} 

Se un foglio di calcolo ha troppe celle individuali con convalida applicata, esiste la possibilità che il foglio di calcolo risultante possa corrompersi. Una possibile soluzione è unire le celle con regole di convalida identiche o è possibile ora utilizzare la proprietà SaveOptions.MergeAreas per indirizzare l'API a unire automaticamente le aree di cella prima dell'operazione di salvataggio.

{{% /alert %}} 
### **Proprietà Shape.Geometry.ShapeAdjustValues aggiunta**
Con il rilascio di v8.5.2, l'API Aspose.Cells ha esposto la proprietà Shape.Geometry.ShapeAdjustValues che può essere utilizzata per [apportare modifiche ai punti di regolazione delle diverse forme](/cells/it/net/change-adjustment-values-of-the-shape/)

{{% alert color="primary" %}} 

Nell'interfaccia di Microsoft Excel, i punti di regolazione vengono visualizzati come nodi a forma di diamante giallo.

{{% /alert %}} 

Ad esempio,

1. Il rettangolo arrotondato ha un punto di regolazione per modificare l'arco
1. Il triangolo ha un punto di regolazione per modificare la posizione del punto
1. Il trapezio ha un punto di regolazione per modificare la larghezza della parte superiore
1. Le frecce hanno due regolazioni per modificare la forma della testa e della coda

Ecco il caso d'uso più semplice.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first three shapes of the worksheet

Shape shape1 = worksheet.Shapes[0];

Shape shape2 = worksheet.Shapes[1];

Shape shape3 = worksheet.Shapes[2];

//Change the adjustment values of the shapes

shape1.Geometry.ShapeAdjustValues[0].Value = 0.5d;

shape2.Geometry.ShapeAdjustValues[0].Value = 0.8d;

shape3.Geometry.ShapeAdjustValues[0].Value = 0.5d;

//Save the workbook

workbook.Save("output.xls);

{{< /highlight >}}


### **Aggiunto Campo di Enumerazione ConsolidationFunction.DistinctCount**
Aspose.Cells for .NET 8.5.2 ha esposto il campo ConsolidationFunction.DistinctCount che può essere utilizzato per [applicare la funzione di consolidamento Count Distinti](/cells/it/net/consolidation-function/) su DataField di un PivotTable.

{{% alert color="primary" %}} 

La funzione di consolidamento Count Distinti è supportata solo da Microsoft Excel 2013.

{{% /alert %}} 
### **Miglior Gestione Eventi per GridDesktop**
Questa versione di Aspose.Cells.GridDesktop ha esposto 4 nuovi eventi. 2 di questi eventi vengono attivati in diversi stati di caricamento dei file di fogli di calcolo in GridDesktop, mentre gli altri 2 vengono attivati al calcolo delle formule.

Gli eventi sono elencati come segue.

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
