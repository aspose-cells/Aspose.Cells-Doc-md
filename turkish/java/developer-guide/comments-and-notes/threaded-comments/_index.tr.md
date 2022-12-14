---
title: Zincirleme Yorumlar
type: docs
weight: 140
url: /tr/java/threaded-comments/
---
# **Zincirleme Yorumlar**
MS Excel 365, dizili yorumlar eklemek için bir özellik sağlar. Bu yorumlar sohbet işlevi görür ve tartışmalar için kullanılabilir. Yorumlar artık zincirleme konuşmalara izin veren bir Yanıt kutusuyla birlikte gelir. Eski yorumlar, Excel 365'te Notlar olarak adlandırılır. Aşağıdaki ekran görüntüsü, Excel'de açıldığında zincir halinde yorumların nasıl görüntülendiğini gösterir.

![yapılacaklar:resim_alternatif_Metin](threaded-comments_1.jpg)

Zincirleme yorumlar, Excel'in eski sürümlerinde bu şekilde gösterilir. Aşağıdaki görseller örnek dosya Excel 2016 programında açılarak çekilmiştir.

![yapılacaklar:resim_alternatif_Metin](threaded-comments_2.jpg)



![yapılacaklar:resim_alternatif_Metin](threaded-comments_3.jpg)



Aspose.Cells ayrıca zincirleme yorumları yönetme özelliği de sağlar.
## **Zincirleme Yorumlar Ekle**
### **Excel ile Zincirli yorum ekleme**
Excel 365'te zincirleme açıklamalar eklemek için aşağıdaki adımları izleyin.

- Yöntem 1
 - Tıkla**Gözden geçirmek**Sekme
 - Tıkla**Yeni yorum**buton
 - Bu, aktif hücreye yorum girmek için bir diyalog açacaktır.
  - ![yapılacaklar:resim_alternatif_Metin](threaded-comments_4.jpg)
- Yöntem 2
 - Yorumu eklemek istediğiniz hücreye sağ tıklayın.
 - Tıkla**Yeni yorum**seçenek.
 - Bu, aktif hücreye yorum girmek için bir diyalog açacaktır.
  - ![yapılacaklar:resim_alternatif_Metin](threaded-comments_5)
### **Aspose.Cells'i kullanarak Zincirli Yorum Ekle**
Aspose.Cells sağlar[Yorumlar.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) zincirleme yorumlar ekleme yöntemi.[Yorumlar.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) yöntemi aşağıdaki üç parametreyi kabul eder.

- Cell Ad: Yorumun ekleneceği hücrenin adı.
- Yorum Metni: Yorum metni.
- [KonuluYorumYazar](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor): Yorumun yazarı

Aşağıdaki kod örneği, kullanımını gösterir[Yorumlar.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) A1 hücresine iş parçacığı Açıklama ekleme yöntemi. Lütfen bkz[çıktı excel dosyası](AddThreadedComments_out.xlsx)referans için kod tarafından oluşturulur.
#### **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **Zincirlenmiş Yorumları Oku**
### **Excel ile Zincirlenmiş yorumları okuyun**
Excel'de dizili yorumları okumak için, yorumları görüntülemek üzere farenizi yorumları içeren hücrenin üzerine getirin. Yorumlar görünümü, aşağıdaki görüntüdeki görünüme benzeyecektir.

![yapılacaklar:resim_alternatif_Metin](threaded-comments_1.jpg)
### **Aspose.Cells'i kullanarak Zincirli yorumları okuyun**
Aspose.Cells sağlar[Yorumlar.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) belirtilen sütun için dizili yorumları alma yöntemi.[Yorumlar.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) yöntemi, sütun adını bir parametre olarak kabul eder ve[KonuluYorum Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). üzerinde yineleme yapabilirsiniz[KonuluYorum Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)yorumları görüntülemek için.

