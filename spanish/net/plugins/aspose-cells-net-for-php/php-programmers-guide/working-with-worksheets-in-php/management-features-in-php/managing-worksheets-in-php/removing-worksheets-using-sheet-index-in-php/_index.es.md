---
title: Eliminar hojas de trabajo usando el índice de hojas en PHP
type: docs
weight: 30
url: /es/net/removing-worksheets-using-sheet-index-in-php/
---
## **Eliminación de hojas de cálculo mediante el índice de hojas**
Eliminación de hojas de cálculo mediante el índice de hojas

**Código PHP**

{{< highlight "php" >}}

         $dataDir = '';

        / Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

        $ptr->Call($worksheets,"RemoveAt",array(0));

        $ptr->Call($workbook,"Save",array($dataDir."/output.xls"));

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Eliminación de hojas de cálculo mediante el índice de hojas (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetIndex.php)
