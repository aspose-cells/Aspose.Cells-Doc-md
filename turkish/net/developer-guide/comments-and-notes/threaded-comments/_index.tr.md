---
title: İz bırakan Yorumlar
type: docs
weight: 140
url: /tr/net/threaded-comments/
---

## **İz bırakan Yorumlar**

MS Excel 365, iz bırakan yorum eklemek için bir özellik sağlar. Bu yorumlar, sohbetler gibi çalışır ve tartışmalar için kullanılabilir. Yorumlar artık, iz bırakan konuşmalar yapma olanağı tanıyan bir Yanıt kutusuyla birlikte gelir. Eski yorumlar, Excel 365'te Notlar olarak adlandırılır. Aşağıdaki ekran görüntüsü, Excel'de açıldığında iz bırakan yorumların nasıl görüntülendiğini göstermektedir.

![todo:image_alt_text](threaded-comments_1.jpg)

İz bırakan yorumlar, Excel'in daha eski sürümlerinde bu şekilde gösterilir. Aşağıdaki resimler, örnek dosyanın Excel 2016'da açılarak alınmıştır.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells ayrıca iz bırakan yorumları yönetme özelliği sağlar.

## **İz Bırakan Yorumlar Ekle**

### **Excel'de İz bırakan yorum eklemek için aşağıdaki adımları izleyin.**

- Yöntem 1

- **İncele** Sekmesine tıklayın
  - **Yeni Yorum** düğmesine tıklayın
  - Bu, etkin hücreye yorum girmek için bir iletişim kutusu açacaktır.
  - Bu, etkin hücreye yorum girmek için bir iletişim kutusu açacaktır.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Yorum eklemek istediğiniz hücreye sağ tıklayın.
  - **Yeni Yorum** seçeneğine tıklayın
  - **Yeni Yorum** seçeneğine tıklayın.
  - Bu, etkin hücreye yorum girmek için bir iletişim kutusu açacaktır.
  - ![todo:image_alt_text](threaded-comments_5)

### **Aspose.Cells Kullanarak İz bırakan Yorum Ekleme**

Aspose.Cells, iz bırakan yorumları eklemek için [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) yöntemi sağlar. [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) yöntemi, aşağıdaki üç parametreyi kabul eder.

- Hücre Adı: Yoruma eklenecek hücrenin adı.
- Yorum Metni: Yorumun metni.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor): Yorumun yazarı

Aşağıdaki kod örneği, A1 hücresine iz bırakan Yorum eklemek için [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) yönteminin kullanımını göstermektedir. Referans için kod tarafından oluşturulan [çıktı Excel dosyasını](89849859.xlsx) lütfen inceleyin.

#### **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **İz Bırakan Yorumları Okuma**

### **Excel'de İz bırakan yorumları okuma**

Excel'de iz bırakan yorumları okumak için, yorum içeren hücrenin üzerine fareyi getirerek yorumları görüntüleyebilirsiniz. Yorumlar görünümü aşağıdaki resimde görüldüğü gibi olacaktır.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Aspose.Cells Kullanarak İz Bırakan Yorumları Okuma**

Aspose.Cells, belirli sütun için iz bırakan yorumları almak için [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) yöntemini sağlar. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) yöntemi, sütun adını parametre olarak alır ve [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)'yi döndürür. Yorumları görüntülemek için [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) üzerinde yinelemeniz gerekebilir.

Aşağıdaki örnek, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek A1 sütunundan yorumları okumayı göstermektedir. Referans için kod tarafından oluşturulan konsol çıktısını inceleyin.

#### **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **Konsol Çıktısı**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Dişli yorumların oluşturulma zamanını okuyun**

Aspose.Cells belirtilen sütun için dişli yorumları almak için [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) metodunu sağlar. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) metodu sütun adını bir parametre olarak alır ve [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) değerini döndürür. [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) üzerinde yineleyebilir ve [**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime) özelliğini kullanabilirsiniz.

Aşağıdaki örnek, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek dişli yorumların oluşturulma zamanını okuma işlemini göstermektedir. Kod tarafından oluşturulan konsol çıktısını referans için lütfen inceleyin.

#### **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **Konsol Çıktısı**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Dişli Yorumları Düzenle**

### **Excel'de Dişli yorumu düzenle**

Excel'de dişli yorumu düzenlemek için, aşağıdaki resimde gösterildiği gibi yorumun üzerindeki **Düzenle** bağlantısına tıklayın.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Aspose.Cells, belirtilen sütun için dişli yorumları almak için {0} metodunu sağlar. {1} metodu sütun adını bir parametre olarak alır ve {2} değerini döndürür. Gereken yorumu {3} içinde güncelleyebilir ve çalışma kitabını kaydedebilirsiniz.**

Aşağıdaki örnek, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek A1 sütunundaki ilk dişli yorumu düzenleme işlemini göstermektedir. Kod tarafından oluşturulan güncellenmiş yorumu içeren [çıktı Excel dosyasını](89849862.xlsx) referans için lütfen inceleyin.

Aşağıdaki örnek, A1 sütunundaki ilk konu başlı yorumu düzenlemeyi, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek gösterir. Lütfen kodla oluşturulan güncellenmiş yorumu referans için [çıktı Excel dosyasını](89849862.xlsx) görün.

#### **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **Dişli Yorumları Kaldır**

### **Excel'de dişli yorumları kaldırın**

Excel'de dişli yorumları kaldırmak için, yorumları içeren hücre üzerinde sağ tıklayın ve aşağıdaki resimde gösterildiği gibi **Yorumu Sil** seçeneğini tıklayın.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Aspose.Cells, belirtilen sütun için yorumları kaldırmak için {0} metodu sağlar. {1} metodu sütun adını bir parametre olarak alır ve o sütundaki yorumları kaldırır.**

Aşağıdaki örnek, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek A1 sütunundaki yorumları kaldırma işlemini göstermektedir. Kod tarafından oluşturulan [çıktı Excel dosyasını](89849864.xlsx) referans için lütfen inceleyin.

Aşağıdaki örnek, A1 sütunundaki yorumları kaldırmayı, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek gösterir. Referans için kodla oluşturulan [çıktı Excel dosyasını](89849864.xlsx) görün.

#### **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

Lütfen Aspose.Cells ile yorum kaldırma işlemi yaparken, yazar otomatik olarak kaldırılmaz. Yazarı da kaldırmak istiyorsanız, lütfen yukarıdaki örnekte [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection) sınıfının RemoveAt metodu kullanın.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
