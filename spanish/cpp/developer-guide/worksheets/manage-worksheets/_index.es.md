---
title: Administrar hojas de trabajo
type: docs
weight: 20
url: /es/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

Los desarrolladores pueden crear y administrar fácilmente hojas de trabajo en archivos Microsoft Excel mediante programación usando Aspose.Cells flexible API. Este tema describe enfoques para agregar y eliminar hojas de trabajo en archivos Microsoft Excel.

{{% /alert %}} 

 Aspose.Cells proporciona una clase[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Excel. El[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)colección que permite el acceso a cada hoja de cálculo del archivo Excel.

Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase. El[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)La clase proporciona una amplia gama de métodos para administrar hojas de trabajo.
##  **Agregar hojas de trabajo a un nuevo archivo de Excel**
Para crear un nuevo archivo de Excel mediante programación:

1.  Crea un objeto de[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)clase.
1.  Llama a[Agregar](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) método de la[Colección de hojas de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) recopilación. Se agrega automáticamente una hoja de trabajo vacía al archivo de Excel. Se puede hacer referencia a él pasando el índice de la hoja de la nueva hoja de trabajo al[Colección de hojas de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)recopilación.
1. Obtenga una referencia de la hoja de trabajo.
1. Realizar trabajos en las hojas de trabajo.
1. Guarde el nuevo archivo de Excel con nuevas hojas de trabajo llamando al[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) clase[Ahorrar](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)método.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
##  **Acceder a hojas de trabajo mediante el índice de hojas**
El siguiente código de muestra muestra cómo acceder u obtener cualquier hoja de trabajo especificando su índice.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
##  **Eliminar hojas de trabajo usando el índice de hojas**
 Eliminar hojas de trabajo por nombre funciona bien cuando se conoce el nombre de la hoja de trabajo. Si no conoce el nombre de la hoja de trabajo, utilice una versión sobrecargada del[Eliminar en](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat)Método que toma el índice de la hoja de trabajo en lugar de su nombre.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
