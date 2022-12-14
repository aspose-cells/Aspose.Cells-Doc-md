---
title: Satırlar ve Sütunlarla Çalışma GridWeb
type: docs
weight: 20
url: /tr/java/working-with-rows-and-columns-gridweb/
---
## **Satır ve Sütun Ekleme**
Bu konuda, Aspose.Cells.GridWeb API kullanılarak bir çalışma sayfasına yeni satırların ve sütunların nasıl ekleneceği açıklanmaktadır. Çalışma sayfasındaki herhangi bir konuma satırlar veya sütunlar eklenebilir.
### **Satır Ekleme**
Çalışma sayfasındaki herhangi bir konuma satır eklemek için:

1. Aspose.Cells.GridWeb denetimini Web Formuna veya sayfasına ekleyin.
1. Satır eklediğiniz çalışma sayfasına erişin.
1. Satırın ekleneceği bir satır dizini belirterek bir satır ekleyin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **Sütun Ekleme**
Çalışma sayfasında herhangi bir konuma sütun eklemek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna veya sayfasına ekleyin.
1. Sütun eklediğiniz çalışma sayfasına erişin.
1. Sütunun ekleneceği sütun dizinini belirterek bir sütun ekleyin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

Çalışma sayfalarına uygun şekilde birden çok satır/sütun eklemek için insertRows()/insertColumns() yöntemlerini de kullanabilirsiniz.

{{% /alert %}} 
## **Satırları ve Sütunları Silme**
Bu konuda, Aspose.Cells.GridWeb API kullanılarak bir çalışma sayfasındaki satırların ve sütunların nasıl silineceği gösterilmektedir. Bu özelliğin yardımıyla, geliştiriciler çalışma zamanında satırları veya sütunları silebilirler.
### **Satırları Silme**
Çalışma sayfanızdan bir satırı silmek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna veya sayfasına ekleyin.
1. Satırlarını silmek istediğiniz çalışma sayfasına erişin.
1. Satır dizinini belirterek çalışma sayfasından bir satırı silin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **Sütunları Silme**
Çalışma sayfanızdan bir sütunu silmek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna veya sayfasına ekleyin.
1. Sütunlarını silmek istediğiniz çalışma sayfasına erişin.
1. Sütun dizinini belirterek çalışma sayfasından bir sütunu silin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **Satır Yüksekliğini ve Sütun Genişliğini Ayarlama**
Bazen hücre değerleri, içinde bulundukları hücreden daha geniştir veya birkaç satırdadır. Bu tür değerler, satırların ve sütunların yükseklik ve genişliklerini değiştirmedikçe kullanıcılar tarafından tam olarak görülemez. Aspose.Cells.GridWeb, satır yüksekliklerini ve sütun genişliğini ayarlamayı tamamen destekler. Bu konuda, bu özellikler örnekler yardımıyla ayrıntılı olarak ele alınmaktadır.
### **Satır Yükseklikleri ve Sütun Genişliği ile Çalışma**
#### **Satır Yüksekliğini Ayarlama**
Bir satırın yüksekliğini ayarlamak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza/sayfanıza ekleyin.
1. Çalışma sayfasının GridCells koleksiyonuna erişin.
1. Belirtilen herhangi bir satırdaki tüm hücrelerin yüksekliğini ayarlayın.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb, nokta, inç, piksel vb. cinsinden satır yüksekliği ve sütun genişliği ölçümlerini kabul eder.

{{% /alert %}} 

**Çıktı: 1. sıranın yüksekliği 50 punto olarak ayarlandı** 

