---
title: JavaScript ile C++ aracılığıyla Belge Özelliklerini Yönetin
linktitle: Belge Portalları
type: docs
weight: 80
url: /tr/javascript-cpp/managing-document-properties/
description: C++ aracılığıyla Aspose.Cells for JavaScript API lerini kullanarak Belge Özelliklerini nasıl yöneteceğinizi öğrenin.
keywords: JavaScript ile C++ kullanarak Belge Özelliklerini nasıl Yöneteceğinizi, Belge Özelliklerini almak veya ayarlamak, Belge Özellikleri eklemek veya silmek via JavaScript kullanmak, Mesajlar veya JavaScript ile Belge Özelliklerini eklemek veya kaldırmak, Belge Özelliklerine erişmek için Aspose.Cells for JavaScript API lerini nasıl kullanacağınızı.
---

## **Giriş**

Microsoft Excel, elektronik tablo dosyalarına özellik eklemek için yetenek sunmaktadır. Bu belge özellikleri kullanışlı bilgiler sağlar ve ayrıntıları aşağıdaki gibi 2 kategoriye ayrılmıştır.

- Sistem tanımlı (hazır) özellikler: Hazır özellikler belge başlığı, yazar adı, belge istatistikleri gibi belge hakkında genel bilgiler içerir.
- Kullanıcı tanımlı (özel) özellikler: Kullanıcı tanımlı özellikler son kullanıcı tarafından ad-değer çifti şeklinde tanımlanan özelleştirilmiş özelliklerdir.

{{% alert color="primary" %}}

Hazır ve özel özellikler hakkında bilinmesi gereken en önemli nokta hazır özelliklerin erişilebilir ve değiştirilebilir olduğudur, ancak oluşturulamaz veya kaldırılamaz. Öte yandan, özel özellikler oluşturulabilir ve yönetilebilir.

{{% /alert %}}

## **Microsoft Excel ile Belge Portalları Nasıl Yönetilir**

Microsoft Excel, Excel dosyalarının belge özelliklerini WYSIWYG tarzında yönetmenize olanak tanır. Lütfen Excel 2016'da **Özellikler** diyaloğunu açmak için aşağıdaki adımları izleyiniz.

1. **Dosya** menüsünden **Bilgi**'yi seçin.

|**Bilgi Menüsünü Seçme**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. **Özellikler** başlığına tıklayıp "Gelişmiş Özellikler”'i seçin.

|**Gelişmiş Özellikler Seçimini Tıklama**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Dosyanın belge özelliklerini yönetin.

|**Özellikler İletişim Kutusu**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
Özellikler iletişim kutusunda Genel, Özet, İstatistikler, İçerik ve Gümrük gibi farklı sekmeler bulunur. Her sekme, dosya ile ilgili farklı türde bilgileri yapılandırmaya yardımcı olur. Gümrük sekmesi, özel özellikleri yönetmek için kullanılır.

## **Aspose.Cells Kullanarak Belge Portalları İle Nasıl Çalışılır**

Geliştiriciler, Aspose.Cells ara yüz yöntemleri kullanarak belge portal değişkenlerini dinamik olarak yönetebilirler. Bu özellik, geliştiricilere dosya ile birlikte alınan bilgiyi depolama olanağı sağlar, örneğin dosyanın ne zaman alındığı, işlendiği, zaman damgalandığı v.b.

{{% alert color="primary" %}}

C++ ile Aspose.Cells for JavaScript doğrudan API ve Sürüm Numarası bilgilerini çıktı belgelerine yazar. Örneğin, belgeyi PDF'ye dönüştürürken, Aspose.Cells for JavaScript API'yi kullanarak **Uygulama** alanını 'Aspose.Cells' ve **PDF Üretici** alanını 'Aspose.Cells v17.9' değeriyle doldurur.

Lütfen, bu bilgiyi çıktı Belgelerinden değiştirmek veya silmek için Aspose.Cells for JavaScript'i kullanamayacağınızı unutmayın.

{{% /alert %}}

