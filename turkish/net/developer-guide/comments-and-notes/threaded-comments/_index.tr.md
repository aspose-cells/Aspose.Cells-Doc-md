---
title: Zincirleme Yorumlar
type: docs
weight: 140
url: /tr/net/threaded-comments/
---
## **Zincirleme Yorumlar**

MS Excel 365, dizili yorumlar eklemek için bir özellik sağlar. Bu yorumlar sohbet işlevi görür ve tartışmalar için kullanılabilir. Yorumlar artık zincirleme konuşmalara izin veren bir Yanıt kutusuyla birlikte gelir. Eski yorumlar, Excel 365'te Notlar olarak adlandırılır. Aşağıdaki ekran görüntüsü, Excel'de açıldığında zincir halinde yorumların nasıl görüntülendiğini gösterir.

![yapılacaklar:resim_alternatif_metin](threaded-comments_1.jpg)

Zincirleme yorumlar, Excel'in eski sürümlerinde bu şekilde gösterilir. Aşağıdaki görseller örnek dosya Excel 2016 programında açılarak çekilmiştir.

![yapılacaklar:resim_alternatif_metin](threaded-comments_2.jpg)

![yapılacaklar:resim_alternatif_metin](threaded-comments_3.jpg)

Aspose.Cells ayrıca zincirleme yorumları yönetme özelliği de sağlar.

## **Zincirleme Yorumlar Ekle**

### **Excel ile Zincirli yorum ekleme**

Excel 365'te zincirleme açıklamalar eklemek için aşağıdaki adımları izleyin.

- Yöntem 1
 - Tıkla**Gözden geçirmek** Sekme
 - Tıkla**Yeni yorum** buton
 - Bu, aktif hücreye yorum girmek için bir diyalog açacaktır.
  - ![yapılacaklar:resim_alternatif_metin](threaded-comments_4.jpg)
- Yöntem 2
 - Yorumu eklemek istediğiniz hücreye sağ tıklayın.
 - Tıkla**Yeni yorum** seçenek.
 - Bu, aktif hücreye yorum girmek için bir diyalog açacaktır.
  - ![yapılacaklar:resim_alternatif_metin](threaded-comments_5)

### **Aspose.Cells'i kullanarak Zincirli Yorum Ekle**

Aspose.Cells sağlar[**Yorumlar.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) zincirleme yorumlar ekleme yöntemi.[**Yorumlar.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)method aşağıdaki üç parametreyi kabul eder.

- Cell Ad: Yorumun ekleneceği hücrenin adı.
- Yorum Metni: Yorum metni.
- [**KonuluYorumYazar**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor): Yorumun yazarı

Aşağıdaki kod örneği, kullanımını gösterir[**Yorumlar.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)A1 hücresine iş parçacıklı Yorum ekleme yöntemi. Lütfen bkz[çıktı excel dosyası](89849859.xlsx) referans için kod tarafından oluşturulur.

#### **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **Zincirlenmiş Yorumları Oku**

### **Excel ile Zincirlenmiş yorumları okuyun**

Excel'de dizili yorumları okumak için, yorumları görüntülemek üzere farenizi yorumları içeren hücrenin üzerine getirin. Yorumlar görünümü, aşağıdaki görüntüdeki görünüme benzeyecektir.

![yapılacaklar:resim_alternatif_metin](threaded-comments_1.jpg)

### **Aspose.Cells'i kullanarak Zincirli yorumları okuyun**

Aspose.Cells sağlar[**Yorumlar.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)belirtilen sütun için dizili yorumları alma yöntemi.[**Yorumlar.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)yöntem, sütun adını bir parametre olarak kabul eder ve[**KonuluYorum Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). üzerinde yineleme yapabilirsiniz[**KonuluYorum Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)yorumları görüntülemek için.

Aşağıdaki örnek, aşağıdakileri yükleyerek A1 sütunundaki açıklamaları okumayı gösterir:[örnek Excel Dosyası](89849861.xlsx). Lütfen referans için kod tarafından oluşturulan konsol çıktısına bakın.

#### **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **Konsol Çıkışı**

Yorum: Dişli Yorumu Test Et

Yazar: Aspose Testi

### **Zincirleme yorumların Oluşturulma Zamanını Oku**

Aspose.Cells sağlar[**Yorumlar.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)belirtilen sütun için dizili yorumları alma yöntemi.[**Yorumlar.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)yöntem, sütun adını bir parametre olarak kabul eder ve[**KonuluYorum Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). üzerinde yineleme yapabilirsiniz[**KonuluYorum Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) ve kullan[**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime) Emlak.

Aşağıdaki örnek, dizili yorumların oluşturulan zamanını yükleyerek okumayı gösterir.[örnek Excel Dosyası](89849861.xlsx). Lütfen referans için kod tarafından oluşturulan konsol çıktısına bakın.

#### **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **Konsol Çıkışı**

Yorum: Dişli Yorumu Test Et

Yazar: Aspose Testi

Oluşturulma Zamanı: 15.05.2019 12:46:23

## **Zincirlenmiş Yorumları Düzenle**

### **Excel ile Zincirlenmiş yorumu düzenleyin**

 Excel'de zincir halinde bir yorumu düzenlemek için,**Düzenlemek** aşağıdaki resimde gösterildiği gibi yorumdaki bağlantı.

![yapılacaklar:resim_alternatif_metin](threaded-comments_7.jpg)

### **Aspose.Cells'i kullanarak Zincirleme yorumu düzenleyin**

Aspose.Cells sağlar[**Yorumlar.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) belirtilen sütun için dizili yorumları alma yöntemi.[**Yorumlar.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)yöntem, sütun adını bir parametre olarak kabul eder ve[**KonuluYorum Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Gerekli yorumu güncelleyebilirsiniz.[**KonuluYorum Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)ve çalışma kitabını kaydedin.

Aşağıdaki örnek, sütunu yükleyerek A1 sütunundaki ilk zincirleme yorumun düzenlenmesini gösterir.[örnek Excel Dosyası](89849861.xlsx). Lütfen bkz[çıktı excel dosyası](89849862.xlsx)referans için güncellenmiş yorumu gösteren kod tarafından oluşturulur.

#### **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **Zincirlenmiş Yorumları Kaldır**

### **Excel ile Zincirlenmiş yorumları kaldırın**

 Excel'de zincirlenmiş yorumları kaldırmak için, yorumları içeren hücreye sağ tıklayın ve**Yorumu Sil** Aşağıdaki resimde gösterildiği gibi seçenek.

![yapılacaklar:resim_alternatif_metin](threaded-comments_8.jpg)

### **Aspose.Cells kullanarak Zincirli yorumları kaldırın**

Aspose.Cells sağlar[**Yorumlar.Kaldır**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index)belirtilen sütun için yorumları kaldırma yöntemi.[**Yorumlar.Kaldır**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index)yöntem, sütun adını bir parametre olarak kabul eder, o sütundaki yorumları kaldırır.

Aşağıdaki örnek, sütunu yükleyerek A1 sütunundaki açıklamaları kaldırmayı gösterir.[örnek Excel Dosyası](89849861.xlsx). Lütfen bkz[çıktı excel dosyası](89849864.xlsx)referans için kod tarafından oluşturulur.

#### **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

 Lütfen Aspose.Cells ile yorumu kaldırarak yazarın otomatik olarak kaldırılmadığını unutmayın. Yazarı da kaldırmanız gerekiyorsa, lütfen RemoveAt yöntemini kullanın.[**ThreadedCommentYazarKoleksiyon**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection) Yukarıdaki örnekte gösterildiği gibi sınıf.

{{% /alert %}}
