---
title: Público API Cambios en Aspose.Cells 8.9.1
type: docs
weight: 320
url: /es/java/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.9.0 a la 8.9.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Fuentes de fuentes configurables**
Aspose.Cells for Java ha expuesto una serie de clases para proporcionar soporte para fuentes de fuentes configurables para la representación de hojas de cálculo. Aquí está la lista de clases que se han agregado con Aspose.Cells for Java 8.9.1.

1. La clase FontConfigs especifica la configuración de la fuente.
1. La clase FontSourceBase es una clase base abstracta para las clases que permiten al usuario especificar varias fuentes de fuentes.
1. La clase FileFontSource representa el único archivo de fuente TrueType almacenado en el sistema de archivos.
1. La clase FolderFontSource representa la carpeta que contiene archivos de fuentes TrueType.
1. La clase MemoryFontSource representa el único archivo de fuente TrueType almacenado en la memoria.
1. La enumeración FontSourceType especifica el tipo de una fuente de fuente.

Con los cambios mencionados anteriormente, el Aspose.Cells for Java permite configurar las fuentes como se detalla a continuación.

1. Configure una carpeta de fuentes personalizada mientras usa el método FontConfigs.setFontFolder.
1. Establezca varias carpetas de fuentes personalizadas mientras usa el método FontConfigs.setFontFolders.
1. Establezca las fuentes de fuentes desde una carpeta de fuentes personalizada, un solo archivo de fuentes o datos de fuentes desde una matriz de bytes mientras usa el método FontConfigs.setFontSources.

Aquí hay un escenario de uso simple de los métodos antes mencionados.

**Java**

{{< highlight "csharp" >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[]{ fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[]bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

 Ambos métodos FontConfigs.setFontFolder y FontConfigs.setFontFolders aceptan un segundo parámetro de tipo booleano. Pasar verdadero como segundo parámetro dirigirá a las API Aspose.Cells para buscar las subcarpetas de los archivos de fuentes.

{{% /alert %}} 

Aspose.Cells for Java también permite configurar la sustitución de fuentes. Este mecanismo es útil cuando una fuente requerida no está disponible en la máquina donde se debe realizar la conversión. Los usuarios pueden proporcionar una lista de nombres de fuentes como alternativa a la fuente requerida originalmente. Para lograr esto, las API Aspose.Cells han expuesto el método FontConfigs.setFontSubstitutes que acepta 2 parámetros. El primer parámetro es de tipo cadena, que debe ser el nombre de la fuente que debe sustituirse. El segundo parámetro es una matriz de tipo cadena. Los usuarios pueden proporcionar una lista de nombres de fuentes como sustitución del nombre de fuente original (especificado en el primer parámetro).

Aquí hay un escenario de uso simple del método FontConfigs.SetFontSubstitutes.

**Java**

{{< highlight "csharp" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

El Aspose.Cells for Java también ha proporcionado medios para recopilar información sobre qué fuentes y sustituciones se han establecido.

1. El método FontConfigs.getFontSources devuelve una matriz de tipo FontSourceBase que contiene la lista de fuentes de fuentes especificadas. En caso de que no se hayan establecido fuentes, el método FontConfigs.getFontSources devolverá una matriz vacía.
1. El método FontConfigs.getFontSubstitutes acepta un parámetro de tipo cadena que permite especificar el nombre de la fuente para la que se ha establecido una sustitución. En caso de que no se haya establecido ninguna sustitución para el nombre de fuente especificado, el método FontConfigs.getFontSubstitutes devolverá un valor nulo.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre FontConfigs, consulte el artículo sobre[Configuración de fuentes para renderizar hojas de cálculo](/cells/es/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Se agregaron la interfaz IFilePathProvider y la propiedad HtmlSaveOptions.FilePathProvider**
Aspose.Cells for Java 8.9.1 permite obtener/establecer IFilePathProvider para exportar hojas de trabajo a archivos HTML separados. Estas nuevas API son útiles en escenarios donde los hipervínculos en una hoja de trabajo apuntan a una ubicación en otra hoja de trabajo, donde el requisito de la aplicación es representar cada hoja de trabajo en un archivo HTML separado. La implementación de IFilePathProvider permite mantener intactos los hipervínculos antes mencionados, independientemente del hecho de que apunten a una ubicación en un archivo HTML resultante separado.

El siguiente es el escenario de uso simple de la propiedad HtmlSaveOptions.FilePathProvider.

**Java**

{{< highlight "csharp" >}}

 //Cargar una hoja de cálculo en una instancia de Workbook

Libro de trabajo book = new Workbook(dir + "sample.xlsx");

//Guardar cada hoja de trabajo en un archivo HTML separado

 para (int i = 0; i< book.getWorksheets().getCount(); i++)

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

 Para obtener más detalles sobre esta mejora, consulte el artículo sobre[Implementación de la interfaz IFilePathProvider](/cells/es/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Se agregó la propiedad CopyOptions.ReferToDestinationSheet y la sobrecarga para el método Cells.copyRows**
Aspose.Cells for Java API ha expuesto la propiedad de tipo booleano CopyOptions.ReferToDestinationSheet junto con una sobrecarga del método Cells.copyRows para facilitar la operación de copia de filas cuando las filas que se copiarán también contienen un gráfico y su fuente de datos. Los desarrolladores pueden hacer uso de estas nuevas API para apuntar la fuente de datos del gráfico a las hojas de trabajo de origen o de destino.

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

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

 Para obtener más detalles sobre esta función, consulte el artículo sobre[Controle la fuente de datos del gráfico mientras copia filas](/cells/es/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Se agregó CalculationOptions. Propiedad recursiva**
Aspose.Cells for Java 8.9.1 ha expuesto el tipo booleano CalculationOptions.Recursive propiedad. Establecer la propiedad CalculationOptions.Recursive en true y pasar el objeto al método Workbook.calculateFormula dirige a las API Aspose.Cells para calcular las celdas dependientes de forma recursiva al calcular celdas que dependen de otras celdas.

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo sobre[Optimizar el tiempo de cálculo](/cells/es/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **API obsoletas**
### **Propiedad CellsHelper.FontDir obsoleta**
Se recomienda utilizar el método FontConfigs.setFontFolder(String, boolean) con carpeta recursiva a false en su lugar.
### **Propiedad CellsHelper.FontDirs obsoleta**
Use el método FontConfigs.setFontFolders(String[], boolean) con carpeta recursiva a false en su lugar.
### **Propiedad CellsHelper.FontFiles obsoleta**
Utilice el método FontConfigs.setFontSources(FontSourceBase[]) en su lugar.
