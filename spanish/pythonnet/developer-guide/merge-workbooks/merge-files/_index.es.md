---
title: Combinar archivos
type: docs
weight: 20
url: /es/python-net/merge-files/
---

## **Introducción**

Aspose.Cells para Python via .NET ofrece diferentes maneras de fusionar archivos. Para archivos simples con datos, formato y fórmulas, se puede usar el método [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) para combinar varios libros de trabajo, y el método [**Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy) para copiar hojas en un nuevo libro de trabajo. Estos métodos son fáciles de usar y efectivos, pero si tienes muchos archivos para fusionar, puede que requieran muchos recursos del sistema. Para evitar esto, usa el método estático [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files), una forma más eficiente de fusionar varios archivos.

## **Fusionar archivos usando Aspose.Cells para Python via .NET**

El siguiente código de ejemplo ilustra cómo combinar archivos grandes utilizando el método [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files). Toma dos archivos simples pero grandes, Libro1.xls y Libro2.xls. Los archivos contienen datos formateados y fórmulas únicamente.

{{% alert color="primary" %}}

El método [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files) solo admite la combinación de datos, estilos, formato y fórmulas. Objetos como gráficos, imágenes, comentarios u otros objetos pueden no ser combinados usando este método. Además, se utiliza un archivo en caché para almacenar datos temporales para el proceso.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CellsHelperClass-MergeFiles-1.py" >}}

