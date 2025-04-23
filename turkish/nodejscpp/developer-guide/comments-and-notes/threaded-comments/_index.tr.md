---  
title: Node.js ile İş Parçacıklı Yorumlar ve C++  
linktitle: İz bırakan Yorumlar  
type: docs  
weight: 140  
url: /tr/nodejs-cpp/threaded-comments/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel belgelerinde iş parçacıklı yorumları yönetin. Yorum ekleme, okuma, düzenleme ve kaldırma öğrenin.  
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

 Aspose.Cells, düzenli yorumlar eklemek için [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) yöntemini sağlar. [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) yöntemi aşağıdaki üç parametreyi kabul eder.  

- Hücre Adı: Yoruma eklenecek hücrenin adı.  
- Yorum Metni: Yorumun metni.  
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentauthor): Yorumun yazarı  

Aşağıdaki kod örneği, cell A1'e iş parçacıklı bir yorum eklemek için [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) metodunun kullanımını gösterir. Lütfen kod tarafından oluşturulan [çıktı Excel dosyasına](89849859.xlsx) bakın.  

#### **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const outDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook();

// Add Author
const authorIndex = workbook.getWorksheets().getThreadedCommentAuthors().add("Aspose Test", "", "");
const author = workbook.getWorksheets().getThreadedCommentAuthors().get(authorIndex);

// Add Threaded Comment
workbook.getWorksheets().get(0).getComments().addThreadedComment("A1", "Test Threaded Comment", author);

workbook.save(outDir + "AddThreadedComments_out.xlsx");
```  

## **İz Bırakan Yorumları Okuma**  

### **Excel'de İz bırakan yorumları okuma**  

Excel'de iz bırakan yorumları okumak için, yorum içeren hücrenin üzerine fareyi getirerek yorumları görüntüleyebilirsiniz. Yorumlar görünümü aşağıdaki resimde görüldüğü gibi olacaktır.  

![todo:image_alt_text](threaded-comments_1.jpg)  

### **Aspose.Cells Kullanarak İz Bırakan Yorumları Okuma**  

Aspose.Cells, belirli sütun için iz bırakan yorumları almak için [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) yöntemini sağlar. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) yöntemi, sütun adını parametre olarak alır ve [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection)'yi döndürür. Yorumları görüntülemek için [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) üzerinde yinelemeniz gerekebilir.  

Aşağıdaki örnek, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek A1 sütunundan yorumları okumayı göstermektedir. Referans için kod tarafından oluşturulan konsol çıktısını inceleyin.  

#### **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data"); // Adjust as necessary

const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");

// Loads the workbook which contains threaded comments
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comments
const threadedComments = worksheet.getComments().getThreadedComments("A1");

const count = threadedComments.getCount();
for (let i = 0; i < count; i++) {
const comment = threadedComments.get(i);
console.log("Comment: " + comment.getNotes());
console.log("Author: " + comment.getAuthor().getName());
}
```  

#### **Konsol Çıktısı**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

{{< /highlight >}}  

### **Dişli yorumların oluşturulma zamanını okuyun**  

Aspose.Cells, belirli sütunun iş parçacıklı yorumlarını almak için [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) metodunu sağlar. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) metodu, sütun adını parametre olarak alır ve [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) döner. [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) üzerinde yineleyebilir ve [**ThreadedComment.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/threadedcomment/#getCreatedTime--) özelliğini kullanabilirsiniz.  

Aşağıdaki örnek, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek dişli yorumların oluşturulma zamanını okuma işlemini göstermektedir. Kod tarafından oluşturulan konsol çıktısını referans için lütfen inceleyin.  

#### **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comments
const threadedComments = worksheet.getComments().getThreadedComments("A1");

const count = threadedComments.getCount();

for (let i = 0; i < count; i++) {
const comment = threadedComments.get(i);
console.log("Comment: " + comment.getNotes());
console.log("Author: " + comment.getAuthor().getName());
console.log("Created Time: " + comment.getCreatedTime());
}
```  

#### **Konsol Çıktısı**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

Created Time: 5/15/2019 12:46:23 PM  

{{< /highlight >}}  

## **Dişli Yorumları Düzenle**  

### **Excel'de Dişli yorumu düzenle**  

Excel'de dişli yorumu düzenlemek için, aşağıdaki resimde gösterildiği gibi yorumun üzerindeki **Düzenle** bağlantısına tıklayın.  

![todo:image_alt_text](threaded-comments_7.jpg)  

### **Aspose.Cells, belirtilen sütun için dişli yorumları almak için {0} metodunu sağlar. {1} metodu sütun adını bir parametre olarak alır ve {2} değerini döndürür. Gereken yorumu {3} içinde güncelleyebilir ve çalışma kitabını kaydedebilirsiniz.**  

Aspose.Cells, belirli sütunun iş parçacıklı yorumlarını almak için [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) metodunu sağlar. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) metodu, sütun adını parametre olarak alır ve [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) döner. Gerekli yorumu [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) üzerinde güncelleyebilir ve kitaplığı kaydedebilirsiniz.  

Aşağıdaki örnek, A1 sütunundaki ilk konu başlı yorumu düzenlemeyi, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek gösterir. Lütfen kodla oluşturulan güncellenmiş yorumu referans için [çıktı Excel dosyasını](89849862.xlsx) görün.  

#### **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comment
const comment = worksheet.getComments().getThreadedComments("A1").get(0);
comment.setNotes("Updated Comment");

workbook.save(outDir + "EditThreadedComments.xlsx");
```  

## **Dişli Yorumları Kaldır**  

### **Excel'de dişli yorumları kaldırın**  

Excel'de dişli yorumları kaldırmak için, yorumları içeren hücre üzerinde sağ tıklayın ve aşağıdaki resimde gösterildiği gibi **Yorumu Sil** seçeneğini tıklayın.  

![todo:image_alt_text](threaded-comments_8.jpg)   


