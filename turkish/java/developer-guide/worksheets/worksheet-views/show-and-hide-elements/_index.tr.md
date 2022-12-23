---
title: Öğeleri Göster ve Gizle
type: docs
weight: 60
url: /tr/java/show-and-hide-elements/
---
{{% alert color="primary" %}}

Aspose.Cells, kullanıcının bir çalışma kitabının çalışma sayfaları, satırlar, sütunlar, sekmeler, kaydırma çubukları, kılavuz çizgileri gibi öğelerini göstermesini ve gizlemesini sağlar.

{{% /alert %}}

## **Bir Çalışma Sayfasını Göster ve Gizle**

 Bir Excel dosyasında bir veya daha fazla çalışma sayfası olabilir. Ne zaman bir Excel dosyası oluştursak, içinde çalıştığımız Excel dosyasına çalışma sayfaları ekleriz. Bir Excel dosyasındaki her çalışma sayfası, kendi verileri ve biçimlendirme ayarları vb. ile diğer çalışma sayfasından bağımsızdır. Bazen, geliştiriciler kendi ilgileri için Excel dosyasında birkaç çalışma sayfasını gizli ve diğerlerini görünür yapmak isteyebilirler. Yani,**Aspose.Cells** geliştiricilerin Excel dosyalarındaki çalışma sayfalarının görünürlüğünü kontrol etmelerini sağlar.

