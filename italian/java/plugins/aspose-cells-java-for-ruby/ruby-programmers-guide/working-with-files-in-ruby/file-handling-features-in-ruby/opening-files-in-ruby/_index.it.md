---
title: Apertura di file in Ruby
type: docs
weight: 10
url: /it/java/opening-files-in-ruby/
---
## **Aspose.Cells - Semplici modi per aprire file Excel**
### **Apertura attraverso il percorso**
Basta aprire un file Microsoft Excel facendo riferimento al percorso del file

**Codice Rubino**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **Apertura tramite Stream**
volte, il file Excel che desideri aprire viene archiviato come flusso. In tal caso, utilizzare una versione di overload del metodo Open che accetta l'oggetto Stream che contiene il file Excel per aprire il file.

**Codice Rubino**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
