---
title: Fusionar archivos con Golang a través de C++
linktitle: Combinar archivos
type: docs
weight: 20
url: /es/go-cpp/merge-files/
description: Aprende cómo fusionar archivos de Excel de manera eficiente usando Aspose.Cells for C++.
---

## **Introducción**

Aspose.Cells ofrece diferentes maneras de fusionar archivos. Para archivos simples con datos, formato y fórmulas, se puede usar el método [**Workbook.Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) para combinar varios libros de trabajo, y el método [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) para copiar hojas de trabajo en un nuevo libro. Estos métodos son fáciles de usar y efectivos, pero si tienes muchos archivos para fusionar, puede que tomen muchos recursos del sistema. Para evitar esto, usa el método estático [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/), una forma más eficiente de fusionar varios archivos.

## **Combina archivos usando Aspose.Cells**

El siguiente código de ejemplo ilustra cómo fusionar archivos grandes usando el método [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/). Toma dos archivos simples pero grandes, Book1.xls y Book2.xls. Los archivos contienen datos formateados y fórmulas solamente.

{{% alert color="primary" %}}

El método [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/) solo admite fusionar datos, estilos, formato y fórmulas. Objetos como gráficos, imágenes, comentarios u otros objetos pueden no fusionarse usando este método. Además, se usa un archivo en caché para almacenar datos temporales del proceso.

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeFiles.go" >}}
