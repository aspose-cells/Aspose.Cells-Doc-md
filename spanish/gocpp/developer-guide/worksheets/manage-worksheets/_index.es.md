---
title: Gestionar hojas de cálculo
type: docs
weight: 20
url: /es/go-cpp/manage-worksheets/
---

{{% alert color="primary" %}}

Los desarrolladores pueden crear y gestionar hojas de cálculo en archivos de Microsoft Excel de forma programática utilizando la API flexible de Aspose.Cells. Este tema describe los enfoques para agregar y eliminar hojas de cálculo en archivos de Microsoft Excel.

{{% /alert %}}

Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) que representa un archivo de Excel. La clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una colección [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) ofrece una amplia gama de métodos para gestionar hojas de cálculo.

## **Añadir hojas de cálculo a un nuevo archivo de Excel**

Para crear un nuevo archivo de Excel programáticamente:

1. Crea un objeto de la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/).
1. Llama al método [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_string/) de la colección [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/). Se agrega automáticamente una hoja de cálculo vacía al archivo de Excel. Se puede hacer referencia a ella pasando el índice de la hoja en la colección [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/).
1. Obtenga una referencia de la hoja de cálculo.
1. Realice el trabajo en las hojas de cálculo.
1. Guarda el nuevo archivo de Excel con las nuevas hojas de cálculo llamando al método [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) de la clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingWorksheetsToNewExcelFile.go" >}}

## **Acceder a las hojas de cálculo usando el índice de hoja**

El siguiente código de ejemplo muestra cómo acceder o obtener cualquier hoja de cálculo especificando su índice.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessingWorksheetsUsingSheetIndex.go" >}}

## **Eliminar hojas de cálculo utilizando el índice de la hoja**

Eliminar hojas de cálculo por nombre funciona bien cuando se conoce el nombre de la hoja. Si no sabe el nombre de la hoja, utilice una versión sobrecargada del método [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat) que toma el índice de la hoja en lugar de su nombre.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingWorksheetsUsingSheetIndex.go" >}}
