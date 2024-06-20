---
title: Cambios en la API pública en Aspose.Cells 16.11.0
type: docs
weight: 360
url: /es/java/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 16.10.0 hasta la 16.11.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases agregadas y eliminadas, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para Configuraciones de Globalización**
Aspose.Cells 16.11.0 ha expuesto la clase GlobalizationSettings junto con la propiedad WorkbookSettings.GlobalizationSettings para hacer cumplir que las APIs de Aspose.Cells utilicen etiquetas personalizadas para los Subtotales. La clase GlobalizationSettings tiene los siguientes métodos que pueden ser anulados en la implementación personalizada para dar nombres deseados a las etiquetas **Total** & **Gran Total**.

- GlobalizationSettings.getTotalName: Obtiene el nombre total de la función.
- GlobalizationSettings.getGrandTotalName: Obtiene el nombre gran total de la función.

Aquí hay una clase personalizada simple que extiende la clase GlobalizationSettings y anula sus métodos mencionados anteriormente para devolver etiquetas personalizadas para la función de consolidación Promedio.

**Java**

{{< highlight csharp >}}

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

El siguiente fragmento carga una hoja de cálculo existente y agrega el Subtotal de tipo Promedio en los datos ya disponibles en la hoja de cálculo. La clase CustomSettings y sus métodos getTotalName y getGrandTotalName serán llamados al agregar el Subtotal a la hoja de cálculo.

**Java**

{{< highlight csharp >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[] { 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

La clase GlobalizationSettings también ofrece el método getOtherName que es útil para obtener el nombre de las etiquetas de "Otro" para los gráficos circulares. Aquí hay un escenario de uso simple del método GlobalizationSettings.getOtherName.

**Java**

{{< highlight csharp >}}

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

El siguiente fragmento carga una hoja de cálculo existente que contiene un gráfico circular, y renderiza el gráfico a imagen utilizando la clase CustomSettings creada anteriormente.

**Java**

{{< highlight csharp >}}

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
### **Clase CellsFactory Agregada**
Aspose.Cells 16.11.0 ha expuesto la clase CellsFactory que actualmente tiene un método, es decir, createStyle. El método CellsFactory.createStyle se puede utilizar para crear una instancia de la clase Style sin agregarla al conjunto de estilos del libro de trabajo.

Aquí hay un escenario de uso simple del método CellsFactory.createStyle.

**Java**

{{< highlight csharp >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Propiedad Workbook.AbsolutePath Agregada**
Aspose.Cells 16.11.0 ha expuesto la propiedad Workbook.AbsolutePath que permite obtener o establecer la ruta de acceso absoluta del libro de trabajo almacenada en el archivo workbook.xml. Esta propiedad es útil al actualizar solo los enlaces externos.
### **Agregado Método GridHyperlinkCollection.getHyperlink**
Aspose.Cells.GridWeb 16.11.0 ha expuesto el método getHyperlink en la clase GridHyperlinkCollection que permite obtener la instancia de GridHyperlink pasando una instancia de GridCell o un par de enteros correspondientes a los índices de fila y columna.

{{% alert color="primary" %}} 

En caso de que no se haya encontrado ningún hipervínculo en la celda especificada, el método getHyperlink devolverá null.

{{% /alert %}} 

Aquí hay un escenario de uso simple del método getHyperlink.

**Java**

{{< highlight csharp >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **APIs obsoletas**
### **Constructor de Estilo Obsoleto**
Por favor, usa el método cellsFactory.createStyle como alternativa.
## **APIs eliminadas**
### **Método Cell.getConditionalStyle Eliminado**
Por favor, usa el método Cell.getConditionalFormattingResult en su lugar.
### **Método Cells.getMaxDataRowInColumn(int column) Eliminado**
Por favor, usa el método Cells.getLastDataRow(int) como alternativa.
### **Propiedad PageSetup.Draft Eliminada**
Se recomienda usar la propiedad PageSetup.PrintDraft en su lugar.
### **Propiedad AutoFilter.FilterColumnCollection Eliminada**
Considera usar la propiedad AutoFilter.FilterColumns para lograr el mismo objetivo.
### **Propiedad TickLabels.Rotation Eliminada**
Por favor, usa la propiedad TickLabels.RotationAngle en su lugar.
