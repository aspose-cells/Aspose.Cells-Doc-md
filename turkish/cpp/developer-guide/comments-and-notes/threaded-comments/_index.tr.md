---
title: C++ ile Tüzenlenmiş Yorumlar
linktitle: İz bırakan Yorumlar
type: docs
weight: 140
url: /tr/cpp/threaded-comments/
description: Aspose.Cells kullanarak C++ ile excel dosyalarında düzenli yorumlar ekleme, okuma, düzenleme ve kaldırma hakkında bilgi edinin.
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

 Aspose.Cells, düzenli yorumlar eklemek için [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) yöntemini sağlar. [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) yöntemi aşağıdaki üç parametreyi kabul eder.

- Hücre Adı: Yoruma eklenecek hücrenin adı.
- Yorum Metni: Yorumun metni.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthor/): Yorumun yazarı

Aşağıdaki kod örneği, A1 hücresine iz bırakan Yorum eklemek için [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) yönteminin kullanımını göstermektedir. Referans için kod tarafından oluşturulan [çıktı Excel dosyasını](89849859.xlsx) lütfen inceleyin.

#### **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add Author
    int authorIndex = workbook.GetWorksheets().GetThreadedCommentAuthors().Add(u"Aspose Test", u"", u"");
    ThreadedCommentAuthor author = workbook.GetWorksheets().GetThreadedCommentAuthors().Get(authorIndex);

    // Add Threaded Comment
    workbook.GetWorksheets().Get(0).GetComments().AddThreadedComment(u"A1", u"Test Threaded Comment", author);

    // Save the workbook
    workbook.Save(outDir + u"AddThreadedComments_out.xlsx");

    std::cout << "Threaded comment added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **İz Bırakan Yorumları Okuma**

### **Excel'de İz bırakan yorumları okuma**

Excel'de iz bırakan yorumları okumak için, yorum içeren hücrenin üzerine fareyi getirerek yorumları görüntüleyebilirsiniz. Yorumlar görünümü aşağıdaki resimde görüldüğü gibi olacaktır.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Aspose.Cells Kullanarak İz Bırakan Yorumları Okuma**

Aspose.Cells, belirli sütun için iz bırakan yorumları almak için [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) yöntemini sağlar. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) yöntemi, sütun adını parametre olarak alır ve [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/)'yi döndürür. Yorumları görüntülemek için [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) üzerinde yinelemeniz gerekebilir.

Aşağıdaki örnek, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek A1 sütunundan yorumları okumayı göstermektedir. Referans için kod tarafından oluşturulan konsol çıktısını inceleyin.

#### **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook
    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get Threaded Comments
    ThreadedCommentCollection threadedComments = worksheet.GetComments().GetThreadedComments(u"A1");

    // Iterate through threaded comments
    for (int i = 0; i < threadedComments.GetCount(); i++)
    {
        ThreadedComment comment = threadedComments.Get(i);
        cout << "Comment: " << comment.GetNotes().ToUtf8() << endl;
        cout << "Author: " << comment.GetAuthor().GetName().ToUtf8() << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

#### **Konsol Çıktısı**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Dişli yorumların oluşturulma zamanını okuyun**

Aspose.Cells belirtilen sütun için dişli yorumları almak için [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) metodunu sağlar. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) metodu sütun adını bir parametre olarak alır ve [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) değerini döndürür. [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) üzerinde yineleyebilir ve [**ThreadedComment.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcomment/getcreatedtime/) özelliğini kullanabilirsiniz.

Aşağıdaki örnek, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek dişli yorumların oluşturulma zamanını okuma işlemini göstermektedir. Kod tarafından oluşturulan konsol çıktısını referans için lütfen inceleyin.

#### **Örnek Kod**

```cpp
#include <iostream>
#include <iomanip>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    ThreadedCommentCollection threadedComments = worksheet.GetComments().GetThreadedComments(u"A1");

    for (int i = 0; i < threadedComments.GetCount(); i++)
    {
        ThreadedComment comment = threadedComments.Get(i);
        cout << "Comment: " << comment.GetNotes().ToUtf8() << endl;
        cout << "Author: " << comment.GetAuthor().GetName().ToUtf8() << endl;
        Date createdTime = comment.GetCreatedTime();
        ostringstream oss;
        oss << setfill('0') 
            << setw(4) << createdTime.year << "-"
            << setw(2) << createdTime.month << "-"
            << setw(2) << createdTime.day << " "
            << setw(2) << createdTime.hour << ":"
            << setw(2) << createdTime.minute << ":"
            << setw(2) << createdTime.second;
        cout << "Created Time: " << oss.str() << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

#### **Konsol Çıktısı**

{{< highlight cpp >}}

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

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the threaded comment from cell A1
    ThreadedComment comment = worksheet.GetComments().GetThreadedComments(u"A1").Get(0);

    // Update the comment text
    comment.SetNotes(u"Updated Comment");

    // Save the workbook
    workbook.Save(outDir + u"EditThreadedComments.xlsx");

    std::cout << "Threaded comment updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Dişli Yorumları Kaldır**

### **Excel'de dişli yorumları kaldırın**

Excel'de dişli yorumları kaldırmak için, yorumları içeren hücre üzerinde sağ tıklayın ve aşağıdaki resimde gösterildiği gibi **Yorumu Sil** seçeneğini tıklayın.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Aspose.Cells, belirtilen sütun için yorumları kaldırmak için {0} metodu sağlar. {1} metodu sütun adını bir parametre olarak alır ve o sütundaki yorumları kaldırır.**

Aşağıdaki örnek, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek A1 sütunundaki yorumları kaldırma işlemini göstermektedir. Kod tarafından oluşturulan [çıktı Excel dosyasını](89849864.xlsx) referans için lütfen inceleyin.

Aşağıdaki örnek, A1 sütunundaki yorumları kaldırmayı, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek gösterir. Referans için kodla oluşturulan [çıktı Excel dosyasını](89849864.xlsx) görün.

#### **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the comments collection
    CommentCollection comments = worksheet.GetComments();

    // Get the author of the first threaded comment in cell A1
    ThreadedCommentAuthor author = worksheet.GetComments().GetThreadedComments(u"A1").Get(0).GetAuthor();

    // Remove the comment at cell A1
    comments.RemoveAt(u"A1");

    // Get the threaded comment authors collection
    ThreadedCommentAuthorCollection authors = workbook.GetWorksheets().GetThreadedCommentAuthors();

    // Save the workbook
    workbook.Save(outDir + u"ThreadedCommentsSample_Out.xlsx");

    std::cout << "Threaded comments processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Lütfen Aspose.Cells ile yorum kaldırma işlemi yaparken, yazar otomatik olarak kaldırılmaz. Yazarı da kaldırmak istiyorsanız, lütfen yukarıdaki örnekte [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthorcollection/) sınıfının RemoveAt metodu kullanın.

{{% /alert %}}
