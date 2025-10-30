---
title: Insertar rebanador
linktitle: Rebanadores
type: docs
weight: 170
url: /es/nodejs-cpp/create-slicer/
description: Gestionar cortadores de archivos de Excel con Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**

Un cortador se usa para filtrar datos rápidamente. Puede usarse para filtrar datos tanto en una tabla como en una tabla dinámica. Microsoft Excel permite crear cortadores seleccionando una tabla o tabla dinámica y luego haciendo clic en *Insertar > Cortador*. Aspose.Cells for Node.js via C++ también permite crear cortadores usando el método [**Worksheet.getSlicers().add()**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#add-pivottable-string-string-).

## **Crear Cortador para una Tabla Dinámica**

Por favor, vea el siguiente código de ejemplo. Carga el [archivo de Excel de muestra](67338470.xlsx) que contiene la tabla dinámica. Luego crea el cortador basado en el primer campo pivote base. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](67338471.xlsx) y [XLSB de salida](67338472.xlsb). La siguiente captura de pantalla muestra el cortador creado por Aspose.Cells for Node.js via C++ en el archivo de Excel de salida.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Código de muestra**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToPivotTable.js" >}}

## **Crear Cortador para Tabla de Excel**

Por favor, consulte el siguiente código de ejemplo. Carga el [archivo de Excel de muestra](sampleCreateSlicerToExcelTable.xlsx) que contiene una tabla. Luego crea el rebanador basado en la primera columna. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](outputCreateSlicerToExcelTable.xlsx).

### **Código de muestra**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToExcelTable-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
