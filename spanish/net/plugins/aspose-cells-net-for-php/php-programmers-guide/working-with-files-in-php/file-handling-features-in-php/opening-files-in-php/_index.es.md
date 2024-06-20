---
title: Abrir Archivos en PHP
type: docs
weight: 10
url: /es/net/opening-files-in-php/
---

## **Aspose.Cells - Abrir Archivos de Excel**
### **Apertura a través de la Ruta**
Simplemente abre un archivo de Microsoft Excel haciendo referencia a la ruta del archivo

**Código PHP**

{{< highlight php >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/Book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Apertura de Archivos (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