**Çalışma Sayfalarının Görünürlüğünü Kontrol Etme:**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Bu bir Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) Bu, Excel dosyasındaki her çalışma sayfasına erişmenizi sağlar.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class, bir çalışma sayfasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Ancak, bir çalışma sayfasının görünürlüğünü kontrol etmek için geliştiriciler[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) yöntemi[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf.

### **Bir Çalışma Sayfasını Görünür Hale Getirme**

 Geliştiriciler, geçiş yaparak bir çalışma sayfasını görünür yapabilir**doğru** parametre olarak[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) yöntemi[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf.

### **Bir Çalışma Sayfasını Gizleme**

 Geliştiriciler bir çalışma sayfasını ileterek gizleyebilirsiniz**YANLIŞ** parametre olarak[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) yöntemi[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf.

**Örnek vermek:**

 kullanımını gösteren eksiksiz bir örnek aşağıda verilmiştir.[**setVisible(yanlış)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) yöntemi[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Excel dosyasının ilk çalışma sayfasını gizlemek için sınıf.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**Çalışma Sayfası - Değişiklikten Önce:**

 Aşağıdaki ekran görüntüsünde, bunu görebilirsiniz**Kitap1.xls** dosyası üç çalışma sayfası içerir:**Sayfa1** , **Sayfa2** ve**Sayfa3** .

![yapılacaklar:resim_alternatif_metin](show-and-hide-elements_1.png)

**Figür:** Herhangi bir değişiklikten önce çalışma sayfası görünümü

**Çalışma Sayfası - Örnek Kodu Çalıştırdıktan Sonra:**

**Kitap1.xls** dosya kullanılarak açılır[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)sınıf ve ardından sınıfın ilk çalışma sayfası**Kitap1.xls** dosya gizlenir. Değiştirilen dosya şu şekilde kaydedilir:**çıktı.xls** resimsel görünümü aşağıda gösterilen dosya:

![yapılacaklar:resim_alternatif_metin](show-and-hide-elements_2.png)

**Figür:** Değişiklikten sonra çalışma sayfası görünümü

**VisibilityType'ı Ayarlama**

 Çalışma sayfalarını özel bir şekilde de gizleyebilirsiniz. Bu özellik çalışma sayfasını gizleyebilir, böylece onu tekrar görünür kılmanın tek yolu[**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) için parametre değeri olarak[**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) yöntemi (burada not edilmelidir, kullanıcı menü seçeneklerini kullanarak doğrudan MS Excel'de nesneyi görünür hale getiremez). Kullanıcılar da kullanabilir[**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) bir çalışma sayfasının VeryHidden olarak işaretlenip işaretlenmediğini kontrol etme yöntemi.

## **Sekmeleri Göster veya Gizle**

Microsoft Excel dosyasının en altına yakından bakarsanız, bir dizi kontrol görürsünüz. Bunlar şunları içerir:

- Sayfa sekmeleri.
- Sekme kaydırma düğmeleri.

Sayfa sekmeleri, Excel dosyasındaki çalışma sayfalarını temsil eder. Söz konusu çalışma sayfasına geçmek için herhangi bir sekmeye tıklayın. Çalışma kitabında ne kadar çok çalışma sayfası varsa, o kadar çok sayfa sekmesi vardır. Excel dosyasında çok sayıda çalışma sayfası varsa, bunlar arasında gezinmek için düğmelere ihtiyacınız vardır. Bu nedenle, Microsoft Excel, sayfa sekmeleri arasında gezinmek için sekme kaydırma düğmeleri sağlar.

**Sayfa sekmeleri ve sekme kaydırma düğmeleri**

![yapılacaklar:resim_alternatif_metin](show-and-hide-elements_3.png)

Geliştiriciler, Aspose.Cells'i kullanarak Excel dosyalarındaki sayfa sekmelerinin ve sekme kaydırma düğmelerinin görünürlüğünü kontrol edebilir.

**Sekmelerin Görünürlüğünü Kontrol Etme:**
 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class, bir Excel dosyasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar.

### **Sekmeleri Gizleme**

 ayarlayarak bir Excel dosyasındaki sekmeleri gizleyin.[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf'[**getSettings().setShowTabs(yanlış)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) yöntem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **Sekmeleri Görünür Hale Getirmek**

 ile sekmeleri görünür yapın[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf'[**getSettings().setShowTabs(doğru)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) yöntem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**Tam Kod Örneği:**

Aşağıda, bir Excel dosyasını (book1.xls) açan, sekmelerini gizleyen ve değiştirilen dosyayı output.xls olarak kaydeden tam bir örnek bulunmaktadır.

Book1.xls dosyasının aşağıdaki şekilde sekmeler içerdiğini görebilirsiniz. Örnek kod yürütüldükten sonra, aşağıdaki output.xls dosyasının ekran görüntüsünden de görebileceğiniz gibi sekmeler gizlenir.

**book1.xls: Herhangi bir değişiklikten önceki Excel dosyası**

![yapılacaklar:resim_alternatif_metin](show-and-hide-elements_4.png)

**output.xls: Değişiklikten sonra Excel dosyası**

![yapılacaklar:resim_alternatif_metin](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **Satırları ve Sütunları Göster ve Gizle**

Bir Excel dosyasındaki tüm çalışma sayfaları, satırlar ve sütunlar halinde düzenlenmiş hücrelerden oluşur. Tüm satırlar ve sütunlar, onları ve tek tek hücreleri tanımlamak için kullanılan benzersiz değerlere sahiptir. Örneğin, satırlar – 1, 2, 3, 4, vb. – numaralandırılır ve sütunlar alfabetik olarak sıralanır – A, B, C, D, vb. Başlıklarda satır ve sütun değerleri görüntülenir. Geliştiriciler, Aspose.Cells'i kullanarak bu satır ve sütun başlıklarının görünürlüğünü kontrol edebilir.

**Çalışma Sayfalarının Görünürlüğünü Kontrol Etme:**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), bu bir Microsoft Excel dosyasını temsil eder. Workbook sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir WorksheetCollection içerir.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)sınıf. Worksheet sınıfı, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Satır ve sütun başlıklarının görünürlüğünü kontrol etmek için Worksheet sınıfını kullanın'[**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) yöntem.

### **Satır/Sütun Başlıklarını Gizleme**

 kullanarak satır ve sütun başlıklarını gizleyin.[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[**setRowColumnHeadersVisible(yanlış)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) yöntem.

### **Satır/Sütun Başlıklarını Görünür Hale Getirme**

 kullanarak satır ve sütun başlıklarını görünür hale getirin.[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[**setRowColumnHeadersVisible(doğru)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) yöntem.

 nasıl kullanılacağını gösteren eksiksiz bir örnek aşağıda verilmiştir.[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[**setRowColumnHeadersVisible(yanlış)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) bir Excel dosyasının ilk çalışma sayfasının satır ve sütun başlıklarını gizleme yöntemi.

Aşağıdaki ekran görüntüsü Book1.xls'in üç çalışma sayfası içerdiğini göstermektedir: Sayfa1, Sayfa2 ve Sayfa3. Her çalışma sayfası satır ve sütun başlıklarını gösteriyor.

**Book1.xls: değişiklikten önceki çalışma sayfası**

![yapılacaklar:resim_alternatif_metin](show-and-hide-elements_6.png)

 Book1.xls kullanılarak açılır[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class' ve ilk çalışma sayfasındaki satır ve sütun başlıkları gizlenir. Değiştirilen dosya output.xls olarak kaydedilir.

**Değişiklikten sonra çalışma sayfası görünümü**

![yapılacaklar:resim_alternatif_metin](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **Kaydırma Çubuklarını Göster ve Gizle**

Kaydırma çubukları, herhangi bir dosyanın içeriğinde gezinmek için çok kullanılır. Normalde iki tür kaydırma çubuğu vardır:

- Dikey kaydırma çubukları
- Yatay kaydırma çubukları

Microsoft Excel, kullanıcıların çalışma sayfası içeriklerinde gezinebilmeleri için yatay ve dikey kaydırma çubukları da sağlar. Geliştiriciler, Aspose.Cells'i kullanarak Excel dosyalarındaki her iki kaydırma çubuğunun da görünürlüğünü kontrol edebilir.

**Kaydırma Çubuklarının Görünürlüğünü Kontrol Etme:**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Bu bir Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class, bir Excel dosyasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Ancak, Excel dosyasındaki kaydırma çubuklarının görünürlüğünü kontrol etmek için geliştiriciler[**setVScrollBarGörünür**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) & [**setHScrollBarGörünür**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) yöntemleri[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf.

### **Kaydırma Çubuklarını Gizleme**

 ayarlayarak kaydırma çubuklarını gizleyin.[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf'[**setVScrollBarGörünür**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) veya[**setHScrollBarGörünür**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) yöntemleri**YANLIŞ**.

### **Kaydırma Çubuklarını Görünür Hale Getirmek**

 Çalışma Kitabı sınıfını ayarlayarak kaydırma çubuklarını görünür yapın'[**setVScrollBarGörünür**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) veya[**setHScrollBarGörünür**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) yöntemleri**doğru**.

**Tam Kod Örneği:**

Aşağıda, kitap1.xls adlı bir Excel dosyasını açan, her iki kaydırma çubuğunu da gizleyen ve ardından değiştirilen dosyayı output.xls olarak kaydeden eksiksiz bir kod bulunmaktadır.

Aşağıdaki ekran görüntüsü, her iki kaydırma çubuğunu da içeren Book1.xls dosyasını göstermektedir. Değiştirilen dosya, aşağıda da gösterilen output.xls dosyası olarak kaydedilir.

**Book1.xls: Herhangi bir değişiklik yapılmadan önceki Excel dosyası**

![yapılacaklar:resim_alternatif_metin](show-and-hide-elements_8.png)

**output.xls: Değişiklikten sonra Excel dosyası**

![yapılacaklar:resim_alternatif_metin](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **Kılavuz Çizgilerini Göster ve Gizle**

Tüm Microsoft Excel çalışma sayfalarında varsayılan olarak kılavuz çizgileri bulunur. Belirli hücrelere veri girmenin kolay olması için hücrelerin tanımlanmasına yardımcı olurlar. Kılavuz çizgileri, bir çalışma sayfasını, her hücrenin kolayca tanımlanabildiği bir hücreler koleksiyonu olarak görmemizi sağlar.

Aspose.Cells ayrıca kılavuz çizgilerinin görünürlüğünü kontrol etmenizi sağlar.

### **Kılavuz Çizgilerin Görünürlüğünü Kontrol Etme**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) dosyadaki her çalışma sayfasına erişim sağlar.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Kılavuz çizgilerinin görünürlüğünü kontrol etmek için[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[**setGridlinesGörünür**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) yöntem.

#### **Kılavuz Çizgilerini Görünür Hale Getirme**

 Kılavuz çizgilerini görünür yapmak için[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[**setGridlinesVisible(doğru)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) yöntem.

#### **Kılavuz Çizgilerini Gizleme**

 kullanarak kılavuz çizgilerini gizleyin.[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[**setGridlinesVisible(yanlış)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) yöntem.

{{% alert color="primary" %}}

Kılavuz çizgileri sayfanın tamamına uygulanır. Çalışma sayfasının bir bölümündeki kılavuz çizgilerini 'gizlemek' için şunu kullanın:[kenarlık biçimlendirme](/cells/tr/java/create-table-by-using-border-lines-for-a-range/) kenarlıkları, sayfanın renk düzeniyle karışan bir renge ayarlamak için.

{{% /alert %}}

**Örnek: Belirli bir Çalışma Sayfasında Kılavuz Çizgileri Gizleme**

 Aşağıdaki örnek,[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[**setGridlinesVisible(yanlış)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) bir Excel dosyasının ilk çalışma sayfasının kılavuz çizgilerini gizleme yöntemi.

Aşağıdaki ekran görüntüsü, Book1.xls dosyasının üç çalışma sayfası içerdiğini gösterir: Sayfa1, Sayfa2 ve Sayfa3. Bu çalışma sayfalarının tümünde kılavuz çizgileri vardır.

**Değişiklikten önce çalışma sayfası görünümü**

![yapılacaklar:resim_alternatif_metin](show-and-hide-elements_10.png)

 Book1.xls dosyası,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class ve ardından ilk çalışma sayfasının kılavuz çizgileri gizlenir. Değiştirilen dosya output.xls dosyası olarak kaydedilir.

**Değişiklikten sonra çalışma sayfası görünümü**

![yapılacaklar:resim_alternatif_metin](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **İlgili Makaleler**

{{% alert color="primary" %}}

- [Sayfa Düzeni Özellikleri](/cells/tr/java/page-setup-features/).
- [Tablo oluşturmak için hücrelere kenarlık ekleme](/cells/tr/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
