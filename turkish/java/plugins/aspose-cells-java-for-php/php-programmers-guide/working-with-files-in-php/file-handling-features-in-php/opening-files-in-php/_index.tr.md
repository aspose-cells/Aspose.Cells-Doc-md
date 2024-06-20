---
title: PHP de Dosyaları Açma
type: docs
weight: 10
url: /tr/java/opening-files-in-php/
---

## **Aspose.Cells - Excel Dosyalarını Açmanın Basit Yolları**
### **Yoluyla Açma**
Bir Microsoft Excel dosyasını basitçe dosyanın yolunu referans vererek açın

PHP Kodu

{{< highlight ruby >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **Akış Üzerinden Açma**
Bazen, açmak istediğiniz Excel dosyası bir akış olarak depolanır. Bu durumda, dosyayı açmak için içeren **Stream** nesnesini alan **Open** metodunun aşırı yüklenmiş bir sürümünü kullanın.

PHP Kodu

{{< highlight ruby >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden **Dosyaları Açma (Aspose.Cells)** örneğini indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
