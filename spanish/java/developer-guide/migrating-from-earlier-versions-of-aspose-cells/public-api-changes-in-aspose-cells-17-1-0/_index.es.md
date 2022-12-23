---
title: Público API Cambios en Aspose.Cells 17.1.0
type: docs
weight: 380
url: /es/java/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 16.12.0 a la 17.1.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Compatibilidad con gráficos de Excel 2016**
Aspose.Cells Las API agregaron compatibilidad con algunos gráficos de Excel 2016 al mejorar la enumeración de ChartType. Se han agregado los siguientes campos nuevos con el lanzamiento de Aspose.Cells 17.1.0.

- ChartType.BOX_WHISKER: la serie se presenta como caja y bigotes.
- ChartType.FUNNEL: la serie se presenta como un embudo.
- ChartType.PARETO_LINE: la serie se presenta como líneas de Pareto.
- ChartType.SUNBURST: la serie se presenta como un rayo de sol.
- ChartType.TREEMAP: la serie se presenta como un mapa de árbol.
- ChartType.WATERFALL: la serie se presenta como una cascada.
- ChartType.HISTOGRAM: la serie se presenta como un histograma.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Lectura de tipos de gráficos de Excel 2016](/cells/es/java/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Setter agregado para la propiedad LoadFilter.LoadDataFilterOptions**
Aspose.Cells 17.1.0 ha agregado setter para la propiedad LoadFilter.LoadDataFilterOptions para reemplazar la variable de instancia m_LoadDataFilterOptions. Los usuarios pueden cambiar la propiedad LoadDataFilterOptions en su propia implementación de la clase LoadFilter para cambiar el comportamiento de carga de archivos de plantilla.

Aquí hay un escenario de uso simple.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Filtrado de plantillas personalizadas](/cells/es/java/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 class CustomLoadFilter extends LoadFilter {

	public void startSheet(Worksheet sheet) {

		if (sheet.getName().equals("NoCharts")) {

			//Load everything and filter charts

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CHART);

		}

		if (sheet.getName().equals("NoShapes")) {

			//Load everything and filter shapes

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.SHAPE);

		}

		if (sheet.getName().equals("NoConditionalFormatting")) {

			//Load everything and filter conditional formatting

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CONDITIONAL_FORMATTING);

		}

	}

}

{{< /highlight >}}
### **Se agregó la propiedad CellsHelper.SignificantDigits**
Aspose.Cells 17.1.0 ha expuesto la propiedad SignificantDigits de la clase CellsHelper que permite obtener o establecer la cantidad de dígitos significativos para valores numéricos en una hoja de cálculo. El valor predeterminado de la propiedad CellsHelper.SignificantDigits es 17, mientras que solo es aplicable si el resultado debe almacenarse en el formato de archivo XLSX.

Aquí hay un escenario simple para demostrar el uso de la propiedad CellsHelper.SignificantDigits.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Configuración del número de dígitos significativos](/cells/es/java/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **Se agregó la propiedad GlowEffect.Color**
Aspose.Cells 17.1.0 ha agregado la propiedad GlowEffect.Color que se puede usar para recuperar el color del efecto de brillo.

El siguiente fragmento utiliza la propiedad GlowEffect.Color.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Lectura del color de resplandor de la forma](/cells/es/java/read-color-of-the-shape-s-glow-effect/)
{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Read the source Excel file

Workbook book = new Workbook(dir + "sample.xlsx");

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access the first shape

Shape shape = sheet.getShapes().get(0);

//Read the glow effect color

GlowEffect glow = shape.getGlow();

CellsColor color = glow.getColor();

{{< /highlight >}}
### **Se agregaron las propiedades PageSetup.PaperWidth y PaperHeight**
Aspose.Cells 17.1.0 ha expuesto las propiedades PaperWidth y PaperHeight para la clase PageSetup. Las propiedades PageSetup.PaperWidth & PageSetup.PaperHeight son del tipo double y representan el ancho y el alto del papel en unidades de pulgadas teniendo en cuenta la orientación de la página.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Recuperación del tamaño de papel de la hoja de cálculo](/cells/es/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **Se agregó la propiedad WorkbookSettings.CheckCustomNumberFormat**
Aspose.Cells 17.1.0 agregó la propiedad CheckCustomNumberFormat a la clase WorkbookSettings. CheckCustomNumberFormat es útil para comprobar si la propiedad Style.Custom se ha configurado correctamente o no. En caso de que la propiedad Style.Custom se haya configurado incorrectamente, es decir; el valor no corresponde a un patrón válido, entonces las API Aspose.Cells generarán CellsException con el mensaje apropiado.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Verificación de forma personalizada](/cells/es/java/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Set CheckCustomNumberFormat property to true

book.getSettings().setCheckCustomNumberFormat(true);

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access a cell

Cell cell = sheet.getCells().get("B5");

//Insert a value to the cell

cell.putValue(2347);

//Access cell's style

Style style = cell.getStyle();



//Set Custom property to an invalid pattern

style.setCustom("ggg @ fff");

//Set the modified style to the cell

cell.setStyle(style);

{{< /highlight >}}
### **Campo DisplayUnitType.PERCENTAGE agregado**
Aspose.Cells 17.1.0 también expuso el campo PERCENTAGE a la enumeración DisplayUnitType. El campo DisplayUnitType.PERCENTAGE indica que los valores del gráfico se dividirán por 0,01.
## **API eliminadas**
### **Variable de instancia m_LoadDataFilterOptions eliminada**
Esta versión eliminó la variable de instancia m_LoadDataFilterOptions. Se recomienda utilizar la propiedad LoadFilter.LoadDataFilterOptions en su lugar.
