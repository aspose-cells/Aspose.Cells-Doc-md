+++
title = "Encrypting Files in PHP" 
description = "" 
weight = 24900 
+++

Aspose.Cells for .NET : Encrypting Files in PHP  

# Aspose.Cells for .NET : Encrypting Files in PHP


## Aspose.Cells - Encrypt Excel Files

Encrypting a Microsoft Excel File

**PHP Code**

{{< code lang="cs" >}}
        $dataDir = '';
        // Create Aspose.Cells Helper Object
        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');
        // Opening through Path
        // Creating a Workbook object and opening an Excel file using its file path
        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/Book1.xls'));
        $XOR = $ptr->New("Aspose.Cells.EncryptionType.XOR",array());
        $crypt = $ptr->New("Aspose.Cells.EncryptionType.StrongCryptographicProvider",array());
        $ptr->Call($workbook,"SetEncryptionOptions",array($XOR,40));
        $ptr->Call($workbook,"SetEncryptionOptions",array($crypt,128));
        $settings = $ptr->Get($workbook,"Settings",array());
        $ptr->Set($settings,"Password","1234",array());
        $ptr->Call($workbook,"Save",array($dataDir."/encryptedoutBook1.xls"));
        print "Completed." . PHP_EOL;
{{< /code >}}

## Download Running Code

Download **Encrypting Files (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/EncryptingFiles.php)

