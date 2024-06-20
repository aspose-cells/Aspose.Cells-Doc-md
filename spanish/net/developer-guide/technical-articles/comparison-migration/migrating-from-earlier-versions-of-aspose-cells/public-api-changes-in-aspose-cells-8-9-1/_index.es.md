---
title: Cambios en la API Pública en Aspose.Cells 8.9.1
type: docs
weight: 310
url: /es/net/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.9.0 a la 8.9.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos métodos públicos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Fuentes de Fuente Configurables**
Aspose.Cells for .NET ha expuesto un número de clases para proporcionar soporte para fuentes de fuente configurables para la representación de hojas de cálculo. Aquí está la lista de clases que se han agregado con Aspose.Cells for .NET 8.9.1.

1. La clase FontConfigs especifica la configuración de fuentes.
1. La clase FontSourceBase es una clase base abstracta para las clases que permiten al usuario especificar varias fuentes.
1. La clase FileFontSource representa el archivo de fuente TrueType único almacenado en el sistema de archivos.
1. La clase FolderFontSource representa la carpeta que contiene archivos de fuente TrueType.
1. La clase MemoryFontSource representa el archivo de fuente TrueType único almacenado en memoria.
1. La enumeración FontSourceType especifica el tipo de fuente.

Con los cambios mencionados anteriormente, el Aspose.Cells for .NET permite configurar las fuentes de la siguiente manera.

1. Establecer una carpeta de fuente personalizada mientras se usa el método FontConfigs.SetFontFolder.
1. Establecer múltiples carpetas de fuentes personalizadas mientras se utiliza el método FontConfigs.SetFontFolders.
1. Establecer fuentes de una carpeta de fuentes personalizada, un solo archivo de fuente o datos de fuente de una matriz de bytes mientras se utiliza el método FontConfigs.SetFontSources.

Aquí hay un escenario de uso simple de los mencionados métodos.

**C#**

