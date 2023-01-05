---
title: Öppna filer i Ruby
type: docs
weight: 10
url: /sv/java/opening-files-in-ruby/
---
## **Aspose.Cells - Enkla sätt att öppna Excel-filer**
### **Öppning genom vägen**
Öppna helt enkelt en Microsoft Excel-fil genom att referera till filens sökväg

**Ruby kod**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **Öppnas genom Stream**
Ibland lagras Excel-filen som du vill öppna som en ström. Använd i så fall en överbelastad version av Open-metoden som tar Stream-objektet som innehåller Excel-filen för att öppna filen.

**Ruby kod**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
