---
title: Público API Cambios en Aspose.Cells 16.11.0
type: docs
weight: 360
url: /es/java/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 16.10.0 a la 16.11.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Compatibilidad con la configuración de globalización**
Aspose.Cells 16.11.0 ha expuesto la clase GlobalizationSettings junto con la propiedad WorkbookSettings.GlobalizationSettings para hacer cumplir las API Aspose.Cells para usar etiquetas personalizadas para subtotales. La clase GlobalizationSettings tiene los siguientes métodos que se pueden anular en la implementación personalizada para dar los nombres deseados a las etiquetas**Total** & **Gran total**.

- GlobalizationSettings.getTotalName: Obtiene el nombre total de la función.
- GlobalizationSettings.getGrandTotalName: Obtiene el nombre del total general de la función.

Aquí hay una clase personalizada simple que extiende la clase GlobalizationSettings y anula sus métodos antes mencionados para devolver etiquetas personalizadas para la función de consolidación Promedio.

**Java**

{{< highlight "csharp" >}}

 public class CustomSettings extends GlobalizationSettings

{    

    public String getTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "AVG";

             default:

                return super.getTotalName(functionType);

         }

    }

    public String getGrandTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "GRAND AVG";

             default:

            	 return super.getGrandTotalName(functionType);

         }



    }

}

{{< /highlight >}}

El siguiente fragmento carga una hoja de cálculo existente y agrega el Subtotal de tipo Promedio en los datos ya disponibles en la hoja de trabajo. La clase CustomSettings y sus métodos getTotalName y getGrandTotalName se llamarán en el momento de agregar Subtotal a la hoja de trabajo.

**Java**

{{< highlight "csharp" >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[]{ 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

La clase GlobalizationSettings también ofrece el método getOtherName, que es útil para obtener el nombre de las etiquetas "Otros" para los gráficos circulares. Aquí hay un escenario de uso simple del método GlobalizationSettings.getOtherName.

**Java**

{{< highlight "csharp" >}}

 public class CustomSettings extends GlobalizationSettings

{ 

	public String getOtherName()

	{

		String language = Locale.getDefault().getLanguage();

		System.out.println(language);

		switch (language)

		{

			case "en":

				return "Other";

			case "fr":

				return "Autre";

			case "de":

				return "Andere";

			//Do other cases

			default:

				return super.getOtherName();

		}

	}

}

{{< /highlight >}}

El siguiente fragmento carga una hoja de cálculo existente que contiene un gráfico circular y representa el gráfico en una imagen mientras utiliza la clase CustomSettings creada anteriormente.

**Java**

{{< highlight "csharp" >}}

 //Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.getWorksheets().get(0);

//Accesses the 1st chart from the collection

Chart chart = sheet.getCharts().get(0);

//Refreshes the chart

chart.calculate();

//Renders the chart to image

chart.toImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}
### **Clase CellsFactory agregada**
Aspose.Cells 16.11.0 ha expuesto la clase CellsFactory que actualmente tiene un método, es decir; crearEstilo. El método CellsFactory.createStyle se puede usar para crear una instancia de la clase Style sin agregarla al conjunto de estilos del libro de trabajo.

Aquí hay un escenario de uso simple del método CellsFactory.createStyle.

**Java**

{{< highlight "csharp" >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Se agregó la propiedad Workbook.AbsolutePath**
Aspose.Cells 16.11.0 ha expuesto la propiedad Workbook.AbsolutePath que permite obtener o establecer la ruta absoluta del libro de trabajo almacenada en el archivo workbook.xml. Esta propiedad es útil solo para actualizar los enlaces externos.
### **Se agregó el método GridHyperlinkCollection.getHyperlink**
Aspose.Cells.GridWeb 16.11.0 ha expuesto el método getHyperlink a la clase GridHyperlinkCollection que permite obtener la instancia de GridHyperlink ya sea pasando una instancia GridCell o un par de enteros correspondientes a los índices de columna de fila.

{{% alert color="primary" %}} 

En caso de que no se haya encontrado un hipervínculo en la celda especificada, el método getHyperlink devolverá un valor nulo.

{{% /alert %}} 

Aquí hay un escenario de uso simple del método getHyperlink.

**Java**

{{< highlight "csharp" >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **API obsoletas**
### **Constructor de estilo obsoleto**
Utilice el método cellFactory.createStyle como alternativa.
## **API eliminadas**
### **Método eliminado Cell.getConditionalStyle**
Utilice el método Cell.getConditionalFormattingResult en su lugar.
### **Método eliminado Cells.getMaxDataRowInColumn (columna int)**
Utilice el método Cells.getLastDataRow(int) como alternativa.
### **Propiedad PageSetup.Draft eliminada**
Se recomienda utilizar la propiedad PageSetup.PrintDraft en su lugar.
### **Propiedad AutoFilter.FilterColumnCollection eliminada**
Considere usar la propiedad AutoFilter.FilterColumns para lograr el mismo objetivo.
### **Propiedad TickLabels.Rotation eliminada**
Utilice la propiedad TickLabels.RotationAngle en su lugar.
