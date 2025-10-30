---
title: Gestionar hojas de cálculo
type: docs
weight: 20
url: /es/cpp/manage-worksheets/
---

{{% alert color="primary" %}} 

Los desarrolladores pueden crear y gestionar hojas de cálculo en archivos de Microsoft Excel de forma programática utilizando la API flexible de Aspose.Cells. Este tema describe los enfoques para agregar y eliminar hojas de cálculo en archivos de Microsoft Excel.

{{% /alert %}} 

Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Excel. La clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una amplia gama de métodos para gestionar hojas de cálculo.
## **Añadir hojas de cálculo a un nuevo archivo de Excel**
Para crear un nuevo archivo de Excel programáticamente:

1. Crear un objeto de la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).
1. Llamar al método [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) de la colección [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/). Se agrega automáticamente una hoja de cálculo vacía al archivo de Excel. Puede ser referenciada pasando el índice de la hoja de cálculo nueva a la colección [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).
1. Obtenga una referencia de la hoja de cálculo.
1. Realice el trabajo en las hojas de cálculo.
1. Guardar el nuevo archivo de Excel con las nuevas hojas de cálculo llamando al método [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) de la clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
## **Acceder a las hojas de cálculo usando el índice de hoja**
El siguiente código de ejemplo muestra cómo acceder o obtener cualquier hoja de cálculo especificando su índice.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
## **Eliminar hojas de cálculo utilizando el índice de la hoja**
Eliminar hojas de cálculo por nombre funciona bien cuando se conoce el nombre de la hoja de cálculo. Si no se conoce el nombre de la hoja de cálculo, utilizar una versión sobrecargada del método [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat) que toma el índice de la hoja de cálculo en lugar de su nombre de hoja.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
