---
title: Sayı Ayarları
linktitle: Sayı Ayarları
description: Aspose.Cells, çeşitli hücre sayı ayarlarını destekleyen, hücrelerle çalışma için bir JavaScript kütüphanesidir. Bu makale, hücrelerin sayı ayarlarını yönetmek ve elektronik tablolarda sayı biçimlerini ayarlamak için Aspose.Cells kütüphanesinin nasıl kullanılacağını tanıtmaktadır.
keywords: Aspose.Cells, JavaScript kütüphanesi, elektronik tablo, hücre sayı ayarları, biçimlendirme, yönetim, Sayı ve Tarih Formatları
type: docs
weight: 10
url: /tr/javascript-cpp/cells-number-settings/
---

## **Sayı ve Tarih Formatlarının Görüntülemesini Nasıl Ayarlayabilirsiniz**  

Microsoft Excel'in çok güçlü bir özelliği, kullanıcıların sayısal değerlerin ve tarihlerin görüntüleme biçimlerini ayarlamalarına izin vermesidir. Sayısal verilerin, ondalık, para birimi, yüzde, kesir veya muhasebe değerleri gibi çeşitli farklı değerleri temsil etmek için kullanılabileceğini biliyoruz. Bu sayısal tüm değerler, temsil ettikleri bilgi türüne göre farklı biçimlerde görüntülenir. Benzer şekilde, bir tarih veya zamanın gösterilebileceği birçok format mevcuttur.  
Aspose.Cells bu işlevselliği destekler ve geliştiricilere bir numaranın veya tarihin herhangi bir görüntüleme formatını ayarlama izni verir.  

### **Microsoft Excel'de Görüntüleme Formatlarını Nasıl Ayarlayabilirsiniz**  

Microsoft Excel'de görüntüleme formatlarını ayarlamak için:  

1. Herhangi bir hücreye sağ tıklayın.  
2. **Hücreleri Biçimlendir** seçeneğini tıklayın. Herhangi bir değer türünün görüntüleme biçimlerini ayarlamak için kullanılan bir ileti kutusu açılır.  

İletişim kutusunun sol tarafında, **Genel**, **Sayı**, **Para Birimi**, **Muhasebe**, **Tarih**, **Saat**, **Yüzde** gibi birçok değer kategorisi vardır. Aspose.Cells, tüm bu görüntüleme biçimlerini destekler.  

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı bir modül sağlar; bu, bir Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) modülü, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) modülü tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) modülü, bir [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) modülünün bir nesnesini temsil eder.  

Aspose.Cells, [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) özelliğini [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) modülü için sağlar. Bu özellik, bir hücrenin biçimlendirmesini almak ve ayarlamak için kullanılır. [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) modülü, sayı ve tarihlerle ilgilenen bazı yararlı özellikler sağlar.  

### **Dahili Sayı Formatlarının Nasıl Kullanılacağı**  

Aspose.Cells, sayıların ve tarihlerinin görüntü formatlarını yapılandırmak için bazı yerleşik sayı formatları sunar. Bu yerleşik sayı formatları, [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) özelliği kullanılarak uygulanabilir. Tüm yerleşik sayı formatları benzersiz sayısal değerler içerir. Geliştiriciler, gösterim biçimini uygulamak için [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) özelliğine istediği sayısal değeri atayabilir. Bu yöntem hızlıdır. Aspose.Cells tarafından desteklenen yerleşik sayı formatları aşağıda listelenmiştir.  

|**Değer**|**Tür**|**Biçim Dizesi**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create/Modify Workbook</h1>
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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = new Date();

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 20;

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 2546;

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  


### **Özel Sayı Formatları Nasıl Kullanılır**  

Kendi özel biçim dizesini tanımlamak için, gösterim biçimini ayarlarken [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesinin [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) özelliğini kullanın. Bu yaklaşım, önceden ayarlanmış biçimleri kullanmaya kıyasla daha yavaş olsa da daha esnektir.  

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

            // Instantiate or open workbook depending on whether a file is provided
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.putValue(new Date());

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.putValue(20);

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.putValue(2546);

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


{{% alert color="primary" %}}  

Eğer sayı biçimini ayarlamak için [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) özelliğini kullanırsanız, önceki format [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) özelliği kullanılarak ayarlanan herhangi bir biçim üzerine yazılır ve vice versa.  

{{% /alert %}}  

## **Gelişmiş Konular**  
- [Stil.Oluştur Özelliğini Ayarlayarak Özel Sayı Formatını Kontrol Edin](/cells/tr/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [Desteklenen Sayı Formatları Listesi](/cells/tr/javascript-cpp/list-of-supported-number-formats/)  
- [Özel Tarih Format Deseni g ve ge mm dd'yi Dönüştürme](/cells/tr/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Çalışmabook için Özel Sayı Ondalık ve Grup Ayraçlarını Belirleme](/cells/tr/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [DBNum Özel Desen Biçimlendirmesini Belirleme](/cells/tr/javascript-cpp/specifying-dbnum-custom-pattern-formatting/)