Aşağıdaki örnek, aşağıdakileri yükleyerek A1 sütunundaki açıklamaları okumayı gösterir:[örnek Excel Dosyası](ThreadedCommentsSample.xlsx). Lütfen referans için kod tarafından oluşturulan konsol çıktısına bakın.
#### **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **Konsol Çıkışı**
Yorum: Dişli Yorumu Test Et

Yazar: Aspose Testi
### **Zincirleme yorumların Oluşturulma Zamanını Oku**
Aspose.Cells sağlar[Yorumlar.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) belirtilen sütun için dizili yorumları alma yöntemi.[Yorumlar.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) yöntemi, sütun adını bir parametre olarak kabul eder ve[KonuluYorum Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). üzerinde yineleme yapabilirsiniz[KonuluYorum Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)ve kullan[ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime)Emlak.

Aşağıdaki örnek, dizili yorumların oluşturulan zamanını yükleyerek okumayı gösterir.[örnek Excel Dosyası](ThreadedCommentsSample.xlsx). Lütfen referans için kod tarafından oluşturulan konsol çıktısına bakın.
#### **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **Konsol Çıkışı**
Yorum: Dişli Yorumu Test Et

Yazar: Aspose Testi

Oluşturulma Zamanı: 2019-05-15T12:46:23
## **Zincirlenmiş Yorumları Düzenle**
### **Excel ile Zincirlenmiş yorumu düzenleyin**
Excel'de zincir halinde bir yorumu düzenlemek için,**Düzenlemek**aşağıdaki resimde gösterildiği gibi yorumdaki bağlantı.

![yapılacaklar:resim_alternatif_Metin](threaded-comments_7.jpg)
### **Aspose.Cells'i kullanarak Zincirleme yorumu düzenleyin**
Aspose.Cells sağlar[Yorumlar.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) belirtilen sütun için dizili yorumları alma yöntemi.[Yorumlar.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) yöntemi, sütun adını bir parametre olarak kabul eder ve[KonuluYorum Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Gerekli yorumu güncelleyebilirsiniz.[KonuluYorum Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)ve çalışma kitabını kaydedin.

Aşağıdaki örnek, sütunu yükleyerek A1 sütunundaki ilk zincirleme yorumun düzenlenmesini gösterir.[örnek Excel Dosyası](ThreadedCommentsSample.xlsx). Lütfen bkz[çıktı excel dosyası](EditThreadedComments.xlsx)referans için güncellenmiş yorumu gösteren kod tarafından oluşturulur.
#### **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **Zincirlenmiş Yorumları Kaldır**
### **Excel ile Zincirlenmiş yorumları kaldırın**
Excel'de zincirlenmiş yorumları kaldırmak için, yorumları içeren hücreye sağ tıklayın ve**Yorumu Sil**Aşağıdaki resimde gösterildiği gibi seçenek.

![yapılacaklar:resim_alternatif_Metin](threaded-comments_8.jpg)
### **Aspose.Cells kullanarak Zincirli yorumları kaldırın**
Aspose.Cells sağlar[Yorumlar.Kaldır](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) belirtilen sütun için yorumları kaldırma yöntemi.[Yorumlar.Kaldır](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) yöntemi sütun adını bir parametre olarak kabul eder ve o sütundaki yorumları kaldırır.

Aşağıdaki örnek, sütunu yükleyerek A1 sütunundaki açıklamaları kaldırmayı gösterir.[örnek Excel Dosyası](ThreadedCommentsSample.xlsx). Lütfen bkz[çıktı excel dosyası](ThreadedCommentsSample_Out.xlsx)referans için kod tarafından oluşturulur.
#### **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

 Lütfen Aspose.Cells ile yorumu kaldırarak yazarın otomatik olarak kaldırılmadığını unutmayın. Yazarı da kaldırmanız gerekirse, lütfen[ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt\(int\)) yöntemi yukarıdaki örnekte gösterildiği gibi.

{{% /alert %}}
