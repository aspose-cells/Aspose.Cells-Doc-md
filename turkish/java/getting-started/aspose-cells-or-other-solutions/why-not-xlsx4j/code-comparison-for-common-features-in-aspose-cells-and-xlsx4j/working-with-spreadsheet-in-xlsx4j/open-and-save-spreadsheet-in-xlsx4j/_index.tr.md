---
title: xlsx4j de Elektronik Tablo Açma ve Kaydetme
type: docs
weight: 40
url: /tr/java/open-and-save-spreadsheet-in-xlsx4j/
---

## **Aspose.Cells - Elektronik Tablo Açma ve Kaydetme**
Geliştiriciler, farklı amaçlar için Aspose.Cells'i kullanır. Örneğin, bir dosyayı verileri almak için açabilir veya geliştirme sürecinizi hızlandırmak için önceden tanımlanmış bir tasarımcı elektronik tablo dosyasını kullanabilirsiniz. Aspose.Cells, geliştiricilere farklı türdeki kaynak dosyalarını açmalarına olanak tanır. Bu kaynak dosyaları Microsoft Excel raporları, Elektronik Tablo Dili, CSV veya Sekme Aralıklı dosyalar olabilir. 

**Aspose.Cells**, esnek API'si kullanılarak sıfırdan Excel dosyaları oluşturmak için geliştiricilere olanak tanır. Excel dosyaları oluşturduktan sonra, çalışma kitabınızı (dosyayı) kaydetmeniz de gerekecektir. Aspose.Cells, bu dosyaları kaydetmek için çeşitli yöntemler sunar.

**Java**

{{< highlight java >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j - Elektronik Tablo Açma ve Kaydetme**
Aşağıdaki örnek, xlsx4j kullanarak elektronik tabloları nasıl açıp kaydedebileceğinizi göstermektedir.

**Java**

{{< highlight java >}}

 String inputfilepath  = dataDir + "pivot.xlsm";

boolean save = true;

String outputfilepath = dataDir + "pivot-rtt-xlsx4j.xlsm";

// Open a document from the file system

// 1. Load the Package

OpcPackage pkg = OpcPackage.load(new java.io.File(inputfilepath));

// Save it

if (save) {

    SaveToZipFile saver = new SaveToZipFile(pkg);

    saver.save(outputfilepath);

}

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/opensavespreadsheet)
