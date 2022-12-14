---
title: Público API Cambios en Aspose.Cells 8.9.1
type: docs
weight: 310
url: /es/net/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.9.0 a la 8.9.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Fuentes de fuentes configurables**
Aspose.Cells for .NET ha expuesto una serie de clases para proporcionar soporte para fuentes de fuentes configurables para la representación de hojas de cálculo. Aquí está la lista de clases que se han agregado con Aspose.Cells for .NET 8.9.1.

1. La clase FontConfigs especifica la configuración de la fuente.
1. La clase FontSourceBase es una clase base abstracta para las clases que permiten al usuario especificar varias fuentes de fuentes.
1. La clase FileFontSource representa el único archivo de fuente TrueType almacenado en el sistema de archivos.
1. La clase FolderFontSource representa la carpeta que contiene archivos de fuentes TrueType.
1. La clase MemoryFontSource representa el único archivo de fuente TrueType almacenado en la memoria.
1. La enumeración FontSourceType especifica el tipo de una fuente de fuente.

Con los cambios mencionados anteriormente, el Aspose.Cells for .NET permite configurar las fuentes como se detalla a continuación.

1. Configure una carpeta de fuentes personalizada mientras usa el método FontConfigs.SetFontFolder.
1. Establezca varias carpetas de fuentes personalizadas mientras usa el método FontConfigs.SetFontFolders.
1. Establezca fuentes de fuente desde una carpeta de fuente personalizada, un solo archivo de fuente o datos de fuente desde una matriz de bytes mientras usa el método FontConfigs.SetFontSources.

Aquí hay un escenario de uso simple de los métodos antes mencionados.

**C#**

{{< highlight "csharp" >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[]{ fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Ambos métodos FontConfigs.SetFontFolder y FontConfigs.SetFontFolders aceptan un segundo parámetro de tipo booleano. Pasar verdadero como segundo parámetro dirigirá a las API Aspose.Cells para buscar las subcarpetas de los archivos de fuentes.

{{% /alert %}} 

Aspose.Cells for .NET también permite configurar la sustitución de fuentes. Este mecanismo es útil cuando una fuente requerida no está disponible en la máquina donde se debe realizar la conversión. Los usuarios pueden proporcionar una lista de nombres de fuentes como alternativa a la fuente requerida originalmente. Para lograr esto, las API Aspose.Cells han expuesto el método FontConfigs.SetFontSubstitutes que acepta 2 parámetros. El primer parámetro es de tipo cadena, que debe ser el nombre de la fuente que debe sustituirse. El segundo parámetro es una matriz de tipo cadena. Los usuarios pueden proporcionar una lista de nombres de fuentes como sustitución del nombre de fuente original (especificado en el primer parámetro).

Aquí hay un escenario de uso simple del método FontConfigs.SetFontSubstitutes.

**C#**

{{< highlight "csharp" >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}



El Aspose.Cells for .NET también ha proporcionado medios para recopilar información sobre qué fuentes y sustituciones se han establecido.

1. El método FontConfigs.GetFontSources devuelve una matriz de tipo FontSourceBase que contiene la lista de fuentes de fuentes especificadas. En caso de que no se hayan establecido fuentes, el método FontConfigs.GetFontSources devolverá una matriz vacía.
1. El método FontConfigs.GetFontSubstitutes acepta un parámetro de tipo cadena que permite especificar el nombre de la fuente para la que se ha establecido una sustitución. En caso de que no se haya establecido ninguna sustitución para el nombre de fuente especificado, el método FontConfigs.GetFontSubstitutes devolverá un valor nulo.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre FontConfigs, consulte el artículo sobre[Configuración de fuentes para renderizar hojas de cálculo](/cells/es/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Se agregaron la interfaz IFilePathProvider y la propiedad HtmlSaveOptions.FilePathProvider**
Aspose.Cells for .NET 8.9.1 permite obtener/establecer IFilePathProvider para exportar hojas de trabajo a archivos HTML separados. Estas nuevas API son útiles en escenarios donde los hipervínculos en una hoja de trabajo apuntan a una ubicación en otra hoja de trabajo, donde el requisito de la aplicación es representar cada hoja de trabajo en un archivo HTML separado. La implementación de IFilePathProvider permite mantener intactos los hipervínculos antes mencionados, independientemente del hecho de que apunten a una ubicación en un archivo HTML resultante separado.

El siguiente es el escenario de uso simple de la propiedad HtmlSaveOptions.FilePathProvider.

**C#**

{{< highlight "csharp" >}}

 // Cargar una hoja de cálculo en una instancia de Workbook

var libro = nuevo libro de trabajo (dir + "muestra.xlsx");

// Guarde cada hoja de trabajo en un archivo HTML separado

 para (int i = 0; i< book.Worksheets.Count; i++)

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

{{< highlight "csharp" >}}

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

 Para obtener más detalles sobre esta mejora, consulte el artículo sobre[Implementación de la interfaz IFilePathProvider](/cells/es/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Se agregó la propiedad CopyOptions.ReferToDestinationSheet y la sobrecarga para el método Cells.CopyRows**
Aspose.Cells for .NET API ha expuesto la propiedad de tipo booleano CopyOptions.ReferToDestinationSheet junto con una sobrecarga del método Cells.CopyRows para facilitar la operación de copia de filas cuando las filas que se van a copiar también contienen un gráfico y su fuente de datos. Los desarrolladores pueden hacer uso de estas nuevas API para apuntar la fuente de datos del gráfico a las hojas de trabajo de origen o de destino.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

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

 Para obtener más detalles sobre esta función, consulte el artículo sobre[Controle la fuente de datos del gráfico mientras copia filas](/cells/es/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Se agregó CalculationOptions. Propiedad recursiva**
Aspose.Cells for .NET 8.9.1 ha expuesto el tipo booleano CalculationOptions.Recursive propiedad. Establecer la propiedad CalculationOptions.Recursive en true y pasar el objeto al método Workbook.CalculateFormula dirige las API Aspose.Cells para calcular las celdas dependientes de forma recursiva al calcular celdas que dependen de otras celdas.

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo sobre[Optimizar el tiempo de cálculo](/cells/es/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **API obsoletas**
### **Propiedad CellsHelper.FontDir obsoleta**
Se recomienda utilizar el método FontConfigs.SetFontFolder(string, bool) con carpeta recursiva a false en su lugar.
### **Propiedad CellsHelper.FontDirs obsoleta**
Use el método FontConfigs.SetFontFolders(string[], bool) con carpeta recursiva a false en su lugar.
### **Propiedad CellsHelper.FontFiles obsoleta**
Utilice el método FontConfigs.SetFontSources(FontSourceBase[]) en su lugar.
