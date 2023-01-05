---
title: Satır Yüksekliğini ve Sütun Genişliğini Ayarlama
type: docs
weight: 10
url: /tr/java/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Elektronik tablolarla çalışırken ve satırlara veya sütunlara veri eklerken, satırların yüksekliğini veya sütunların genişliğini değiştirmeniz gerekebilir. Bazen satırlara veya sütunlara biçimlendirme uygulamak, verileri göstermek için geçerli yükseklik veya genişliğin değişmesi gerektiği anlamına gelir. Normalde, kullanıcılar bir WYSIWYG ortamında Microsoft Excel kullanarak satır yüksekliklerini ve sütun genişliklerini ayarlar. Ancak, Aspose.Cells ile geliştiriciler bu işlemleri çalışma zamanında gerçekleştirebilir. Satır ve sütun dizinleri 0'dan başlayacaktır.

{{% /alert %}} 
## **Satırlarla Çalışmak**
### **Satır Yüksekliğini Ayarlama**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf bir sağlar[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

 bu[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)koleksiyon, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda daha ayrıntılı olarak tartışılmaktadır.
### **Satır Yüksekliğini Ayarlama**
 çağırarak tek bir satırın yüksekliğini ayarlamak mümkündür.[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonun[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\) ) yöntem. bu[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) yöntemi aşağıdaki parametreleri alır:

- **Satır dizini**, yüksekliğini değiştirdiğiniz satırın dizini.
- **Satır yüksekliği**, satıra uygulanacak satır yüksekliği.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **Tüm Satırların Yüksekliğini Ayarlama**
 Bir çalışma sayfasındaki tüm satırlar için aynı satır yüksekliğini ayarlamak üzere[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonun[setStandartYükseklik](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight)yöntem.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **Sütunlarla Çalışmak**
### **Bir Sütunun Genişliğini Ayarlama**
 öğesini çağırarak bir sütunun genişliğini ayarlayın.[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonun[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\) ) yöntem. bu[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) yöntemi aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliğini değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, istenen sütun genişliği.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **Tüm Sütunların Genişliğini Ayarlama**
 Bir çalışma sayfasındaki tüm sütunlar için aynı sütun genişliğini ayarlamak üzere[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonun[setStandartGenişlik](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth)yöntem.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
