---
title: Открытие Файлов в Ruby
type: docs
weight: 10
url: /ru/java/opening-files-in-ruby/
---

## **Aspose.Cells - Простые Способы Открытия Файлов Excel**
### **Открытие через путь**
Просто откройте файл Microsoft Excel, указав путь к файлу

**Код на Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **Открытие через Поток**
Иногда файл Excel, который вы хотите открыть, хранится как поток. В этом случае используйте перегруженную версию метода Открыть, который принимает объект Поток, содержащий файл Excel, чтобы открыть файл.

**Код на Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
