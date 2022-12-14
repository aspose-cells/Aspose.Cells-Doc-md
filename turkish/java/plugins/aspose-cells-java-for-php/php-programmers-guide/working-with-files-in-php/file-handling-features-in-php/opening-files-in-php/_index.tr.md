---
title: Dosyaları PHP'de Açmak
type: docs
weight: 10
url: /tr/java/opening-files-in-php/
---
## **Aspose.Cells - Excel Dosyalarını Açmanın Basit Yolları**
### **Yoldan Açma**
Dosyanın yoluna başvurarak bir Microsoft Excel dosyasını açmanız yeterlidir

**PHP Kodu**

{{< highlight "ruby" >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **Akış yoluyla açma**
Bazen açmak istediğiniz Excel dosyası bir akış olarak saklanır. Bu durumda, dosyayı açmak için Excel dosyasını içeren Akış nesnesini alan Open yönteminin aşırı yüklenmiş bir sürümünü kullanın.

**PHP Kodu**

{{< highlight "ruby" >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Dosyaları Açma (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
