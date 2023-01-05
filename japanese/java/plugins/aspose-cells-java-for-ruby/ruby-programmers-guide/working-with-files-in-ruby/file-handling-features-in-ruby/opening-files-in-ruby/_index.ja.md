---
title: Ruby でファイルを開く
type: docs
weight: 10
url: /ja/java/opening-files-in-ruby/
---
## **Aspose.Cells - Excel ファイルを開く簡単な方法**
### **パスを介して開く**
ファイルのパスを参照して、Microsoft Excel ファイルを開くだけです。

**ルビーコード**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **ストリームを介して開く**
開こうとしている Excel ファイルがストリームとして保存されている場合があります。その場合は、Excel ファイルを含む Stream オブジェクトを受け取る Open メソッドのオーバーロード バージョンを使用して、ファイルを開きます。

**ルビーコード**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
