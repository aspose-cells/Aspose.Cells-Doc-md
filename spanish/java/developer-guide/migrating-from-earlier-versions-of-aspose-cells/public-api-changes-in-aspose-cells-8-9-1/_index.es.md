---
title: Cambios en la API Pública en Aspose.Cells 8.9.1
type: docs
weight: 320
url: /es/java/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.9.0 a la 8.9.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos métodos públicos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Fuentes de Fuente Configurables**
Aspose.Cells for Java ha expuesto numerosas clases para proporcionar el soporte para fuentes configurables para renderizar hojas de cálculo. Aquí está la lista de clases que se han agregado con Aspose.Cells for Java 8.9.1.

1. La clase FontConfigs especifica la configuración de fuentes.
1. La clase FontSourceBase es una clase base abstracta para las clases que permiten al usuario especificar varias fuentes.
1. La clase FileFontSource representa el archivo de fuente TrueType único almacenado en el sistema de archivos.
1. La clase FolderFontSource representa la carpeta que contiene archivos de fuente TrueType.
1. La clase MemoryFontSource representa el archivo de fuente TrueType único almacenado en memoria.
1. La enumeración FontSourceType especifica el tipo de fuente.

Con los cambios mencionados anteriormente, el Aspose.Cells for Java permite establecer las fuentes como se detalla a continuación.

1. Establecer una carpeta de fuente personalizada mientras se utiliza el método FontConfigs.setFontFolder.
1. Establecer varias carpetas de fuente personalizada mientras se utiliza el método FontConfigs.setFontFolders.
1. Establecer fuentes desde una carpeta de fuente personalizada, un solo archivo de fuente o datos de fuente de una matriz de bytes mientras se utiliza el método FontConfigs.setFontSources.

Aquí hay un escenario de uso simple de los mencionados métodos.

**Java**

{{< highlight csharp >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[] { fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[] bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Both FontConfigs.setFontFolder & FontConfigs.setFontFolders methods aceptan un segundo parámetro de tipo Booleano. Pasar true como segundo parámetro dirigirá a las APIs de Aspose.Cells a buscar los subdirectorios para los archivos de fuentes. 

{{% /alert %}} 

Aspose.Cells for Java también permite configurar la sustitución de fuentes. Este mecanismo es útil cuando una fuente requerida no está disponible en la máquina donde debe tener lugar la conversión. Los usuarios pueden proporcionar una lista de nombres de fuentes como alternativa a la fuente originalmente requerida. Para lograr esto, las APIs de Aspose.Cells han expuesto el método FontConfigs.setFontSubstitutes que acepta 2 parámetros. El primer parámetro es de tipo cadena, que debería ser el nombre de la fuente que se necesita sustituir. El segundo parámetro es una matriz de tipo cadena. Los usuarios pueden brindar una lista de nombres de fuentes como substitución al nombre de fuente original (especificado en el primer parámetro).

Aquí hay un escenario de uso simple del método FontConfigs.SetFontSubstitutes.

**Java**

{{< highlight csharp >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

El Aspose.Cells for Java también ha proporcionado medios para recopilar información sobre qué fuentes y sustituciones se han establecido.

1. El método FontConfigs.getFontSources devuelve una matriz de tipo FontSourceBase que contiene la lista de fuentes especificadas. En caso de que no se hayan establecido fuentes, el método FontConfigs.getFontSources devolverá una matriz vacía.
1. El método FontConfigs.getFontSubstitutes acepta un parámetro de tipo cadena permitiendo especificar el nombre de la fuente para la cual se ha establecido una sustitución. En caso de que no se haya establecido una sustitución para el nombre de fuente especificado, entonces el método FontConfigs.getFontSubstitutes devolverá nulo.

{{% alert color="primary" %}} 

Para obtener más detalles sobre FontConfigs, revise el artículo sobre [Configuración de fuentes para renderizar hojas de cálculo](/cells/es/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Se agregó la interfaz IFilePathProvider & la propiedad HtmlSaveOptions.FilePathProvider**
Aspose.Cells for Java 8.9.1 permite obtener/configurar la IFilePathProvider para exportar hojas de cálculo a archivos HTML separados. Estas nuevas API son útiles en escenarios donde los hipervínculos en una hoja apuntan a una ubicación en otra hoja, y los requisitos de la aplicación son renderizar cada hoja a un archivo HTML separado. Implementar la IFilePathProvider permite mantener los hipervínculos mencionados independientemente de si apuntan a una ubicación en un archivo HTML resultado separado.

A continuación se muestra un escenario de uso simple de la propiedad HtmlSaveOptions.FilePathProvider.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save each Worksheet to separate  HTML file

for (int i = 0; i < book.getWorksheets().getCount(); i++)

{

	book.getWorksheets().setActiveSheetIndex(i);

	//Create an instance of HtmlSaveOptions & set FilePathProvider property

	HtmlSaveOptions options = new HtmlSaveOptions();

	options.setExportActiveWorksheetOnly(true);

	options.setFilePathProvider(new IFilePathProvider() 

	{ 

		public String getFullName(String sheetName)

		{

		    if ("Sheet2".equals(sheetName))

		    {

		        return "sheet1.html";

		    }

		    else if ("Sheet3".equals(sheetName))

		    {

		        return "sheet2.html";

		    }



		    return "";

		}

	});



	 //Write HTML file to disc

	 book.save(dir + "sheet"+ i +".html", options);

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Para más detalles sobre esta mejora, revise el artículo sobre [Implementar la interfaz IFilePathProvider](/cells/es/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Se añadió la propiedad CopyOptions.ReferToDestinationSheet & Sobrecarga para el método Cells.copyRows**
La API Aspose.Cells for Java ha expuesto la propiedad CopyOptions.ReferToDestinationSheet de tipo Boolean junto con una sobrecarga del método Cells.copyRows para facilitar la operación de copiar filas cuando las filas a copiar también contienen un gráfico y su fuente de datos. Los desarrolladores pueden hacer uso de estas nuevas API para apuntar la fuente de datos del gráfico a las hojas de origen o destino.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet containing the chart & its data source

Worksheet source = book.getWorksheets().get(0);

//Add a new worksheet to the collection

Worksheet destination = book.getWorksheets().get(book.getWorksheets().add());

//Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.setReferToDestinationSheet(true);

//Copy the rows

destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Para más detalles sobre esta funcionalidad, revise el artículo sobre [Controlar la fuente de datos del gráfico al copiar filas](/cells/es/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Se añadió la propiedad CalculationOptions.Recursive**
Aspose.Cells for Java 8.9.1 ha expuesto la propiedad CalculationOptions.Recursive de tipo Boolean. Establecer la propiedad CalculationOptions.Recursive en true y pasar el objeto al método Workbook.calculateFormula dirige a las API de Aspose.Cells a calcular las celdas dependientes de forma recursiva al calcular celdas que dependen de otras celdas.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

Para más detalles sobre esta funcionalidad, revise el artículo sobre [Optimizar el tiempo de cálculo](/cells/es/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **APIs obsoletas**
### **Propiedad CellsHelper.FontDir Obsoleta**
Se recomienda utilizar el método FontConfigs.setFontFolder(String, boolean) con recursividad de carpeta en falso en su lugar.
### **Propiedad CellsHelper.FontDirs Obsoleta**
Utilice el método FontConfigs.setFontFolders(String[], boolean) con la propiedad folder recursive en false en su lugar.
### **Propiedad CellsHelper.FontFiles obsoleta**
Utilice el método FontConfigs.setFontSources(FontSourceBase[]) en su lugar.
