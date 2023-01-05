---
title: Sauvegarder des fichiers en PHP
type: docs
weight: 20
url: /fr/net/saving-files-in-php/
---
## **Aspose.Cells - Enregistrer les fichiers Excel**
### **Ouverture par chemin**
Enregistrement d'un fichier Excel Microsoft en référençant le chemin du fichier

**Code PHP**

{{< highlight "php" >}}

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
## **Télécharger le code d'exécution**
 Télécharger**Enregistrement de fichiers (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
