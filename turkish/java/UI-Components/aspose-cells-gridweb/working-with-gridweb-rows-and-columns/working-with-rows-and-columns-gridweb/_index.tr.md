---
title: GridWeb de Satırlar ve Sütunlarla Çalışmak
type: docs
weight: 20
url: /tr/java/working-with-rows-and-columns-gridweb/
---

## **Satırlar ve Sütunlar Eklemek**
Bu konu, Aspose.Cells.GridWeb API'sını kullanarak bir çalışma sayfasına yeni satırlar ve sütunlar eklemenin nasıl olduğunu açıklar. Satırlar veya sütunlar çalışma sayfasında herhangi bir konuma eklenebilir.
### **Satırlar Eklemek**
Çalışma sayfasında herhangi bir konuma satır eklemek için:

1. Aspose.Cells.GridWeb denetimini Web Formuna veya sayfaya ekleyin.
1. Satır eklemek istediğiniz çalışma sayfasına erişin.
1. Satırın ekleneceği satır dizinini belirterek bir satır ekleyin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **Sütunlar Eklemek**
Çalışma sayfasında herhangi bir konuma sütun eklemek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formu veya sayfaya ekleyin.
1. Sütun eklemek istediğiniz çalışma sayfasına erişin.
1. Kolon eklemek için kolonun ekleneceği sütun indisini belirterek bir sütun ekleyin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

Ayrıca insertRows()/insertColumns() yöntemlerini kullanarak çalışma sayfasına uygun olarak birden fazla satır/sütun ekleyebilirsiniz.

{{% /alert %}} 
## **Satırları ve Sütunları Silme**
Bu konu, Aspose.Cells.GridWeb API'sını kullanarak bir çalışma sayfasından satırları ve sütunları nasıl sileceğinizi göstermektedir. Bu özellik sayesinde geliştiriciler çalışma zamanında satırları veya sütunları silebilirler.
### **Satırları Silme**
Çalışma sayfanızdan bir satırı silmek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formu veya sayfaya ekleyin.
1. Satırları silmek istediğiniz çalışma sayfasına erişin.
1. Satırın indisini belirterek çalışma sayfasından bir satırı silin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **Sütunları Silme**
Çalışma sayfanızdan bir sütunu silmek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formu veya sayfaya ekleyin.
1. Sütunları silmek istediğiniz çalışma sayfasına erişin.
1. Sütunun indisini belirterek çalışma sayfasından bir sütunu silin.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **Satır Yüksekliği ve Sütun Genişliği Ayarlama**
Bazı hücre değerleri, hücrelerinin genişliğinden daha geniştir veya birkaç satıra yayılmıştır. Bu tür değerler, kullanıcılar tarafından tamamen görülemez, hücre yüksekliği ve sütun genişliğini değiştirmedikçe. Aspose.Cells.GridWeb, satır yükseklikleri ve sütun genişliklerini ayarlama konusunu detaylı bir şekilde destekler. Bu konu, örneklerin yardımıyla bu özellikleri ayrıntılı bir şekilde tartışmaktadır.
### **Satır Yükseklikleri ve Sütun Genişlikleriyle Çalışma**
#### **Satır Yüksekliği Ayarlama**
Bir satırın yüksekliğini ayarlamak için:

1. Aspose.Cells.GridWeb denetimini Web Formu/sayfanıza ekleyin.
1. Çalışma sayfasının GridCells koleksiyonuna erişin.
1. Belirli bir satırdaki tüm hücrelerin yüksekliğini ayarlayın.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb, satır yüksekliği ve sütun genişlik ölçümlerini puan, inç, piksel vb. olarak kabul eder.

{{% /alert %}} 

**Çıktı: 1. satırın yüksekliği 50 puan olarak ayarlandı** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **Sütun Genişliği Ayarlama**
Bir sütunun genişliğini ayarlamak için:

1. Aspose.Cells.GridWeb denetimini Web Formu/sayfanıza ekleyin.
1. Çalışma sayfasının GridCells koleksiyonuna erişin.
1. Belirli bir sütundaki tüm hücrelerin genişliğini ayarlayın.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **Satır ve Sütun Başlıklarını Özelleştirme**
Microsoft Excel'e benzer şekilde, Aspose.Cells.GridWeb ayrıca sıralar (1, 2, 3 gibi) ve sütunlar (A, B, C gibi) için standart başlıkları veya başlıkları kullanır. Aspose.Cells.GridWeb, başlıkları özelleştirmeyi de mümkün kılar. Bu konu, Aspose.Cells.GridWeb API'sını kullanarak çalışma zamanında sıra ve sütun başlıklarını özelleştirmeyi tartışmaktadır.
### **Sıra Başlığını Özelleştirme**
Bir sıra başlığını veya başlığını özelleştirmek için:

