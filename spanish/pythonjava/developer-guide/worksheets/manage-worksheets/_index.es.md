---
title: Gestionar hojas de cálculo
type: docs
weight: 10
url: /es/python-java/manage-worksheets/
---

Gestionar hojas de cálculo utilizando Aspose.Cells for Python via Java es muy sencillo. En este artículo, demostraremos cómo añadir, acceder y eliminar hojas de cálculo utilizando la API de Aspose.Cells.
## **Añadir hojas de cálculo a un nuevo archivo de Excel**
Para crear un nuevo libro de trabajo, crea un objeto de la clase [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook). La clase [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) representa un archivo de Excel. Luego, mediante el uso del método [add](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\)) de la [WorksheetCollection](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection), se añaden nuevas hojas de cálculo al archivo de Excel. Finalmente, para guardar el archivo de Excel recién creado, llama al método [save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\)) de la clase [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook).

El siguiente fragmento de código demuestra cómo crear un nuevo archivo de Excel y agregar una hoja de cálculo a él.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Añadir hojas de cálculo a una hoja de cálculo de diseñador**
Agregar hojas de cálculo a una hoja de diseño es exactamente lo mismo que agregar la hoja de cálculo a un nuevo archivo de Excel. La única diferencia es que en lugar de crear un nuevo archivo de Excel, abrimos un archivo existente mediante la clase [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook).

El siguiente fragmento de código demuestra cómo agregar una hoja de cálculo a una hoja de diseño.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Acceso a las hojas de cálculo usando el nombre de la hoja**
Después de cargar un libro de trabajo, los desarrolladores pueden acceder a cualquier hoja de cálculo usando su índice o nombre. El siguiente fragmento de código demuestra cómo acceder a una hoja de cálculo usando su nombre.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Eliminación de hojas de cálculo**
Puede haber momentos en los que algunas hojas necesiten ser eliminadas del libro de trabajo. Para esto, la API proporciona el método [WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)). Puede pasar el índice de la hoja o el nombre de la hoja que se eliminará. Los siguientes ejemplos demuestran cómo eliminar hojas de cálculo usando el índice de la hoja y el nombre de la hoja.
### **Eliminación de hojas de cálculo usando el índice de la hoja**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Eliminar hojas de cálculo utilizando el nombre de la hoja**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
