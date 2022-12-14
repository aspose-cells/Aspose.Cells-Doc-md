---
title: Combinar archivos
type: docs
weight: 20
url: /es/net/merge-files/
---
## **Introducción**

 Aspose.Cells proporciona diferentes formas de combinar archivos. Para archivos simples con datos, formato y fórmulas, el[**Libro de trabajo.Combinar()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) El método se puede utilizar para combinar varios libros de trabajo, y el[**Hoja de trabajo.Copiar()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)El método se puede utilizar para copiar hojas de trabajo en un nuevo libro de trabajo. Estos métodos son fáciles de usar y efectivos, pero si tiene muchos archivos para fusionar, es posible que consuman muchos recursos del sistema. Para evitar esto, utilice el[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)método estático, una forma más eficiente de fusionar varios archivos.

## **Combinar archivos usando Aspose.Cells**

 El siguiente código de ejemplo ilustra cómo fusionar archivos grandes usando el[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)método. Se necesitan dos archivos simples pero grandes, Book1.xls y Book2.xls. Los archivos contienen solo datos con formato y fórmulas.

{{% alert color="primary" %}}

 los[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) El método solo admite la combinación de datos, estilos, formato y fórmulas. Es posible que los objetos como gráficos, imágenes, comentarios u otros objetos no se combinen con este método. Además, se utiliza un archivo en caché para almacenar datos temporales para el proceso.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
