---
title: Utilizando la API de LightCells
type: docs
weight: 160
url: /es/net/using-lightcells-api/
---

{{% alert color="primary" %}} 

A veces necesitas leer y escribir archivos de Excel de Microsoft grandes con una enorme lista de datos o contenido en la hoja de cálculo. La API de LightCells es útil para crear hojas de cálculo de Excel extensas: con ella, necesita menos memoria y obtiene un mejor rendimiento y eficiencia.

{{% /alert %}} 
# Arquitectura Orientada a Eventos
Aspose.Cells proporciona la API de LightCells, diseñada principalmente para manipular los datos de las celdas una por una sin construir un modelo completo de datos (usando la colección de Celdas, etc.) en la memoria. Funciona en modo de eventos.

Para guardar libros de trabajo, proporciona el contenido de la celda una por una al guardar, y el componente lo guarda directamente en el archivo de salida.

Al leer archivos de plantilla, el componente analiza cada celda y proporciona su valor uno por uno.

En ambos procedimientos, se procesa un objeto de Celda y luego se descarta, el objeto de Libro de trabajo no retiene la colección. En este modo, por lo tanto, se ahorra memoria al importar y exportar archivos de Microsoft Excel que tienen un gran conjunto de datos que de otra manera usaría mucha memoria.

Aunque la API de LightCells procesa las celdas de la misma manera para archivos XLSX y XLS (no carga todas las celdas en la memoria sino que procesa una celda y luego la descarta), ahorra memoria de manera más efectiva para archivos XLSX que para archivos XLS debido a los diferentes modelos de datos y estructuras de los dos formatos.

Sin embargo, **para archivos XLS**, para ahorrar más memoria, los desarrolladores pueden especificar una ubicación temporal para guardar los datos temporales generados durante el proceso de Guardar. Comúnmente, **utilizando la API de LightCells para guardar archivos XLSX se puede ahorrar un 50% o más de memoria** que utilizando el método común, **guardando XLS puede ahorrar alrededor del 20-40% de memoria**.
## Escribir un Archivo de Excel Grande
Aspose.Cells proporciona una interfaz, LightCellsDataProvider, que debe implementarse en su programa. La interfaz representa el proveedor de datos para guardar grandes archivos de hojas de cálculo en modo ligero.

Cuando se guarda un libro de trabajo en este modo, se comprueba StartSheet(int) al guardar cada hoja de cálculo en el libro. Para una hoja, si StartSheet(int) es verdadero, entonces se proporcionan todos los datos y propiedades de filas y celdas de esta hoja que se guardarán mediante esta implementación. En primer lugar, se llama a NextRow() para obtener el índice de fila siguiente que se va a guardar. Si se devuelve un índice de fila válido (el índice de fila debe estar en orden ascendente para que las filas se guarden), se proporciona un objeto Row que representa esta fila para que la implementación establezca sus propiedades mediante StartRow(Row).

Para una fila, primero se comprueba NextCell(). Si se devuelve un índice de columna válido (el índice de columna debe estar en orden ascendente para que se guarden todas las celdas de una fila), entonces se proporciona un objeto Cell que representa esa celda para que la implementación establezca sus datos y propiedades mediante StartCell(Cell). Después de establecer los datos de la celda, la celda se guarda directamente en el archivo de hoja de cálculo generado y se comprueba y procesa la siguiente celda.
### Escribir un Archivo de Excel Grande: Ejemplo
Consulte el siguiente código de muestra para ver el funcionamiento de la API LightCells. Agregue, elimine o actualice los segmentos de código según sus necesidades.

El programa crea un archivo enorme con **10,000 registros (matriz de 10000x30)** en una hoja de cálculo y los llena con datos ficticios. Puede especificar su propia matriz cambiando las variables rowsCount y colsCount en el método Main().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## Leer Archivos de Excel Grandes
Aspose.Cells proporciona una interfaz, LightCellsDataHandler que debe implementarse en su programa. La interfaz representa un proveedor de datos para leer grandes archivos de hojas de cálculo en modo ligero.

Al leer un libro de trabajo en este modo, se comprueba StartSheet al leer cada hoja de cálculo en el libro. Para una hoja, si StartSheet devuelve verdadero, entonces se comprueban y procesan todos los datos y propiedades de las celdas en filas y columnas de la hoja mediante la implementación de esta interfaz. Para cada fila, se llama a StartRow para comprobar si necesita ser procesada. Si una fila necesita ser procesada, primero se leen sus propiedades y el desarrollador puede acceder a sus propiedades con ProcessRow. Si las celdas de la fila también necesitan ser procesadas, entonces ProcessRow debería devolver verdadero y luego se llama a StartCell para cada celda existente en la fila para comprobar si una celda necesita ser procesada. Si una celda necesita ser procesada, entonces se llama a ProcessCell para procesar la celda mediante la implementación de esta interfaz.
### Leer Archivos de Excel Grandes: Ejemplo
Consulte el siguiente código de muestra para ver el funcionamiento de la API LightCells. Agregue, elimine o actualice los segmentos de código según sus necesidades.

El programa lee un archivo enorme con millones de registros en una hoja de cálculo. Se tarda un poco en leer cada hoja de cálculo en el libro. El código de muestra lee el archivo y recupera el número total de celdas, el recuento de cadenas y el recuento de fórmulas en cada hoja de cálculo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
