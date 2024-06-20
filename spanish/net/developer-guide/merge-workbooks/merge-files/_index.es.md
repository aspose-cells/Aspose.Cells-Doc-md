---
title: Combinar archivos
type: docs
weight: 20
url: /es/net/merge-files/
---

## **Introducción**

Aspose.Cells proporciona diferentes formas de combinar archivos. Para archivos simples con datos, formato y fórmulas, el método [**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) se puede utilizar para combinar varios libros de trabajo, y el método [**Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index) se puede utilizar para copiar hojas de cálculo en un nuevo libro de trabajo. Estos métodos son fáciles de usar y efectivos, pero si tienes muchos archivos para combinar, puede que encuentres que utilizan muchos recursos del sistema. Para evitar esto, utiliza el método estático [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles), una forma más eficiente de combinar varios archivos.

## **Combina archivos usando Aspose.Cells**

El siguiente código de ejemplo ilustra cómo combinar archivos grandes utilizando el método [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles). Toma dos archivos simples pero grandes, Libro1.xls y Libro2.xls. Los archivos contienen datos formateados y fórmulas únicamente.

{{% alert color="primary" %}}

El método [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) solo admite la combinación de datos, estilos, formato y fórmulas. Objetos como gráficos, imágenes, comentarios u otros objetos pueden no ser combinados usando este método. Además, se utiliza un archivo en caché para almacenar datos temporales para el proceso.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
