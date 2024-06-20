---
title: Elemanları Göster ve Gizle
type: docs
weight: 60
url: /tr/java/show-and-hide-elements/
---

{{% alert color="primary" %}}

Aspose.Cells, çalışma kitabının elemanlarını, çalışma sayfalarını, satırları, sütunları, sekmeleri, kaydırmaları, ızgaraları gösterip gizlemek için kullanıcıya olanak tanır.

{{% /alert %}}

## **Bir Çalışma Sayfasını Gösterme ve Gizleme**

Bir Excel dosyasında bir veya birden fazla çalışma sayfası olabilir. Excel dosyası oluşturduğumuzda, içinde çalıştığımız Excel dosyasına çalışma sayfaları ekleriz. Bir Excel dosyasındaki her çalışma sayfası kendi veri ve biçimlendirme ayarları gibi diğer çalışma sayfalarından bağımsızdır. Bazı durumlarda, geliştiriciler kendi ilgileri için Excel dosyalarındaki birkaç çalışma sayfasını gizlemek ve diğerlerini göstermek isteyebilirler. **Aspose.Cells** bu nedenle geliştiricilere Excel dosyalarında çalışma sayfalarının görünürlüğünü kontrol etme imkanı sunar.

**Çalışma Sayfalarının Görünürlüğünü Kontrol Etme:**

Aspose.Cells, bir Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişime olanak tanıyan bir [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş bir yelpazede özellik ve yöntem sağlar. Ancak, bir çalışma sayfasının görünürlüğünü kontrol etmek için, geliştiriciler [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) yöntemini kullanabilirler.

### **Bir Çalışma Sayfasını Görünür Yapma**

Geliştiriciler, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) yöntemine parametre olarak **true** geçirerek bir çalışma sayfasını görünür hale getirebilirler.

### **Bir Çalışsayıyı Gizleme**

Geliştiriciler, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) yöntemine parametre olarak **false** geçirerek bir çalışma sayfasını gizleyebilirler.

**Örnek:**

Aşağıda, Excel dosyasının ilk çalışma sayfasını gizlemek için [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**setVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) yönteminin kullanımını gösteren tam bir örnek verilmiştir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**Düzenlemeden Önce Çalışma Sayfası:**

Aşağıdaki ekran görüntüsünde, **Book1.xls** dosyasının üç çalışma sayfası olan **Sheet1**, **Sheet2** ve **Sheet3** içerdiğini görebilirsiniz.

![todo:image_alt_text](show-and-hide-elements_1.png)

**Şekil:** Herhangi bir değişiklik öncesi çalışma sayfası görünümü

**Düzenleme Örneği Kodu Çalıştırıldıktan Sonra Çalışma Sayfası:**

