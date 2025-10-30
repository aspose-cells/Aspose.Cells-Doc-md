---
title: JavaScript ile C++ kullanarak Çalışma Sayfası ve Sekmeleri Göster ve Gizle
linktitle: Sayfaları ve Tabları Gösterme ve Gizleme
type: docs
weight: 10
url: /tr/javascript-cpp/show-and-hide-worksheets-and-tabs/
description: Bu makale, JavaScript API veya JavaScript Kütüphanesi kullanarak Excel çalışma sayfasını programatik olarak gösterme ve gizleme ile ilgili örnek kodlar sağlar. Ayrıca, Excel çalışma kitabı sekmelerini gösterme ve gizleme nasıl yapılır açıklanmıştır.
---

{{% alert color="primary" %}}
Aspose.Cells kullanıcının çalışma sayfalarını ve sekmelerini gösterebilmesine ve gizleyebilmesine olanak tanır.
{{% /alert %}}

## **Bir Çalışma Sayfasını Gösterme ve Gizleme**

Bir Excel dosyasında bir veya birden fazla çalışma sayfası olabilir. Excel dosyası oluşturduğumuzda, içinde çalıştığımız Excel dosyasına çalışma sayfaları ekleriz. Bir Excel dosyasındaki her çalışma sayfası kendi veri ve biçimlendirme ayarları gibi diğer çalışma sayfalarından bağımsızdır. Bazı durumlarda, geliştiriciler kendi ilgileri için Excel dosyalarındaki birkaç çalışma sayfasını gizlemek ve diğerlerini göstermek isteyebilirler. **Aspose.Cells** bu nedenle geliştiricilere Excel dosyalarında çalışma sayfalarının görünürlüğünü kontrol etme imkanı sunar.

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş özellikler ve yöntemler sunar. Bir çalışma sayfasının görünürlüğünü kontrol etmek için, [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) özelliğini [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfının kullanın. [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) bir Boolean özelliğidir, bu da yalnızca **doğru** veya **yanlış** değerleri depolayabilir.

### **Bir Çalışma Sayfasını Görünür Yapma**

Bir çalışma sayfasını görünür yapmak için [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfının [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) özelliğini **true** olarak ayarlayın.

### **Bir Çalışsayıyı Gizleme**

Bir çalışma sayfasını gizlemek için [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfının [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) özelliğini **false** olarak ayarlayın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hide Worksheet Example</title>
    </head>
    <body>
        <h1>Hide Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the first worksheet of the Excel file
            worksheet.isVisible = false;

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Tabları Gösterme ve Gizleme**

Microsoft Excel dosyasının alt kısmına dikkatlice baktığınızda, bir dizi kontrolü göreceksiniz. Bunlar şunları içerir:

- Sayfa sekmeleri.
- Sekme kaydırma düğmeleri.

Sayfa sekmeleri, Excel dosyasındaki çalışma sayfalarını temsil eder. Herhangi bir sekmeye tıklayarak o çalışma sayfasına geçebilirsiniz. Çalışma kitabında daha fazla çalışma sayfası olduğunda, daha fazla sayfa sekmesi olacaktır. İyi bir sayıda çalışma sayfasının olduğu Excel dosyasında bunları dolaşmak için düğmeler kullanmanız gerekebilir. Bu nedenle, Microsoft Excel, sayfa sekmeleri ve sekmeler arasında kaydırmak için düğmeler sağlar.

Aspose.Cells kullanarak geliştiriciler Excel dosyalarında sayfa sekmelerinin ve sekmelerin kaydırma düğmelerinin görünürlüğünü kontrol edebilirler.

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, bir Excel dosyasını yönetmek için geniş bir özellik ve yöntem yelpazesi sunar. Bir Excel dosyasındaki sekmelerin görünürlüğünü kontrol etmek için geliştiriciler [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) özelliğini kullanabilirler. [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) Boolean bir özelliktir, bu da sadece **true** veya **false** değeri depolayabileceği anlamına gelir.

### **Sekmeleri Görünür Yapma**

Sekmeleri görünür yapmak için [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) özelliğini **true** yapın.

### **Sekmeleri Gizleme**

Bir Excel dosyasında sekmeleri gizlemek için [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) özelliğini **false** yapın.

Aşağıda, bir Excel dosyasını (book1.xls) açan, sekmelerini gizleyen ve değiştirilmiş dosyayı output.xls olarak kaydeden tam bir örnek bulunmaktadır. Kodun çalıştırılmasından sonra çalışma kitabının sekmelerinin gizlendiğini göreceksiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Worksheet Tabs Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the tabs of the Excel file
            workbook.settings.showTabs = false;

            // To show the tabs instead, you could set:
            // workbook.settings.showTabs = true;

            // Saving the modified Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Tabs hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Sekme Çubuğu Genişliğini Kontrol Etme**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Tabs</title>
    </head>
    <body>
        <h1>Hide Tabs Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the tabs of the Excel file (converted setter to property)
            workbook.settings.showTabs = true;

            // Adjusting the sheet tab bar width (converted setter to property)
            workbook.settings.sheetTabBarWidth = 800;

            // Saving the modified Excel file (SaveFormat.Xls -> SaveFormat.Excel97To2003)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
