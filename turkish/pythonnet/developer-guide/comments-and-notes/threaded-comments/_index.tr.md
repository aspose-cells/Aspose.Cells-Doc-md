---
title: İz bırakan Yorumlar
type: docs
weight: 140
url: /tr/python-net/threaded-comments/
---

## **İz bırakan Yorumlar**

MS Excel 365, iz bırakan yorum eklemek için bir özellik sağlar. Bu yorumlar, sohbetler gibi çalışır ve tartışmalar için kullanılabilir. Yorumlar artık, iz bırakan konuşmalar yapma olanağı tanıyan bir Yanıt kutusuyla birlikte gelir. Eski yorumlar, Excel 365'te Notlar olarak adlandırılır. Aşağıdaki ekran görüntüsü, Excel'de açıldığında iz bırakan yorumların nasıl görüntülendiğini göstermektedir.

![todo:image_alt_text](threaded-comments_1.jpg)

İz bırakan yorumlar, Excel'in daha eski sürümlerinde bu şekilde gösterilir. Aşağıdaki resimler, örnek dosyanın Excel 2016'da açılarak alınmıştır.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells for Python via .NET ayrıca zincirlenmiş yorumları yönetmek için özelliğe sahiptir.

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

### **Aspose.Cells for Python via .NET kullanarak Zincirlenmiş Yorum Ekleme**

Aspose.Cells for Python via .NET, zincirlenmiş yorumlar eklemek için [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment/) yöntemini sağlar. [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment) yöntemi üç parametre kabul eder.

- Hücre Adı: Yoruma eklenecek hücrenin adı.
- Yorum Metni: Yorumun metni.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentauthor): Yorumun yazarı

Aşağıdaki kod örneği, A1 hücresine iz bırakan Yorum eklemek için [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment) yönteminin kullanımını göstermektedir. Referans için kod tarafından oluşturulan [çıktı Excel dosyasını](89849859.xlsx) lütfen inceleyin.

#### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-AddThreadedComments-1.py" >}}

## **İz Bırakan Yorumları Okuma**

### **Excel'de İz bırakan yorumları okuma**

Excel'de iz bırakan yorumları okumak için, yorum içeren hücrenin üzerine fareyi getirerek yorumları görüntüleyebilirsiniz. Yorumlar görünümü aşağıdaki resimde görüldüğü gibi olacaktır.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Aspose.Cells for Python via .NET kullanarak Zincirlenmiş Yorumları Okuma**

Aspose.Cells for Python via .NET, belirli sütun için zincirlenmiş yorumları almak için [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) yöntemini sağlar. [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) yöntemi sütun adını parametre olarak alır ve [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) döndürür. Yorumları görmek için [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) üzerinden döngü yapabilirsiniz.

Aşağıdaki örnek, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek A1 sütunundan yorumları okumayı göstermektedir. Referans için kod tarafından oluşturulan konsol çıktısını inceleyin.

#### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedComments-1.py" >}}

#### **Konsol Çıktısı**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Dişli yorumların oluşturulma zamanını okuyun**

Aspose.Cells for Python via .NET, belirli sütun için zincirlenmiş yorumları almak amacıyla [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) yöntemini sağlar. [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) yöntemi sütun adını parametre olarak alır ve [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) döndürür. [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) üzerinde döngü yapabilir ve [**ThreadedComment.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcomment/created_time) özelliğini kullanabilirsiniz.

Aşağıdaki örnek, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek dişli yorumların oluşturulma zamanını okuma işlemini göstermektedir. Kod tarafından oluşturulan konsol çıktısını referans için lütfen inceleyin.

#### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedCommentCreatedTime-1.py" >}}

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

### **Aspose.Cells for Python via .NET kullanarak Zincirlenmiş yorumu düzenle**

Aspose.Cells for Python via .NET, belirli sütun için zincirlenmiş yorumları almak amacıyla [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) yöntemini sağlar. [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) yöntemi sütun adını parametre olarak alır ve [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) döndürür. Gerekli yorumu [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) içinde güncelleyebilir ve çalışma kitabını kaydedebilirsiniz.

Aşağıdaki örnek, A1 sütunundaki ilk konu başlı yorumu düzenlemeyi, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek gösterir. Lütfen kodla oluşturulan güncellenmiş yorumu referans için [çıktı Excel dosyasını](89849862.xlsx) görün.

#### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-EditThreadedComments-1.py" >}}

