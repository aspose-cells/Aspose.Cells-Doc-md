---
title: Insertar rebanador
linktitle: Rebanadores
type: docs
weight: 170
url: /es/net/create-slicer/
description: Gestionar rebanadores de archivos de Excel con Aspose.Cells.
---

## **Escenarios de uso posibles**

Un segmentador se usa para filtrar datos rápidamente. Puede usarse para filtrar datos tanto en una tabla como en una tabla dinámica. Microsoft Excel le permite crear un segmentador seleccionando una tabla o tabla dinámica y luego haciendo clic en *Insertar > Segmentador*. Aspose.Cells también le permite crear un segmentador usando el método [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercollection/methods/add/index).

## **Crear Cortador para una Tabla Dinámica**

Por favor, consulte el siguiente código de ejemplo. Carga el [archivo de Excel de muestra](67338470.xlsx) que contiene la tabla dinámica. Luego crea el rebanador basado en el primer campo de la tabla pivote. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](67338471.xlsx) y [XLSB de salida](67338472.xlsb). La siguiente captura de pantalla muestra el rebanador creado por Aspose.Cells en el archivo de Excel de salida.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-CreateSlicerToPivotTable.cs" >}}

## **Crear Cortador para Tabla de Excel**

Por favor, consulte el siguiente código de ejemplo. Carga el [archivo de Excel de muestra](sampleCreateSlicerToExcelTable.xlsx) que contiene una tabla. Luego crea el rebanador basado en la primera columna. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](outputCreateSlicerToExcelTable.xlsx).

### **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.cs" >}}

## **Temas avanzados**
- [Cambiar propiedades del rebanador](/cells/es/net/change-slicer-properties/)
- [Dibujar un rebanador al renderizar Excel a PDF](/cells/es/net/draw-slicer-while-rendering-excel-to-pdf/)
- [ Formatear rebanador](/cells/es/net/formatting-slicer/)
- [Eliminar rebanador](/cells/es/net/removing-slicer/)
- [Renderización de rebanador](/cells/es/net/rendering-slicer/)
- [Actualización de rebanador](/cells/es/net/updating-slicer/)
{{< app/cells/assistant language="csharp" >}}
