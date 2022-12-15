---
title: Sauvegarder des fichiers en PHP
type: docs
weight: 20
url: /fr/java/saving-files-in-php/
---
## **Aspose.Cells - Enregistrement de fichiers**
### **Enregistrement du fichier à un emplacement**
 Si les développeurs ont besoin d'enregistrer leurs fichiers à l'aide de**Aspose.Cells Java for PHP** à un emplacement de stockage, ils peuvent simplement spécifier le nom du fichier (avec son chemin de stockage complet) et le format de fichier souhaité (en utilisant le**TypeFormatFichier**énumération) en appelant le**enregistrer**méthode de**Cahier**objet.

**Code PHP**

{{< highlight "php" >}}

 $fileFormatType = new FileFormatType();

//Creating an Workbook object with an Excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Save in default (Excel2003) format

$workbook->save($dataDir . "book.default.out.xls");

//Save in Excel2003 format

$workbook->save($dataDir . "book.out.xls",$fileFormatType->EXCEL_97_TO_2003);

//Save in Excel2007 xlsx format

$workbook->save($dataDir . "book.out.xlsx", $fileFormatType->XLSX);

//Save in SpreadsheetML format

$workbook->save($dataDir . "book.out.xml", $fileFormatType->EXCEL_2003_XML);

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Enregistrement de fichiers (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
