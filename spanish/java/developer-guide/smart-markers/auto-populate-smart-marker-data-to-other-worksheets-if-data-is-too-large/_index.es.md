---
title: Auto rellenar datos de marcador inteligente a otras hojas de cálculo si los datos son demasiado grandes
type: docs
weight: 10
url: /es/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **Escenarios de uso posibles**

A veces, desea auto-rellenar datos de marcador inteligente a otras hojas de cálculo si son demasiados. Suponga que su fuente de datos tiene 1500000 registros. Estos son demasiados registros para una sola hoja de cálculo, entonces puede mover el resto de los registros a la siguiente hoja de cálculo.

## **Autocompletar Datos de Marcador Inteligente en Otras Hojas de Cálculo si los Datos son muy Grandes**

El siguiente código de ejemplo tiene una fuente de datos que tiene 21 registros. Queremos mostrar solo 15 registros en una hoja de cálculo, luego el resto de los registros se moverán automáticamente a la segunda hoja de cálculo. Tenga en cuenta que la segunda hoja de cálculo también debe tener la misma etiqueta de marcador inteligente y debe llamar al método [**WorkbookDesigner.process(sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process(int,%20boolean)) para ambas hojas. Consulte el [archivo de base de datos de Microsoft Access](60489777.accdb) utilizado en este código, así como el [archivo de Excel de salida](60489786.xlsx) generado por el código como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
