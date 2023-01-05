---
title: Usando LightCells API
type: docs
weight: 160
url: /es/net/using-lightcells-api/
---
{{% alert color="primary" %}} 

A veces, necesita leer y escribir archivos de Excel grandes Microsoft con una gran lista de datos o contenido en la hoja de trabajo. LightCells API es útil para crear enormes hojas de cálculo de Excel: con él, necesita menos memoria y obtiene un mejor rendimiento y eficiencia.

{{% /alert %}} 
# Arquitectura impulsada por eventos
Aspose.Cells proporciona LightCells API, diseñado principalmente para manipular datos de celda uno por uno sin construir un bloque de modelo de datos completo (usando la colección Cell, etc.) en la memoria. Funciona en un modo controlado por eventos.

Para guardar libros de trabajo, proporcione el contenido de la celda celda por celda al guardar, y el componente lo guarda directamente en el archivo de salida.

Al leer archivos de plantilla, el componente analiza cada celda y proporciona su valor uno por uno.

En ambos procedimientos, se procesa un objeto Cell y luego se descarta, el objeto Workbook no contiene la colección. En este modo, por lo tanto, se ahorra memoria al importar y exportar Microsoft un archivo de Excel que tiene un gran conjunto de datos que, de lo contrario, usaría mucha memoria.

Aunque LightCells API procesa las celdas de la misma manera para los archivos XLSX y XLS (en realidad no carga todas las celdas en la memoria sino que procesa una celda y luego la descarta), ahorra memoria de manera más efectiva para los archivos XLSX que para los archivos XLS debido a los diferentes modelos de datos y estructuras de los dos formatos.

 Sin embargo,**para archivos XLS** , para ahorrar más memoria, los desarrolladores pueden especificar una ubicación temporal para guardar los datos temporales generados durante el proceso Guardar. Comúnmente,**usar LightCells API para guardar el archivo XLSX puede ahorrar un 50% o más de memoria** que usar la forma común,**guardar XLS puede ahorrar entre un 20 y un 40 % de memoria**.
## Escribir un archivo de Excel grande
Aspose.Cells proporciona una interfaz, LightCellsDataProvider, que debe implementarse en su programa. La interfaz representa el proveedor de datos para guardar archivos de hojas de cálculo grandes en modo ligero.

Al guardar un libro de trabajo en este modo, StartSheet (int) se verifica al guardar cada hoja de trabajo en el libro de trabajo. Para una hoja, si StartSheet(int) es verdadero, esta implementación proporciona todos los datos y propiedades de las filas y celdas de esta hoja que se van a guardar. En primer lugar, se llama a NextRow() para obtener el índice de la siguiente fila que se guardará. Si se devuelve un índice de fila válido (el índice de fila debe estar en orden ascendente para que se guarden las filas), se proporciona un objeto Row que representa esta fila para que la implementación establezca sus propiedades mediante StartRow(Row).

Para una fila, NextCell() se verifica primero. Si se devuelve un índice de columna válido (el índice de columna debe estar en orden ascendente para que se guarden todas las celdas de una fila), se proporciona un objeto Cell que representa esa celda para que StartCell(Cell) establezca sus datos y propiedades. Una vez que se configuran los datos de la celda, la celda se guarda directamente en el archivo de hoja de cálculo generado y la siguiente celda se verifica y procesa.
### Escribir un archivo de Excel grande: Ejemplo
Consulte el siguiente código de muestra para ver el funcionamiento de LightCells API. Agregue y elimine, o actualice los segmentos de código según sus necesidades.

 El programa crea un archivo enorme con**10.000 (matriz 10000x30) registros** en una hoja de trabajo y los llena con datos ficticios. Puede especificar su propia matriz cambiando las variables rowsCount y colsCount en el método Main().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-WritingLargeExcelFile.cs" >}}
## Leer archivos grandes de Excel
Aspose.Cells proporciona una interfaz, LightCellsDataHandler, que debe implementarse en su programa. La interfaz representa el proveedor de datos para leer grandes archivos de hojas de cálculo en modo ligero.

Al leer un libro de trabajo en este modo, StartSheet se verifica al leer cada hoja de trabajo en el libro de trabajo. Para una hoja, si StartSheet devuelve verdadero, la implementación de esta interfaz verifica y procesa todos los datos y propiedades de las celdas en filas y columnas de la hoja. Para cada fila, se llama a StartRow para verificar si es necesario procesarla. Si es necesario procesar una fila, primero se leen sus propiedades y el desarrollador puede acceder a sus propiedades con ProcessRow. Si las celdas de la fila también deben procesarse, ProcessRow debe devolver verdadero y luego se llama a StartCell para cada celda existente en la fila para verificar si una celda necesita ser procesada. Si es necesario procesar una celda, se llama a ProcessCell para procesar la celda mediante la implementación de esta interfaz.
### Leer archivos grandes de Excel: Ejemplo
Consulte el siguiente código de muestra para ver el funcionamiento de LightCells API. Agregue y elimine, o actualice los segmentos de código según sus necesidades.

El programa lee un archivo enorme con millones de registros en una hoja de trabajo. Se necesita un poco de tiempo para leer cada hoja del libro de trabajo. El código de ejemplo lee el archivo y recupera el número total de celdas, el recuento de cadenas y el recuento de fórmulas en cada hoja de cálculo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingLightCellsAPI-ReadingLargeExcelFile.cs" >}}
