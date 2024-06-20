---
title: Rubyでファイルを開く
type: docs
weight: 10
url: /ja/java/opening-files-in-ruby/
---

## **Aspose.Cells - Excelファイルを開く簡単な方法**
### **ファイルのパスを通じて開く**
単純に、Microsoft Excelファイルをファイルのパスを参照して開きます

**Ruby Code**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **ストリームを介した開く**
開きたいExcelファイルがストリームとして保存されている場合は、Excelファイルを含むStreamオブジェクトを取る**Open**メソッドのオーバーロードバージョンを使用してファイルを開きます。

**Ruby Code**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
