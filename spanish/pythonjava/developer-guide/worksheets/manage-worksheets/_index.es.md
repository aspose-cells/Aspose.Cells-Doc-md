---
title: Administrar hojas de trabajo
type: docs
weight: 10
url: /es/python-java/manage-worksheets/
---
Administrar hojas de trabajo usando Aspose.Cells para Python a través de Java es muy fácil. En este artículo, demostraremos cómo agregar, acceder y eliminar hojas de trabajo utilizando el Aspose.Cells API.
## **Agregar hojas de trabajo a un nuevo archivo de Excel**
 Para crear un nuevo libro de trabajo, cree un objeto de la[Libro de trabajo](https://reference.aspose.com/cells/python/asposecells.api/Workbook) clase. los[Libro de trabajo](https://reference.aspose.com/cells/python/asposecells.api/Workbook) clase representa un archivo de Excel. Entonces usando el[agregar](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\) ) método de la[Colección de hojas de trabajo](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) , se agregan nuevas hojas de cálculo al archivo de Excel. Finalmente, para guardar el archivo de Excel recién creado, llame al[ahorrar](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\) ) método de la[Libro de trabajo](https://reference.aspose.com/cells/python/asposecells.api/Workbook)clase.

El siguiente fragmento de código demuestra cómo crear un nuevo archivo de Excel y agregarle una hoja de trabajo.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Adición de hojas de trabajo a una hoja de cálculo de Designer**
Agregar hojas de trabajo a una hoja de cálculo de diseñador es exactamente lo mismo que agregar la hoja de trabajo a un nuevo archivo de Excel. La única diferencia es que en lugar de crear un nuevo archivo de Excel, abrimos un archivo existente por el[Libro de trabajo](https://reference.aspose.com/cells/python/asposecells.api/Workbook)clase.

El siguiente fragmento de código muestra cómo agregar una hoja de trabajo a una hoja de cálculo de diseñador.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Acceder a las hojas de trabajo usando el nombre de la hoja**
Después de cargar un libro de trabajo, los desarrolladores pueden acceder a cualquier hoja de trabajo usando su índice o nombre. El siguiente fragmento de código muestra cómo acceder a una hoja de trabajo usando su nombre.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Quitar hojas de trabajo**
Puede haber momentos en que algunas hojas se encuentren para ser eliminadas del libro de trabajo. Para esto, el API proporciona el[WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)) método. Puede pasarle el índice de hoja o el nombre de hoja de la hoja que se eliminará. Los siguientes ejemplos muestran la eliminación de hojas de cálculo mediante el uso del índice y el nombre de la hoja.
### **Eliminación de hojas de cálculo mediante el índice de hojas**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Eliminación de hojas de trabajo usando el nombre de la hoja**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