![yapılacaklar:resim_alternatif_Metin](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **Sütun Genişliğini Ayarlama**
Bir sütunun genişliğini ayarlamak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza/sayfanıza ekleyin.
1. Çalışma sayfasının GridCells koleksiyonuna erişin.
1. Belirtilen herhangi bir sütundaki tüm hücrelerin genişliğini ayarlayın.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **Satır ve Sütun Başlıklarını Özelleştirme**
Microsoft Excel gibi, Aspose.Cells.GridWeb de satırlar (1, 2, 3 gibi sayılar) ve sütunlar (A, B, C vb. gibi alfabetik) için standart başlıklar veya başlıklar kullanır. Aspose.Cells.GridWeb, altyazıları özelleştirmeyi de mümkün kılar. Bu konu, çalışma zamanında Aspose.Cells.GridWeb API kullanarak satır ve sütun başlıklarını özelleştirmeyi ele almaktadır.
### **Satır Başlığını Özelleştirme**
Bir satırın başlığını veya başlığını özelleştirmek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna/sayfasına ekleyin.
1. Çalışma sayfasına GridWorksheetCollection'dan erişin.
1. Belirtilen herhangi bir satırın başlığını ayarlayın.

**1. ve 2. satırın başlıkları özelleştirildi** 

![yapılacaklar:resim_alternatif_Metin](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **Sütun Başlığını Özelleştirme**
Bir sütunun başlığını veya başlığını özelleştirmek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna/sayfasına ekleyin.
1. Çalışma sayfasına GridWorksheetCollection'dan erişin.
1. Belirtilen herhangi bir sütunun başlığını ayarlayın.

**1. ve 2. sütunun başlıkları özelleştirildi** 

![yapılacaklar:resim_alternatif_Metin](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **Satırları ve Sütunları Dondurun ve Çözün**
Bu konuda, satırların ve sütunların nasıl dondurulacağı ve çözüleceği açıklanmaktadır. Sütunları veya satırları dondurmak, kullanıcıların çalışma sayfasının diğer bölümlerine kaydırırken sütun başlıklarını veya satır başlıklarını görünür tutmalarına olanak tanır. Bu özellik, büyük miktarda veri içeren çalışma sayfalarıyla çalışırken çok faydalıdır. Kullanıcılar yalnızca kaydırdığında veriler aşağı kaydırılır ve başlıklar yerinde kalarak tarihin okunmasını kolaylaştırır. Bölmeleri dondurma özelliği yalnızca Internet Explorer 6.0 veya sonraki sürümlerde desteklenir.
### **Satırları ve Sütunları Dondurma**
Belirli sayıda satır ve sütunu dondurmak için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna/sayfasına ekleyin.
1. Bir çalışma sayfasına erişin.
1. Bir dizi satır ve sütunu dondurun.

{{% alert color="primary" %}} 

 Arayüzü kullanarak belirli sayıda satır ve sütunu dondurmak da mümkündür. Satırları ve sütunları dondurmak istediğiniz hücreye sağ tıklayın ve seçin**Donmak** listeden.

{{% /alert %}} 

**Dondurulmuş durumdaki satırlar ve sütunlar** 

![yapılacaklar:resim_alternatif_Metin](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **Satırları ve Sütunları Çözme**
Satırları ve sütunları çözmek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna/sayfasına ekleyin.
1. Bir çalışma sayfasına erişin.
1. Satırları ve sütunları çözün.

**Çözüldükten sonra çalışma sayfası** 

![yapılacaklar:resim_alternatif_Metin](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **Satırları ve Sütunları Koruma**
Bu konuda, satır ve sütunlardaki hücreleri son kullanıcılar tarafından gerçekleştirilen her türlü eylemden korumaya yönelik birkaç teknik ele alınmaktadır. Geliştiriciler bu korumayı iki teknik kullanarak uygulayabilir: satır ve sütunlardaki hücreleri salt okunur yaparak veya GridWeb'in bağlam menüsü seçeneklerini kısıtlayarak.
### **Bağlam Menüsü Seçeneklerini Kısıtlama**
GridWeb, son kullanıcıların kontrol üzerinde işlem yapmak için kullanabilecekleri bir içerik menüsü sağlar. Menü, hücreleri, satırları ve sütunları işlemek için birçok seçenek sunar.

**Eksiksiz bağlamsal seçenekler** 

![yapılacaklar:resim_alternatif_Metin](working-with-rows-and-columns-gridweb_6.png)

Bağlam menüsünde bulunan seçenekleri kısıtlayarak, satırlar ve sütunlar üzerinde her türlü istemci tarafı işlemi kısıtlamak mümkündür. GridWeb denetiminin EnableClientColumnOperations ve EnableClientRowOperations öznitelikleri false olarak ayarlanarak yapılabilir. GridWeb kontrolünün EnableClientFreeze özniteliğini false olarak ayarlayarak kullanıcıların satırları ve sütunları dondurmasını kısıtlamak da mümkündür.

**Satır ve sütun seçeneklerini kısıtladıktan sonra içerik menüsü** 

![yapılacaklar:resim_alternatif_Metin](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
