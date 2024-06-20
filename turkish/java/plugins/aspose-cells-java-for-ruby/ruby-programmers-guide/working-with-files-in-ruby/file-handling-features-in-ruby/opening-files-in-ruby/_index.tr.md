---
title: Ruby de Dosyaları Açma
type: docs
weight: 10
url: /tr/java/opening-files-in-ruby/
---

## **Aspose.Cells - Excel Dosyalarını Açmanın Basit Yolları**
### **Yoluyla Açma**
Bir Microsoft Excel dosyasını basitçe dosyanın yolunu referans vererek açın

**Ruby Kodu**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **Akış Üzerinden Açma**
Bazen, açmak istediğiniz Excel dosyası bir akış olarak depolanır. Bu durumda, dosyayı açmak için içeren **Stream** nesnesini alan **Open** metodunun aşırı yüklenmiş bir sürümünü kullanın.

**Ruby Kodu**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