**Book1.xls** dosyası [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı kullanılarak açılır ve ardından **Book1.xls** dosyasının ilk çalışma sayfası gizlenir. Değiştirilmiş dosya **output.xls** olarak kaydedilir ve aşağıda görsel görünümü gösterilmiştir:

![todo:image_alt_text](show-and-hide-elements_2.png)

**Şekil:** Değişiklik sonrası çalışma sayfası görünümü

**VisibilityType Ayarlama:**

Kullanıcılar, çalışma sayfalarını özel bir şekilde gizleyebilirler. Bu özellik, çalışma sayfasını öyle gizleyebilir ki kullanıcıların onu tekrar görünür yapmanın tek yolu, kod içinde [**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) yönteminin parametre değeri olarak [**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) vermeleridir (burada dikkat edilmesi gereken nokta, kullanıcılar MS Excel'in menü seçeneklerini kullanarak nesneyi doğrudan görünür yapamazlar). Kullanıcılar ayrıca, bir çalışma sayfasının VeryHidden olarak işaretlenip işaretlenmediğini kontrol etmek için [**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) yöntemini de kullanabilirler.

## **Sekmeleri Göster veya Gizle**

Microsoft Excel dosyasının alt kısmına dikkatlice baktığınızda, bir dizi kontrolü göreceksiniz. Bunlar şunları içerir:

- Sayfa sekmeleri.
- Sekme kaydırma düğmeleri.

Sayfa sekmeleri, Excel dosyasındaki çalışma sayfalarını temsil eder. Herhangi bir sekmeye tıklayarak o çalışma sayfasına geçebilirsiniz. Çalışma kitabında daha fazla çalışma sayfası olduğunda, daha fazla sayfa sekmesi olacaktır. İyi bir sayıda çalışma sayfasının olduğu Excel dosyasında bunları dolaşmak için düğmeler kullanmanız gerekebilir. Bu nedenle, Microsoft Excel, sayfa sekmeleri ve sekmeler arasında kaydırmak için düğmeler sağlar.

**Sayfa sekmeleri & sekme kaydırma düğmeleri**

![todo:image_alt_text](show-and-hide-elements_3.png)

Aspose.Cells kullanarak geliştiriciler Excel dosyalarında sayfa sekmelerinin ve sekmelerin kaydırma düğmelerinin görünürlüğünü kontrol edebilirler.

**Sekmelerin Görünürlüğünü Kontrol Etme:**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, bir Excel dosyasını yönetmek için geniş bir özellik ve yöntem yelpazesi sunar.

### **Sekmeleri Gizleme**

Bir Excel dosyasında sekme gizlemek için [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfının [**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) yöntemini ayarlayın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **Sekmeleri Görünür Yapma**

[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfının [**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) yöntemi ile sekme görünür yapın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**Tam Kod Örneği:**

Aşağıda, bir Excel dosyasını (book1.xls) açan, sekmesini gizleyen ve değiştirilmiş dosyayı output.xls olarak kaydeden tam bir örnek bulunmaktadır.

Book1.xls dosyasının aşağıdaki şekilde sekmeler içerdiğini görebilirsiniz. Örnek kod çalıştırıldıktan sonra, sekmeler gizlenir ve output.xls dosyasının ekran görüntüsünde gördüğünüz gibi görünür.

**book1.xls: Herhangi bir değişiklik öncesi Excel dosyası**

![todo:image_alt_text](show-and-hide-elements_4.png)

**output.xls: Değişiklik sonrası Excel dosyası**

![todo:image_alt_text](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **Satır ve Sütunları Göster ve Gizle**

Bir Excel dosyasındaki tüm çalışma sayfaları, satır ve sütunlarda düzenlenen hücrelerden oluşur. Tüm satırlar ve sütunlar, bunları tanımlamak ve tek hücreleri tanımlamak için kullanılan benzersiz değerlere sahiptir. Örneğin, satırlar - 1, 2, 3, 4, vb. - numaralandırılır ve sütunlar alfabetik olarak sıralanır - A, B, C, D, vb. Satır ve sütun değerleri başlıklarda gösterilir. Aspose.Cells kullanarak geliştiriciler, bu satır ve sütun başlıklarının görünürlüğünü kontrol edebilir.

**Çalışma Sayfalarının Görünürlüğünü Kontrol Etme:**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) adında bir sınıf sağlar. Workbook sınıfı, bir Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan WorksheetCollection içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir. Worksheet sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Satır ve sütun başlıklarının görünürlüğünü kontrol etmek için Worksheet sınıfının [**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) yöntemini kullanabilirsiniz.

### **Satır/Sütun Başlıklarını Gizleme**

Satır ve sütun başlıklarını gizlemek için [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) yöntemini kullanın.

### **Satır/Sütun Başlıklarını Görünür Yapma**

Satır ve sütun başlıklarını görünür yapmak için [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) yöntemini kullanın.

Aşağıda, bir Excel dosyasının ilk çalışma sayfasının satır ve sütun başlıklarını gizlemek için [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) yöntemi nasıl kullanılacağını gösteren tam bir örnek verilmiştir.

Aşağıdaki ekran görüntüsü, Book1.xls dosyasının Sheet1, Sheet2 ve Sheet3 olmak üzere üç çalışma sayfasını içerdiğini göstermektedir. Her çalışma sayfası, satır ve sütun başlıklarını göstermektedir.

**Book1.xls: herhangi bir değişiklik yapılmadan önce çalışma sayfası**

![todo:image_alt_text](show-and-hide-elements_6.png)

Book1.xls, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı kullanılarak açılır ve ilk çalışma sayfasındaki satır ve sütun başlıkları gizlenir. Değiştirilmiş dosya output.xls olarak kaydedilir.

**Değişiklikten Sonra Çalışma Sayfası Görünümü**

![todo:image_alt_text](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **Kaydırma Çubuklarını Göster ve Gizle**

Kaydırma çubukları, herhangi bir dosyanın içeriğini gezinmek için kullanılır. Genellikle iki tür kaydırma çubuğu bulunmaktadır:

- Dikey kaydırma çubukları
- Yatay kaydırma çubukları

Microsoft Excel ayrıca yatay ve dikey kaydırma çubukları sağlar böylece kullanıcılar çalışma sayfası içeriğinde kaydırma yapabilirler. Aspose.Cells kullanarak geliştiriciler Excel dosyalarında her iki türde de kaydırma çubuklarının görünürlüğünü kontrol edebilirler.

**Kaydırma Çubuklarının Görünürlüğünün Kontrol Edilmesi:**

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, bir Excel dosyasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Ancak, Excel dosyasındaki kaydırma çubuklarının görünürlüğünü kontrol etmek için geliştiriciler, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfının [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) ve [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) yöntemlerini kullanabilir.

### **Kaydırma çubuklarını gizleme**

Dikey veya yatay kaydırma çubuklarını **false** olarak ayarlayarak [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfının [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) veya [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) yöntemlerini kullanarak kaydırma çubuklarını gizleyin.

### **Kaydırma Çubuklarını Görünür Yapma**

Dikey veya yatay kaydırma çubuklarını **true** olarak ayarlayarak Workbook sınıfının [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) veya [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) yöntemlerini kullanarak kaydırma çubuklarını görünür yapın.

**Tam Kod Örneği:**

Aşağıda, bir Excel dosyasını, book1.xls'yi açan, her iki kaydırma çubuğunu gizleyen ve ardından değiştirilmiş dosyayı output.xls olarak kaydeden tam bir kod bulunmaktadır.

Aşağıdaki ekran görüntüsü, her iki kaydırma çubuğunu da içeren Book1.xls dosyasını göstermektedir. Değiştirilmiş dosya output.xls olarak gösterilmektedir.

**Book1.xls: herhangi bir değişiklik yapılmadan önce Excel dosyası**

![todo:image_alt_text](show-and-hide-elements_8.png)

**output.xls: Değişiklik sonrası Excel dosyası**

![todo:image_alt_text](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **Izgara Çizgilerini Gösterme ve Gizleme**

Tüm Microsoft Excel çalışma sayfaları varsayılan olarak kılavuz çizgilere sahiptir. Bu çizgiler, hücreleri belirlemeye yardımcı olur, böylece belirli hücrelere veri girmek kolay hale gelir. Kılavuz çizgiler, her hücrenin kolayca tanımlanabildiği bir çalışma sayfasını görüntülememizi sağlar.

Aspose.Cells ayrıca kılavuz çizgilerin görünürlüğünü kontrol etmenizi sağlar.

### **Kılavuz Çizgilerinin Görünürlüğünü Kontrol Etmek**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, dosyadaki her çalışma sayfasına erişim sağlayan bir [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Kılavuz çizgilerinin görünürlüğünü kontrol etmek için, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) yöntemini kullanın.

#### **Izgaraları Görünür Yapma**

Kılavuz çizgilerini görünür yapmak için, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) yöntemini kullanın.

#### **Izgaraları Gizleme**

Kılavuz çizgilerini gizlemek için, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) yöntemini kullanın.

{{% alert color="primary" %}}

Kılavuz çizgileri tüm sayfaya uygulanır. Bir çalışma sayfasının bir bölümünde kılavuz çizgilerini 'gizlemek' için, kenar biçimlendirme'yi kullanarak, kenarları sayfanın renk şemasına karışan bir renge ayarlayarak [kenar formatlama](/cells/tr/java/create-table-by-using-border-lines-for-a-range/) kullanın.

{{% /alert %}}

**Örnek: Belirli Bir Çalışma Sayfasında Kılavuz Çizgilerini Gizleme**

Aşağıdaki örnek, bir Excel dosyasının ilk çalışma sayfasının kılavuz çizgilerini gizlemek için [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) yönteminin kullanımını göstermektedir.

Aşağıdaki ekran görüntüsü, Book1.xls dosyasının üç çalışma sayfası olan Sheet1, Sheet2 ve Sheet3 içerdiğini göstermektedir. Bu çalışma sayfalarının hepsinin kılavuz çizgileri bulunmaktadır.

**Değişiklikten Önce Çalışma Sayfası Görünümü**

![todo:image_alt_text](show-and-hide-elements_10.png)

Book1.xls dosyası [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı kullanılarak açılır ve ardından ilk çalışma sayfasının kılavuz çizgileri gizlenir. Değiştirilmiş dosya output.xls olarak kaydedilir.

**Değişiklikten Sonra Çalışma Sayfası Görünümü**

![todo:image_alt_text](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **İlgili Makaleler**

{{% alert color="primary" %}}

- [Sayfa Yerleşimi Özellikleri](/cells/tr/java/page-setup-features/).
- [Bir tablo oluşturmak için hücrelere kenar çizgileri eklemek](/cells/tr/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
