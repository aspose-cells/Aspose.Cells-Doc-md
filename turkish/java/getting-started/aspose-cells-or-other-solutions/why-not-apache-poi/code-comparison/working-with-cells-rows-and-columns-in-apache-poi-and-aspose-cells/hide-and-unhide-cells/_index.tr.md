---
title: Hücreleri Gizle ve Göster
type: docs
weight: 30
url: /tr/java/hide-and-unhide-cells/
---

## **Aspose.Cells - Satırları ve Sütunları Gizle ve Göster**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) adlı bir sınıf sağlar. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir WorksheetCollection içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı ile temsil edilir. Worksheet sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir Cells koleksiyonu sağlar. Cells koleksiyonu, çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar. 

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

cells.hideRow(2); //Hiding the 3rd row of the worksheet

cells.hideColumn(1); //Hiding the 2nd column of the worksheet

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Hücreleri Gizle / Göster**
Bir satırı veya sütunu gizlemek için, Apache POI SS, Row.setZeroHeight(boolean) yöntemini sağlar.

**Java**

{{< highlight java >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet();

Row row = sheet.createRow(0);

row.setZeroHeight(true);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/hideunhidecells)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Satır ve Sütunları Gizleme ve Gösterme](/java/satir-ve-sutunlari-gizleme-ve-gosterme) sayfasını ziyaret edin.

{{% /alert %}}
