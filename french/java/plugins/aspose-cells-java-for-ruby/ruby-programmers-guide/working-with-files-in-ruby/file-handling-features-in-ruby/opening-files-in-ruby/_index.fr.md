---
title: Ouverture de fichiers dans Ruby
type: docs
weight: 10
url: /fr/java/opening-files-in-ruby/
---
## **Aspose.Cells - Façons simples d'ouvrir des fichiers Excel**
### **Ouverture par chemin**
Ouvrez simplement un fichier Excel Microsoft en référençant le chemin du fichier

**Code rubis**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **Ouverture via Stream**
Parfois, le fichier Excel que vous souhaitez ouvrir est stocké sous forme de flux. Dans ce cas, utilisez une version surchargée de la méthode Open qui prend l'objet Stream qui contient le fichier Excel pour ouvrir le fichier.

**Code rubis**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
