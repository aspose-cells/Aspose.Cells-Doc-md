---
title: PHP de Dosya Kaydetme
type: docs
weight: 20
url: /tr/net/saving-files-in-php/
---

## **Aspose.Cells - Excel Dosyalarını Kaydetme**
### **Yoluyla Açma**
Bir Microsoft Excel dosyasını dosyanın yolunu referans alarak kaydetme

PHP Kodu

{{< highlight php >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array());

        //Your Code goes here for any workbook related operations

        $ptr->Call($workbook,"Save",array($dataDir.'/book1.xls'));

        print "File saved successfully!" . PHP_EOL;

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi bir aşağıda belirtilen sosyal kodlama sitesinden **Dosyaları Kaydetme (Aspose.Cells)**'ı indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
