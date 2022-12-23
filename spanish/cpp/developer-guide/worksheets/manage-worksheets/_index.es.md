---
title: Administrar hojas de trabajo
type: docs
weight: 20
url: /es/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

Los desarrolladores pueden crear y administrar fácilmente hojas de trabajo en archivos Microsoft de Excel mediante programación usando Aspose.Cells flexible API. Este tema describe enfoques para agregar y eliminar hojas de trabajo en archivos Microsoft de Excel.

{{% /alert %}} 

 Aspose.Cells proporciona una clase[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) que representa un archivo de Excel. Él[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)colección que permite el acceso a cada hoja de trabajo en el archivo de Excel.

 Una hoja de trabajo está representada por el[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. Él[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)La clase proporciona una amplia gama de métodos para administrar hojas de trabajo.
## **Agregar hojas de trabajo a un nuevo archivo de Excel**
Para crear un nuevo archivo de Excel mediante programación:

1.  Crea un objeto de la[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)clase.
1.  Llama a[Agregar](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa2bb166f57a4d8eba8e25ce1f99d0c55) metodo de la[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) recopilación. Una hoja de cálculo vacía se agrega automáticamente al archivo de Excel. Se puede hacer referencia al pasar el índice de la hoja de la nueva hoja de trabajo al[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)recopilación.
1. Obtenga una referencia de la hoja de trabajo.
1. Realizar el trabajo en las hojas de trabajo.
1.  Guarde el nuevo archivo de Excel con nuevas hojas de trabajo llamando al[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) clase[Ahorrar](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)método.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile.cpp" >}}
## **Acceder a las hojas de trabajo mediante el índice de hojas**
El siguiente código de ejemplo muestra cómo acceder u obtener cualquier hoja de trabajo especificando su índice.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex.cpp" >}}
## **Eliminación de hojas de cálculo mediante el índice de hojas**
 La eliminación de hojas de trabajo por nombre funciona bien cuando se conoce el nombre de la hoja de trabajo. Si no conoce el nombre de la hoja de cálculo, utilice una versión sobrecargada de la[Eliminar en](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#addabcc7d7d76874694018fb3ba37b72c)método que toma el índice de hoja de la hoja de trabajo en lugar de su nombre de hoja.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex.cpp" >}}
