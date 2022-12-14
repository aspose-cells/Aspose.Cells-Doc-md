---
title: Apache POI ve Aspose.Cells'de Bölmeleri Dondur
type: docs
weight: 80
url: /tr/java/freeze-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Bölmeleri Dondur**
Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)bu bir Microsoft Excel dosyasını temsil eder. Workbook sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir WorksheetCollection içerir.

Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)sınıf. Worksheet sınıfı, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Dondurma bölmelerini yapılandırmak için Worksheet sınıfının frozenPanes yöntemini çağırın. FreezePanes yöntemi aşağıdaki parametreleri alır:

- **Sıra**, dondurmanın başlayacağı hücrenin satır dizini.
- **Kolon**, dondurmanın başlayacağı hücrenin sütun dizini.
- **Donmuş satırlar**, üst bölmedeki görünür satırların sayısı.
- **Dondurulmuş sütunlar**, sol bölmedeki görünür sütunların sayısı

**Java**

{{< highlight "java" >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Bölmeleri Dondur**
Sheet.createFreezePane, Apache POI SS - HSSF ve XSSF kullanırken FreezePane işlevselliğini elde etmek için kullanılabilir

**Java**

{{< highlight "java" >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/Java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Donma bölmeleri](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes).

{{% /alert %}}
