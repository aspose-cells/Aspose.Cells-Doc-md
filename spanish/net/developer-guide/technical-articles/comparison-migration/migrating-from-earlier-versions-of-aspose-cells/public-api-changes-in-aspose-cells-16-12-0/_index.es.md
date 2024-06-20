---
title: Cambios en la API pública en Aspose.Cells 16.12.0
type: docs
weight: 360
url: /es/net/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios realizados en la API de Aspose.Cells desde la versión 16.11.0 hasta la 16.12.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases añadidas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento interno en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Objetos de filtro en el momento de carga**
Aspose.Cells 16.12.0 ha expuesto la clase LoadFilter junto con la propiedad LoadOptions.LoadFilter que juntas pueden controlar el tipo de datos a cargar al inicializar una instancia de Workbook desde un archivo de plantilla.

A continuación se muestra un escenario de uso simple para cargar solo las propiedades del documento desde un archivo de plantilla.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



El siguiente fragmento carga todo, excepto los gráficos, de una hoja de cálculo existente.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



El siguiente código carga solo los datos de celda (junto con fórmulas) y el formato de una hoja de cálculo existente.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



La clase LoadFilter también permite personalizar el proceso de carga según las propiedades de la Hoja de Cálculo. Para personalizar el proceso de carga según la hoja de cálculo, es necesario anular el método LoadFilter.StartSheet como se muestra a continuación.

**C#**

{{< highlight csharp >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}



El siguiente fragmento hace uso de la clase CustomFilter definida anteriormente.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **Añadida la enumeración FileFormatType.OTS**
Aspose.Cells 16.12.0 ha agregado la entrada OTS a la enumeración FileFormatType para detectar el formato de archivos OTS.

El siguiente fragmento hace uso de FileFormatType.OTS.

**C#**

{{< highlight csharp >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **Añadida la propiedad PreferSystemFontSubstitutes de FontConfigs.**
Aspose.Cells 16.12.0 ha expuesto la propiedad PreferSystemFontSubstitutes para la clase FontConfigs. Esta propiedad es de tipo booleano, indicando si la API debe usar primero el mecanismo de sustitución de fuentes del sistema, en caso de que no esté presente una fuente requerida y no se haya definido ninguna sustitución para la fuente en particular. El valor predeterminado de la propiedad PreferSystemFontSubstitutes de FontConfigs es falso.
### **Añadida la propiedad ScaleCrop de BuiltInDocumentPropertyCollection**
Aspose.Cells 16.12.0 ha añadido la propiedad ScaleCrop a la clase BuiltInDocumentPropertyCollection. ScaleCrop indica el modo de visualización de la miniatura del documento. Establecer este elemento en true habilita el escalamiento de la miniatura del documento según la visualización, mientras que establecerlo en false habilita el recorte de la miniatura del documento para mostrar la sección que se ajusta a la visualización.
### **Añadida la propiedad LinksUpToDate de BuiltInDocumentPropertyCollection**
Aspose.Cells 16.12.0 también ha expuesto la propiedad LinksUpToDate para la clase BuiltInDocumentPropertyCollection. Esta propiedad indica si los hipervínculos en un documento están actualizados.
### **Añadido el método ExportXml a la clase Workbook.**
Aspose.Cells 16.12.0 ha expuesto el método ExportXml que permite almacenar los datos del mapa XML en la ruta de archivo especificada. El método ExportXml de Workbook acepta 2 parámetros, donde el primer parámetro de tipo cadena debe ser el nombre del mapa XML y el segundo parámetro debe ser la ubicación de la ruta de archivo para almacenar los datos XML.
### **Añadido el método CreateRange a la clase WorksheetCollection.**
Aspose.Cells 16.12.0 ha añadido el método CreateRange a la clase WorksheetCollection que permite crear un rango basado en una dirección (referencia de área de celda) e índice de hoja de cálculo.

El siguiente fragmento hace uso del método CreateRange de WorksheetCollection para crear un rango de celdas que abarca de A1 a A2 en la primera (predeterminada) hoja de cálculo.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

{{< /highlight >}}
## **APIs obsoletas**
### **Propiedad LoadOptions.LoadDataOptions Obsoleta**
Por favor, utilice la propiedad LoadOptions.LoadFilter como alternativa.
### **Propiedad LoadOptions.LoadDataFilterOptions Obsoleta**
Por favor, utilice la propiedad LoadOptions.LoadFilter en su lugar.
### **Propiedad LoadOptions.OnlyLoadDocumentProperties Obsoleta**
Por favor, utilice la propiedad LoadOptions.LoadFilter como alternativa.
### **Propiedad LoadOptions.LoadDataAndFormatting Obsoleta**
Por favor, utilice la propiedad LoadOptions.LoadFilter en su lugar.

{{% alert color="primary" %}} 

Se han compartido fragmentos de código para todas las APIs obsoletas anteriormente.

{{% /alert %}}
## **APIs eliminadas**
### **Propiedad DataLabels.Rotation Eliminada**
Por favor, utilice la propiedad DataLabels.RotationAngle en su lugar.
### **Propiedad Title.Rotation Eliminada**
Por favor, utilice la propiedad Title.RotationAngle como alternativa.
### **Propiedad DataLabels.Background Eliminada**
Se recomienda utilizar la propiedad DataLabels.BackgroundMode en su lugar.
### **Propiedad Rotation de DisplayUnitLabel eliminada**
Por favor considere usar la propiedad DisplayUnitLabel.RotationAngle para lograr el mismo objetivo.
