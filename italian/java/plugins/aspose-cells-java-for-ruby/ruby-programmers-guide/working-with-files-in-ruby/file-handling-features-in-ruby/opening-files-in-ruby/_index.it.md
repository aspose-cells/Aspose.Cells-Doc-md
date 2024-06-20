---
title: Apertura file in Ruby
type: docs
weight: 10
url: /it/java/opening-files-in-ruby/
---

## **Aspose.Cells - Modi semplici per aprire file Excel**
### **Apertura attraverso percorso**
Apri semplicemente un file Microsoft Excel facendo riferimento al percorso del file

**Codice Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **Apertura tramite flusso**
A volte, il file Excel che si desidera aprire è memorizzato come stream. In tal caso, utilizzare una versione sovraccaricata del metodo Open che prende l'oggetto Stream che contiene il file Excel per aprire il file.

**Codice Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
