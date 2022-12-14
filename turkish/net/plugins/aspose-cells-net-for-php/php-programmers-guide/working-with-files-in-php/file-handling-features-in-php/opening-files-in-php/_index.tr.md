---
title: Dosyaları PHP'de Açmak
type: docs
weight: 10
url: /tr/net/opening-files-in-php/
---
## **Aspose.Cells - Excel Dosyalarını Aç**
### **Yoldan Açma**
Dosyanın yoluna başvurarak bir Microsoft Excel dosyasını açmanız yeterlidir

**PHP Kodu**

{{< highlight "php" >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/Book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Dosyaları Açma (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
