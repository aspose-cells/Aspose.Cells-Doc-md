---
title: Público API Cambios en Aspose.Cells 16.12.0
type: docs
weight: 360
url: /es/net/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 16.11.0 a la 16.12.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Filtrar objetos en tiempo de carga**
Aspose.Cells 16.12.0 ha expuesto la clase LoadFilter junto con la propiedad LoadOptions.LoadFilter que juntas pueden controlar el tipo de datos que se cargarán al inicializar una instancia de Workbook desde un archivo de plantilla.

Aquí hay un escenario de uso simple para cargar solo las propiedades del documento desde un archivo de plantilla.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



El siguiente fragmento carga todo desde una hoja de cálculo existente excepto los gráficos.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



El siguiente código carga solo los datos de la celda (junto con las fórmulas) y el formato de una hoja de cálculo existente.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



La clase LoadFilter también permite personalizar el proceso de carga según las propiedades de la hoja de trabajo. Para personalizar el proceso de carga según la hoja de trabajo, se debe anular el método LoadFilter.StartSheet como se muestra a continuación.

**C#**

{{< highlight "csharp" >}}

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



El siguiente fragmento utiliza la clase CustomFilter definida anteriormente.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **Enumeración FileFormatType.OTS añadida**
Aspose.Cells 16.12.0 agregó la entrada OTS a la enumeración FileFormatType para detectar el formato de los archivos OTS.

El siguiente fragmento hace uso de FileFormatType.OTS.

**C#**

{{< highlight "csharp" >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **Se agregó la propiedad FontConfigs.PreferSystemFontSubstitutes**
Aspose.Cells 16.12.0 ha expuesto la propiedad PreferSystemFontSubstitutes para la clase FontConfigs. La propiedad FontConfigs.PreferSystemFontSubstitutes es de tipo booleano, lo que indica si API debe usar primero el mecanismo de sustitución de fuentes del sistema, en caso de que no haya una fuente requerida y no se haya definido ninguna sustitución para la fuente en particular. El valor predeterminado de la propiedad FontConfigs.PreferSystemFontSubstitutes es falso.
### **Se agregó la propiedad BuiltInDocumentPropertyCollection.ScaleCrop**
Aspose.Cells 16.12.0 agregó la propiedad ScaleCrop a la clase BuiltInDocumentPropertyCollection. ScaleCrop indica el modo de visualización de la miniatura del documento. Establecer este elemento en verdadero habilita la escala de la miniatura del documento según la visualización, mientras que establecerlo en falso permite recortar la miniatura del documento para mostrar la sección que se ajusta a la visualización.
### **Se agregó la propiedad BuiltInDocumentPropertyCollection.LinksUpToDate**
Aspose.Cells 16.12.0 también expuso la propiedad LinksUpToDate para la clase BuiltInDocumentPropertyCollection. La propiedad LinksUpToDate indica si los hipervínculos de un documento están actualizados.
### **Método Workbook.ExportXml agregado**
Aspose.Cells 16.12.0 ha expuesto el método Workbook.ExportXml que permite almacenar los datos del mapa XML en la ruta de archivo especificada. El método Workbook.ExportXml acepta 2 parámetros donde el primer parámetro de tipo cadena debe ser el nombre del mapa XML y el segundo parámetro debe ser la ubicación de la ruta del archivo para almacenar los datos XML.
### **Se agregó el método WorksheetCollection.CreateRange**
Aspose.Cells 16.12.0 ha agregado el método WorksheetCollection.CreateRange que permite crear un rango basado en una dirección (referencia de área de celda) y el índice de la hoja de trabajo.

El siguiente fragmento utiliza el método WorksheetCollection.CreateRange para crear un rango de celdas que se extiende de A1 a A2 en la primera hoja de trabajo (predeterminada).

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

{{< /highlight >}}
## **API obsoletas**
### **Propiedad LoadOptions.LoadDataOptions obsoleta**
Utilice la propiedad LoadOptions.LoadFilter como alternativa.
### **Propiedad LoadOptions.LoadDataFilterOptions obsoleta**
Utilice la propiedad LoadOptions.LoadFilter en su lugar.
### **Propiedad LoadOptions.OnlyLoadDocumentProperties obsoleta**
Utilice la propiedad LoadOptions.LoadFilter como alternativa.
### **Propiedad LoadOptions.LoadDataAndFormatting obsoleta**
Utilice la propiedad LoadOptions.LoadFilter en su lugar.

{{% alert color="primary" %}} 

Los fragmentos de código para todas las API obsoletas se han compartido anteriormente.

{{% /alert %}}
## **API eliminadas**
### **Propiedad DataLabels.Rotation eliminada**
Utilice la propiedad DataLabels.RotationAngle en su lugar.
### **Propiedad Title.Rotation eliminada**
Utilice la propiedad Title.RotationAngle como alternativa.
### **Propiedad DataLabels.Background eliminada**
Se recomienda utilizar la propiedad DataLabels.BackgroundMode en su lugar.
### **Propiedad DisplayUnitLabel.Rotation eliminada**
Considere usar la propiedad DisplayUnitLabel.RotationAngle para lograr el mismo objetivo.
