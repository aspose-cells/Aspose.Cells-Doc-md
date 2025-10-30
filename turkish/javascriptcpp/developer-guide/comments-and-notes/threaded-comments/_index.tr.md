---
title: JavaScript ile C++ kullanarak İşlemli Yorumlar
linktitle: İz bırakan Yorumlar
type: docs
weight: 140
url: /tr/javascript-cpp/threaded-comments/
description: Excel belgelerinde işlemli yorumları yönetmek için Aspose.Cells for JavaC++ betiğini kullanın. Ekleyin, okuyun, düzenleyin ve kaldırın öğrenin.
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

 Aspose.Cells, düzenli yorumlar eklemek için [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) yöntemini sağlar. [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) yöntemi aşağıdaki üç parametreyi kabul eder.

- Hücre Adı: Yoruma eklenecek hücrenin adı.
- Yorum Metni: Yorumun metni.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentauthor): Yorumun yazarı

Aşağıdaki kod örneği, cell A1'e iş parçacıklı bir yorum eklemek için [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) metodunun kullanımını gösterir. Lütfen kod tarafından oluşturulan [çıktı Excel dosyasına](89849859.xlsx) bakın.

#### **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Threaded Comment</title>
    </head>
    <body>
        <h1>Add Threaded Comment Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create a new workbook
            const workbook = new Workbook();

            // Add Author
            const authorIndex = workbook.worksheets.threadedCommentAuthors.add("Aspose Test", "", "");
            const author = workbook.worksheets.threadedCommentAuthors.get(authorIndex);

            // Add Threaded Comment to cell A1 in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.comments.addThreadedComment("A1", "Test Threaded Comment", author);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddThreadedComments_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Threaded comment added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **İz Bırakan Yorumları Okuma**

### **Excel'de İz bırakan yorumları okuma**

Excel'de iz bırakan yorumları okumak için, yorum içeren hücrenin üzerine fareyi getirerek yorumları görüntüleyebilirsiniz. Yorumlar görünümü aşağıdaki resimde görüldüğü gibi olacaktır.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Aspose.Cells Kullanarak İz Bırakan Yorumları Okuma**

Aspose.Cells, belirli sütun için iz bırakan yorumları almak için [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) yöntemini sağlar. [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) yöntemi, sütun adını parametre olarak alır ve [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection)'yi döndürür. Yorumları görüntülemek için [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) üzerinde yinelemeniz gerekebilir.

Aşağıdaki örnek, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek A1 sütunundan yorumları okumayı göstermektedir. Referans için kod tarafından oluşturulan konsol çıktısını inceleyin.

#### **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Threaded Comments Example</title>
    </head>
    <body>
        <h1>Threaded Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comments for cell A1
            const threadedComments = worksheet.comments.threadedComments("A1");

            const count = threadedComments.count;
            let html = '<h2>Threaded Comments</h2>';
            if (count === 0) {
                html += '<p>No threaded comments found for A1.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < count; i++) {
                    const comment = threadedComments.get(i);
                    const notes = comment.notes;
                    const authorName = comment.author.name;
                    html += `<li><strong>Author:</strong> ${authorName} <br/><strong>Comment:</strong> ${notes}</li>`;
                }
                html += '</ul>';
            }

            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

#### **Konsol Çıktısı**

{{< highlight javascript >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Dişli yorumların oluşturulma zamanını okuyun**

Aspose.Cells, belirli sütunun iş parçacıklı yorumlarını almak için [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) metodunu sağlar. [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) metodu, sütun adını parametre olarak alır ve [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) döner. [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) üzerinde yineleyebilir ve [**ThreadedComment.createdTime**](https://reference.aspose.com/cells/javascript-cpp/threadedcomment/#createdTime--) özelliğini kullanabilirsiniz.

Aşağıdaki örnek, [örnek Excel Dosyasını](89849861.xlsx) yükleyerek dişli yorumların oluşturulma zamanını okuma işlemini göstermektedir. Kod tarafından oluşturulan konsol çıktısını referans için lütfen inceleyin.

#### **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Threaded Comments Example</title>
    </head>
    <body>
        <h1>Threaded Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // No try-catch: allow errors to propagate for testing
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comments for cell A1
            const threadedComments = worksheet.comments.threadedComments("A1");

            const count = threadedComments.count;

            let html = '<h2>Threaded Comments (Cell A1)</h2>';
            if (count === 0) {
                html += '<p>No threaded comments found in cell A1.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < count; i++) {
                    const comment = threadedComments.get(i);
                    const notes = comment.notes;
                    const authorName = comment.author.name;
                    const createdTime = comment.createdTime;

                    console.log("Comment: " + notes);
                    console.log("Author: " + authorName);
                    console.log("Created Time: " + createdTime);

                    html += `<li><strong>Author:</strong> ${authorName} <br/><strong>Created:</strong> ${createdTime} <br/><strong>Comment:</strong> ${notes}</li>`;
                }
                html += '</ul>';
            }

            resultDiv.innerHTML = html;

            // No file modifications or save in this example; hide download link
            downloadLink.style.display = 'none';
        });
    </script>
</html>
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

Aspose.Cells, belirli sütunun iş parçacıklı yorumlarını almak için [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) metodunu sağlar. [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) metodu, sütun adını parametre olarak alır ve [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) döner. Gerekli yorumu [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) üzerinde güncelleyebilir ve kitaplığı kaydedebilirsiniz.

 Aşağıdaki örnek, ilk işlemli yorumu düzenlemeyi göstermektedir: [örnek Excel Dosyası](89849861.xlsx) yüklenerek. Üretilen [çıkış Excel dosyası](89849862.xlsx) referans için güncellenen yorumu gösterir.

#### **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Edit Threaded Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comment from cell A1
            const comment = worksheet.comments.threadedComments("A1").get(0);

            // Update the threaded comment notes
            comment.notes = "Updated Comment";

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'EditThreadedComments.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Edited Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Threaded comment updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Dişli Yorumları Kaldır**

### **Excel'de dişli yorumları kaldırın**

Excel'de dişli yorumları kaldırmak için, yorumları içeren hücre üzerinde sağ tıklayın ve aşağıdaki resimde gösterildiği gibi **Yorumu Sil** seçeneğini tıklayın.

![todo:image_alt_text](threaded-comments_8.jpg)
