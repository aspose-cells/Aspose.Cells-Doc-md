---
title: Satırları ve Sütunları Gizleme ve Gösterme
type: docs
weight: 50
url: /tr/java/hiding-and-showing-rows-and-columns/
---
## **Giriş**
Bazen, kullanıcılar tarafından çalışma sayfasının belirli satırlarını veya sütunlarını gizlemek ve daha sonra bunları görüntülemek de gerekebilir. Microsoft Excel bu özelliği sağlar ve Aspose.Cells gibi.
## **Satırların ve Sütunların Görünürlüğünü Kontrol Etme**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf bir sağlar[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon. bu[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)[](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)koleksiyon, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda tartışılmaktadır.
### **Satırları veya Sütunları Gizleme**
 Geliştiriciler, çağırarak bir satırı veya sütunu gizleyebilirsiniz.[Satırı Gizle](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow\(int\) ) ve[Sütunu Gizle](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn\(int\) ) yöntemleri[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)sırasıyla koleksiyon. Her iki yöntem de belirli satır veya sütunu gizlemek için satır/sütun dizinini parametre olarak alır.

{{% alert color="primary" %}} 

Not: Sırasıyla satır yüksekliğini veya sütun genişliğini 0 olarak ayarlarsak, bir satırı veya sütunu gizlemek de mümkündür.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Satırları ve Sütunları Gösterme**
 Geliştiriciler, çağırarak herhangi bir gizli satırı veya sütunu gösterebilir.[Satırı Göster](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow\(int,%20double\) ) ve[Sütunu Göster](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn\(int,%20double\) ) yöntemleri[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)sırasıyla koleksiyon. Her iki yöntem de iki parametre alır:

- **Satır veya sütun dizini** - belirli bir satır veya sütunu göstermek için kullanılan bir satır veya sütun dizini.
- **Satır yüksekliği veya sütun genişliği** - gösterildikten sonra satıra veya sütuna atanan satır yüksekliği veya sütun genişliği.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

Gizli bir sütunu/satırı görünür hale getirirken, daha önce atanmış genişliğe veya yüksekliğe veya orijinal genişliğine veya yüksekliğine geri döndürmeniz gerekirse, lütfen negatif genişlik veya yüksekliğe sahip sütunu veya satırı gösterin. Örneğin, worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
