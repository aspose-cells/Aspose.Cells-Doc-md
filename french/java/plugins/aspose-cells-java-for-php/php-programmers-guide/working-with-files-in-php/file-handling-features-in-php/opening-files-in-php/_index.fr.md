---
title: Ouverture de fichiers en PHP
type: docs
weight: 10
url: /fr/java/opening-files-in-php/
---

## **Aspose.Cells - Manières simples d'ouvrir des fichiers Excel**
### **Ouverture par chemin**
Ouvrir simplement un fichier Microsoft Excel en référençant le chemin du fichier

**Code PHP**

{{< highlight ruby >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **Ouverture via un flux**
Parfois, le fichier Excel que vous souhaitez ouvrir est stocké sous forme de flux. Dans ce cas, utilisez une version surchargée de la méthode Ouvrir qui prend l'objet Flux qui contient le fichier Excel pour ouvrir le fichier.

**Code PHP**

{{< highlight ruby >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Télécharger **Ouverture de fichiers (Aspose.Cells)** de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
