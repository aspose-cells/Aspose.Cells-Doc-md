---
title: Apache POI ve Aspose.Cells'de Bölme Bölmeleri
type: docs
weight: 70
url: /tr/java/split-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Bölmeli Bölmeler**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir Çalışma Kitabı sınıfı sağlar. Workbook sınıfı, Excel dosyalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Bölünmüş görünümler uygulamak için Worksheet sınıfının split yöntemini kullanın. Bölünmüş bölmeleri kaldırmak için removeSplit yöntemini kullanın.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Bölünmüş Bölmeler**
Bölünmüş Bölmeler işlevi, Apache POI SS (HSSF & XSSF) API kullanılırken createSplitPane yöntemiyle elde edilebilir

**Java**

{{< highlight "java" >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Bölme Bölmeleri](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}
