---
title: Cambios en la API pública en Aspose.Cells 16.12.0
type: docs
weight: 370
url: /es/java/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios realizados en la API de Aspose.Cells desde la versión 16.11.0 hasta la 16.12.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases añadidas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento interno en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Objetos de filtro en el momento de carga**
Aspose.Cells 16.12.0 ha expuesto la clase LoadFilter junto con la propiedad LoadOptions.LoadFilter que juntas pueden controlar el tipo de datos a cargar al inicializar una instancia de Workbook desde un archivo de plantilla.

A continuación se muestra un escenario de uso simple para cargar solo las propiedades del documento desde un archivo de plantilla.

**Java**

{{< highlight csharp >}}

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

El siguiente fragmento carga todo, excepto los gráficos, de una hoja de cálculo existente.

**Java**

{{< highlight csharp >}}

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

El siguiente código carga solo los datos de celda (junto con fórmulas) y el formato de una hoja de cálculo existente.

**Java**

{{< highlight csharp >}}

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
### **Añadida la enumeración FileFormatType.OTS**
Aspose.Cells 16.12.0 ha agregado la entrada OTS a la enumeración FileFormatType para detectar el formato de archivos OTS.

El siguiente fragmento hace uso de FileFormatType.OTS.

**Java**

{{< highlight csharp >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **Añadida la propiedad ScaleCrop de BuiltInDocumentPropertyCollection**
Aspose.Cells 16.12.0 ha añadido la propiedad ScaleCrop a la clase BuiltInDocumentPropertyCollection. ScaleCrop indica el modo de visualización de la miniatura del documento. Establecer este elemento en true habilita el escalamiento de la miniatura del documento según la visualización, mientras que establecerlo en false habilita el recorte de la miniatura del documento para mostrar la sección que se ajusta a la visualización.
### **Añadida la propiedad LinksUpToDate de BuiltInDocumentPropertyCollection**
Aspose.Cells 16.12.0 también ha expuesto la propiedad LinksUpToDate para la clase BuiltInDocumentPropertyCollection. Esta propiedad indica si los hipervínculos en un documento están actualizados. 
### **Añadido el método Workbook.exportXml**
Aspose.Cells 16.12.0 ha expuesto el método Workbook.exportXml que permite almacenar los datos del mapa XML en la ruta de archivo especificada. El método Workbook.exportXml acepta 2 parámetros donde el primer parámetro de tipo string debe ser el nombre del mapa XML y el segundo parámetro debe ser la ubicación de la ruta de archivo para almacenar los datos XML.
### **Agregado el Método WorksheetCollection.createRange**
Aspose.Cells 16.12.0 ha añadido el método WorksheetCollection.createRange que permite crear un rango basado en una dirección (referencia de área de celdas) e índice de la Hoja de cálculo.

El siguiente fragmento utiliza el método WorksheetCollection.createRange para crear un rango de celdas que abarca desde A1 hasta A2 en la primera hoja de cálculo (por defecto).

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

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
### **Método getTitle.getCharacters eliminado**
Por favor, utilice el método Title.characters en su lugar.
