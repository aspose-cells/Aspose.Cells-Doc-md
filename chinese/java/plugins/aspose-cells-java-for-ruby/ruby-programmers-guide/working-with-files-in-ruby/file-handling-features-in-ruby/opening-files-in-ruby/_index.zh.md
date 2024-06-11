---
title: 在Ruby中打开文件
type: docs
weight: 10
url: /zh/java/opening-files-in-ruby/
---

## **Aspose.Cells - 打开Excel文件的简单方法**
### **通过路径打开**
通过引用文件路径简单地打开Microsoft Excel文件

**Ruby 代码**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **通过流打开**
有时，要打开的Excel文件存储为流。在这种情况下，使用**Stream**对象包含的Excel文件的重载版本的 **Open** 方法来打开文件。

**Ruby 代码**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
