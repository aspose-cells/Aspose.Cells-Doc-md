---
title: Открытие файлов в Ruby
type: docs
weight: 10
url: /ru/java/opening-files-in-ruby/
---
## **Aspose.Cells - Простые способы открытия файлов Excel**
### **Открытие через Путь**
Просто откройте файл Excel Microsoft, указав путь к файлу.

**Рубиновый код**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **Открытие через поток**
Иногда файл Excel, который вы хотите открыть, хранится в виде потока. В этом случае используйте перегруженную версию метода Open, который принимает объект Stream, содержащий файл Excel, для открытия файла.

**Рубиновый код**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
