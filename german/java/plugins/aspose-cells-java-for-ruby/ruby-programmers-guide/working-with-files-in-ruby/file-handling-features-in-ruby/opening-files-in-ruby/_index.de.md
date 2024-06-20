---
title: Dateien in Ruby öffnen
type: docs
weight: 10
url: /de/java/opening-files-in-ruby/
---

## **Aspose.Cells - Einfache Möglichkeiten zum Öffnen von Excel-Dateien**
### **Öffnen durch Pfad**
Öffnen Sie einfach eine Microsoft Excel-Datei, indem Sie auf den Dateipfad verweisen

**Ruby-Code**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **Öffnen durch Stream**
Manchmal wird die Excel-Datei, die Sie öffnen möchten, als Stream gespeichert. Verwenden Sie in diesem Fall eine überladene Version der Open-Methode, die das Stream-Objekt enthält, das die Excel-Datei enthält, um die Datei zu öffnen.

**Ruby-Code**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