{{< highlight csharp >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[] { fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Tanto los métodos FontConfigs.SetFontFolder como FontConfigs.SetFontFolders aceptan un segundo parámetro de tipo Boolean. Pasar true como segundo parámetro dirigirá a las APIs de Aspose.Cells a buscar en las subcarpetas los archivos de fuentes.

{{% /alert %}} 

Aspose.Cells for .NET también permite configurar la sustitución de fuentes. Este mecanismo es útil cuando una fuente requerida no está disponible en la máquina donde debe realizarse la conversión. Los usuarios pueden proporcionar una lista de nombres de fuente como alternativa a la fuente originalmente requerida. Para lograr esto, las APIs de Aspose.Cells han expuesto el método FontConfigs.SetFontSubstitutes que acepta 2 parámetros. El primer parámetro es de tipo string, que debería ser el nombre de la fuente que debe ser sustituida. El segundo parámetro es una matriz de tipo string. Los usuarios pueden proporcionar una lista de nombres de fuente como sustitución del nombre de fuente original (especificado en el primer parámetro).

Aquí hay un escenario de uso simple del método FontConfigs.SetFontSubstitutes.

**C#**

{{< highlight csharp >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[] { "Times New Roman", "Calibri" });

{{< /highlight >}}



Aspose.Cells for .NET también ha proporcionado medios para recopilar información sobre qué fuentes y sustituciones se han establecido.

1. El método FontConfigs.GetFontSources devuelve una matriz de tipo FontSourceBase que contiene la lista de fuentes especificadas. En caso de que no se hayan establecido fuentes, el método FontConfigs.GetFontSources devolverá una matriz vacía.
1. El método FontConfigs.GetFontSubstitutes acepta un parámetro de tipo string que permite especificar el nombre de la fuente para la cual se ha establecido una sustitución. En caso de que no se haya establecido una sustitución para el nombre de fuente especificado, entonces el método FontConfigs.GetFontSubstitutes devolverá null.

{{% alert color="primary" %}} 

Para obtener más detalles sobre FontConfigs, por favor revise el artículo sobre [Configurar fuentes para renderizar hojas de cálculo](/cells/es/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Se agregó la interfaz IFilePathProvider & la propiedad HtmlSaveOptions.FilePathProvider**
Aspose.Cells for .NET 8.9.1 permite obtener/establecer el IFilePathProvider para exportar hojas de cálculo a archivos HTML separados. Estas nuevas APIs son útiles en escenarios donde los hipervínculos en una hoja de cálculo apuntan a una ubicación en otra hoja de cálculo, y donde el requisito de la aplicación es renderizar cada hoja de cálculo en un archivo HTML separado. Implementar el IFilePathProvider permite mantener los mencionados hipervínculos intactos independientemente de si apuntan a una ubicación en un archivo HTML resultante separado.

A continuación se muestra un escenario de uso simple de la propiedad HtmlSaveOptions.FilePathProvider.

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save each Worksheet to separate HTML file

for (int i = 0; i < book.Worksheets.Count; i++)

{

    book.Worksheets.ActiveSheetIndex = i;

    // Create an instance of HtmlSaveOptions & set FilePathProvider property

    var options = new HtmlSaveOptions

    {

        ExportActiveWorksheetOnly = true,

        FilePathProvider = new FilePathProvider()

    };

    // Write HTML file to disc

    book.Save(dir + string.Format(@"sheet{0}.html", i), options);

}

{{< /highlight >}}



Aquí se explica cómo implementar la interfaz IFilePathProvider.

**C#**

{{< highlight csharp >}}

 public class FilePathProvider : IFilePathProvider

{

    public FilePathProvider()

    {

    }

    /// <summary>

    /// Gets the full path of the file by Worksheet name when exporting Worksheet to html separately.

    /// So the references among the Worksheets can be exported correctly.

    /// </summary>

    /// <param name="sheetName">Worksheet name</param>

    /// <returns>the full path of the file</returns>

    public string GetFullName(string sheetName)

    {

        if ("Sheet2".Equals(sheetName))

        {

            return "sheet1.html";

        }

        else if ("Sheet3".Equals(sheetName))

        {

            return "sheet2.html";

        }

        return "";

    }

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Para más detalles sobre esta mejora, por favor revise el artículo sobre [Implementar la interfaz IFilePathProvider](/cells/es/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Agregada la propiedad CopyOptions.ReferToDestinationSheet y la sobrecarga para el método Cells.CopyRows**
Aspose.Cells for .NET API ha expuesto la propiedad CopyOptions.ReferToDestinationSheet de tipo Boolean junto con la sobrecarga del método Cells.CopyRows para facilitar la operación de copiar filas cuando las filas a copiar también contienen un gráfico y su origen de datos. Los desarrolladores pueden hacer uso de estas nuevas APIs para apuntar el origen de datos del gráfico a las hojas de cálculo de origen o destino.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet containing the chart & its data source

var source = book.Worksheets[0];

// Add a new worksheet to the collection

var destination = book.Worksheets[book.Worksheets.Add()];

// Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.ReferToDestinationSheet = true;

// Copy the rows

destination.Cells.CopyRows(source.Cells, 0, 0, source.Cells.MaxDisplayRange.RowCount, options);

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Para más detalles sobre esta característica, por favor revise el artículo sobre [Controlar el origen de datos del gráfico al copiar filas](/cells/es/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Se añadió la propiedad CalculationOptions.Recursive**
Aspose.Cells for .NET 8.9.1 ha expuesto la propiedad Booleana CalculationOptions.Recursive. Establecer la propiedad CalculationOptions.Recursive en true y pasar el objeto al método Workbook.CalculateFormula dirige a las APIs de Aspose.Cells a calcular las celdas dependientes de forma recursiva al calcular celdas que dependen de otras celdas.

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

Para más detalles sobre esta característica, por favor revise el artículo en [Optimizar el Tiempo de Cálculo](/cells/es/net/reducir-el-tiempo-de-cálculo-del-método-calculate-de-celdas/).

{{% /alert %}}
## **APIs obsoletas**
### **Propiedad CellsHelper.FontDir Obsoleta**
Se recomienda utilizar el método FontConfigs.SetFontFolder(string, bool) con recursividad de carpeta en falso en su lugar.
### **Propiedad CellsHelper.FontDirs Obsoleta**
Utilice el método FontConfigs.SetFontFolders(string[], bool) con recursividad de carpeta en falso en su lugar.
### **Propiedad CellsHelper.FontFiles obsoleta**
Utilice el método FontConfigs.SetFontSources(FontSourceBase[]) en su lugar.
