---
title: Satırlar ve Sütunlarla Çalışma GridWeb
type: docs
weight: 20
url: /tr/java/working-with-rows-and-columns-gridweb/
---
##  **Satır ve Sütun Ekleme**
Bu konu, Aspose.Cells.GridWeb API kullanılarak bir çalışma sayfasına nasıl yeni satır ve sütunların ekleneceğini açıklamaktadır. Satır veya sütunlar, çalışma sayfasında herhangi bir konuma eklenebilir.
###  **Satır Ekleme**
Çalışma sayfasında herhangi bir konuma satır eklemek için:

1. Aspose.Cells.GridWeb denetimini Web Formuna veya sayfasına ekleyin.
1. Satır eklediğiniz çalışma sayfasına erişin.
1. Satırın ekleneceği satır dizini belirterek satır ekleyin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
###  **Sütun Ekleme**
Çalışma sayfasında herhangi bir konuma sütun eklemek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna veya sayfaya ekleyin.
1. Sütun eklediğiniz çalışma sayfasına erişin.
1. Sütunun ekleneceği sütun dizinini belirterek bir sütun ekleyin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

Çalışma sayfalarına uygun şekilde birden fazla satır/sütun eklemek için insertRows()/insertColumns() yöntemlerini de kullanabilirsiniz.

{{% /alert %}} 
##  **Satırları ve Sütunları Silme**
Bu konu, Aspose.Cells.GridWeb API kullanılarak bir çalışma sayfasındaki satırların ve sütunların nasıl silineceğini gösterir. Bu özelliğin yardımıyla, geliştiriciler çalışma zamanında satırları veya sütunları silme işlemini gerçekleştirebilir.
###  **Satırları Silme**
Çalışma sayfanızdan bir satırı silmek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna veya sayfaya ekleyin.
1. Satırlarını silmek istediğiniz çalışma sayfasına erişin.
1. Satır dizinini belirterek çalışma sayfasından bir satırı silin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
###  **Sütunları Silme**
Çalışma sayfanızdan bir sütunu silmek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna veya sayfaya ekleyin.
1. Sütunlarını silmek istediğiniz çalışma sayfasına erişin.
1. Sütun dizinini belirterek çalışma sayfasından bir sütunu silin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
##  **Satır Yüksekliğini ve Sütun Genişliğini Ayarlama**
Bazen hücre değerleri bulundukları hücreden daha geniş olabilir veya birkaç satırda yer alabilir. Bu tür değerler, satır ve sütunların yüksekliğini ve genişliğini değiştirmediği sürece kullanıcılar tarafından tam olarak görülemez. Aspose.Cells.GridWeb, satır yüksekliklerini ve sütun genişliğini ayarlamayı tamamen destekler. Bu konu, bu özellikleri örnekler yardımıyla ayrıntılı olarak açıklamaktadır.
###  **Satır Yükseklikleri ve Sütun Genişliğiyle Çalışmak**
####  **Satır Yüksekliğini Ayarlama**
Bir satırın yüksekliğini ayarlamak için:

1. Aspose.Cells.GridWeb kontrolünü Web Formunuza/sayfanıza ekleyin.
1. Çalışma sayfasının GridCells koleksiyonuna erişin.
1. Belirtilen herhangi bir satırdaki tüm hücrelerin yüksekliğini ayarlayın.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb nokta, inç, piksel vb. cinsinden satır yüksekliği ve sütun genişliği ölçümlerini kabul eder.

{{% /alert %}} 

**Çıktı: 1. sıranın yüksekliği 50 puana ayarlandı** 

