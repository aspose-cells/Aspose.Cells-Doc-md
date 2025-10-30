---
title: C++ ve JavaScript kullanarak Bağımlı ve Bağımlıların İzlenmesi
linktitle: Önceden Gelir ve Bağımlılar
type: docs
weight: 230
url: /tr/javascript-cpp/precedents-and-dependents/
description: İşletim sisteminde ve karmaşık finansal tablolar gibi durumlarda, bağımlı ve bağımlıların izlenmesi konusunda bilgi edinin ve Aspose.Cells for JavaScript via C++ kullanarak hücrelerin bağımlılarını ve bağımlılarını nasıl izleyebileceğinizi öğrenin.
---

{{% alert color="primary" %}} 

Özellikle ortak geliştirilen karmaşık finansal çalışma tabloları, en utanç verici hataları saklayabilir. Formüllerin doğruluğunu kontrol etmek ve bir hatanın kaynağını bulmak, öncü hücreler ve bağımlı hücreleri kullanan formülün olduğu durumlarda zor olabilir.

{{% /alert %}} 
## **Giriş**
- **Öncül hücreler**, başka bir Hücredeki bir formül tarafından başvurulan hücrelerdir. Örneğin, eğer D10 hücresi =B5 formülünü içeriyorsa, B5 hücresi D10 hücresinin öncül hücresidir.
- **Bağımlı hücreler**, diğer hücrelere referans veren formüller içerir. Örneğin, D10 hücresinde =B5 formülü varsa, D10 hücresi B5 hücresine bağımlıdır.

Elektronik tabloyu okunabilir hale getirmek için belki de bir formülde kullanılan hangi hücreleri açıkça göstermek istersiniz. Benzer şekilde, diğer hücrelerin bağımlı hücrelerini çıkarmak isteyebilirsiniz.

Aspose.Cells, hücreleri izlemenize ve hangi hücrelerin bağlı olduğunu bulmanıza olanak tanır.
## **Öncekileri ve Bağımlı Hücreleri İzleme: Microsoft Excel**
Formüller, müşteri tarafından yapılan değişikliklere bağlı olarak değişebilirler. Örneğin, C3 ve C4 hücrelerinde bir formül içeren ve C1'in C3 ve C4'e bağımlı olduğu durumu düşünelim (bu durumda formül geçersiz kılınmış olur), diğer hücrelerin iş kurallarına göre tabloyu dengelemek için değişmesi gerekebilir.

Benzer şekilde, C1 hücresi '=(B1*22)/(M2*N32)' formülünü içeriyorsa, C1'in bağımlı olduğu hücreleri, yani precedent hücreleri (B1, M2 ve N32), bulmak istiyorum.

Belirli bir hücrenin bağımlılığını başka hücrelere izlemek isteyebilirsiniz. İş kuralları formüllerde gömülüyse, bağımlılığı bulmak ve buna göre bazı kuralları uygulamak isteriz. Benzer şekilde, belirli bir hücrenin değeri değiştirilirse, çalışma sayfasındaki hangi hücrelerin bu değişimden etkilendiğini bilmek isteriz.

Microsoft Excel, öncekileri ve bağımlıları izlemek için kullanıcılara olanak sağlar.

1. **Görünüm Araç Çubuğu**'nda **Formül Denetimi**'ni seçin. Formül Denetimi iletişim kutusu görüntülenecektir.
1. Önceden Gelenleri İzleme:
   1. Önceden gelen hücreleri bulmak istediğiniz formül içeren hücreyi seçin.
   1. Doğrudan veri sağlayan her hücreye izleyici okunu göstermek için **Formül Denetimi** araç çubuğunda **Önceden Gelenleri İzle**'yi tıklatın.
1. Belirli bir hücreyi referans olarak alan formülleri izle (bağımlılar)
   1. Bağımlı hücreleri belirlemek istediğiniz hücreyi seçin.
   1. Aktif hücreye bağımlı olan her hücreye izleyici okunu göstermek için Formül Denetimi araç çubuğunda **Trace Dependents**'a tıklayın.
## **Öncekileri ve Bağımlı Hücreleri İzleme: Aspose.Cells**
### **Öncüleri İzleme**
Aspose.Cells, precedent hücreleri almayı kolaylaştırır. Basit formül precedentlerine veri sağlayan hücreleri almanın yanı sıra adlandırılmış aralıklara göre karmaşık formül precedentlerine veri sağlayan hücreleri de bulabilir.

Aşağıdaki örnekte, bir şablon excel dosyası olan Book1.xls kullanılmıştır. Elektronik tabloda veri ve formüller bulunmaktadır.

Aspose.Cells, hücrenin bağımlılarını izlemek için kullanılan [Cell](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfının [Cell.precedents()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedents--) metodunu sağlar. Bu, referans edilen alanların bir koleksiyonunu döndürür. Yukarıda görüldüğü gibi, Book1.xls'te, B7 hücresinde "=SUM(A1:A3)" formülü bulunur. Yani A1:A3 hücreleri B7 hücresinin bağımlılarıdır. Aşağıdaki örnek, Book1.xls şablon dosyasını kullanarak bağımlı izleme özelliğini gösterir.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Precedents Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet's cells
            const cells = workbook.worksheets.get(0).cells;

            // Get cell B4
            const cell = cells.get("B4");

            if (cell) {
                // Get precedents (converted from getPrecedents)
                const ret = cell.precedents;

                if (!ret.isNull() && ret.count > 0) {
                    const area = ret.get(0);

                    const sheetName = area.sheetName;
                    const startAddress = AsposeCells.CellsHelper.cellIndexToName(area.startRow, area.startColumn);
                    const endAddress = AsposeCells.CellsHelper.cellIndexToName(area.endRow, area.endColumn);

                    console.log(sheetName);
                    console.log(startAddress);
                    console.log(endAddress);

                    document.getElementById('result').innerHTML = `<pre>Sheet: ${sheetName}\nStart: ${startAddress}\nEnd: ${endAddress}</pre>`;
                } else {
                    document.getElementById('result').innerHTML = '<p style="color: red;">No precedents found for the cell.</p>';
                }
            } else {
                document.getElementById('result').innerHTML = '<p style="color: red;">Cell B4 is null.</p>';
            }
        });
    </script>
