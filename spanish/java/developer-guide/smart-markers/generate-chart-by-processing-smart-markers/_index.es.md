---
title: Generar gráfico mediante el procesamiento de marcadores inteligentes
type: docs
weight: 180
url: /es/java/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}} 

Las API de Aspose.Cells proporcionan la clase WorkbookDesigner para trabajar con los marcadores inteligentes, donde el formato y las fórmulas se colocan en las hojas de cálculo del diseñador y luego se procesan con las fuentes de datos especificadas para completar los datos de acuerdo con los marcadores inteligentes. También es posible crear gráficos de Excel mediante el procesamiento de los marcadores inteligentes, lo que requerirá los siguientes pasos.

- Creación de hoja de cálculo de diseñador
- Procesamiento de hojas de cálculo del diseñador con fuentes de datos especificadas
- Creación de gráfico basada en datos poblados

{{% /alert %}} 
## **Creación de hoja de cálculo del diseñador**
Una hoja de cálculo del diseñador es un archivo de Excel simple creado con la aplicación Microsoft Excel o las API de Aspose.Cells que contiene el formato visual, las fórmulas y los marcadores inteligentes, cuyos contenidos se deben poblar en tiempo de ejecución.

{{% alert color="primary" %}} 

Información detallada sobre los marcadores inteligentes está disponible [aquí](/cells/es/java/smart-markers/).

{{% /alert %}} 

Por simplicidad, crearemos la hoja de cálculo del diseñador utilizando la API Aspose.Cells for Java, y luego la procesaremos con una fuente de datos creada dinámicamente con fines de demostración.

**Java**

{{< highlight csharp >}}

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

Si guarda la hoja de cálculo resultante en esta etapa, los datos en la hoja de cálculo se verán como sigue.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_1.png)
## **Procesamiento de hoja de cálculo del diseñador**
Para procesar la hoja de cálculo del diseñador, debemos tener una fuente de datos que corresponda a los marcadores inteligentes utilizados en la hoja de cálculo del diseñador. Por ejemplo, hemos creado una entrada de marcador inteligente como **&=$Headers(horizontal)**, que representa la variable por nombre Headers, mientras que la clave **(horizontal)** sugiere que los datos deben ser poblados horizontalmente.

Para demostrar este caso de uso, crearemos la fuente de datos desde cero y la procesaremos con la hoja de cálculo del diseñador creada en el paso anterior. Sin embargo, en un escenario en tiempo real, los datos podrían estar disponibles para su procesamiento posterior, por lo que puede omitir la creación de la fuente de datos si los datos ya están disponibles.

**Java**

{{< highlight csharp >}}

 //Create string arrays which will serve as data sources to the smart markers

String[] headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[] year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[] year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[] year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[] year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

El procesamiento de los marcadores inteligentes es bastante simple como sigue.

**Java**

{{< highlight csharp >}}

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

Si guarda la hoja de cálculo en esta etapa, los datos se verán como sigue.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

El fragmento de código anterior utiliza la instancia existente de la clase Workbook creada en el primer paso. Si ya tiene el archivo de hoja de cálculo del diseñador en disco o en memoria, puede crear una instancia de la clase Workbook cargando el archivo de hoja de cálculo del diseñador existente.

{{% /alert %}} 
## **Creación de gráfico**
Una vez que los datos estén en su lugar, todo lo que necesitamos hacer es crear un gráfico en función de la fuente de datos. Para mantener el ejemplo simple, utilizaremos el método Chart.setChartDataRange para que no tengamos que configurar el gráfico posteriormente.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





El gráfico final se verá como sigue.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_3.png)
{{< app/cells/assistant language="java" >}}
