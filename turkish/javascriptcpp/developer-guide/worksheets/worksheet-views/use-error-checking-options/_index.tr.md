---
title: Hata Kontrol Seçeneklerini JavaScript ile C++ kullanarak kullanma
linktitle: Hata Kontrolü Seçeneklerini Kullanma
type: docs
weight: 140
url: /tr/javascript-cpp/use-error-checking-options/
description: Excel çalışma sayfalarında hata denetimi seçeneklerini Aspose.Cells for JavaScript kullanarak programatik olarak nasıl kullanılır öğrenin.
keywords: Excel de sayıyı metin olarak depolama ve hata denetimi seçeneklerini JavaScript ile C++ kullanarak kullanma
---

{{% alert color="primary" %}}  
Microsoft Excel, kullanıcıların hata kontrol seçeneklerini ve kurallarını tanımlamalarına izin verir. Kullanıcılar, formüller oluştururken sık ​​sık hata kontrolleri görür, bir hücrenin sağ üst köşesinde küçük bir üçgen, bir hücrede bir sorun olduğunda vurgulanır. Excel, kullanıcılara hücreyle ilgili yaygın problemleri düzeltmelerine yardımcı olacak bilgiler sağlar.  
{{% /alert %}}  

## **Hata türleri**  

Formülü sonucu döndürmeyen hatalar — sıfıra bölmek gibi — acil dikkat gerektirir ve hücrede bir hata değeri görüntülenir. Yeşil üçgen üzerine tıklamak ünlem işareti gösterir; buna tıklandığında seçenekler listesi açılır.  

Hata, seçenekler kullanılarak çözülebilir veya görmezden gelinebilir. Bir hatayı görmezden gelmek, o hatanın sonraki hata kontrollerinde görünmeyeceği anlamına gelir.  

Aspose.Cells, hata kontrolü özellikleri sağlar. [**ErrorCheckOption**](https://reference.aspose.com/cells/javascript-cpp/errorcheckoption) sınıfı farklı hata kontrolleri yönetir, örneğin, metin olarak saklanan sayılar, formül hesaplama hataları ve doğrulama hataları. İstenen hata kontrolünü ayarlamak için [**ErrorCheckType**](https://reference.aspose.com/cells/javascript-cpp/errorchecktype) adlı sıralamayı kullanın.  

## **Metin Olarak Saklanan Sayılar**  

Bazen, sayılar hücrelerde metin olarak biçimlendirilmiş ve saklanmış olabilir. Bu, hesaplamalarda sorunlara neden olabilir veya karışık sıralama düzenleri oluşturabilir. Metin olarak biçimlendirilmiş sayılar, hücrede sağa hizalanmış olarak değil, sola hizalanmış olarak bırakılır. Bir hücrelerde matematiksel bir işlem yapması gereken bir formül değeri döndürmezse, formülün başvurduğu hücrelerdeki hizalama kontrol edilmelidir - bu hücrelerin bazıları veya tümü metin olarak biçimlendirilmiş sayılar olabilir.  

Metin olarak saklanan sayıları hızlı bir şekilde gerçek sayılara dönüştürmek için hata kontrol seçeneklerini kullanabilirsiniz. Microsoft Excel 2003'te:  

1. **Araçlar** menüsünde **Seçenekler**'i tıklayın.  
1. Hata Kontrolü sekmesini seçin.  
   **Metin olarak saklanan sayı** seçeneği varsayılan olarak işaretlidir.  
1. Bu seçeneği devre dışı bırakın.  

Aşağıdaki örnek kod, Aspose.Cells API'lerini kullanarak bir çalışma sayfasındaki metin olarak saklanan sayılar hata kontrol seçeneğini devre dışı bırakmanın nasıl yapıldığını göstermektedir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Error Check Options</title>
    </head>
    <body>
        <h1>Error Check Options Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a Workbook by reading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Instantiate the error checking options
            const opts = sheet.errorCheckOptions;

            const index = opts.add();
            const opt = opts.get(index);
            // Disable the numbers stored as text option
            // Converted from opt.setErrorCheck(type, value) to a property-style assignment
            opt.errorCheck = opt.errorCheck || {};
            opt.errorCheck[AsposeCells.ErrorCheckType.NumberStoredAsText] = false;
            // Set the range
            opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

            // Save the Excel file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_test.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
