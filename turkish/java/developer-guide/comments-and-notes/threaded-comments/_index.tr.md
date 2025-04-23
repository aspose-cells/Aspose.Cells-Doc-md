---
title: İz bırakan Yorumlar
type: docs
weight: 140
url: /tr/java/threaded-comments/
---

# **İz bırakan Yorumlar**
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
  - **İnceleme** Sekmesine tıklayın
  - **Yeni Yorum** düğmesine tıklayın
  - Bu, etkin hücreye yorum girmek için bir iletişim kutusu açacaktır.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Yorum eklemek istediğiniz hücreye sağ tıklayın.
  - **Yeni Yorum** seçeneğine tıklayın
  - **Yeni Yorum** seçeneğine tıklayın
  - Bu, etkin hücreye yorum girmek için bir iletişim kutusu açacaktır.
  - ![todo:image_alt_text](threaded-comments_5)
### **Aspose.Cells Kullanarak İz bırakan Yorum Ekleme**
Aspose.Cells, threaded yorumlar eklemek için [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) yöntemini sağlar. [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) yöntemi aşağıdaki üç parametreyi kabul eder.

- Hücre Adı: Yoruma eklenecek hücrenin adı.
- Yorum Metni: Yorumun metni.
- [ThreadedCommentAuthor](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor): Yorumun yazarı

Aşağıdaki kod örneği, hücre A1'e threaded yorum eklemek için [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) kullanımını göstermektedir. Lütfen, kod tarafından oluşturulan [çıktı Excel dosyasını](AddThreadedComments_out.xlsx) referans olarak inceleyin.
#### **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **İz Bırakan Yorumları Okuma**
### **Excel'de İz bırakan yorumları okuma**
Excel'de iz bırakan yorumları okumak için, yorum içeren hücrenin üzerine fareyi getirerek yorumları görüntüleyebilirsiniz. Yorumlar görünümü aşağıdaki resimde görüldüğü gibi olacaktır.

![todo:image_alt_text](threaded-comments_1.jpg)
### **Aspose.Cells Kullanarak İz Bırakan Yorumları Okuma**
Aspose.Cells, belirli bir sütun için threaded yorumları almak amacıyla [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) yöntemini sağlar. [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) yöntemi, sütun adını parametre olarak kabul eder ve [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) döner. Bu koleksiyon üzerinde gezinerek yorumları görebilirsiniz.

Aşağıdaki örnek, A1 sütunundan yorumları alarak [örnek Excel Dosyasını](ThreadedCommentsSample.xlsx) yükleyerek kullanıcı tarafından oluşturulan çıktıyı referans için konsol çıktısını gösterir.
#### **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **Konsol Çıktısı**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Dişli yorumların oluşturulma zamanını okuyun**
Aspose.Cells, belirli bir sütun için threaded yorumları almak amacıyla [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) yöntemini sağlar. [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) yöntemi, sütun adını parametre olarak kabul eder ve [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) döner. Bu koleksiyon üzerinde gezinerek yorumları görebilirsiniz ve [ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime) özelliğini kullanabilirsiniz.

Aşağıdaki örnek, [örnek Excel Dosyasını](ThreadedCommentsSample.xlsx) yükleyerek oluşturulan konsol çıktısı referans için konu yorumlarının oluşturulma zamanını okur.
#### **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **Konsol Çıktısı**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 2019-05-15T12:46:23

{{< /highlight >}}

## **Dişli Yorumları Düzenle**
### **Excel'de Dişli yorumu düzenle**
Excel'de bir dikey yorumu düzenlemek için, aşağıdaki resimde gösterildiği gibi yoruma tıklayarak **Düzenle** bağlantısına tıklayın.

![todo:image_alt_text](threaded-comments_7.jpg)
### **Aspose.Cells, belirtilen sütun için dişli yorumları almak için {0} metodunu sağlar. {1} metodu sütun adını bir parametre olarak alır ve {2} değerini döndürür. Gereken yorumu {3} içinde güncelleyebilir ve çalışma kitabını kaydedebilirsiniz.**
Aspose.Cells, belirli bir sütun için threaded yorumları almak amacıyla [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) yöntemini sağlar. [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) yöntemi, sütun adını parametre olarak kabul eder ve [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) döner. Bu koleksiyon üzerinde gerekli yorumu güncelleyebilir ve çalışma kitabını kaydedebilirsiniz.

Aşağıdaki örnek, [örnek Excel Dosyasını](ThreadedCommentsSample.xlsx) yükleyerek A1 sütununda ilk threaded yorumu düzenleme işlemini göstermektedir. Kod tarafından oluşturulan [çıktı Excel dosyasını](EditThreadedComments.xlsx) inceleyerek güncellenmiş yorumu görebilirsiniz.
#### **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **Dişli Yorumları Kaldır**
### **Excel'de dişli yorumları kaldırın**
Aspose.Cells ile threaded yorumları kaldırmak için [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) yöntemi sağlar. [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) yöntemi, belirtilen sütun için yorumları kaldırır.

![todo:image_alt_text](threaded-comments_8.jpg)
### **Aspose.Cells, belirtilen sütun için yorumları kaldırmak için {0} metodu sağlar. {1} metodu sütun adını bir parametre olarak alır ve o sütundaki yorumları kaldırır.**
Aspose.Cells, belirli bir sütun için yorumları kaldırmak amacıyla [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt-int-) yöntemini sağlar. [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt-int-) yöntemi, sütun adını parametre olarak alır ve o sütundaki yorumları kaldırır. 

Aşağıdaki örnek, [örnek Excel Dosyasını](ThreadedCommentsSample.xlsx) yükleyerek A1 sütunundaki yorumları kaldırma işlemini göstermektedir. Kod tarafından oluşturulan [çıktı Excel dosyasını](ThreadedCommentsSample_Out.xlsx) inceleyerek referans için görebilirsiniz.
#### **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

Lütfen dikkat edin, Aspose.Cells kullanarak yorum kaldırıldığında, yazar otomatik olarak silinmez. Eğer yazar da kaldırılmak istenirse, yukarıdaki örnekte gösterildiği gibi [ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt-int-) yöntemini kullanmalısınız.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
