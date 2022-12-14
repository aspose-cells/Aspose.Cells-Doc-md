---
title: Público API Cambios en Aspose.Cells 8.8.1
type: docs
weight: 280
url: /es/java/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.8.0 a la 8.8.1 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Filtrar los datos para cargar**
Aspose.Cells for Java 8.8.1 ha expuesto la enumeración LoadDataFilterOptions junto con la propiedad LoadOptions.LoadDataFilterOptions que se puede usar para especificar el tipo de datos que se debe cargar al crear el libro de trabajo a partir de un archivo de plantilla. Filtrar los datos cargados puede mejorar el rendimiento para propósitos especiales, especialmente cuando se usan las API de LightCells.

La enumeración LoadDataFilterOptions proporciona las siguientes selecciones.

1. ALL para cargar todo desde la hoja de cálculo.
1. NONE para cargar nada desde la hoja de cálculo.
1. CELL_BLANK carga las celdas cuyos valores están en blanco.
1. CELL_BOOL carga celdas cuyos valores son booleanos.
1. CELL_DATA carga datos de celdas, incluidos valores, fórmulas y formato.
1. CELL_ERROR carga celdas cuyos valores son erróneos.
1. CELL_NUMERIC carga celdas cuyos valores son numéricos (incluyendo fecha y hora).
1. CELL_STRING carga celdas cuyos valores son texto/cadena.
1. CELL_VALUE carga solo valores de celda (todos los tipos).
1. CHART carga solo gráficos.
1. CONDITIONAL_FORMATTING solo carga reglas de formato condicional.
1. DATA_VALIDATION solo carga reglas de validación de datos.
1. DOCUMENT_PROPERTIES carga solo las propiedades del documento.
1. FORMULA carga fórmulas que incluyen nombres definidos.
1. MERGED_AREA carga solo celdas combinadas.
1. PIVOT_TABLE carga tablas dinámicas.
1. CONFIGURACIÓN carga solo la configuración del libro y la hoja de trabajo.
1. SHAPE carga solo formas.
1. STYLE carga el formato de las celdas.
1. TABLE carga tablas de Excel/Lista de objetos.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Filtrar datos para cargar](/cells/es/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Convertir directamente el gráfico a PDF**
Aspose.Cells Las API ya han brindado la posibilidad de representar gráficos en PDF mientras se usa el método Chart.toPdf. Con este lanzamiento, el API ha expuesto otra versión sobrecargada de dicho método que podría aceptar una instancia de OutputStream, lo que permite a los usuarios guardar el PDF del gráfico en una instancia de ByteArrayOutputStream.

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

Workbook workbook = new Workbook(filePath);

//Access first worksheet containing a chart

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart from the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart to PDF as Stream

ByteArrayOutputStream outStream = new ByteArrayOutputStream();

chart.toPdf(outStream);

{{< /highlight >}}
### **Se agregó la propiedad WorkbookSettings.PaperSize**
Aspose.Cells for Java 8.8.1 ha expuesto la propiedad WorkbookSettings.PaperSize para establecer el tamaño de papel de impresión predeterminado para toda la hoja de cálculo. La propiedad WorkbookSettings.PaperSize acepta un valor de la enumeración PaperSizeType que contiene los tamaños predefinidos para los tipos de papel de impresión más utilizados.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Se agregó la propiedad Shape.TextBody**
Esta versión de Aspose.Cells for Java API ha expuesto Shape.TextBody para manipular los aspectos del texto en formas. El siguiente fragmento usa dicha propiedad para establecer el efecto de sombra del texto en un cuadro de texto.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Configuración del efecto de sombra para el texto](/cells/es/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Crear una instancia de Workbook

Libro de trabajo libro = nuevo libro de trabajo ();

// Acceder a la primera hoja de trabajo del Libro de trabajo

hoja de trabajo = book.getWorksheets().get(0);

//Añadir un TextBox a la ShapeCollection

índice int = hoja.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = hoja.getTextBoxes().get(index);

//Establecer el texto del cuadro de texto

textBox.setText("Este texto tiene la siguiente configuración.\n\nEfectos de texto > Sombra > Compensación inferior");

//Establecer efecto de sombra para el texto

 para (int i = 0; i< textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Se agregó el método Worksheet.calculateFormula (fórmula de cadena, Opciones de cálculo)**
Aspose.Cells for Java 8.8.1 ha expuesto otra sobrecarga para el método Worksheet.calculateFormula que brinda la capacidad de calcular una fórmula determinada directamente con opciones personalizadas.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Cálculo directo de la función personalizada](/cells/es/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Se agregó el método GridCell.createValidation**
Aspose.Cells.GridWeb ha brindado la capacidad de agregar directamente la regla de validación a una sola celda mientras se usa el método GridCell.createValidation. Dicho método requiere 2 parámetros. El primero es de tipo GridValidationType que determina el tipo de validación, mientras que el segundo parámetro (isRequied) es de tipo booleano.

**Java**

{{< highlight "csharp" >}}

 //Access first worksheet

GridWorksheet sheet = gridweb.getWorkSheets().get(0);

//Access cell B3

GridCell cell = sheet.getCells().get("B3");

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.createValidation(GridValidationType.WHOLE_NUMBER, true);

val.setFormula1("=20");

val.setFormula2("=40");

val.setOperator(OperatorType.BETWEEN);

val.setShowError(true);

val.setShowInput(true);

{{< /highlight >}}
### **Se agregó el método GridCell.removeValidation**
Aspose.Cells.GridWeb también ha brindado la capacidad de eliminar la regla de validación de datos de GridCell mientras se usa el método GridCell.removeValidation.
## **API obsoletas**
### **Propiedad Shape.TextFrame obsoleta**
Se recomienda utilizar la propiedad Shape.TextBody.TextAlignment en su lugar.
