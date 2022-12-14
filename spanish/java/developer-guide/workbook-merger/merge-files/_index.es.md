---
title: Combinar archivos
type: docs
weight: 10
url: /es/java/merge-files/
---
## **Introducción**

 Aspose.Cells proporciona diferentes formas de combinar archivos. Para archivos simples con datos, formato y fórmulas, el[**Libro de trabajo.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook) ) se puede usar para combinar varios libros de trabajo, y el[**Hoja de trabajo.copia(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)se puede usar para copiar hojas de trabajo en un nuevo libro de trabajo. Estos métodos son fáciles de usar y efectivos, pero si tiene muchos archivos para fusionar, es posible que consuman muchos recursos del sistema. Para evitar esto, use el método estático CellsHelper.mergeFiles, una forma más eficiente de fusionar varios archivos.

## **Combinar archivos usando Aspose.Cells**

El siguiente código de ejemplo ilustra cómo combinar archivos grandes mediante el método CellsHelper.mergeFiles. Se necesitan dos archivos simples pero grandes, MyBook1.xls y MyBook2.xls. Los archivos contienen solo datos con formato y fórmulas.

{{% alert color="primary" %}}

El método CellsHelper.mergeFiles solo admite la combinación de datos, estilos, formatos y fórmulas. Es posible que los objetos como gráficos, imágenes, comentarios u otros objetos no se combinen con este método. Además, se utiliza un archivo en caché para almacenar datos temporales para el proceso.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
