---
title: Usando LightCells API
type: docs
weight: 80
url: /es/java/using-lightcells-api/
---
{{% alert color="primary" %}}

A veces, necesita leer y escribir archivos grandes de Excel Microsoft con una gran lista de datos o contenidos en la hoja de trabajo. LightCells API es útil para crear enormes hojas de cálculo de Excel: con él, necesita memoria y obtiene un mejor rendimiento y eficiencia.

{{% /alert %}}

## **Arquitectura impulsada por eventos**

Aspose.Cells proporciona LightCells API, diseñado principalmente para manipular datos de celda uno por uno sin construir un bloque de modelo de datos completo (usando la colección Cell, etc.) en la memoria. Funciona en un modo controlado por eventos.

Para guardar libros de trabajo, proporcione el contenido de la celda celda por celda al guardar, y el componente lo guarda directamente en el archivo de salida.

Al leer archivos de plantilla, el componente analiza cada celda y proporciona su valor uno por uno.

En ambos procedimientos, se procesa un objeto Cell y luego se descarta, el objeto Workbook no contiene la colección. En este modo, por lo tanto, se ahorra memoria al importar y exportar Microsoft un archivo de Excel que tiene un gran conjunto de datos que, de lo contrario, usaría mucha memoria.

Aunque LightCells API procesa las celdas de la misma manera para los archivos XLSX y XLS (en realidad, no carga todas las celdas en la memoria sino que procesa una celda y luego la descarta), ahorra memoria de manera más efectiva para los archivos XLSX que para los archivos XLS debido a los diferentes modelos de datos y estructuras de los dos formatos.

 Sin embargo,**para archivos XLS** , para ahorrar más memoria, los desarrolladores pueden especificar una ubicación temporal para guardar los datos temporales generados durante el proceso Guardar. Comúnmente,**usar LightCells API para guardar el archivo XLSX puede ahorrar un 50% o más de memoria** que usar la forma común,**guardar XLS puede ahorrar entre un 20 y un 40 % de memoria**.

### **Escribir archivos grandes de Excel**

Aspose.Cells proporciona una interfaz, LightCellsDataProvider, que debe implementarse en su programa. La interfaz representa el proveedor de datos para guardar archivos de hojas de cálculo grandes en modo ligero.

Al guardar un libro de trabajo en este modo, startSheet (int) se verifica al guardar cada hoja de trabajo en el libro de trabajo. Para una hoja, si startSheet(int) es verdadero, esta implementación proporciona todos los datos y propiedades de las filas y celdas de esta hoja que se van a guardar. En primer lugar, se llama a nextRow() para obtener el índice de la siguiente fila que se guardará. Si se devuelve un índice de fila válido (el índice de fila debe estar en orden ascendente para que se guarden las filas), se proporciona un objeto Row que representa esta fila para que la implementación establezca sus propiedades mediante startRow(Row).

Para una fila, nextCell() se verifica primero. Si se devuelve un índice de columna válido (el índice de columna debe estar en orden ascendente para que se guarden todas las celdas de una fila), se proporciona un objeto Cell que representa esta celda para establecer los datos y las propiedades mediante startCell(Cell). Después de configurar los datos de esta celda, esta celda se guarda directamente en el archivo de hoja de cálculo generado y la siguiente celda se verificará y procesará.

El siguiente ejemplo muestra cómo funciona LightCells API.

El siguiente programa crea un archivo enorme con 100 000 registros en una hoja de trabajo, llena de datos. Hemos agregado algunos hipervínculos, valores de cadena, valores numéricos y también fórmulas a ciertas celdas en la hoja de trabajo. Además, también hemos formateado un rango de celdas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **Leer archivos grandes de Excel**

Aspose.Cells proporciona una interfaz, LightCellsDataHandler, que debe implementarse en su programa. La interfaz representa el proveedor de datos para leer grandes archivos de hojas de cálculo en un modo ligero.

Al leer un libro de trabajo en este modo, startSheet() se verifica al leer cada hoja de trabajo en el libro de trabajo. Para una hoja, si startSheet() devuelve verdadero, entonces todos los datos y propiedades de las celdas en las filas y columnas de la hoja se verifican y procesan. Para cada fila, se llama a startRow() para verificar si es necesario procesarla. Si es necesario procesar una fila, primero se leen las propiedades de la fila y los desarrolladores pueden acceder a sus propiedades con processRow().

Si las celdas de la fila también deben procesarse, entonces processRow() devuelve verdadero y se llama a startCell() para cada celda existente en la fila para verificar si es necesario procesarla. Si lo hace, se llama a processCell().

El siguiente código de ejemplo ilustra este proceso. El programa lee un archivo grande con millones de registros. Se necesita un poco de tiempo para leer cada hoja del libro de trabajo. El código de ejemplo lee el archivo y recupera el número total de celdas, el recuento de cadenas y el recuento de fórmulas para cada hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

Una clase que implementa la interfaz LightCellsDataHandler

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
