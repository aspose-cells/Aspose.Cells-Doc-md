---
title: Ouvrir des fichiers en Ruby
type: docs
weight: 10
url: /fr/java/opening-files-in-ruby/
---

## **Aspose.Cells - Manières simples d'ouvrir des fichiers Excel**
### **Ouverture par chemin**
Ouvrir simplement un fichier Microsoft Excel en référençant le chemin du fichier

**Code Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **Ouverture via un flux**
Parfois, le fichier Excel que vous souhaitez ouvrir est stocké sous forme de flux. Dans ce cas, utilisez une version surchargée de la méthode Ouvrir qui prend l'objet Flux qui contient le fichier Excel pour ouvrir le fichier.

**Code Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