### **Belge Portallarına Erişim Yöntemleri**

Aspose.Cells API'leri, hem yerleşik hem de özel belge özelliklerini destekler. Aspose.Cells'in [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, bir Excel dosyasını temsil eder ve tıpkı bir Excel dosyası gibi, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı birçok çalışma sayfası içerebilir ve her biri [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfıyla temsil edilir; çalışma sayfaları koleksiyonu ise [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) sınıfı tarafından temsil edilir.

Dosyanın belge özelliklerine aşağıda anlatıldığı gibi erişmek için [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) kullanın.

- Hazır belge özelliklerine ulaşmak için [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--) kullanın.
- Özel belge özelliklerine ulaşmak için [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--) kullanın.

Hem [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--) hem de [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--), [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/) örneğinde gösterildiği gibi [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/) örneğinin örneğini döndürür. Bu koleksiyon, her biri tek bir yerleşik veya özel belge özelliğini temsil eden [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) nesnesinden oluşur.

Bir özelliğe erişmek uygulama gereksinimlerine bağlıdır; yani, örneğin [**DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/) ile gösterildiği gibi, özelliğin indeks veya adını kullanabilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Document Properties</title>
    </head>
    <body>
        <h1>Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Load Document Properties</button>
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object and opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Accessing a custom document property by using the property name
            const customProperty1 = customProperties.get("ContentTypeId");
            // Accessing the same custom document property by using the property index
            const customProperty2 = customProperties.get(0);

            const outputs = [];
            if (customProperty1) {
                outputs.push(`<p>${customProperty1.name} ${customProperty1.value}</p>`);
            }
            if (customProperty2) {
                outputs.push(`<p>${customProperty2.name} ${customProperty2.value}</p>`);
            }
            if (!outputs.length) {
                resultEl.innerHTML = '<p style="color: orange;">No custom document properties found.</p>';
            } else {
                resultEl.innerHTML = outputs.join('');
            }
        });
    </script>
</html>
```

[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) sınıfı, belge özelliğinin adını, değerini ve türünü almak için izin verir:

- Özellik adını almak için [**DocumentProperty.name()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#name--) kullanın.
- Özellik değerini almak için [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--). [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--) değeri bir Nesne olarak döndürür.
- Özellik türünü almak için [**DocumentProperty.type()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#type--). Bu, [**PropertyType**](https://reference.aspose.com/cells/javascript-cpp/propertytype/) sıralama değeri içinden birini döndürür. Özellik türünü aldıktan sonra, uygun değeri almak için **DocumentProperty.ToXXX** metodlarından birini kullanın; [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--) kullanmak yerine. **DocumentProperty.ToXXX** metodları aşağıdaki tabloda açıklanmıştır.

{{% alert color="primary" %}}

[**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) sınıfı ayrıca diğer veri tiplerinin değerlerini döndüren metodlar da sağlar.

{{% /alert %}}

|**Üye Adı**|**Açıklama**|**ToXXX Yöntemi**|
| :- | :- | :- |
|Boolean| Özellik veri türü Boolean'dır|ToBool|
|Date| Özellik veri türü DateTime'dir. Microsoft Excel'in bu tür özel bir özelliğinde sadece tarih kısmının saklandığına dikkat edin, zaman saklanamaz|ToDateTime|
|Float| Özellik veri türü Double'dır|ToDouble|
|Number| Özellik veri türü Int32'dir|ToInt|
|String|Özellik veri tipi string|ToString|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Retrieve Custom Document Properties Example</h1>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            let outputHtml = '<h2>Custom Document Properties</h2>';

            // Accessing a custom document property (first)
            const customProperty1 = customProperties.get(0);
            if (customProperty1) {
                // Storing the value of the document property as an object
                const objectValue = customProperty1.value;
                outputHtml += `<p><strong>${customProperty1.name}</strong> (type: ${customProperty1.type}) : ${objectValue}</p>`;
            } else {
                outputHtml += '<p>No first custom property found.</p>';
            }

            // Accessing a custom document property (second)
            const customProperty2 = customProperties.get(1);
            if (customProperty2) {
                // Checking the type of the document property and then storing the value according to that type
                if (customProperty2.type === AsposeCells.PropertyType.String) {
                    const value = customProperty2.value.toString();
                    outputHtml += `<p>${customProperty2.name} : ${value}</p>`;
                } else {
                    outputHtml += `<p>${customProperty2.name} (type: ${customProperty2.type}) : ${customProperty2.value}</p>`;
                }
            } else {
                outputHtml += '<p>No second custom property found.</p>';
            }

            resultDiv.innerHTML = outputHtml;
        });
    </script>
</html>
```

