---
title: Autocompletar datos de marcador inteligente en otras hojas de trabajo si los datos son demasiado grandes
type: docs
weight: 50
url: /es/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---
## **Posibles escenarios de uso**
A veces, desea completar automáticamente los datos del marcador inteligente en otras hojas de trabajo si es demasiado grande. Supongamos que su fuente de datos tiene 1500000 registros. Estos son demasiados registros para una sola hoja de trabajo, luego puede mover el resto de los registros a la siguiente hoja de trabajo.
## **Completar automáticamente los datos del marcador inteligente en otras hojas de trabajo si los datos son demasiado grandes**
 El código de ejemplo siguiente tiene un origen de datos que tiene 21 registros. Queremos mostrar solo 15 registros en una hoja de trabajo, luego el resto de los registros se moverán automáticamente a la segunda hoja de trabajo. Tenga en cuenta que la segunda hoja de trabajo también debe tener la misma etiqueta de marcador inteligente y debe llamar[WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) método para ambas hojas. Por favor vea el[archivo de salida de Excel](60489775.xlsx) generado por el código para una referencia.
## **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
