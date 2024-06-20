---
title: Cambios en la API pública en Aspose.Cells 17.1.0
type: docs
weight: 380
url: /es/java/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 16.12.0 hasta la 17.1.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases añadidas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para gráficos de Excel 2016**
Las APIs de Aspose.Cells han añadido soporte para algunos gráficos de Excel 2016 mediante la mejora de la enumeración ChartType. Se han añadido los siguientes nuevos campos con la versión Aspose.Cells 17.1.0.

- ChartType.BOX_WHISKER: La serie se representa como caja y bigote.
- ChartType.FUNNEL: La serie se representa como embudo.
- ChartType.PARETO_LINE: La serie se representa como líneas de Pareto.
- ChartType.SUNBURST: La serie se representa como un sunburst.
- ChartType.TREEMAP: La serie se representa como un mapa de árbol.
- ChartType.WATERFALL: La serie se representa como un gráfico de cascada.
- ChartType.HISTOGRAM: La serie se representa como un histograma.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Lectura de tipos de gráficos de Excel 2016](/cells/es/java/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Setter añadido para la propiedad LoadFilter.LoadDataFilterOptions**
Aspose.Cells 17.1.0 ha añadido un setter para la propiedad LoadFilter.LoadDataFilterOptions para reemplazar la variable de instancia m_LoadDataFilterOptions. Los usuarios pueden cambiar la propiedad LoadDataFilterOptions en su propia implementación de la clase LoadFilter para cambiar el comportamiento de carga de archivos de plantilla.

Aquí hay un escenario de uso simple.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Filtrado de plantillas personalizadas](/cells/es/java/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **Propiedad CellsHelper.SignificantDigits añadida**
Aspose.Cells 17.1.0 ha expuesto la propiedad SignificantDigits de la clase CellsHelper que permite obtener o establecer el número de dígitos significativos para valores numéricos en una hoja de cálculo. El valor predeterminado de la propiedad CellsHelper.SignificantDigits es 17 y solo es aplicable si el resultado debe almacenarse en formato de archivo XLSX.

Aquí hay un escenario simple para demostrar el uso de la propiedad CellsHelper.SignificantDigits.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Establecer número de dígitos significativos](/cells/es/java/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **Propiedad GlowEffect.Color añadida**
Aspose.Cells 17.1.0 ha agregado la propiedad GlowEffect.Color que se puede utilizar para recuperar el color del efecto de resplandor.

El siguiente fragmento hace uso de la propiedad GlowEffect.Color.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Lectura del color del resplandor de la forma](/cells/es/java/read-color-of-the-shape-s-glow-effect/)
{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **Propiedades PageSetup.PaperWidth y PaperHeight añadidas**
Aspose.Cells 17.1.0 ha expuesto las propiedades PaperWidth y PaperHeight para la clase PageSetup. Las propiedades PageSetup.PaperWidth y PageSetup.PaperHeight son de tipo double que representan el ancho y alto del papel en unidades de pulgadas considerando la orientación de la página.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Recuperar el tamaño del papel de la hoja de cálculo](/cells/es/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **Propiedad WorkbookSettings.CheckCustomNumberFormat añadida**
Aspose.Cells 17.1.0 ha agregado la propiedad CheckCustomNumberFormat a la clase WorkbookSettings. CheckCustomNumberFormat es útil para verificar si la propiedad Style.Custom se ha establecido correctamente. En caso de que la propiedad Style.Custom se haya establecido incorrectamente, es decir; el valor no corresponde a un patrón válido, entonces las API de Aspose.Cells lanzarán CellsException con el mensaje apropiado.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Verificación de formato personalizado](/cells/es/java/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **Añadido campo DisplayUnitType.PERCENTAGE**
Aspose.Cells 17.1.0 también ha expuesto el campo PERCENTAGE en la enumeración DisplayUnitType. El campo DisplayUnitType.PERCENTAGE indica que los valores en el gráfico se dividirán por 0.01.
## **APIs Eliminadas**
### **Variable de instancia m_LoadDataFilterOptions removida**
Esta versión ha removido la variable de instancia m_LoadDataFilterOptions. Se recomienda utilizar en su lugar la propiedad LoadFilter.LoadDataFilterOptions.