### **Özel Belge Özellikleri Nasıl Eklenir veya Kaldırılır**

Bu konunun başında daha önce açıkladığımız gibi, geliştiriciler yerleşik özellikler ekleyemez veya kaldıramaz çünkü bu özellikler sistem tanımlıdır, ancak kullanıcı tanımlı olduğu için özel özellikler eklemek veya kaldırmak mümkündür.

### **Özel Özellikler Nasıl Eklenir**

Aspose.Cells API'leri, koleksiyonlara özel özellikler eklemek için [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-) metodunu [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/) sınıfı ile açığa çıkarmıştır. [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-) metodu, özelliği Excel dosyasına ekler ve yeni belge özelliğine referans olarak bir [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) nesnesi döner.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Custom Document Property</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object and opening the Excel file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Retrieve a list of all custom document properties of the Excel file
                const customProperties = workbook.customDocumentProperties;

                // Adding a custom document property to the Excel file
                customProperties.add("Publisher", "Aspose");

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'out_sample-document-properties.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Custom property added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```

### **“İçeriğe bağlantı” Özel Özelliğin Yapılandırılması Nasıl Yapılır**

Belirli bir alanın içeriğiyle bağlantılı özel bir özellik oluşturmak için [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) metodunu çağırın ve özellik adını ve kaynağını iletin. Bir özelliğin içeriğe bağlı olarak yapılandırılıp yapılandırılmadığını [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#isLinkedToContent--) özelliği ile kontrol edebilirsiniz. Ayrıca, [**source()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#source--) özelliği kullanılarak kaynak alan alınabilir ve [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) sınıfının.

Örneğin basit bir şablon Microsoft Excel dosyası kullanıyoruz. Çalışma kitabında, **MyRange** olarak etiketlenmiş tanımlanan bir adlandırılmış aralık, bir hücre değerine atıfta bulunur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Custom Document Properties</h1>
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
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.worksheets.customDocumentProperties;

            // Add link to content.
            customProperties.addLinkToContent("Owner", "MyRange");

            // Accessing the custom document property by using the property name
            const customProperty1 = customProperties.get("Owner");

            // Check whether the property is linked to content
            const isLinkedToContent = customProperty1.isLinkedToContent;

            // Get the source for the property
            const source = customProperty1.source;

            // Save the file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = `<p style="color: green;">Operation completed successfully! Property linked: ${isLinkedToContent}. Source: ${source}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

### **Özel Özellikler Nasıl Kaldırılır**

Aspose.Cells kullanarak özel özellikleri kaldırmak için, [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/#remove-string-) metodunu çağırın ve kaldırılacak belge özelliği adını iletin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Remove Custom Document Property Example</title>
    </head>
    <body>
        <h1>Remove Custom Document Property Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Removing a custom document property named "Publisher"
            customProperties.remove("Publisher");

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom property removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Belge Bilgi Paneli içinde görülebilen Özel Özellikler eklemek](/cells/tr/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Yerleşik Belge Özellikleri için ScaleCrop ve LinksUpToDate özelliklerini ayarlama](/cells/tr/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Aspose.Cells kullanarak Excel Dosyasının Belge Sürümünü Belirtme](/cells/tr/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Dahili Belge Özelliklerini Kullanarak Excel Dosyasının Dilini Belirtme](/cells/tr/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
