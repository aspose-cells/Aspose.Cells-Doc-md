---
title: Ouverture de fichiers en PHP
type: docs
weight: 10
url: /fr/net/opening-files-in-php/
---

## **Aspose.Cells - Ouvrir des fichiers Excel**
### **Ouverture par chemin**
Ouvrir simplement un fichier Microsoft Excel en référençant le chemin du fichier

**Code PHP**

{{< highlight php >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/Book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Télécharger **Ouverture de fichiers (Aspose.Cells)** de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
