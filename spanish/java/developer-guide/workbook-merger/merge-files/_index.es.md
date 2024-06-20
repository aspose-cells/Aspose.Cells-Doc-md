---
title: Combinar archivos
type: docs
weight: 10
url: /es/java/merge-files/
---

## **Introducción**

Aspose.Cells proporciona diferentes formas de combinar archivos. Para archivos simples con datos, formato y fórmulas, el método [**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook)) puede utilizarse para combinar varios libros de trabajo, y el método [**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)) puede utilizarse para copiar hojas de cálculo en un nuevo libro de trabajo. Estos métodos son fáciles de usar y efectivos, pero si tiene muchos archivos para combinar, podría encontrar que utilizan muchos recursos del sistema. Para evitar esto, utilice el método estático CellsHelper.mergeFiles, una forma más eficiente de combinar varios archivos.

## **Combina archivos usando Aspose.Cells**

El siguiente código de muestra ilustra cómo combinar archivos grandes utilizando el método CellsHelper.mergeFiles. Toma dos archivos simples pero grandes, MyBook1.xls y MyBook2.xls. Los archivos contienen datos y fórmulas formateados únicamente.

{{% alert color="primary" %}}

El método CellsHelper.mergeFiles solo admite la combinación de datos, estilos, formato y fórmulas. Objetos como gráficos, imágenes, comentarios u otros objetos podrían no combinarse usando este método. Además, se utiliza un archivo en caché para almacenar datos temporales para el proceso.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
