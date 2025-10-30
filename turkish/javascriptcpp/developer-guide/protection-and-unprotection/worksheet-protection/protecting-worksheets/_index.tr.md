---
title: JavaScript aracılığıyla C++ ile Çalışma Sayfalarını Koruma
linktitle: Çalışma Sayfalarını Koruma
type: docs
weight: 10
url: /tr/javascript-cpp/protecting-worksheets/
description: Excel de çalışma sayfalarını koruma yöntemlerini öğrenin, dahil olmak üzere satırları, sütunları ve belirli hücreleri koruma
---

{{% alert color="primary" %}}

Bir çalışma sayfası korunduğunda, kullanıcıların yapabileceği işlemler kısıtlanır. Örneğin, veri girişi yapamazlar, satırları veya sütunları ekleyip silemezler vb.

{{% /alert %}}

## **Çalışma Sayfalarını Koruma**

### **Giriş**

Microsoft Excel'de genel koruma seçenekleri:

- İçerik
- Nesneler
- Senaryolar

Korunan çalışma sayfaları hassas verileri gizlemez veya korumaz, bu nedenle dosya şifrelemesinden farklıdır. Genellikle, çalışma sayfası koruması sunumsal amaçlar için uygundur. Kullanıcının çalışma sayfasındaki veri, içerik ve biçimlendirmeyi değiştirmesini önler.

### **Bir Çalışma Sayfasını Koruma**

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı bir sınıf sağlar, bu da bir Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir.

[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, çalışma sayfası üzerinde koruma uygulamak için kullanılan [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) yöntemini sağlar. [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) yöntemi aşağıdaki parametreleri kabul eder:

- Koruma Türü, çalışma sayfasına uygulanacak koruma türü. Koruma türü, [**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype) numaralandırması ile uygulanır.
- Yeni Parola, çalışma sayfasını korumak için kullanılan yeni parola.
- Eski Parola, çalışma sayfası zaten parola korumalıysa eski paroladır. Çalışma sayfası zaten korunmamışsa sadece null geçirin.

[**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype) enum'unda şu ön tanımlı koruma türleri bulunur:

|**Koruma Türleri**|**Açıklama**|
| :- | :- |
|All|Kullanıcı bu çalışma sayfasında herhangi bir şeyi değiştiremez|
|Contents|Kullanıcı bu çalışma sayfasında veri giremez|
|Objects|Kullanıcı çizim nesnelerini değiştiremez|
|Scenarios|Kullanıcı, kaydedilmiş senaryoları değiştiremez|
|Structure|Kullanıcı yapıyı değiştiremez|
|Windows|Koruma, pencerelere uygulanır|
|None|Koruma uygulanmaz|

Aşağıdaki örnek, bir çalışma sayfasını bir şifre ile korumanın nasıl yapıldığını göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Protect Worksheet Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Ensure Aspose.Cells is initialized before proceeding
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Protecting the worksheet with a password
            worksheet.protect(ProtectionType.All, "aspose", null);

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Yukarıdaki kod çalışma sayfasını korumak için kullanıldıktan sonra, çalışma sayfasının korumasını açarak kontrol edebilirsiniz. Dosyayı açtığınızda çalışma sayfasına bazı veriler eklemeye çalıştığınızda aşağıdaki iletişim kutusunu göreceksiniz:

|**Kullanıcının çalışma sayfasını değiştiremeyeceği konusunda uyarı veren iletişim kutusu**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Çalışma sayfasında çalışmak için **Koruma**, ardından **Sayfayı Korumayı Kaldır** öğesini **Araçlar** menü öğesinden seçerek çalışma sayfasının korumasını kaldırın.

**Sayfayı Korumayı Kaldır** menü öğesini seçtikten sonra, bir iletişim kutusu açılacaktır ve size çalışma sayfasında çalışmanız için şifreyi girmenizi isteyecektir, aşağıda gösterildiği gibi:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Microsoft Excel Kullanarak Çalışma Sayfasındaki Birkaç Hücreyi Koruma**

Belli senaryolarda, sadece birkaç hücreyi kilitlemeniz gerekebilir. Belirli hücreleri kilitlemek istiyorsanız, diğer tüm hücreleri kilidini açmanız gerekir. Bir çalışma sayfasındaki tüm hücreler zaten kilitlenmek üzere ayarlanmıştır; bunu, herhangi bir Excel dosyasını MS Excel'de açıp **Biçim | Hücreler...** sekmesine tıklayarak ve **Koruma** sekmesine geçip "Kilitlemiş" onay kutusunun varsayılan olarak işaretli olduğunu görerek kontrol edebilirsiniz.

Microsoft Excel'de birkaç hücreyi kilitlemenin nasıl yapılacağını anlatan noktalar aşağıdadır. Bu yöntem, Microsoft Office Excel 97, 2000, 2002, 2003 ve sonraki sürümler için geçerlidir.

1. Satır numarası için doğrudan üzerindeki gri dikdörtgen (satır 1'in hemen üstündeki ve A sütun harfinin solundaki). **Tümünü Seç** düğmesine tıklayarak tüm çalışma sayfasını seçin.
2. **Biçim** menüsünde **Hücreler** seçeneğine tıklayın, **Koruma** sekmesine geçin ve ardından **Kilitlemiş** onay kutusunu temizleyin.
   Bu işlem, çalışma sayfasındaki tüm hücrelerin kilidini kaldırır.
   **Hücreler** komutu kullanılamıyorsa, çalışma sayfasının bazı bölümleri zaten kilitli olabilir. **Araçlar** menüsünde **Koruma**'ya gelin ve ardından **Sayfayı Korumayı Kaldır**'a tıklayın.
3. Sadece kilitlemek istediğiniz hücreleri seçin ve 2. adımı tekrarlayın, ancak bu sefer **Kilidi Açık** kutusunu seçin.
4. **Araçlar** menüsünden, **Koruma** üzerine gelin, **Sayfayı Koru** seçeneğine tıklayın ve ardından **Tamam** a tıklayın.
5. **Sayfayı Koru** iletişim kutusunda, bir şifre belirleme ve kullanıcıların değiştirmesini istediğiniz öğeleri seçme seçeneğiniz var.

### **Aspose.Cells Kullanarak Çalışma Sayfasında Birkaç Hücreyi Koru**

Bu yöntemde, yalnızca Aspose.Cells API'sini kullanarak bu işlemi gerçekleştiririz.

Örnek: Aşağıdaki örnek, çalışma sayfasında birkaç hücreyi nasıl koruyacağınızı gösterir. İlk olarak çalışma sayfasındaki tüm hücreleri açar ve ardından 3 hücreyi (A1, B1, C1) kilitler. Son olarak, çalışma sayfasını korur. [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesi, bir boolean özellik, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) içerir. [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) özelliğini true veya false yapabilir ve *Column/Row.applyStyle()* metodunu kullanarak satır/sütun kilit veya kilit açabilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unlock Columns and Protect Specific Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            await readyPromise;

            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object
            const styleflag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                styleflag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, styleflag);
            }

            // Lock the three cells...i.e. A1, B1, C1.
            style = sheet.cells.get("A1").style;
            style.isLocked = true;
            sheet.cells.get("A1").style = style;

            style = sheet.cells.get("B1").style;
            style.isLocked = true;
            sheet.cells.get("B1").style = style;

            style = sheet.cells.get("C1").style;
            style.isLocked = true;
            sheet.cells.get("C1").style = style;

            // Finally, Protect the sheet now.
            sheet.protect(ProtectionType.All);

            // Save the excel file and provide download link
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Çalışma Sayfasında Bir Satırı Koruma**

