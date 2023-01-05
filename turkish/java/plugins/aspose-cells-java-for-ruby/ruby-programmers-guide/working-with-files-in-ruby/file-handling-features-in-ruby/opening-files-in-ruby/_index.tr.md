---
title: Dosyaları Ruby'de Açmak
type: docs
weight: 10
url: /tr/java/opening-files-in-ruby/
---
## **Aspose.Cells - Excel Dosyalarını Açmanın Basit Yolları**
### **Yoldan Açma**
Dosyanın yoluna başvurarak bir Microsoft Excel dosyasını açmanız yeterlidir

**Yakut Kodu**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **Akış yoluyla açma**
Bazen açmak istediğiniz Excel dosyası bir akış olarak saklanır. Bu durumda, dosyayı açmak için Excel dosyasını içeren Akış nesnesini alan Open yönteminin aşırı yüklenmiş bir sürümünü kullanın.

**Yakut Kodu**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
