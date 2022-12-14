---
title: Público API Cambios en Aspose.Cells 16.12.0
type: docs
weight: 370
url: /es/java/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 16.11.0 a la 16.12.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Filtrar objetos en tiempo de carga**
Aspose.Cells 16.12.0 ha expuesto la clase LoadFilter junto con la propiedad LoadOptions.LoadFilter que juntas pueden controlar el tipo de datos que se cargarán al inicializar una instancia de Workbook desde un archivo de plantilla.

Aquí hay un escenario de uso simple para cargar solo las propiedades del documento desde un archivo de plantilla.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.DOCUMENT_PROPERTIES);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

El siguiente fragmento carga todo desde una hoja de cálculo existente excepto los gráficos.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

El siguiente código carga solo los datos de la celda (junto con las fórmulas) y el formato de una hoja de cálculo existente.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.CELL_DATA);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}
### **Enumeración FileFormatType.OTS añadida**
Aspose.Cells 16.12.0 agregó la entrada OTS a la enumeración FileFormatType para detectar el formato de los archivos OTS.

El siguiente fragmento hace uso de FileFormatType.OTS.

**Java**

{{< highlight "csharp" >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **Se agregó la propiedad BuiltInDocumentPropertyCollection.ScaleCrop**
Aspose.Cells 16.12.0 agregó la propiedad ScaleCrop a la clase BuiltInDocumentPropertyCollection. ScaleCrop indica el modo de visualización de la miniatura del documento. Establecer este elemento en verdadero habilita la escala de la miniatura del documento según la visualización, mientras que establecerlo en falso permite recortar la miniatura del documento para mostrar la sección que se ajusta a la visualización.
### **Se agregó la propiedad BuiltInDocumentPropertyCollection.LinksUpToDate**
 Aspose.Cells 16.12.0 también expuso la propiedad LinksUpToDate para la clase BuiltInDocumentPropertyCollection. La propiedad LinksUpToDate indica si los hipervínculos de un documento están actualizados.
### **Método Workbook.exportXml agregado**
Aspose.Cells 16.12.0 ha expuesto el método Workbook.exportXml que permite almacenar los datos del mapa XML en la ruta de archivo especificada. El método Workbook.exportXml acepta 2 parámetros donde el primer parámetro de tipo cadena debe ser el nombre del mapa XML y el segundo parámetro debe ser la ubicación de la ruta del archivo para almacenar los datos XML.
### **Se agregó el método WorksheetCollection.createRange**
Aspose.Cells 16.12.0 ha agregado el método WorksheetCollection.createRange que permite crear un rango basado en una dirección (referencia de área de celda) y el índice de la hoja de trabajo.

El siguiente fragmento utiliza el método WorksheetCollection.createRange para crear un rango de celdas que se extiende de A1 a A2 en la primera hoja de trabajo (predeterminada).

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

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
### **Método Title.getCharacters eliminado**
Utilice el método Título.caracteres en su lugar.