1. Aspose.Cells.GridWeb denetimini Bir Web Form/ sayfasına ekleyin.
1. GridWorksheetCollection'daki çalışsayıya erişin.
1. Belirli bir satırın başlığını ayarlayın.

**1. ve 2. satırın başlıkları özelleştirildi** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **Sütun Başlığını Özelleştirme**
Bir sütun başlığını veya başlığını özelleştirmek için:

1. Aspose.Cells.GridWeb denetimini Bir Web Form/ sayfasına ekleyin.
1. GridWorksheetCollection'daki çalışsayıya erişin.
1. Belirli bir sütunun başlığını ayarlayın.

**1. ve 2. sütunun başlıkları özelleştirildi** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **Sıraları ve Sütunları Sabitleme ve Şeffaflık**
Bu konu, sıraları ve sütunları sabitlemenin ve şeffaflığını kaldırmanın nasıl yapılacağını açıklar. Sütunları veya sıraları dondurmak, kullanıcıların çalışsayfasının diğer kısımlarına kaydırırken sütun başlıklarını veya sıra başlıklarını görünür tutmalarını sağlar. Bu özellik, büyük veri miktarı içeren çalışsayfalarıyla çalışırken çok yardımcıdır. Kullanıcılar yalnızca verileri kaydırırken başlıklar yerinde kalır ve veriyi okumayı kolaylaştırır. Sabitlenmiş paneller özelliği yalnızca Internet Explorer 6.0 veya üzerinde desteklenir.
### **Sıraları ve Sütunları Dondurma**
Belirli bir sayıda sırayı ve sütunu dondurmak için:

1. Aspose.Cells.GridWeb denetimini Bir Web Form/ sayfasına ekleyin.
1. Bir çalışsayı açın.
1. Belirli bir sayıda sırayı ve sütunu dondurun.

{{% alert color="primary" %}} 

Ayrıca, arabirim kullanarak belirli bir sayıda sırayı ve sütunu dondurmak mümkündür. Sıraları ve sütunları dondurmak istediğiniz hücreye sağ tıklayın ve listeden **Dondur**'u seçin.

{{% /alert %}} 

**Dondurulmuş durumdaki sıralar ve sütunlar** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **Sıraları ve Sütunları Serbest Bırakma**
Sıraları ve sütunları serbest bırakmak için:

1. Aspose.Cells.GridWeb denetimini Bir Web Form/ sayfasına ekleyin.
1. Bir çalışsayı açın.
1. Sıraları ve sütunları serbest bırakın.

**Serbest bırakıldıktan sonraki çalışsayfa** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **Sıraları ve Sütunları Koruma**
Bu konu, geliştiricilerin son kullanıcılar tarafından gerçekleştirilen her türlü eylemden satır ve sütunlardaki hücreleri korumak için birkaç teknik tartışır. Geliştiriciler, hücreleri satır ve sütunlarda salt okunur yaparak veya GridWeb'in bağlam menü seçeneklerini kısıtlayarak bu korumayı uygulayabilirler.
### **Bağlam Menü Seçeneklerini Kısıtlama**
GridWeb, denetim üzerinde işlemler yapmak için kullanıcıların kullanabileceği bağlam menüsünü sağlar. Menü, hücreleri, satırları ve sütunları manipüle etmek için birçok seçenek sağlar.

**Tüm bağlamsal seçenekler** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

Bağlam menüsündeki seçeneklerin kullanıcı tarafından kısıtlanması mümkündür. Bu, GridWeb denetiminin EnableClientColumnOperations ve EnableClientRowOperations özelliklerinin false olarak ayarlanarak yapılabilir. Ayrıca, GridWeb denetiminin EnableClientFreeze özelliğinin false olarak ayarlanarak kullanıcıların satırları ve sütunları dondurması da mümkündür.

**Satır ve sütun seçenekleri kısıtlandıktan sonra bağlam menüsü** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
