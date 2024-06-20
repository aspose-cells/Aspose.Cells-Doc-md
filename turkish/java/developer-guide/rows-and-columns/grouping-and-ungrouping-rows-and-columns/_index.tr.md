---
title: Satır ve Sütunları Gruplandırma ve Grubu Çözme
type: docs
weight: 40
url: /tr/java/grouping-and-ungrouping-rows-and-columns/
---

## **Giriş**
Bir Microsoft Excel dosyasında, veriler için bir biçim oluşturarak tek bir fare tıklamasıyla ayrıntı seviyelerini gösterip gizleyebilirsiniz.

Yalnızca özetler veya başlıkların bulunduğu satırları veya sütunları hızlı bir şekilde görüntülemek için **Özet Sembolleri**, 1,2,3, + ve - simgelerine tıklayabilirsiniz veya simgeleri kullanarak bir çalışma sayfasındaki bir bölümün altındaki ayrıntıları görebilirsiniz, aşağıdaki şekilde gösterildiği gibi:

Satır ve sütunların gruplandırılması 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)
## **Satır ve Sütunların Grup Yönetimi**
Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) adlı bir sınıf sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişime izin veren [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) koleksiyonunu içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunu sağlar.

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonu, çalışma sayfasındaki satırları veya sütunları yönetmek için birkaç yöntem sağlar, bunlardan bazıları ayrıntılı olarak aşağıda ele alınmıştır.
### **Satır ve Sütunların Gruplandırılması**
[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunu arayarak [groupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\)) ve [groupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\)) yöntemlerini çağırarak satırları veya sütunları gruplamak mümkündür. Her iki yöntem de aşağıdaki parametreleri alır:

- İlk satır/sütun indeksi, grup içindeki ilk satır veya sütun.
- Son satır/sütun indeksi, grup içindeki son satır veya sütun.
- Gizli mi, satırları/sütunları gruplandırmadan sonra gizlemek için bir Boolean parametre.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **Grup Ayarları**
Microsoft Excel ayrıca gösterilmesi için grup ayarlarını yapılandırmanıza izin verir:

- Detayın altında özet satırlar.
- Detayın sağında özet sütunları.

**Grup ayarları** 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_2.png)

Bu grup ayarlarını, Çalışma Sayfası sınıfının Anahat özelliğini kullanarak yapılandırmak mümkündür.
### **Detayın Altında Özet Satırlar**
Geliştiriciler, [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) sınıfının [SummaryRowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) yöntemini kullanarak detayın altında özet satırların görüntülenmesini kontrol edebilirler.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **Detayın Sağına Özet Sütunlar**
[Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) sınıfının [SummaryColumnRight](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight) yöntemi ile özet sütunlarının detayın sağına gösterilip gösterilmeyeceği kontrol edilebilir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **Satır ve Sütunların Grubunu Çıkarma**
Gruplandırılmış satır veya sütunları [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunun [UngroupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\)) ve [UngroupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\)) yöntemlerini çağırarak çözebilirsiniz. Her iki yöntem de aynı parametreleri alır:

- İlk satır veya sütun dizini, ayrılmak istenen ilk satır/sütun.
- Son satır veya sütun dizini, ayrılmak istenen son satır/sütun.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
