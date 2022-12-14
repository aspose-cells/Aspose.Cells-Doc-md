---
title: Público API Cambios en Aspose.Cells 16.11.0
type: docs
weight: 350
url: /es/net/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 16.10.0 a la 16.11.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Compatibilidad con la configuración de globalización**
Aspose.Cells 16.11.0 ha expuesto la clase GlobalizationSettings junto con la propiedad WorkbookSettings.GlobalizationSettings para hacer cumplir las API Aspose.Cells para usar etiquetas personalizadas para subtotales. La clase GlobalizationSettings tiene los siguientes métodos que se pueden anular en la implementación personalizada para dar los nombres deseados a las etiquetas**Total** & **Gran total**.

- GlobalizationSettings.GetTotalName: Obtiene el nombre total de la función.
- GlobalizationSettings.GetGrandTotalName: Obtiene el nombre del total general de la función.

Aquí hay una clase personalizada simple que extiende la clase GlobalizationSettings y anula sus métodos antes mencionados para devolver etiquetas personalizadas para la función de consolidación Promedio.

**C#**

{{< highlight "csharp" >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "AVG";

            default:

                return base.GetTotalName(functionType);

        }

    }

    public override string GetGrandTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "GRD AVG";

            default:

                return base.GetGrandTotalName(functionType);

        }

    }

}

{{< /highlight >}}



El siguiente fragmento carga una hoja de cálculo existente y agrega el Subtotal de tipo Promedio en los datos ya disponibles en la hoja de trabajo. La clase CustomSettings y sus métodos GetTotalName y GetGrandTotalName se llamarán en el momento de agregar Subtotal a la hoja de trabajo.

**C#**

{{< highlight "csharp" >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[]{ 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



La clase GlobalizationSettings también ofrece el método GetOtherName, que es útil para obtener el nombre de las etiquetas "Otros" para los gráficos circulares. Aquí hay un escenario de uso simple del método GlobalizationSettings.GetOtherName.

**C#**

{{< highlight "csharp" >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetOtherName()

    {

        int lcid = System.Globalization.CultureInfo.CurrentCulture.LCID;

        switch (lcid)

        {

            case 1033:

                return "Other";

            case 1036:

                return "Autre";

            case 1031:

                return "Andere";

            //Do other case

            default:

                return base.GetOtherName();

        }

    }

}

{{< /highlight >}}



El siguiente fragmento carga una hoja de cálculo existente que contiene un gráfico circular y representa el gráfico en una imagen mientras utiliza la clase CustomSettings creada anteriormente.

**C#**

{{< highlight "csharp" >}}

 // Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.Worksheets[0];

// Accesses the 1st chart from the collection

Chart chart = sheet.Charts[0];

// Refreshes the chart

chart.Calculate();

// Renders the chart to image

chart.ToImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}


### **Clase CellsFactory agregada**
Aspose.Cells 16.11.0 ha expuesto la clase CellsFactory que actualmente tiene un método, es decir; CrearEstilo. El método CellsFactory.CreateStyle se puede usar para crear una instancia de la clase Style sin agregarla al conjunto de estilos del libro de trabajo.

Este es un escenario de uso simple del método CellsFactory.CreateStyle.

**C#**

{{< highlight "csharp" >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **Se agregó la propiedad Workbook.AbsolutePath**
Aspose.Cells 16.11.0 ha expuesto la propiedad Workbook.AbsolutePath que permite obtener o establecer la ruta absoluta del libro de trabajo almacenada en el archivo workbook.xml. Esta propiedad es útil solo para actualizar los enlaces externos.
### **Se agregó el método GridHyperlinkCollection.GetHyperlink**
Aspose.Cells.GridWeb 16.11.0 ha expuesto el método GetHyperlink a la clase GridHyperlinkCollection que permite obtener la instancia de GridHyperlink pasando una instancia GridCell o un par de enteros correspondientes a los índices de columna de fila.

{{% alert color="primary" %}} 

En caso de que no se haya encontrado un hipervínculo en la celda especificada, el método GetHyperlink devolvería un valor nulo.

{{% /alert %}} 

Aquí hay un escenario de uso simple del método GetHyperlink.

**C#**

{{< highlight "csharp" >}}

 // Gets the active worksheet from the collection

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.Hyperlinks;

// Gets hyperlink from cell A1

GridHyperlink link = links.GetHyperlink(sheet.Cells["A1"]);

// Gets hyperlink from cell D1

link = links.GetHyperlink(0, 3);

{{< /highlight >}}
## **API obsoletas**
### **Constructor de estilo obsoleto**
Utilice el método cellFactory.CreateStyle como alternativa.
## **API eliminadas**
### **Eliminado Cell. Método GetConditionalStyle**
Utilice el método Cell.GetConditionalFormattingResult en su lugar.
### **Método eliminado Cells. MaxDataRowInColumn (columna int)**
Utilice el método Cells.GetLastDataRow(int) como alternativa.
### **Propiedad PageSetup.Draft eliminada**
Se recomienda utilizar la propiedad PageSetup.PrintDraft en su lugar.
### **Propiedad AutoFilter.FilterColumnCollection eliminada**
Considere usar la propiedad AutoFilter.FilterColumns para lograr el mismo objetivo.
### **Propiedad TickLabels.Rotation eliminada**
Utilice la propiedad TickLabels.RotationAngle en su lugar.
