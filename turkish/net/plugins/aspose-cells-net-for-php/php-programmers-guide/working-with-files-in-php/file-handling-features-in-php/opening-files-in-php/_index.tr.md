---
title: PHP de Dosyaları Açma
type: docs
weight: 10
url: /tr/net/opening-files-in-php/
---

## **Aspose.Cells - Excel Dosyalarını Açma**
### **Yoluyla Açma**
Bir Microsoft Excel dosyasını basitçe dosyanın yolunu referans vererek açın

PHP Kodu

{{< highlight php >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/Book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden **Dosyaları Açma (Aspose.Cells)** örneğini indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
