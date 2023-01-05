---
title: Pubblico API Modifiche Aspose.Cells 8.5.2
type: docs
weight: 190
url: /it/java/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

 Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.5.1 alla 8.5.2 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati,[classi aggiunte ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-5-2/), ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Renderizza il foglio di lavoro nel contesto grafico**
Questa versione di Aspose.Cells for Java API ha esposto un altro overload del metodo SheetRender.toImage che ora consente di accettare un'istanza della classe Graphics2D per[eseguire il rendering del foglio di lavoro nel contesto grafico](/cells/it/java/render-worksheet-to-graphic-context/). Le firme del metodo appena aggiunto sono le seguenti.

- SheetRender.toImage(int pageIndex, grafica Graphics2D)

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

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
### **Metodo PivotTable.getCellByDisplayName aggiunto**
 Aspose.Cells for Java 8.5.2 ha esposto il metodo PivotTable.getCellByDisplayName che può essere utilizzato per[recuperare l'oggetto Cell con il nome del PivotField](/cells/it/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Questo metodo potrebbe essere utile negli scenari in cui si desidera evidenziare o formattare l'intestazione PivotField.

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

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
### **Proprietà SaveOptions.MergeAreas aggiunta**
Aspose.Cells for Java 8.5.2 ha esposto la proprietà SaveOptions.MergeAreas che può accettare un valore di tipo booleano. Il valore predefinito è false tuttavia, se impostato su true, Aspose.Cells for Java API tenta di unire la singola CellArea prima di salvare il file.

{{% alert color="primary" %}} 

Se un foglio di calcolo ha troppe singole celle con convalida applicata, è possibile che il foglio di calcolo risultante venga danneggiato. Una possibile soluzione consiste nell'unire le celle con regole di convalida identiche oppure è ora possibile utilizzare la proprietà SaveOptions.MergeAreas per indicare a API di unire automaticamente CellAreas prima dell'operazione di salvataggio.

{{% /alert %}} 
### **Proprietà Geometry.ShapeAdjustValues aggiunto**
 Con il rilascio della v8.5.2, Aspose.Cells API ha esposto il metodo Geometry.getShapeAdjustValues che può essere utilizzato per[accedere e apportare modifiche ai punti di regolazione di diverse forme](/cells/it/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

Nell'interfaccia Excel Microsoft, i punti di regolazione vengono visualizzati come nodi romboidali gialli.

{{% /alert %}} 

 Ad esempio,

1. Rettangolo arrotondato ha una regolazione per cambiare l'arco
1. Triangolo ha una regolazione per cambiare la posizione del punto
1. Il trapezio ha una regolazione per modificare la larghezza della parte superiore
1. Le frecce hanno due regolazioni per cambiare la forma della testa e della coda

Ecco lo scenario di utilizzo più semplice.

**Java**

{{< highlight "csharp" >}}

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
### **Campo di enumerazione ConsolidationFunction.DISTINCT_COUNT Aggiunto**
Aspose.Cells for Java 8.5.2 ha esposto il campo ConsolidationFunction.DISTINCT_COUNT che può essere utilizzato per applicare la funzione consolidata Distinct Count su DataField di una tabella pivot.

{{% alert color="primary" %}} 

La funzione di consolidamento Distinct Count è supportata solo da Microsoft Excel 2013.

{{% /alert %}}
