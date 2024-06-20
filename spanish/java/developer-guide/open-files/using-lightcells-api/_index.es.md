---
title: Utilizando la API de LightCells
type: docs
weight: 80
url: /es/java/using-lightcells-api/
---

{{% alert color="primary" %}}

A veces necesitas leer y escribir archivos grandes de Microsoft Excel con una enorme lista de datos o contenidos en la hoja de cálculo. La API de LightCells es útil para crear hojas de cálculo de Excel enormes: con ella, necesitas menos memoria y obtienes un mejor rendimiento y eficiencia.

{{% /alert %}}

## **Arquitectura Orientada a Eventos**

Aspose.Cells proporciona la API de LightCells, diseñada principalmente para manipular los datos de las celdas una por una sin construir un modelo completo de datos (usando la colección de Celdas, etc.) en la memoria. Funciona en modo de eventos.

Para guardar libros de trabajo, proporciona el contenido de la celda una por una al guardar, y el componente lo guarda directamente en el archivo de salida.

Al leer archivos de plantilla, el componente analiza cada celda y proporciona su valor uno por uno.

En ambos procedimientos, se procesa un objeto de Celda y luego se descarta, el objeto de Libro de trabajo no retiene la colección. En este modo, por lo tanto, se ahorra memoria al importar y exportar archivos de Microsoft Excel que tienen un gran conjunto de datos que de otra manera usaría mucha memoria.

Aunque la API de LightCells procesa las celdas de la misma manera para archivos XLSX y XLS (no carga todas las celdas en la memoria sino que procesa una celda y luego la descarta), ahorra memoria de manera más efectiva para archivos XLSX que para archivos XLS debido a los diferentes modelos de datos y estructuras de los dos formatos.

Sin embargo, **para archivos XLS**, para ahorrar más memoria, los desarrolladores pueden especificar una ubicación temporal para guardar los datos temporales generados durante el proceso de Guardar. Comúnmente, **utilizando la API de LightCells para guardar archivos XLSX se puede ahorrar un 50% o más de memoria** que utilizando el método común, **guardando XLS puede ahorrar alrededor del 20-40% de memoria**.

### **Escribiendo Archivos de Excel Grandes**

Aspose.Cells proporciona una interfaz, LightCellsDataProvider, que debe ser implementada en tu programa. La interfaz representa un proveedor de datos para guardar archivos de hojas de cálculo grandes en modo ligero.

Al guardar un libro de trabajo en este modo, se comprueba startSheet(int) al guardar cada hoja de cálculo en el libro. Para una hoja, si startSheet(int) es verdadero, entonces todos los datos y propiedades de las filas y celdas de esta hoja que se van a guardar son proporcionados por esta implementación. En primer lugar, se llama a nextRow() para obtener el próximo índice de fila que se guardará. Si se devuelve un índice de fila válido (el índice de fila debe estar en orden ascendente para las filas que se van a guardar), entonces se proporciona un objeto Row que representa esta fila para que la implementación establezca sus propiedades mediante startRow(Row).

Para una fila, se comprueba primero nextCell(). Si se devuelve un índice de columna válido (el índice de columna debe estar en orden ascendente para todas las celdas de una fila que se van a guardar), entonces se proporciona un objeto Cell que representa esta celda para establecer los datos y propiedades mediante startCell(Cell). Después de que se establecen los datos de esta celda, esta se guarda directamente en el archivo de hoja de cálculo generado y se comprueba y procesa la siguiente celda.

El siguiente ejemplo muestra cómo funciona la API LightCells.

El siguiente programa crea un archivo enorme con 100,000 registros en una hoja de cálculo, rellenada con datos. Hemos agregado algunos hipervínculos, valores de cadena, valores numéricos y también fórmulas a ciertas celdas en la hoja de cálculo. Además, hemos formateado un rango de celdas también.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **Lectura de archivos Excel grandes**

Aspose.Cells proporciona una interfaz, LightCellsDataHandler, que debe ser implementada en su programa. La interfaz representa el proveedor de datos para la lectura de archivos de hojas de cálculo grandes en modo liviano.

Al leer un libro de trabajo en este modo, se comprueba startSheet() al leer cada hoja de cálculo en el libro. Para una hoja, si startSheet() devuelve verdadero, entonces se comprueban y procesan todos los datos y propiedades de las celdas en las filas y columnas de la hoja. Para cada fila, se llama a startRow() para comprobar si necesita ser procesada. Si una fila necesita ser procesada, primero se leen las propiedades de la fila y los desarrolladores pueden acceder a sus propiedades con processRow().

Si las celdas de la fila también necesitan ser procesadas, entonces processRow() devuelve verdadero y se llama a startCell() para cada celda existente en la fila para comprobar si necesita ser procesada. Si lo hace, se llama a processCell().

El siguiente código de ejemplo ilustra este proceso. El programa lee un archivo grande con millones de registros. Se tarda un poco en leer cada hoja de cálculo en el libro. El código de ejemplo lee el archivo y recupera el número total de celdas, conteo de cadenas y conteo de fórmulas para cada hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

Una clase que implementa la interfaz LightCellsDataHandler

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
