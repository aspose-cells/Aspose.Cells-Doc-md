---
title: Apache POI ve Aspose.Cells te Sabit Dondurulan Panolar
type: docs
weight: 80
url: /tr/java/freeze-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Panoları Sabitleme**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) adlı bir sınıf sağlar. Workbook sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir WorksheetCollection içerir.

Bir çalışma sayfası, [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) sınıfı ile temsil edilir. Worksheet sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Sabit dondurma panolarını yapılandırmak için Worksheet sınıfının freezePanes metodunu çağırın. FreezePanes metodu şu parametreleri alır:

- **Satır**, dondurulmanın başlayacağı hücrenin satır indeksi.
- **Sütun**, dondurulmanın başlayacağı hücrenin sütun indeksi.
- **Dondurulan satırlar**, üst bölmedeki görünür satır sayısı.
- **Dondurulan sütunlar**, sol bölmedeki görünür sütun sayısı

**Java**

{{< highlight java >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Sabit Dondurulan Panolar**
Apache POI SS - HSSF ve XSSF kullanılırken FreezePane işlevselliğine ulaşmak için sheet.createFreezePane kullanılabilir

**Java**

{{< highlight java >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Sabit Dondurulan Panolar](http://docs.aspose.com:8082/docs/display/cellsjava/Sabit+Dondurulan+Panolar) sayfasını ziyaret edin.

{{% /alert %}}