</html>
```
### **Bağımlıları İzleme**
Aspose.Cells, çalışma sayfalarındaki bağlı hücreleri almanıza olanak tanır. Sadece basit bir formüle ilişkin verileri sağlayan hücreleri değil, aynı zamanda isimli alanlar içeren karmaşık formüllerin bağımlılarını sağlayan hücreleri de bulabilir.

Aspose.Cells, hücrenin bağımlılarını izlemek için kullanılan [Cell](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfının [Cell.dependents(boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dependents-boolean-) metodunu sağlar. Örneğin, Book1.xlsx'te B2 ve C2 hücrelerinde "=A1+20" ve "=A1+30" formülleri bulunur. Aşağıdaki örnek, şablon dosyasını kullanarak A1 hücresinin bağımlılarını nasıl izleyebileceğinizi gösterir.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Get Cell Dependents Example</h1>
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("B2");
            // Ensure dependents is accessed as a property (converted from getDependents)
            const dependents = cell.dependents;

            if (Array.isArray(dependents)) {
                let out = '<p>Dependents found:</p><ul>';
                for (const c of dependents) {
                    console.log(c.name);
                    out += `<li>${c.name}</li>`;
                }
                out += '</ul>';
                resultDiv.innerHTML = out;
            } else {
                console.error("Dependents is not an array");
                resultDiv.innerHTML = '<p style="color: red;">Dependents is not an array</p>';
            }
        });
    </script>
</html>
```
### **Hesaplama zincirine göre precedent ve bağımlı hücreleri izleme**
Yukarıdaki bağımlı ve bağımlıların izlenmesine ilişkin API'ler, formül ifadesine göre çalışır. Sadece birkaç formül için bağımlılıkları izlemek amacıyla kullanışlı bir yöntem sağlarlar. Eğer çalışma kitabında çok sayıda formül varsa ve her hücrenin bağımlılarını ve bağımlılarını izlemek gerekiyorsa, performans düşük olur. Bu durumda, kullanıcı [Cell.precedentsInCalculation()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedentsInCalculation--) ve [Cell.dependentsInCalculation(boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dependentsInCalculation-boolean-) metodlarını kullanmayı düşünmelidir. Bu iki metod, bağımlılıkları hesaplama zincirine göre izler. Bu nedenle, önce [FormulaSettings.enableCalculationChain()](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--) ile hesaplama zincirini etkinleştirmeniz gerekir. Ardından, [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) ile çalışma kitabının tam hesaplamasını yapabilirsiniz. Daha sonra, bu hücrelerin bağımlılıklarını veya bağımlılarını izleyebilirsiniz.

Bazı formüllerde, bağımlılar ve hesaplamada kullanılan bağımlılarInCalculation farklı olabilir ve bağlı olanlar da dependents ve dependentsInCalculation ile farklı olabilir. Örneğin, A1 hücresinin formülü "=IF(TRUE,B2,C3)" ise, bağımlılar B2 ve C3'tür. Buna göre, B2 ve C3, bağımlıların kontrol edilmesi sırasında A1'in bağımlılarıdır. Ancak, bu formülün hesaplaması için, yalnızca B2'nin sonucu etkilediği açıktır. Bu nedenle, dependentsInCalculation A1 için C3'ü sağlamayacak ve C3 için dependentsInCalculation A1'i sağlamayacaktır. Bazen kullanıcılar, sadece çalışma kitabındaki mevcut verilere dayanarak, formüllerin gerçek sonucu etkileyen bağımlılıkları takip etmek isteyebilirler; bu durumda, dependentsInCalculation/precedentsInCalculation kullanmaları gerekir.

Aşağıdaki örnek, hücreler için hesaplama zincirine göre öncüleri ve bağımlıları nasıl izleyebileceğinizi gösterir:


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
            resultDiv.innerHTML = '';
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;

            // Setting formulas
            cells.get("A1").formula = "=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2";
            cells.get("A2").formula = "=IF(TRUE,B2,B1)";

            // Enable calculation chain
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate formulas
            workbook.calculateFormula();

            // Collect output
            let output = '';

            let en = cells.get("B1").dependentsInCalculation;
            output += "B1's calculation dependents:\n";
            if (en && en.length !== undefined) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            } else if (en) {
                // If it's an iterable but doesn't have length
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            }
            output += "\n";

            en = cells.get("B2").dependentsInCalculation;
            output += "B2's calculation dependents:\n";
            if (en && en.length !== undefined) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            } else if (en) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            }
            output += "\n";

            en = cells.get("A1").precedentsInCalculation;
            output += "A1's calculation precedents:\n";
            if (en && en.length !== undefined) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            } else if (en) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            }
            output += "\n";

            en = cells.get("A2").precedentsInCalculation;
            output += "A2's calculation precedents:\n";
            if (en && en.length !== undefined) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            } else if (en) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            }

            resultDiv.innerHTML = '<pre>' + output.replace(/</g, '&lt;') + '</pre>';

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
        });
    </script>
</html>
```
