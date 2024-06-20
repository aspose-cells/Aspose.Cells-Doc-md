---
title: Cambios en la API pública en Aspose.Cells 16.11.0
type: docs
weight: 350
url: /es/net/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 16.10.0 hasta la 16.11.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases agregadas y eliminadas, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para Configuraciones de Globalización**
Aspose.Cells 16.11.0 ha expuesto la clase GlobalizationSettings junto con la propiedad WorkbookSettings.GlobalizationSettings para hacer cumplir que las APIs de Aspose.Cells utilicen etiquetas personalizadas para los Subtotales. La clase GlobalizationSettings tiene los siguientes métodos que pueden ser anulados en la implementación personalizada para dar nombres deseados a las etiquetas **Total** & **Gran Total**.

- GlobalizationSettings.GetTotalName: Obtiene el nombre total de la función.
- GlobalizationSettings.GetGrandTotalName: Obtiene el nombre total general de la función.

Aquí hay una clase personalizada simple que extiende la clase GlobalizationSettings y anula sus métodos mencionados anteriormente para devolver etiquetas personalizadas para la función de consolidación Promedio.

**C#**

{{< highlight csharp >}}

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



El siguiente fragmento carga una hoja de cálculo existente y agrega el Subtotal de tipo Promedio en datos ya disponibles en la hoja de cálculo. La clase CustomSettings y sus métodos GetTotalName y GetGrandTotalName serán llamados al momento de agregar el Subtotal a la hoja de cálculo.

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[] { 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



La clase GlobalizationSettings también ofrece el método GetOtherName que es útil para obtener el nombre de las etiquetas "Otros" para gráficos circulares. Aquí hay un simple escenario de uso del método GlobalizationSettings.GetOtherName.

**C#**

{{< highlight csharp >}}

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



El siguiente fragmento carga una hoja de cálculo existente que contiene un gráfico circular, y renderiza el gráfico a imagen utilizando la clase CustomSettings creada anteriormente.

**C#**

{{< highlight csharp >}}

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


### **Clase CellsFactory Agregada**
Aspose.Cells 16.11.0 ha expuesto la clase CellsFactory que actualmente tiene un método, que es; CreateStyle. El método CellsFactory.CreateStyle se puede utilizar para crear una instancia de la clase Style sin añadirla al grupo de estilos del libro de trabajo.

Aquí hay un escenario simple de uso del método CellsFactory.CreateStyle.

**C#**

{{< highlight csharp >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **Propiedad Workbook.AbsolutePath Agregada**
Aspose.Cells 16.11.0 ha expuesto la propiedad Workbook.AbsolutePath que permite obtener o establecer la ruta de acceso absoluta del libro de trabajo almacenada en el archivo workbook.xml. Esta propiedad es útil al actualizar solo los enlaces externos.
### **Añadido el Método GridHyperlinkCollection.GetHyperlink**
Aspose.Cells.GridWeb 16.11.0 ha expuesto el método GetHyperlink a la clase GridHyperlinkCollection que permite obtener la instancia de GridHyperlink al pasar una instancia de GridCell o un par de enteros correspondientes a los índices de columna de fila.

{{% alert color="primary" %}} 

En caso de que no se encuentre ningún hipervínculo en la celda especificada, el método GetHyperlink devolverá nulo.

{{% /alert %}} 

Aquí hay un escenario simple de uso del método GetHyperlink.

**C#**

{{< highlight csharp >}}

 // Gets the active worksheet from the collection

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.Hyperlinks;

// Gets hyperlink from cell A1

GridHyperlink link = links.GetHyperlink(sheet.Cells["A1"]);

// Gets hyperlink from cell D1

link = links.GetHyperlink(0, 3);

{{< /highlight >}}
## **APIs obsoletas**
### **Constructor de Estilo Obsoleto**
Por favor, utilice el método cellsFactory.CreateStyle como alternativa.
## **APIs eliminadas**
### **Método Cell.GetConditionalStyle eliminado**
Por favor, utilice el método Cell.GetConditionalFormattingResult como alternativa.
### **Método Cells.MaxDataRowInColumn(int column) eliminado**
Por favor, utilice el método Cells.GetLastDataRow(int) como alternativa.
### **Propiedad PageSetup.Draft Eliminada**
Se recomienda usar la propiedad PageSetup.PrintDraft en su lugar.
### **Propiedad AutoFilter.FilterColumnCollection Eliminada**
Considera usar la propiedad AutoFilter.FilterColumns para lograr el mismo objetivo.
### **Propiedad TickLabels.Rotation Eliminada**
Por favor, usa la propiedad TickLabels.RotationAngle en su lugar.
