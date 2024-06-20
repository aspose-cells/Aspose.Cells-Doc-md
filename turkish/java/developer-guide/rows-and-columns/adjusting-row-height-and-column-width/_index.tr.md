---
title: Satır Yüksekliğini ve Sütun Genişliğini Ayarlama
type: docs
weight: 10
url: /tr/java/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

E-tablolarıyla çalışırken veri ekleyip sütunlara veya satırlara veri eklediğinizde, satırların yüksekliğini veya sütunların genişliğini değiştirmeniz gerekebilir. Bazen satırlara veya sütunlara biçimlendirme uygulamak, mevcut yüksekliğin veya genişliğin veriyi gösterebilmesi için değişmesi anlamına gelir. Normalde, kullanıcılar sıradan biçimde WYSIWYG ortamında Microsoft Excel kullanarak satır yüksekliklerini ve sütun genişliklerini ayarlar. Ancak Aspose.Cells geliştiricileri bu işlemleri çalışma zamanında yapabilirler. Satır ve sütunların dizinleri 0'dan başlayacaktır.

{{% /alert %}} 
## **Satırlarla Çalışmak**
### **Satır Yüksekliğini Ayarlamak**
Aspose.Cells, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) adında bir Microsoft Excel dosyasını temsil eden bir sınıf sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) içerir. Bir çalışma sayfası [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) kolleksiyonu sağlar.

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) kolleksiyonu, çalışma sayfasındaki satırları veya sütunları yönetmek için birçok yöntem sağlar. Bunlardan bazıları aşağıda daha detaylı bir şekilde tartışılmaktadır.
### **Satır Yüksekliğini Ayarlamak**
Tek bir satırın yüksekliğini ayarlamak için [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) kolleksiyonunun [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) yöntemini çağırarak ayarlanabilir. [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) yöntemi aşağıdaki parametreleri alır:

- **Satır dizini**, yüksekliği değiştirdiğiniz satırın dizini.
- **Satır yüksekliği**, satıra uygulanan satır yüksekliği.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **Tüm Satırların Yüksekliğini Ayarlamak**
Bir çalışma sayfasındaki tüm satırlar için aynı satır yüksekliğini ayarlamak için [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) kolleksiyonunun [setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight) yöntemini kullanın.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **Sütunlarla Çalışmak**
### **Bir Sütunun Genişliğini Ayarlamak**
Bir sütunun genişliğini, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) kolleksiyonunun [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) yöntemini çağırarak ayarlayın. [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) yöntemi aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliği değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, istenen sütun genişliği.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **Tüm Sütunların Genişliğini Ayarlamak**
Bir çalışma sayfasındaki tüm sütunlar için aynı sütun genişliğini ayarlamak için [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) kolleksiyonunun [setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth) yöntemini kullanın.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
