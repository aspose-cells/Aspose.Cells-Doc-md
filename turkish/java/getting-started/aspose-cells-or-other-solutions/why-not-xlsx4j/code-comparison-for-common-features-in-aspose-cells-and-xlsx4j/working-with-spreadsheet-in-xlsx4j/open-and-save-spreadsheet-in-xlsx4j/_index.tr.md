---
title: Elektronik Tabloyu xlsx4j'de Açın ve Kaydedin
type: docs
weight: 40
url: /tr/java/open-and-save-spreadsheet-in-xlsx4j/
---
## **Aspose.Cells - Elektronik Tabloyu Aç ve Kaydet**
Geliştiriciler, dosyaları farklı amaçlarla açmak için Aspose.Cells'i kullanır. Örneğin, bir dosyadan veri almak için açın veya geliştirme sürecinizi hızlandırmak için önceden tanımlanmış bir tasarımcı elektronik tablo dosyası kullanın. Aspose.Cells, geliştiricilerin farklı türde kaynak dosyaları açmasına olanak tanır. Bu kaynak dosyalar Microsoft Excel raporları, SpreadsheetML, CSV veya Sekmeyle Ayrılmış dosyalar olabilir.

**Aspose.Cells**geliştiricilerin esnek API'i kullanarak sıfırdan Excel dosyaları oluşturmasına olanak tanır. Excel dosyalarını oluşturduktan sonra çalışma kitabınızı (dosyayı) da kaydetmeniz gerekir. Aspose.Cells, bu dosyaları kaydetmenin çeşitli yollarını sunar.

**Java**

{{< highlight "java" >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j - Elektronik Tabloyu Aç ve Kaydet**
Aşağıdaki örnek, xlsx4j kullanırken elektronik tabloların nasıl açılacağını ve kaydedileceğini gösterir.

**Java**

{{< highlight "java" >}}

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
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/opensavespreadsheet)
