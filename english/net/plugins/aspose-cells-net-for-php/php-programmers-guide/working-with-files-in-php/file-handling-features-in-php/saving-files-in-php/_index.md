---
title: Saving Files in PHP
type: docs
weight: 20
url: /net/saving-files-in-php/
---

## **Aspose.Cells - Save Excel Files**
### **Opening through Path**
Saving a Microsoft Excel file by referencing the file's path

**PHP Code**

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
## **Download Running Code**
Download **Saving Files (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