![yapılacak şey:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
####  **Sütun Genişliğini Ayarlama**
Bir sütunun genişliğini ayarlamak için:

1. Aspose.Cells.GridWeb kontrolünü Web Formunuza/sayfanıza ekleyin.
1. Çalışma sayfasının GridCells koleksiyonuna erişin.
1. Belirtilen herhangi bir sütundaki tüm hücrelerin genişliğini ayarlayın.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
##  **Satır ve Sütun Başlıklarını Özelleştirme**
Microsoft Excel gibi, Aspose.Cells.GridWeb de satırlar (1, 2, 3 vb. gibi sayılar) ve sütunlar (A, B, C vb. gibi alfabetik) için standart başlıklar veya başlıklar kullanır. Aspose.Cells.GridWeb ayrıca altyazıları özelleştirmeyi de mümkün kılar. Bu konu, Aspose.Cells.GridWeb API'i kullanarak çalışma zamanında satır ve sütun başlıklarını özelleştirmeyi açıklamaktadır.
###  **Satır Başlığını Özelleştirme**
Bir satırın başlığını veya başlığını özelleştirmek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formu/sayfasına ekleyin.
1. GridWorksheetCollection'daki çalışma sayfasına erişin.
1. Belirtilen herhangi bir satırın başlığını ayarlayın.

**1. ve 2. satırların başlıkları özelleştirildi** 

![yapılacak şey:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
###  **Sütun Başlığını Özelleştirme**
Bir sütunun başlığını veya başlığını özelleştirmek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formu/sayfasına ekleyin.
1. GridWorksheetCollection'daki çalışma sayfasına erişin.
1. Belirtilen herhangi bir sütunun başlığını ayarlayın.

**1. ve 2. sütunun başlıkları özelleştirilmiştir** 

![yapılacak şey:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
##  **Satırları ve Sütunları Dondurma ve Çözme**
Bu konu, satırların ve sütunların nasıl dondurulacağını ve çözüleceğini açıklamaktadır. Sütunların veya satırların dondurulması, kullanıcıların çalışma sayfasının diğer bölümlerine kaydırırken sütun başlıklarını veya satır başlıklarını görünür tutmasına olanak tanır. Bu özellik, büyük miktarda veri içeren çalışma sayfalarıyla çalışırken çok faydalıdır. Kullanıcılar yalnızca ekranı kaydırdığında veriler aşağı kaydırılır ve başlıklar yerinde kalır, böylece tarihin okunması kolaylaşır. Bölmeleri dondurma özelliği yalnızca Internet Explorer 6.0 veya üzeri sürümlerde desteklenir.
###  **Satırların ve Sütunların Dondurulması**
Belirli sayıda satır ve sütunu dondurmak için:

1. Aspose.Cells.GridWeb denetimini bir Web Formu/sayfasına ekleyin.
1. Bir çalışma sayfasına erişin.
1. Bir dizi satırı ve sütunu dondurun.

{{% alert color="primary" %}} 

 Arayüzü kullanarak belirli sayıda satır ve sütunu dondurmak da mümkündür. Satırları ve sütunları dondurmak istediğiniz hücreye sağ tıklayın ve**Donmak** listeden.

{{% /alert %}} 

**Dondurulmuş durumdaki satırlar ve sütunlar** 

![yapılacak şey:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
###  **Satırların ve Sütunların Dondurulması**
Satır ve sütunların dondurmasını çözmek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formu/sayfasına ekleyin.
1. Bir çalışma sayfasına erişin.
1. Satırları ve sütunları çözün.

**Dondurulduktan sonraki çalışma sayfası** 

![yapılacak şey:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
##  **Satır ve Sütunların Korunması**
Bu konu, satır ve sütunlardaki hücreleri son kullanıcılar tarafından gerçekleştirilen her türlü eylemden korumaya yönelik birkaç tekniği tartışmaktadır. Geliştiriciler bu korumayı iki teknik kullanarak uygulayabilirler: satır ve sütunlardaki hücreleri salt okunur hale getirerek veya GridWeb'in içerik menüsü seçeneklerini kısıtlayarak.
###  **İçerik Menüsü Seçeneklerini Kısıtlama**
GridWeb, son kullanıcıların kontrol üzerinde işlemler gerçekleştirmek için kullanabileceği bir içerik menüsü sağlar. Menü, hücreleri, satırları ve sütunları değiştirmek için birçok seçenek sunar.

**Bağlamsal seçenekleri tamamlayın** 

![yapılacak şey:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

Bağlam menüsündeki seçenekleri kısıtlayarak satır ve sütunlarda her türlü istemci taraflı işlemi kısıtlamak mümkündür. Bu, GridWeb denetiminin EnableClientColumnOperations ve EnableClientRowOperations özniteliklerini false olarak ayarlayarak yapılabilir. GridWeb denetiminin EnableClientFreeze özniteliğini false olarak ayarlayarak kullanıcıların satırları ve sütunları dondurmasını kısıtlamak da mümkündür.

**Satır ve sütun seçeneklerini kısıtladıktan sonra içerik menüsü** 

![yapılacak şey:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
