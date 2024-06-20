---
title: Auto rellenar datos de marcador inteligente a otras hojas de cálculo si los datos son demasiado grandes
type: docs
weight: 50
url: /es/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **Escenarios de uso posibles**
A veces, desea auto-completar datos de marcador inteligente en otras hojas de cálculo si son demasiados. Suponga que su origen de datos tiene 1500000 registros. Estos son demasiados registros para una sola hoja de cálculo, entonces puede mover el resto de los registros a la siguiente hoja de cálculo. 
## **Auto-completar datos de marcador inteligente en otras hojas de cálculo si los datos son demasiado grandes**
El siguiente código de muestra tiene un origen de datos que tiene 21 registros. Queremos mostrar solo 15 registros en una hoja de cálculo, luego el resto de los registros se moverán automáticamente a la segunda hoja de cálculo. Tenga en cuenta que la segunda hoja de cálculo también debe tener la misma etiqueta de marcador inteligente y debe llamar al método [WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) para ambas hojas. Consulte el [archivo de Excel de salida](60489775.xlsx) generado por el código como referencia.
## **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
