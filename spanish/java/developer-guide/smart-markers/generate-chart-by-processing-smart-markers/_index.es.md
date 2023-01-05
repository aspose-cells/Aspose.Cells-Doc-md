---
title: Generar gráfico procesando marcadores inteligentes
type: docs
weight: 180
url: /es/java/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}} 

Aspose.Cells Las API brindan la clase WorkbookDesigner para trabajar con Smart Markers donde el formato y las fórmulas se colocan en las hojas de cálculo del diseñador y luego se procesan en fuentes de datos específicas para completar los datos de acuerdo con los Smart Markers. También es posible crear gráficos de Excel mediante el procesamiento de marcadores inteligentes, que requerirán los siguientes pasos.

- Creación de hoja de cálculo de diseñador.
- Hoja de cálculo del diseñador de procesamiento contra la fuente de datos especificada
- Creación de gráfico basado en datos poblados

{{% /alert %}} 
## **Creación de la hoja de cálculo del diseñador**
Una hoja de cálculo de diseñador es un archivo de Excel simple creado con la aplicación de Excel Microsoft o las API Aspose.Cells que contiene el formato visual, las fórmulas y los marcadores inteligentes, donde los contenidos se completarán en tiempo de ejecución.

{{% alert color="primary" %}} 

 La información detallada sobre los marcadores inteligentes está disponible[aquí](/cells/es/java/smart-markers/).

{{% /alert %}} 

En aras de la simplicidad, crearemos la hoja de cálculo del diseñador usando Aspose.Cells for Java API, y luego la procesaremos contra una fuente de datos creada dinámicamente con fines de demostración.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access the first (default) Worksheet from the collection

Worksheet dataSheet = book.getWorksheets().get(0);

//Name the first Worksheet for referencing

dataSheet.setName("ChartData");

//Access the CellsCollection of ChartData Worksheet

Cells cells = dataSheet.getCells();

//Place the markers in the Worksheet according to desired layout

cells.get("A1").putValue("&=$Headers(horizontal)");

cells.get("A2").putValue("&=$Year2000(horizontal)");

cells.get("A3").putValue("&=$Year2005(horizontal)");

cells.get("A4").putValue("&=$Year2010(horizontal)");

cells.get("A5").putValue("&=$Year2015(horizontal)");

{{< /highlight >}}

Si guarda la hoja de cálculo resultante en esta etapa, los datos en la hoja de trabajo se verán de la siguiente manera.

![todo:imagen_alternativa_texto](generate-chart-by-processing-smart-markers_1.png)
## **Hoja de cálculo del diseñador de procesamiento**
 Para procesar la hoja de cálculo del diseñador, debemos tener una fuente de datos que corresponda a los marcadores inteligentes utilizados en la hoja de cálculo del diseñador. Por ejemplo, hemos creado una entrada de marcador inteligente como**&=$Encabezados(horizontales)** que representa la variable por nombre Encabezados mientras que la clave**(horizontal)** sugiere que los datos se llenen horizontalmente.

Para demostrar este caso de uso, crearemos la fuente de datos desde cero y la procesaremos contra la hoja de cálculo del diseñador creada en el paso anterior. Sin embargo, en un escenario en tiempo real, los datos ya podrían estar disponibles para su posterior procesamiento, por lo que puede omitir la creación de la fuente de datos si los datos ya están disponibles.

**Java**

{{< highlight "csharp" >}}

 //Create string arrays which will serve as data sources to the smart markers

String[]headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[]year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[]year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[]year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[]year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

El procesamiento de Smart Markers es bastante simple como sigue.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner();

//Set the Workbook property for the instance of WorkbookDesigner

designer.setWorkbook(book);

//Set data sources for smart markers

designer.setDataSource("Headers", headers);

designer.setDataSource("Year2000", year2000);

designer.setDataSource("Year2005", year2005);

designer.setDataSource("Year2010", year2010);

designer.setDataSource("Year2015", year2015);

//Process the designer spreadsheet against the provided data sources

designer.process();

{{< /highlight >}}

Si guarda la hoja de cálculo en esta etapa, los datos se verán de la siguiente manera.

![todo:imagen_alternativa_texto](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

El fragmento de código anterior utiliza la instancia existente de la clase Workbook creada en el primer paso. Si ya tiene el archivo de hoja de cálculo del diseñador en el disco o en la memoria, puede crear una instancia de la clase Workbook cargando la hoja de cálculo del diseñador existente.

{{% /alert %}} 
## **Creación de gráfico**
Una vez que los datos están en su lugar, todo lo que tenemos que hacer es crear un gráfico basado en la fuente de datos. Para simplificar el ejemplo, usaremos el método Chart.setChartDataRange para que no tengamos que configurar más el gráfico.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





El gráfico final se ve como sigue.

![todo:imagen_alternativa_texto](generate-chart-by-processing-smart-markers_3.png)
