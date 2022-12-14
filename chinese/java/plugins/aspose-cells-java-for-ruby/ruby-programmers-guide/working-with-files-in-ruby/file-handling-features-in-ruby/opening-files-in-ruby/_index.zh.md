---
title: 在 Ruby 中打开文件
type: docs
weight: 10
url: /zh/java/opening-files-in-ruby/
---
## **Aspose.Cells - 打开 Excel 文件的简单方法**
### **通过路径打开**
只需通过引用文件路径打开 Microsoft Excel 文件

**红宝石代码**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **通过流打开**
有时，您要打开的 Excel 文件存储为流。在这种情况下，请使用 Open 方法的重载版本，该方法采用包含 Excel 文件的 Stream 对象来打开文件。

**红宝石代码**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
