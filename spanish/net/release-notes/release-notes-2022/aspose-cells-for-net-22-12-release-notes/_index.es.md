---
title: Aspose.Cells for .NET 22.12 Notas de la versión
type: docs
weight: 1
url: /es/net/aspose-cells-for-net-22-12-release-notes/
---
{{% alert color="primary" %}}

 Esta página contiene notas de la versión para[Aspose.Cells for .NET 22.12](https://www.nuget.org/packages/Aspose.Cells/22.12.0).

{{% /alert %}}

|**Llave**|**Resumen**|**Categoría**|
|:- |:- |:- |
|CELLSNET-42315|Compatibilidad con archivos crtx: aplicación de plantillas de gráficos personalizadas|
|CELLSNET-47895|Las imágenes están distorsionadas en la representación de Excel a PDF/HTML|
|CELLSNET-47946|El efecto de rotación de imagen no se muestra correctamente en pdf/html|
|CELLSNET-47947|El efecto de rotación de caja rectangular en el grupo de gráficos no se muestra correctamente en pdf/html|
|CELLSNET-52126|Algunas formas se cambian después de convertir un archivo de Excel a PDF|
|CELLSNET-52197|Los cuadros cambiaron al convertir un documento XLSX a PDF|
|CELLSNET-52330|Las formas de dibujo no se representan bien en HTML|
|CELLSNET-50042| El nombre definido se cambia después de volver a guardar|
|CELLSNET-52270|La función YEARFRAC no se calcula correctamente|
|CELLSNET-52305|MMULT con OFFSET no se calcula correctamente|
|CELLSNET-52307|¡La fórmula de enlace roto devuelve 0 en lugar de #REF!|
|CELLSNET-52325| Workbook.CalculateFormula se cuelga en algunas circunstancias|
|CELLSNET-52387|Cell las referencias a tablas dan como resultado errores #REF después de eliminar columnas|
|CELLSNET-52290|El eje de los gráficos no se captura correctamente|
|CELLSNET-52301|Gráfico XLSX a imagen: las barras de gráficos combinados personalizados se representan incorrectamente|
|CELLSNET-52336|El gráfico de histograma no se representa correctamente en la conversión de XLSX a HTML/PDF|
|CELLSNET-52292|El texto se muestra en la página incorrecta en el PDF de salida: conversión de Excel a PDF|
|CELLSNET-52367|AutofitRows da como resultado texto recortado en la salida de conversión de PDF|
|CELLSNET-52242|La jerarquía padre-hijo es incorrecta al convertir Excel a JSON y viceversa|
|CELLSNET-52281|El encabezado Json no se puede ignorar|
|CELLSNET-52289|El formato de número se pierde al convertir html a excel|
|CELLSNET-52298|La opción AutoSort está habilitada para el campo dinámico al volver a guardar XLSX|
|CELLSNET-52299| El atributo HasRevisions es incorrecto después de guardar un libro de trabajo|
|CELLSNET-52332|Los números se muestran como '#' o número científico durante la conversión a html|
|CELLSNET-52338| El HTML de salida no es determinista.|
|CELLSNET-52344|Faltan hipervínculos en la conversión de HTML a JSON|

## **Public API y cambios incompatibles con versiones anteriores**

La siguiente es una lista de los cambios realizados al público API, como miembros agregados, renombrados, eliminados o obsoletos, así como cualquier cambio no compatible con versiones anteriores realizado en Aspose.Cells for .NET. Si tiene inquietudes sobre cualquier cambio enumerado, plantéelo en el foro de soporte Aspose.Cells.

### **Agrega la enumeración JsonExportHyperlinkType**

Representa el tipo de hipervínculo de exportación a archivos json.

### **Agrega JsonUtility.ExportRangeToJson(Range, JsonSaveOptions) y obsoleta el método ExportRangeToJson(Range, ExportRangeToJsonOptions)**

Use JsonUtility.ExportRangeToJson(Range, JsonSaveOptions) en su lugar.

### **Agrega la propiedad PivotTable.DataFieldHeaderName**

Obtiene y establece el nombre del encabezado del campo del área de valor en la tabla dinámica.

### **Agrega el método de anulación Range.SetStyle(Style,System.Boolean)**

Solo sobrescriba el formato que se establece explícitamente cuando se establece la bandera

### **Agrega la propiedad PivotField.NonAutoSortDefault**

Indica si una operación de clasificación que se aplicará a este campo dinámico es una operación de clasificación automática o una clasificación de datos simple.

### **Agrega el método GlobalizationSettings.GetDataFieldHeaderNameOfPivotTable()**

Obtiene el nombre local del encabezado del campo del área de valor en la tabla dinámica.

### **Agrega la propiedad Chart.PlotVisibleCellsOnly y obsoleta la propiedad Chart.PlotVisibleCells.**

Utilice la propiedad Chart.PlotVisibleCellsOnly en su lugar.

### **Agrega la propiedad JsonSaveOptions.ExportEmptyCells.**

Indica si exportar celdas vacías como nulas.

### **Agrega la propiedad JsonSaveOptions.ExportHyperlinkType.**

Representa el tipo de hipervínculo de exportación a json.

### **Agrega la propiedad JsonSaveOptions.ExportNestedStructure.**

Exportado como estructura Json de jerarquía padre-hijo.

### **Agrega la propiedad JsonSaveOptions.SkipEmptyRows.**

Indica si se saltan filas vacías.

### **Elimina el método obsoleto SheetRender.GetPageSize(System.Int32)**

Utilice SheetRender.GetPageSizeInch(System.Int32) en su lugar.

### **Elimina el método obsoleto WorkbookRender.GetPageSize(System.Int32)**

Use WorkbookRender.GetPageSizeInch(System.Int32) en su lugar.

### **Elimina la enumeración obsoleta AutoShapeType.TextWave3 y AutoShapeType.TextWave4**

Use UseAutoShape.TextDoubleWave1 y UseAutoShape.TextDoubleWave2 en su lugar.
