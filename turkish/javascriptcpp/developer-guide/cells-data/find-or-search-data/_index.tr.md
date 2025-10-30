---
title: Veri Bulma veya Arama
type: docs
weight: 50
url: /tr/javascript-cpp/find-or-search-data/
description: Belirtilen veriyi içeren hücreleri bulmak veya aramak için C++ ile Aspose.Cells for JavaScript kullanmayı öğrenin.
keywords: C++ üzerinden JavaScript ile veri bulma, C++ üzerinden JavaScript ile veri arama, C++ üzerinden JavaScript ile Formül İçeren Hücreleri Bulma, C++ üzerinden JavaScript ile Formül İçeren Hücreleri Arama, C++ üzerinden JavaScript ile FindOptions kullanarak Veri veya Formülleri Bulma, C++ üzerinden JavaScript ile FindOptions kullanarak Veri veya Formülleri Arama, C++ üzerinden JavaScript ile Belirtilen Dize Değeri veya Sayı İçeren Hücreleri Bulma veya Arama, Belirtilen Veri içeren hücreleri bulma veya arama
---

{{% alert color="primary" %}}  
Microsoft Excel, belirli veriyi içeren hücreleri bulma imkanı sağlar.  
{{% /alert %}}  

## **Belirli Verileri İçeren Hücreleri Bulma**  

### **Microsoft Excel Kullanımı**  

Microsoft Excel, belirli veriyi içeren hücreleri bulma imkanı sağlar. Microsoft Excel'de **İşle** menüsünden **Bul** seçildiğinde, arama değerini belirtebileceğiniz bir iletişim kutusu göreceksiniz.  

Burada, "Portakallar" değerini arıyoruz. Aspose.Cells, ayrıca belirli değerleri içeren hücreleri bulmayı sağlar.  

### **Aspose.Cells for JavaScript kullanılarak C++ üzerinden**  

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonunu sağlar. [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonu, kullanıcı tarafından belirlenen verileri içeren hücreleri bulmak için çeşitli yöntemler sunar. Bu yöntemlerden birkaçını detaylıca aşağıda görebilirsiniz.  

{{% alert color="primary" %}}  
Tüm Bul yöntemleri, belirtilen verileri içeren hücrelerin referanslarını döndürür.  
{{% /alert %}}  

## **Formül İçeren Hücreleri Bulma**  

Geliştiriciler, belirli bir formülü [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunun [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) yöntemiyle bulabilirler. Genellikle, [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) metodu üç parametre alır:  

- Aranacak nesne. Türü int, double, DateTime, string, bool olmalıdır.  
-  Aynı nesneye sahip önceki hücre. Bu parametre başlangıçtan itibaren aranıyorsa null olarak ayarlanabilir.  
-  Gerekli nesneyi bulma seçenekleri.  

Aşağıdaki örnekler, bulma yöntemlerini uygulamak için çalışma sayfası verilerini kullanır:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Cell Containing Formula</title>
    </head>
    <body>
        <h1>Find Cell Containing Formula</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FindOptions, LookInType } = AsposeCells;

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

            // Instantiate FindOptions Object and set to look in formulas
            const findOptions = new FindOptions();
            findOptions.lookInType = LookInType.Formulas;

            // Finding the cell containing the specified formula
            const cell = worksheet.cells.find("=SUM(A5:A10)", null, findOptions);

            // Displaying the name of the cell found after searching worksheet
            document.getElementById('result').innerHTML = `<p style="color: green;">Name of the cell containing formula: ${cell.name}</p>`;
        });
    </script>
</html>
```  


## **FindOptions Kullanarak Veri veya Formülleri Bulma**  

Belirtilen değerleri, [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunun [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-) metodu ve çeşitli [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions) parametrelerle bulmak mümkündür. Genellikle, [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) metodu şu parametreleri kabul eder:  

- **Arama değeri**, aranmak istenen veri veya değer.  
- **Önceki hücre**, aynı değere sahip son hücre. Aramaya başlangıçtan itibaren arıyorsanız bu parametre null olarak ayarlanabilir.  
- **Bul seçenekleri**, bul seçenekleri.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Using FindOptions</title>
    </head>
    <body>
        <h1>Find Using FindOptions Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FindOptions, CellArea, LookInType, LookAtType } = AsposeCells;

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

            // Calculate formulas in workbook
            workbook.calculateFormula();

            // Get Cells collection from first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Instantiate FindOptions Object
            const findOptions = new FindOptions();

            // Create a Cells Area
            const ca = new CellArea();
            ca.startRow = 8;
            ca.startColumn = 2;
            ca.endRow = 17;
            ca.endColumn = 13;

            // Set cells area for find options
            findOptions.range = ca;

            // Set searching properties
            findOptions.searchBackward = false;
            findOptions.searchOrderByRows = true;

            // Set the lookintype, you may specify, values, formulas, comments etc.
            findOptions.lookInType = LookInType.Values;

            // Set the lookattype, you may specify Match entire content, endswith, startswith etc.
            findOptions.lookAtType = LookAtType.EntireContent;

            // Find the cell with value
            const cell = cells.find(341, null, findOptions);

            if (cell !== null) {
                document.getElementById('result').innerHTML = `<p>Name of the cell containing the value: ${cell.name}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p>Record not found</p>';
            }
        });
    </script>
</html>
```  


## **Belirli Dize Değeri veya Numarası İçeren Hücreleri Bulma**  

Belirli dizgi değerleri, aynı [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) metodunu farklı [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions) parametreleriyle çağırarak bulunabilir.  

[**FindOptions.lookInType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookInType-lookintype-) ve [**FindOptions.lookAtType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookAtType-lookattype-) özelliklerini belirtin. Aşağıdaki örnek kod, bu özelliklerin nasıl kullanılacağını gösterir ve hücrenin başında, ortasında veya sonunda çeşitli sayıda dizge içeren hücreleri bulmak için kullanılır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Find Examples</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate the workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection
            const cells = workbook.worksheets.get(0).cells;

            const opts = new AsposeCells.FindOptions();
            opts.lookInType = AsposeCells.LookInType.Values;
            opts.lookAtType = AsposeCells.LookAtType.EntireContent;

            let messages = '';

            // Find the cell with the input integer or double
            let cell1 = cells.find(205, null, opts);

            if (cell1 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell1.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell with the input string
            let cell2 = cells.find("Items A", null, opts);

            if (cell2 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell2.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell containing the input string (partial match)
            opts.lookAtType = AsposeCells.LookAtType.Contains;
            let cell3 = cells.find("Data", null, opts);

            if (cell3 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell3.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            document.getElementById('result').innerHTML = messages;
        });
    </script>
</html>
``` 



## **Gelişmiş Konular**  
- [Belirli Stile Sahip Hücreleri Bulma](/cells/tr/javascript-cpp/find-cells-with-specific-style/)  
- [Hücre Değerinin Tek Tırnak İşareti ile Başlayıp Başlamadığını Bulma](/cells/tr/javascript-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Orijinal Değerler Kullanarak Veri Arama](/cells/tr/javascript-cpp/search-data-using-original-values/)
