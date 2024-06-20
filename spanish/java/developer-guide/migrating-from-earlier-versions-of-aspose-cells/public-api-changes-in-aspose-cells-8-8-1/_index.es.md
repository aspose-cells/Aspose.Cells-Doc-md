---
title: Cambios en la API Pública en Aspose.Cells 8.8.1
type: docs
weight: 280
url: /es/java/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.8.0 hasta la 8.8.1 que pueden interesar a los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases añadidas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escenas en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Filtrar los Datos para Cargar**
Aspose.Cells for Java 8.8.1 ha expuesto la enumeración LoadDataFilterOptions junto con la propiedad LoadOptions.LoadDataFilterOptions que puede ser utilizada para especificar el tipo de datos que se deben cargar al construir el libro de un archivo de plantilla. Filtrar los datos cargados puede mejorar el rendimiento para propósitos especiales, especialmente al usar las APIs de LightCells.

La enumeración LoadDataFilterOptions proporciona las siguientes selecciones.

1. TODO para cargar todo desde la hoja de cálculo.
1. NADA para no cargar nada desde la hoja de cálculo.
1. CELDA_EN_BLANCO carga las celdas cuyos valores están en blanco.
1. CELDA_BOOL carga celdas cuyos valores son booleanos.
1. CELDA_DATOS carga los datos de celdas incluyendo valores, fórmulas y formato.
1. CELDA_ERROR carga celdas cuyos valores son errores.
1. CELDA_NUMÉRICO carga celdas cuyos valores son numéricos (incluyendo Fecha y Hora).
1. CELL_STRING carga celdas cuyos valores son texto/cadena.
1. CELL_VALUE carga solo valores de celda (todos los tipos).
1. CHART carga solo gráficos.
1. CONDITIONAL_FORMATTING carga solo reglas de formato condicional.
1. DATA_VALIDATION carga solo reglas de validación de datos.
1. DOCUMENT_PROPERTIES carga solo propiedades del documento.
1. FORMULA carga fórmulas, incluidos nombres definidos.
1. MERGED_AREA carga solo celdas fusionadas.
1. PIVOT_TABLE carga tablas dinámicas.
1. SETTINGS carga solo configuraciones de Libro y Hoja de cálculo.
1. SHAPE carga solo formas.
1. STYLE carga formato de celdas.
1. TABLE carga tablas de Excel/Objetos de lista.

{{% alert color="primary" %}} 

Para más detalles sobre esta característica, revise el artículo detallado en [Filtrar Datos para Cargar](/cells/es/java/filtrar-el-tipo-de-datos-al-cargar-el-libro-desde-el-archivo-de-plantilla/).

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Convertir directamente el gráfico a PDF**
Las API de Aspose.Cells ya han proporcionado la facilidad de renderizar gráficos a PDF mientras se usa el método Chart.toPdf. Con este lanzamiento, la API ha expuesto otra versión sobrecargada de dicho método que podría aceptar una instancia de OutputStream, permitiendo a los usuarios guardar el PDF del gráfico en una instancia de ByteArrayOutputStream.

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

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
### **Añadida la propiedad WorkbookSettings.PaperSize**
Aspose.Cells for Java 8.8.1 ha expuesto la propiedad WorkbookSettings.PaperSize para establecer el tamaño de papel de impresión predeterminado para toda la hoja de cálculo. La propiedad WorkbookSettings.PaperSize acepta un valor de la enumeración PaperSizeType que contiene los tamaños predefinidos para los tipos de papel de impresión más utilizados.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Añadida la propiedad Shape.TextBody**
Esta versión de la API Aspose.Cells for Java ha expuesto la propiedad Shape.TextBody para manipular los aspectos del texto en formas. El siguiente fragmento de código utiliza dicha propiedad para establecer el efecto de sombra del texto en un cuadro de texto.

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta característica, consulte el artículo detallado sobre [Configuración del efecto de sombra para texto](/cells/es/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet of the Workbook

Worksheet sheet = book.getWorksheets().get(0);

//Add a TextBox to the ShapeCollection

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

//Set the text of the TextBox

textBox.setText("This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

//Set shadow effect for text

for (int i = 0; i < textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Añadido el método Worksheet.calculateFormula(string formula, CalculationOptions opts)**
Aspose.Cells for Java 8.8.1 ha expuesto otra sobrecarga para el método Worksheet.calculateFormula que proporciona la capacidad de calcular una fórmula dada directamente con opciones personalizadas.

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta característica, consulte el artículo detallado sobre [Cálculo directo de función personalizada](/cells/es/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Añadido el método GridCell.createValidation**
Aspose.Cells.GridWeb ha proporcionado la capacidad de agregar directamente la regla de validación a una celda individual mediante el método GridCell.createValidation. Dicho método requiere 2 parámetros. El primero es del tipo GridValidationType que determina el tipo de validación, mientras que el segundo parámetro (isRequied) es del tipo Boolean.

**Java**

{{< highlight csharp >}}

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
### **Añadido el método GridCell.removeValidation**
Aspose.Cells.GridWeb también ha proporcionado la capacidad de eliminar la regla de validación de datos de una GridCell mediante el método GridCell.removeValidation.
## **APIs obsoletas**
### **Propiedad Shape.TextFrame obsoleta**
Se recomienda utilizar la propiedad Shape.TextBody.TextAlignment en su lugar.
