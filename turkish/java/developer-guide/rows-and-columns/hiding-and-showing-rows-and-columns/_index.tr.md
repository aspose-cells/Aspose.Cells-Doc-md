---
title: Satır ve Sütunları Gizleme ve Gösterme
type: docs
weight: 50
url: /tr/java/hiding-and-showing-rows-and-columns/
---

## **Giriş**
Bazı durumlarda, çalışma sayfasının belirli satır veya sütunlarını gizlemek ve daha sonra göstermek gerekebilir. Bu özelliği Microsoft Excel sağladığı gibi Aspose.Cells de sağlar.
## **Satır ve Sütunların Görünürlüğünü Kontrol Etme**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonu sağlar. [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonu, çalışma sayfasındaki satır veya sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda tartışılmıştır.
### **Satır veya Sütunları Gizleme**
Geliştiriciler, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunun [HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow-int-) ve [HideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn-int-) metodlarını çağırarak satır veya sütunu gizleyebilirler. Her iki yöntem de gizlenecek satır/sütunun indeksini parametre olarak alır.

{{% alert color="primary" %}} 

Not: Bir satır veya sütunu gizlemek için sırasıyla satır yüksekliğini veya sütun genişliğini 0 olarak ayarlarsak da mümkündür.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Satır ve Sütunları Gösterme**
Geliştiriciler, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunun [UnhideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow-int-double-) ve [UnhideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn-int-double-) metodlarını çağırarak herhangi bir gizli satır veya sütunu gösterilebilir. Her iki yöntem de iki parametre alır:

- **Satır veya sütun dizini** - belirli bir satır veya sütunun gösterilmesi için kullanılan dizin.
- **Satır yüksekliği veya sütun genişliği** - Gösterildikten sonra satır veya sütuna atanan satır yüksekliği veya sütun genişliği.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

Gizlenmiş bir sütunu/satırı görünür hale getirirken, onu önceden atanan genişliğe veya yüksekliğe veya orijinal genişliğe veya yüksekliğe geri döndürmeniz gerekiyorsa, lütfen sütunu veya satırı negatif genişlik veya yükseklikle görünmez yapın. Örneğin, worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
