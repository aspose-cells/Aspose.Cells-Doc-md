---
title: Modifiche all API pubblica in Aspose.Cells 8.5.2
type: docs
weight: 190
url: /it/java/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.5.1 a 8.5.2 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, [classi aggiunte ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-5-2/), ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Renderizzare il foglio di lavoro al contesto grafico**
Questa versione dell'API Aspose.Cells for Java ha esposto un altro sovraccarico del metodo SheetRender.toImage che ora consente di accettare un'istanza della classe Graphics2D per [rendere il foglio di lavoro nel contesto grafico](/cells/it/java/render-worksheet-to-graphic-context/). Le firme del nuovo metodo aggiunto sono le seguenti.

- SheetRender.toImage(int pageIndex, Graphics2D graphic)

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Create empty image and fill it with blue color

int width = 800;

int height = 800;

BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);

Graphics2D g = image.createGraphics();

g.setColor(java.awt.Color.blue);

g.fillRect(0, 0, width, height);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setOnePagePerSheet(true);

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.toImage(0, g);

//Save the graphics context image in Png format

File outputfile = new File("test.png");

ImageIO.write(image, "png", outputfile);

{{< /highlight >}}
### **Aggiunto il metodo PivotTable.getCellByDisplayName**
Aspose.Cells for Java 8.5.2 ha esposto il metodo PivotTable.getCellByDisplayName che può essere utilizzato per [recuperare l'oggetto Cell per il nome del PivotField](/cells/it/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Questo metodo potrebbe essere utile in scenari in cui si desidera evidenziare o formattare l'intestazione di PivotField.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Access cell by display name of 2nd data field of the pivot table

String displayName = pivotTable.getDataFields().get(1).getDisplayName();

Cell cell = pivotTable.getCellByDisplayName(displayName);

//Access cell style and set its fill color and font color

Style style = cell.getStyle();

style.setForegroundColor(Color.getLightBlue());

style.getFont().setColor(Color.getBlack());

//Set the style of the cell

pivotTable.format(cell.getRow(), cell.getColumn(), style);

//Save workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Aggiunta la Proprietà SaveOptions.MergeAreas**
Aspose.Cells for Java 8.5.2 ha esposto la proprietà SaveOptions.MergeAreas che può accettare un valore di tipo booleano. Il valore predefinito è falso, tuttavia, se impostato su true, l'API Aspose.Cells for Java cerca di unire le singole aree di cella prima di salvare il file.

{{% alert color="primary" %}} 

Se un foglio di calcolo ha troppe celle individuali con convalida applicata, esiste la possibilità che il foglio di calcolo risultante possa corrompersi. Una possibile soluzione è unire le celle con regole di convalida identiche o è possibile ora utilizzare la proprietà SaveOptions.MergeAreas per indirizzare l'API a unire automaticamente le aree di cella prima dell'operazione di salvataggio.

{{% /alert %}} 
### **Aggiunta la proprietà Geometry.ShapeAdjustValues**
Con il rilascio di v8.5.2, l'API Aspose.Cells ha esposto il metodo Geometry.getShapeAdjustValues che può essere utilizzato per [accedere e apportare modifiche ai punti di regolazione di diverse forme](/cells/it/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

Nell'interfaccia di Microsoft Excel, i punti di regolazione vengono visualizzati come nodi diamante gialli.

{{% /alert %}} 

Ad esempio, 

1. Il rettangolo arrotondato ha un punto di regolazione per modificare l'arco
1. Il triangolo ha un punto di regolazione per modificare la posizione del punto
1. Il trapezio ha un punto di regolazione per modificare la larghezza della parte superiore
1. Le frecce hanno due regolazioni per modificare la forma della testa e della coda

Ecco il caso d'uso più semplice.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first three shapes of the worksheet

Shape shape1 = worksheet.getShapes().get(0);

Shape shape2 = worksheet.getShapes().get(1);

Shape shape3 = worksheet.getShapes().get(2);

//Change the adjustment values of the shapes

shape1.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

shape2.getGeometry().getShapeAdjustValues().get(0).setValue(0.8d);

shape3.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Aggiunta l'enumerazione Field ConsolidationFunction.DISTINCT_COUNT**
Aspose.Cells for Java 8.5.2 ha esposto il campo ConsolidationFunction.DISTINCT_COUNT che può essere utilizzato per applicare la funzione di consolidamento Distinct Count su DataField di un PivotTable.

{{% alert color="primary" %}} 

La funzione di consolidamento Count Distinti è supportata solo da Microsoft Excel 2013.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
