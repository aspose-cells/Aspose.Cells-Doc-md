---
title: JavaScript ile C++ kullanarak Excel dosyalarına Resim ve Şekil Ekleme  
linktitle: Şekiller  
type: docs  
weight: 140  
url: /tr/javascript-cpp/insert-shapes/  
description: C++ kullanarak Excel dosyalarında resimler, OLE nesneleri ve şekilleri yönetin.  
---  

{{% alert color="primary" %}}  
Bazen çalışma sayfasına gerekli şekillerden bazılarını eklemeniz gerekir. Aynı şekli farklı konumlara eklemeniz gerekebilir. Veya çalışma sayfasına toplu halde şekil eklemek isteyebilirsiniz.  
Endişelenmeyin! [Aspose.Cells](https://products.aspose.com/cells/), tüm bu operasyonları destekler.  
{{% /alert %}}  

Excel'deki şekiller esasen aşağıdaki türlere ayrılır:  
- **Resimler**  
- **OleObjects**  
- **Çizgiler**  
- **Dikdörtgenler**  
- **Temel Şekiller**  
- **Blok Okları**  
- **Denklem Şekilleri**  
- **Akış Şemaları**  
- **Yıldızlar ve Pankartlar**  
- **Çağrılar**  

Bu kılavuz belgesi, her türden bir veya iki şekli örnek olarak seçecek. Bu örnekler aracılığıyla, [Aspose.Cells](https://products.aspose.com/cells/) kullanarak belirli şekli çalışma sayfasına nasıl ekleyeceğinizi öğreneceksiniz.  

## **JavaScript kullanarak Excel Çalışma Sayfasına Resim Ekleme**  

Bir elektron mikroskobuna resim eklemek çok kolaydır. Sadece birkaç satır kod gerektirir:  
Sadece [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-) metodunu çağırın ve [**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection) koleksiyonunu kullanarak (bunun içinde [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) nesnesi). [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-) metodu aşağıdaki parametreleri alır:  

- **Sol üst satır dizini**, sol üst sütunun dizini.  
- **Sol üst sütun dizini**, sol üst sütunun dizini.  
- **Resim dosya adı**, yol bilgisi ile birlikte resim dosyasının adı.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Picture to Workbook Example</h1>
        <p>
            Optional: select an existing Excel file to modify, or leave empty to create a new workbook.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>
            Select an image to insert into the worksheet (required):
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // If an Excel file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const arrayBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Add a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read the selected image file as Uint8Array
            const imageFile = imageInput.files[0];
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(imageArrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            worksheet.pictures.add(5, 5, imageBytes);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **JavaScript kullanarak Excel Çalışma Sayfasına OLE Nesnesi Ekleme**  

Aspose.Cells, çalışma sayfalarında OLE nesneleri ekleme, çıkarma ve düzenleme desteği sağlar. Bu nedenle, Aspose.Cells, koleksiyon listesine yeni bir OLE Nesnesi ekmek için kullanılan [**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection) sınıfına sahiptir. Diğer bir sınıf olan [**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject), bir OLE Nesnesini temsil eder. Bazı önemli üyeleri şunlardır:  

- [**OleObject.imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--) özelliği, bayt dizisi biçiminde olan resim (simge) verisini belirtir. Bu görüntü, çalışma sayfasında OLE Nesnesini göstermek için gösterilecektir.  
- [**OleObject.objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--) özelliği, nesne verisini bayt dizisi biçiminde belirtir. Bu veriyi çift tıklayarak ilgili programda gösterilir.  

Aşağıdaki örnek, çalışsayan elemanları çalışsayan eleman(lar)ı çalışsayan eleman yapıştırma.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Insert OLE Object Example</h1>
        <p>
            Select an image to display as the OLE object's icon and an Excel file to embed as the OLE object.
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <input type="file" id="excelInput" accept=".xls,.xlsx" />
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
            const imageInput = document.getElementById('imageInput');
            const excelInput = document.getElementById('excelInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file for the OLE icon.</p>';
                return;
            }
            if (!excelInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file to embed.</p>';
                return;
            }

            const imageFile = imageInput.files[0];
            const excelFile = excelInput.files[0];

            // Read files as ArrayBuffers
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const excelArrayBuffer = await excelFile.arrayBuffer();

            // Convert to Uint8Array for Aspose.Cells
            const imageData = new Uint8Array(imageArrayBuffer);
            const objectData = new Uint8Array(excelArrayBuffer);

            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Add an Ole object into the worksheet with the image shown in MS Excel.
            sheet.oleObjects.add(14, 3, 200, 220, imageData);

            // Set embedded ole object data.
            sheet.oleObjects.get(0).objectData = objectData;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">OLE object embedded successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **JavaScript kullanarak Excel Çalışma Sayfasına Çizgi Ekleme**  

Çizgi şekli, **çizgiler** kategorisine aittir.  

*  

- Satırı eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Daha sonra, 'Son Kullanılan Şekiller' veya 'Çizgiler' arasından çizgiyi seçin  

![](line.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına bir satır eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Yöntem bir [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape) nesnesi döndürür.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına nasıl çizgi ekleyeceğinizi gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Line Example</h1>
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
            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Create workbook from uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Access first worksheet from the collection
                const sheet = workbook.worksheets.get(0);

                // Add the line to the worksheet
                sheet.shapes.addLine(2, 0, 2, 0, 100, 300);

                // Save workbook to XLSX format and create download link
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'sample.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Line added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](line2.png)  

## **JavaScript kullanarak Excel Çalışma Sayfasına çizgi ok ekleme**  

Çizgi okuğu şekli, **Çizgiler** kategorisine aittir. Bu, çizginin özel bir durumudur.  

*  

- Ok satırını eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Daha sonra, 'Son Kullanılan Şekiller' veya 'Çizgiler' arasından çizgi okuğu seçin  

![](line_arrow1.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına bir ok satırı eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Yöntem bir [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape) nesnesi döndürür.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına nasıl çizgi okuğu ekleyeceğinizi gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Line Arrow Example</h1>
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

            // Loads the workbook which contains shapes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the line arrow to the worksheet
            let s = sheet.shapes.addLine(2, 0, 2, 0, 100, 300); // method 1
            // let s = sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
            // let s = sheet.shapes.addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

            // add a arrow at the line begin
            s.line.beginArrowheadStyle = AsposeCells.MsoArrowheadStyle.Arrow; // arrow type
            s.line.beginArrowheadWidth = AsposeCells.MsoArrowheadWidth.Wide; // arrow width
            s.line.beginArrowheadLength = AsposeCells.MsoArrowheadLength.Short; // arrow length

            // add a arrow at the line end
            s.line.endArrowheadStyle = AsposeCells.MsoArrowheadStyle.ArrowOpen; // arrow type
            s.line.endArrowheadWidth = AsposeCells.MsoArrowheadWidth.Narrow; // arrow width
            s.line.endArrowheadLength = AsposeCells.MsoArrowheadLength.Long; // arrow length

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.with_arrow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Arrow';

            document.getElementById('result').innerHTML = '<p style="color: green;">Arrow added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](line_arrow2.png)  

## **JavaScript kullanarak Excel Çalışma Sayfasına Dikdörtgen Ekleme**  

Dikdörtgen şekli, **Dikdörtgenler** kategorisine aittir.  

*  

- Dikdörtgeni eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Daha sonra, 'Son Kullanılan Şekiller' veya 'Dikdörtgenler' arasından dikdörtgeni seçin  

![](rectangle.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına bir dikdörtgen eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
Yöntem bir [RectangleShape](https://reference.aspose.com/cells/javascript-cpp/rectangleshape) nesnesi döndürür.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına nasıl dikdörtgen ekleyeceğinizi gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Rectangle</title>
    </head>
    <body>
        <h1>Add Rectangle to Worksheet</h1>
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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the rectangle to the worksheet
            sheet.shapes.addRectangle(2, 0, 2, 0, 100, 300);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Rectangle added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](rectangle2.png)  

## **JavaScript kullanarak Excel Çalışma Sayfasına Küp Ekleme**  

Küpün şekli **Temel Şekiller** kategorisine aittir.  

*  

- Küpü eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Ardından, **Temel Şekiller**'den Küpü seçin  

![](cube.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına bir küp eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Yöntem bir [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) nesnesi döndürür.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına küp nasıl ekleneceğini gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Cube</title>
    </head>
    <body>
        <h1>Add Cube to Worksheet</h1>
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
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the cube to the worksheet
            sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Cube added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](cube2.png)  

## **JavaScript kullanarak Excel Çalışma Sayfasına çağrı kutusu dörtlü ok ekleme**  

Çağrı kutusu dörtlü ok şekli **Blok Oklar** kategorisine aittir.  

*  

- Çağrı ok dört ok eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Ardından, **Blok Oklar**'dan çağrı kutusu dörtlü ok seçin  

![](callout_quad_arrow.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına bir çağrı oku dört ok eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Yöntem bir [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) nesnesi döner.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına çağrı kutusu dörtlü ok nasıl eklenir gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Callout Quad Arrow</title>
    </head>
    <body>
        <h1>Add Callout Quad Arrow Shape</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const sheet = workbook.worksheets.get(0);

            sheet.shapes.addAutoShape(AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shape added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](callout_quad_arrow2.png)  

## **Excel Çalışma Sayfasına Çarpma İşareti Ekleme JavaScript Kullanarak**  

Çarpım işaretinin şekli **Denklem Şekilleri** kategorisine aittir.  

*  

- Çarpma işareti eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Ardından, **Denklem Şekilleri**'nden çarpım işaretini seçin  

![](multiplication_sign.png)  

***Aspose.Cells Kullanarak***  

Çarpma işaretini çalışma sayfasına eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Yöntem bir [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) nesnesi döner.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına çarpım işareti nasıl eklenir gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Multiply Sign</title>
    </head>
    <body>
        <h1>Add Multiplication Sign to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the multiplication sign to the worksheet
            sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Multiplication sign added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](multiplication_sign2.png)  

## **Excel Çalışma Sayfasına Çoklu Belge Ekleme JavaScript Kullanarak**  

Çoklu belgenin şekli **Akış Diyagramları** kategorisine aittir.  

*  

- Çoklu belgeyi eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Ardından, **Akış Diyagramları**'ndan çoklu belgeyi seçin  

![](multidocument.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına çoklu belge eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Yöntem bir [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) nesnesi döner.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına çoklu belge nasıl eklenir gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the multidocument to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](multidocument2.png)  

## **Excel Çalışma Sayfasına Beş Köşeli Yıldız Ekleme JavaScript Kullanarak**  

Beş Uçlu Yıldızın şekli **Yıldızlar ve Bayraklar** kategorisine aittir.  

*  

- Beş köşeli yıldızı eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Ardından, **Yıldızlar ve Bayraklar**'ndan Beş Uçlu Yıldızı seçin  

![](star_5_points.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına beş köşeli yıldız eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Yöntem bir [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) nesnesi döner.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına Beş Uçlu Yıldız nasıl eklenir gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Star Shape</title>
    </head>
    <body>
        <h1>Add Five-Pointed Star to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Add the Five-pointed star to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Star shape added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](star_5_points2.png)  

## **Excel Çalışma Sayfasına Düşünce Balonu Bulutu Ekleme JavaScript Kullanarak**  

Düşünce balonu bulutunun şekli **Çağrı** kategorisine aittir.  

*  

- Düşünce balonu bulutu eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Ardından, **Çağrı**'dan Düşünce Balonu Bulutunu seçin  

![](thought_bubble_cloud.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına düşünce balonu bulutu eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Yöntem bir [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) nesnesi döner.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına Düşünce Balonu Bulutu nasıl eklenir gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Cloud Callout Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the thought bubble cloud to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cloud callout added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](thought_bubble_cloud2.png)  

## **Gelişmiş Konular**  
- [Şekil Ayar Değerlerini Değiştirme](/cells/tr/javascript-cpp/change-adjustment-values-of-the-shape/)  
- [Çalışma Sayfaları Arasında Şekilleri Kopyalama](/cells/tr/javascript-cpp/copy-shapes-between-worksheets/)  
- [İlkel Olmayan Şekildeki Veri](/cells/tr/javascript-cpp/data-in-non-primitive-shape/)  
- [Çalışma Sayfası İçindeki Şeklin Mutlak Konumunu Bulma](/cells/tr/javascript-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [Şekilden Bağlantı Noktalarını Al](/cells/tr/javascript-cpp/get-connection-points-from-shape/)  
- [Denetimleri Yönetme](/cells/tr/javascript-cpp/managing-controls/)  
- [Çalışma Sayfasına Simgeler Ekleme](/cells/tr/javascript-cpp/insert-svg-to-excel/)  
- [OLE Nesnelerini Yönetme](/cells/tr/javascript-cpp/managing-ole-objects/)  
- [Resimleri Yönetme](/cells/tr/javascript-cpp/managing-pictures/)  
- [Akıllı Sanatı Yönetme](/cells/tr/javascript-cpp/managing-smartart/)  
- [Metin Kutularını Yönetme](/cells/tr/javascript-cpp/managing-textbox-of-excel/)  
- [Çalışma Sayfasına WordArt Fili Ekleme](/cells/tr/javascript-cpp/add-wordart-watermark-to-worksheet/)  
- [Bağlantılı Şekillerin Değerlerini Yenileme](/cells/tr/javascript-cpp/refresh-values-of-linked-shapes/)  
- [Çalışma Sayfası İçinde Şekil Önüne veya Arkasına Gönderme](/cells/tr/javascript-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [Şekil Seçeneklerini Yönetme](/cells/tr/javascript-cpp/managing-shape-options/)  
- [Şekil Metin Seçeneklerini Yönetme](/cells/tr/javascript-cpp/managing-shape-text-options/)  
- [Web Uzantıları - Office Eklentileri](/cells/tr/javascript-cpp/web-extensions-office-add-ins/)
