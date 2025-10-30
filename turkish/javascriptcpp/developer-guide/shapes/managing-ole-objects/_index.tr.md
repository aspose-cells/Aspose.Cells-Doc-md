---
title: C++ ile JavaScript ile OLE Nesnelerini Yönetme
linktitle: OLE Nesneleri Yönetme
type: docs
weight: 50
url: /tr/javascript-cpp/managing-ole-objects/
description: C++ ile Aspose.Cells for JavaScript kullanarak OLE nesnelerini yönetmeyi öğrenin. Çalışma sayfaları içinde OLE nesneleri ekleyin, çıkarın ve manipüle edin.
---

## **Giriş**  

OLE (Nesne Bağlama ve Gömme), karmaşık belge teknolojileri için bir çerçevedir. Kısaca, karmaşık bir belge, görsel ve bilgi nesnelerini içerebilen bir masaüstü görünümüne sahip şeydir: metinler, takvimler, animasyonlar, ses, hareketli video, 3D, sürekli güncellenen haberler, kontroller ve diğerleri. Her masaüstü nesnesi, kullanıcıyla etkileşim kurabilen ve ayrıca masaüstündeki diğer nesnelerle iletişim kurabilen bağımsız bir program birimidir.  

OLE birçok farklı program tarafından desteklenir ve bir programda oluşturulan içeriğin başka bir programda kullanılabilir hale getirilmesi amacıyla kullanılır. Örneğin, bir Microsoft Word belgesini Microsoft Excel'e ekleyebilirsiniz. Hangi içerik türlerinin ekleneceğine bakmak için, **Ekle** menüsünden **Nesne**'ye tıklayın. Yüklenmiş ve OLE nesnelerini destekleyen programlar **Nesne Türü** kutusunda görünür.  

### **Çalışsayan Elemanları Çalışsayan Eleman (OLE) Nesnesi Ekleme**  

Aspose.Cells for JavaScript C++ kullanarak çalışma sayfalarına OLE nesneleri ekleme, çıkarma ve manipüle etmeyi destekler. Bu nedenle, Aspose.Cells'in koleksiyona yeni bir OLE Nesnesi ekmek için kullanılan [**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection) sınıfı ve bir OLE Nesnesini temsil eden [**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject) adlı başka bir sınıfı vardır. Bazı önemli üyeleri şunlardır:  

- [**imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--) özelliği, bayt dizisi biçiminde olan resim (simge) verisini belirtir. Bu görüntü, çalışma sayfasında OLE Nesnesini göstermek için gösterilecektir.  
- [**objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--) özelliği, nesne verisini bayt dizisi biçiminde belirtir. Bu veriyi çift tıklayarak ilgili programda gösterilir.  

Aşağıdaki örnek, çalışsayan elemanları çalışsayan eleman(lar)ı çalışsayan eleman yapıştırma.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add OLE Object Example</title>
    </head>
    <body>
        <h1>Add OLE Object Example</h1>
        <p>
            Select an image to display for the OLE object (e.g., logo.jpg) and a file to embed into the OLE object (e.g., book1.xls).
        </p>
        <label>Image (for OLE display): <input type="file" id="imageInput" accept="image/*" /></label>
        <br/>
        <label>Object to embed (e.g., .xls): <input type="file" id="objectInput" accept=".xls,.xlsx,.doc,.docx,.pdf" /></label>
        <br/>
        <button id="runExample">Add OLE Object and Save</button>
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
            const imageInput = document.getElementById('imageInput');
            const objectInput = document.getElementById('objectInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file for the OLE display.</p>';
                return;
            }
            if (!objectInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a file to embed into the OLE object.</p>';
                return;
            }

            // Read files
            const imageFile = imageInput.files[0];
            const objectFile = objectInput.files[0];

            const imageBuffer = await imageFile.arrayBuffer();
            const objectBuffer = await objectFile.arrayBuffer();

            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Add an Ole object into the worksheet with the image shown in MS Excel.
            // Position: row 14, column 3, width 200, height 220 (same as JavaScript example)
            sheet.oleObjects.add(14, 3, 200, 220, new Uint8Array(imageBuffer));

            // Set embedded ole object data (converted setter to property assignment)
            sheet.oleObjects.get(0).objectData = new Uint8Array(objectBuffer);

            // Save the excel file (Excel97To2003 format to match .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">OLE object added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Çalışsayan Elemanlar'ın Çalışsayan Elemanları Çıkarma**  

Aşağıdaki örnek, bir çalışma kitabından çalışsayan elemanları çıkarmayı göstermektedir. Örnek, mevcut bir XLS dosyasından farklı çalışsayan elemanlar alır ve farklı dosyalar (DOC, XLS, PPT, PDF vb.) çalışsayan elemanın dosya biçim türüne dayalı olarak kaydeder.  

