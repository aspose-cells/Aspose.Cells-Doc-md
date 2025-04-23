---
title: Apache POI ve Aspose.Cells kullanarak Yakınlaştırma Faktörü
type: docs
weight: 70
url: /tr/java/zoom-factor-using-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Yakınlaştırma Faktörü**
Microsoft Excel, kullanıcıların bir çalışma sayfasının yakınlaştırma veya ölçek faktörünü ayarlamasını sağlayan bir özellik sağlar. Bu özellik, kullanıcıların çalışma sayfası içeriğini küçük veya büyük görüntülerde görmelerine yardımcı olur.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden Workbook adlı bir sınıf sağlar. Workbook sınıfı, bir Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir WorksheetCollection içerir.

Bir çalışma sayfası, Worksheet sınıfı tarafından temsil edilir. Worksheet sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir çalışma sayfasının yakınlaştırma faktörünü ayarlamak için, Worksheet sınıfının setZoom yöntemini kullanın.

**Java**

{{< highlight java >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Yakınlaştırma Faktörü**
Apache POI, Sheet.setZoom() yöntemiyle yakınlaştırma özelliğini sağlar.

**Java**

{{< highlight java >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)
{{< app/cells/assistant language="java" >}}
