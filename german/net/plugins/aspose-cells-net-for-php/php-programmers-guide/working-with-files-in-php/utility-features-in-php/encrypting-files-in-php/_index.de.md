---
title: Verschlüsseln von Dateien in PHP
type: docs
weight: 10
url: /de/net/encrypting-files-in-php/
---

## **Aspose.Cells - Excel-Dateien verschlüsseln**
Verschlüsseln einer Microsoft Excel-Datei

**PHP-Code**

{{< highlight php >}}

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

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Dateien verschlüsseln (Aspose.Cells)** von einer der unten genannten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/EncryptingFiles.php)