Kodu çalıştırdıktan sonra, ilgili Çalışsayan Elemanın biçim türlerine dayalı olarak farklı dosyaları kaydedebiliriz.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Extract OLE Objects</title>
    </head>
    <body>
        <h1>Extract OLE Objects from Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb" />
        <button id="runExample">Extract OLE Objects</button>
        <div id="downloadContainer"></div>
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
            const downloadContainer = document.getElementById('downloadContainer');
            const result = document.getElementById('result');
            downloadContainer.innerHTML = '';
            result.innerHTML = '';

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the OleObject Collection in the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const oles = worksheet.oleObjects;

            // Loop through all the oleobjects and extract each object.
            for (let i = 0; i < oles.count; i++) {
                const ole = oles.get(i);

                // Specify the output filename.
                let ext = 'jpg';

                // Specify each file format based on the oleobject format type.
                switch (ole.fileFormatType) {
                    case AsposeCells.FileFormatType.Doc:
                        ext = "doc";
                        break;
                    case AsposeCells.FileFormatType.Xlsx:
                        ext = "xlsx";
                        break;
                    case AsposeCells.FileFormatType.Ppt:
                        ext = "ppt";
                        break;
                    case AsposeCells.FileFormatType.Pdf:
                        ext = "pdf";
                        break;
                    case AsposeCells.FileFormatType.Unknown:
                        ext = "jpg";
                        break;
                    default:
                        ext = "bin";
                        break;
                }

                const fileName = `ole_${i}.${ext}`;

                // Save the oleobject as a new excel file if the object type is xlsx.
                if (ole.fileFormatType === AsposeCells.FileFormatType.Xlsx) {
                    const ms = new Uint8Array(ole.objectData);
                    const oleBook = new Workbook(ms);
                    oleBook.settings.isHidden = false;
                    const outputData = oleBook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData]);
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);
                    link.download = `Excel_File${i}.out.xlsx`;
                    link.textContent = `Download Excel_File${i}.out.xlsx`;
                    link.style.display = 'block';
                    downloadContainer.appendChild(link);
                } else {
                    // Create the files based on the oleobject format types.
                    const data = ole.objectData;
                    const blob = new Blob([data]);
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);
                    link.download = fileName;
                    link.textContent = `Download ${fileName}`;
                    link.style.display = 'block';
                    downloadContainer.appendChild(link);
                }
            }

            result.innerHTML = '<p style="color: green;">OLE object extraction completed. Use the links above to download the files.</p>';
        });
    </script>
</html>
```  

### **Gömülü MOL Dosyasının Çıkarılması**  

Aspose.Cells for JavaScript C++ kullanarak mol (Atomlar ve bağlar hakkında bilgi içeren moleküler veri dosyası) gibi nadir türde nesneleri çıkarma desteği sağlar. Aşağıdaki kod örneği, gömülü bir MOL dosyasını çıkarıp diskete kaydetmek için bu [örnek excel dosyasını](94896196.xlsx) kullanmaktadır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Extract OLE Objects Example</title>
    </head>
    <body>
        <h1>Extract OLE Objects Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            let index = 1;

            const worksheets = workbook.worksheets;
            const sheetCount = worksheets.count;
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            for (let i = 0; i < sheetCount; i++) {
                const sheet = worksheets.get(i);
                const oles = sheet.oleObjects;
                const oleCount = oles.count;
                for (let j = 0; j < oleCount; j++) {
                    const ole = oles.get(j);
                    const data = ole.objectData;
                    const blob = new Blob([data], { type: 'application/octet-stream' });
                    const url = URL.createObjectURL(blob);
                    const fileName = `OleObject${index}.mol`;
                    const link = document.createElement('a');
                    link.href = url;
                    link.download = fileName;
                    link.textContent = `Download ${fileName}`;
                    link.style.display = 'block';
                    resultDiv.appendChild(link);
                    index++;
                }
            }

            if (!resultDiv.hasChildNodes()) {
                resultDiv.innerHTML = '<p>No OLE objects found in the workbook.</p>';
            } else {
                const info = document.createElement('p');
                info.style.color = 'green';
                info.textContent = 'OLE objects extracted. Click the links to download the extracted .mol files.';
                resultDiv.insertBefore(info, resultDiv.firstChild);
            }
        });
    </script>
</html>
```  

## **Gelişmiş Konular**  
- [Bağlı Ole Nesnesinin Görüntü Etiketini Erişme ve Değiştirme](/cells/tr/javascript-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [Microsoft Excel kullanarak Aspose.Cells ile Çalışmayan Elemanı Otomatik Yenileme](/cells/tr/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [Çalışma Kitabından Çalışmayan Elemanları Çıkarma](/cells/tr/javascript-cpp/extract-ole-objects-from-workbook/)  
- [Gömülü Çalışmayan Elemanın Sınıf Tanımlayıcısını Al veya Ayarla](/cells/tr/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Ole Nesnesi Olarak Bir WAV Dosyası Eklemek](/cells/tr/javascript-cpp/inserting-a-wav-file-as-an-ole-object/)
