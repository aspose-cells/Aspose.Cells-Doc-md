---
title: تحويل Excel إلى PDF في PHP
type: docs
weight: 20
url: /ar/net/excel-to-pdf-conversion-in-php/
---

## **Aspose.Cells - تحويل Excel إلى PDF**
تحويل ملف Excel لمايكروسوفت إلى PDF

**كود PHP**

{{< highlight php >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/Book1.xls'));

        $ptr->Call($workbook,"Save",array($dataDir."/outBook1.pdf"));

        print "Conversion Completed" . PHP_EOL;

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **تحويل Excel إلى PDF (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PDFConversion.php)
