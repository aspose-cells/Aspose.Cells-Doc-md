---
title: Público API Cambios en Aspose.Cells 17.1.0
type: docs
weight: 370
url: /es/net/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 16.12.0 a la 17.1.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Compatibilidad con gráficos de Excel 2016**
Aspose.Cells Las API agregaron compatibilidad con algunos gráficos de Excel 2016 al mejorar la enumeración de ChartType. Se han agregado los siguientes campos nuevos con el lanzamiento de Aspose.Cells 17.1.0.

- ChartType.BoxWhisker: la serie se presenta como caja y bigotes.
- ChartType.Funnel: la serie se presenta como un embudo.
- ChartType.ParetoLine: la serie se presenta como líneas de Pareto.
- ChartType.Sunburst: la serie se presenta como un rayo de sol.
- ChartType.Treemap: la serie se presenta como un mapa de árbol.
- ChartType.Waterfall: la serie se presenta como una cascada.
- ChartType.Histogram: la serie se presenta como un histograma.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Lectura de tipos de gráficos de Excel 2016](/cells/es/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Setter agregado para la propiedad LoadFilter.LoadDataFilterOptions**
Aspose.Cells 17.1.0 ha agregado setter para la propiedad LoadFilter.LoadDataFilterOptions para reemplazar la variable de instancia m_LoadDataFilterOptions. Los usuarios pueden cambiar la propiedad LoadDataFilterOptions en su propia implementación de la clase LoadFilter para cambiar el comportamiento de carga de archivos de plantilla.

Aquí hay un escenario de uso simple.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Filtrado de plantillas personalizadas](/cells/es/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            this.LoadDataFilterOptions = LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            this.LoadDataFilterOptions = LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}


### **Se agregó la propiedad CellsHelper.SignificantDigits**
Aspose.Cells 17.1.0 ha expuesto la propiedad SignificantDigits de la clase CellsHelper que permite obtener o establecer la cantidad de dígitos significativos para valores numéricos en una hoja de cálculo. El valor predeterminado de la propiedad CellsHelper.SignificantDigits es 17, mientras que solo es aplicable si el resultado debe almacenarse en formato de archivo XLSX.

Aquí hay un escenario simple para demostrar el uso de la propiedad CellsHelper.SignificantDigits.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Configuración del número de dígitos significativos](/cells/es/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **Se agregó la propiedad GlowEffect.Color**
Aspose.Cells 17.1.0 ha agregado la propiedad GlowEffect.Color que se puede usar para recuperar el color del efecto de brillo.

El siguiente fragmento utiliza la propiedad GlowEffect.Color.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Lectura del color de resplandor de la forma](/cells/es/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Read the source excel file

var book = new Workbook(dir + "sample.xlsx");

// Access first worksheet

var sheet = book.Worksheets[0];

// Access the first shape

var shape = sheet.Shapes[0];

// Read the glow effect color

var glow = shape.Glow;

var color = glow.Color;

{{< /highlight >}}


### **Se agregaron las propiedades PageSetup.PaperWidth y PaperHeight**
Aspose.Cells 17.1.0 ha expuesto las propiedades PaperWidth y PaperHeight para la clase PageSetup. Las propiedades PageSetup.PaperWidth & PageSetup.PaperHeight son del tipo double y representan el ancho y el alto del papel en unidades de pulgadas teniendo en cuenta la orientación de la página.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Recuperación del tamaño de papel de la hoja de trabajo](/cells/es/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **Se agregó la propiedad WorkbookSettings.CheckCustomNumberFormat**
Aspose.Cells 17.1.0 agregó la propiedad CheckCustomNumberFormat a la clase WorkbookSettings. CheckCustomNumberFormat es útil para comprobar si la propiedad Style.Custom se ha configurado correctamente o no. En caso de que la propiedad Style.Custom se haya configurado incorrectamente, es decir; el valor no corresponde a un patrón válido, entonces las API Aspose.Cells generarán CellsException con el mensaje apropiado.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Verificación del formato personalizado](/cells/es/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Set CheckCustomNumberFormat property to true

book.Settings.CheckCustomNumberFormat = true;

// Access first worksheet

var sheet = book.Worksheets[0];

// Access a cell

var cell = sheet.Cells["B5"];

// Insert a value to the cell

cell.PutValue(2347);

// Access cell's style

Style style = cell.GetStyle();



// Set Custom property to an invalid pattern

style.Custom = "ggg @ fff";

// Set the modified style to the cell

cell.SetStyle(style);

{{< /highlight >}}


### **Se agregó el campo DisplayUnitType.Percentage**
Aspose.Cells 17.1.0 también expuso el campo Porcentaje a la enumeración DisplayUnitType. El campo DisplayUnitType.Percentage indica que los valores del gráfico se dividirán por 0,01.
## **API eliminadas**
### **Variable de instancia m_LoadDataFilterOptions eliminada**
Esta versión eliminó la variable de instancia m_LoadDataFilterOptions. Se recomienda utilizar la propiedad LoadFilter.LoadDataFilterOptions en su lugar.