Aspose.Cells, çalışma sayfasındaki herhangi bir satırı kolayca kilitlemenize olanak tanır. Burada, [**Aspose.Cells.Row**](https://reference.aspose.com/cells/javascript-cpp/row) sınıfının [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) metodunu kullanarak belirli bir satıra [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) uygulayabiliriz. Bu metod iki argüman alır: bir [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesi ve tüm üyeleri ilgili biçimlendirmeyle olan [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) nesnesi.

Aşağıdaki örnek, bir çalışma sayfasında satırı nasıl koruyacağınızı gösterir. İlk olarak çalışma sayfasındaki tüm hücreleri açar ve ardından ilk satırı kilitler. Son olarak, çalışma sayfasını korur. [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesi, bir boolean özellik, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) içerir. [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) özelliğini true veya false yaparak satır/sütunu [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) nesnesi kullanarak kilitleyebilir veya kilit açılsını açabilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType, Utils } = AsposeCells;

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
            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first row style.
            style = sheet.cells.rows.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Set the lock setting.
            flag.locked = true;

            // Apply the style to the first row.
            sheet.cells.applyRowStyle(0, style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and protected. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Çalışma Sayfasında Bir Sütunu Koruma**

Aspose.Cells, herhangi bir sütunu kolayca kilitlemenize izin verir. Burada, [**Aspose.Cells.Column**](https://reference.aspose.com/cells/javascript-cpp/column) sınıfının [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/column/#applyStyle-style-styleflag-) metodunu kullanarak belirli bir sütuna [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) uygulayabiliriz. Bu metod iki argüman alır: bir [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesi ve tüm üyeleri ilgili biçimlendirmeyle olan [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) nesnesi.

Aşağıdaki örnek, bir çalışma sayfasında sütunu nasıl koruyacağınızı gösterir. İlk olarak çalışma sayfasındaki tüm hücreleri açar ve ardından ilk sütunu kilitler. Son olarak, çalışma sayfasını korur. [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesi, bir boolean özellik, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) içerir. [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) özelliğini true veya false yaparak satır/sütunu [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) nesnesi kullanarak kilitleyebilir veya kilit açabilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Unlock Columns and Protect Sheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            if (!fileInput.files.length) {
                // If no file provided, a new workbook will be created
                document.getElementById('result').innerHTML = '<p style="color: orange;">No file selected. A new workbook will be created and processed.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Processing selected file...</p>';
            }

            await readyPromise;

            // Load workbook from file if provided, otherwise create new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a worksheet object and obtain the first sheet.
            const sheet = workbook.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first column style.
            style = sheet.cells.columns.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Apply the style to the first column.
            sheet.cells.columns.get(0).applyStyle(style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Kullanıcılara Düzenleme Aralığı Izin Ver**

Aşağıdaki örnek, korunan bir çalışma sayfasında kullanıcılara bir aralığı düzenleme izni vermenin nasıl yapıldığını göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Protect Range</title>
    </head>
    <body>
        <h1>Protect Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Instantiate a new or loaded Workbook
            let book;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                book = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                book = new Workbook();
            }

            // Get the first (default) worksheet
            const sheet = book.worksheets.get(0);

            // Get the Allow Edit Ranges
            const allowRanges = sheet.allowEditRanges;

            // Define ProtectedRange
            let protected_range;

            // Create the range
            const idx = allowRanges.add("r2", 1, 1, 3, 3);
            protected_range = allowRanges.get(idx);

            // Specify the password
            protected_range.password = "123";

            // Protect the sheet
            sheet.protect(ProtectionType.All);

            // Save the Excel file
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'protectedrange.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Range Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Protected range added and sheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
