---
title: Cambios en la API pública en Aspose.Cells 17.1.0
type: docs
weight: 370
url: /es/net/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 16.12.0 hasta la 17.1.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases añadidas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para gráficos de Excel 2016**
Las APIs de Aspose.Cells han añadido soporte para algunos gráficos de Excel 2016 mediante la mejora de la enumeración ChartType. Se han añadido los siguientes nuevos campos con la versión Aspose.Cells 17.1.0.

- ChartType.BoxWhisker: La serie está dispuesta como caja y bigote.
- ChartType.Funnel: La serie se presenta como un embudo.
- ChartType.ParetoLine: La serie se presenta como líneas de Pareto.
- ChartType.Sunburst: La serie se presenta como un sunburst.
- ChartType.Treemap: La serie se presenta como un treemap.
- ChartType.Waterfall: La serie se presenta como un waterfall.
- ChartType.Histogram: La serie se presenta como un histograma.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Tipos de gráficos de Excel 2016](/cells/es/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Setter añadido para la propiedad LoadFilter.LoadDataFilterOptions**
Aspose.Cells 17.1.0 ha añadido un setter para la propiedad LoadFilter.LoadDataFilterOptions para reemplazar la variable de instancia m_LoadDataFilterOptions. Los usuarios pueden cambiar la propiedad LoadDataFilterOptions en su propia implementación de la clase LoadFilter para cambiar el comportamiento de carga de archivos de plantilla.

Aquí hay un escenario de uso simple.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Filtrado de plantillas personalizadas](/cells/es/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Propiedad CellsHelper.SignificantDigits añadida**
Aspose.Cells 17.1.0 ha expuesto la propiedad SignificantDigits de la clase CellsHelper que permite obtener o establecer el número de dígitos significativos para valores numéricos en una hoja de cálculo. El valor predeterminado de la propiedad CellsHelper.SignificantDigits es 17 y solo es aplicable si el resultado debe almacenarse en formato de archivo XLSX.

Aquí hay un escenario simple para demostrar el uso de la propiedad CellsHelper.SignificantDigits.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Especificación del número de dígitos significativos que se almacenarán en el archivo de Excel](/cells/es/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **Propiedad GlowEffect.Color añadida**
Aspose.Cells 17.1.0 ha agregado la propiedad GlowEffect.Color que se puede utilizar para recuperar el color del efecto de resplandor.

El siguiente fragmento hace uso de la propiedad GlowEffect.Color.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Lectura del color de resplandor de la forma](/cells/es/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Propiedades PageSetup.PaperWidth y PaperHeight añadidas**
Aspose.Cells 17.1.0 ha expuesto las propiedades PaperWidth y PaperHeight para la clase PageSetup. Las propiedades PageSetup.PaperWidth y PageSetup.PaperHeight son de tipo double que representan el ancho y alto del papel en unidades de pulgadas considerando la orientación de la página.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Obtención del tamaño de papel de la hoja de cálculo](/cells/es/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **Propiedad WorkbookSettings.CheckCustomNumberFormat añadida**
Aspose.Cells 17.1.0 ha agregado la propiedad CheckCustomNumberFormat a la clase WorkbookSettings. CheckCustomNumberFormat es útil para verificar si la propiedad Style.Custom se ha establecido correctamente. En caso de que la propiedad Style.Custom se haya establecido incorrectamente, es decir; el valor no corresponde a un patrón válido, entonces las API de Aspose.Cells lanzarán CellsException con el mensaje apropiado.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Verificación de formato personalizado](/cells/es/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Añadido el campo DisplayUnitType.Percentage**
Aspose.Cells 17.1.0 también ha expuesto el campo Percentage en la enumeración DisplayUnitType. El campo DisplayUnitType.Percentage indica que los valores en el gráfico se dividirán por 0.01.
## **APIs Eliminadas**
### **Variable de instancia m_LoadDataFilterOptions removida**
Esta versión ha removido la variable de instancia m_LoadDataFilterOptions. Se recomienda utilizar en su lugar la propiedad LoadFilter.LoadDataFilterOptions.
{{< app/cells/assistant language="csharp" >}}
