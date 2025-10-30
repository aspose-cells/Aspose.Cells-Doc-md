---
title: Pivot Tablosu ve Kaynak Veri
type: docs
weight: 30
url: /tr/javascript-cpp/pivot-table-and-source-data/
---

## **Pivot Tablosunun Kaynak Verisi**

Farklı veri kaynaklarından (örneğin bir veritabanı) alınan verileri alan ve tasarım zamanında bilinmeyen pivota tabloları olan Microsoft Excel raporları oluşturmak istediğinizde bazı durumlar olabilir. Bu makale, bir pivot tablosunun veri kaynağını dinamik olarak değiştirmenin bir yaklaşımını sunar.

### **Bir Pivot Tablosunun Veri Kaynağını Değiştirme**

1. Yeni bir tasarımcı şablonu oluşturma.
   1. Aşağıdaki ekran görüntüsünde olduğu gibi yeni bir tasarımcı şablonu dosyası oluşturun.
   1. Ardından bu hücre aralığına atıfta bulunan **DataSource** adlı bir adlandırılmış aralık tanımlayın.

      **Bir tasarımcı şablon oluşturma ve DataSource adlı adlandırılmış aralık tanımlama** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Bu adlandırılmış aralığa dayalı bir Özet Tablo Oluşturma.
   1. Microsoft Excel'de **Veri**'yi seçin, ardından **Özet Tablo** ve **Özet Tablo Grafik Raporu'nu** seçin.
   1. İlk adımda oluşturulan adlandırılmış aralığa dayalı bir özet tablo oluşturun.

      **DataSource** adlı adlandırılmış aralığa dayalı bir özet tablo oluşturma 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. İlgili alanı özet tablo satır ve sütununa sürükleyin, ardından aşağıdaki ekran görüntüsünde olduğu gibi sonuç özet tablosunu oluşturun.

   **İlgili alana dayalı bir özet tablo oluşturmak** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Özet tabloyu sağ tıklayın ve **Tablo Seçenekleri**'ni seçin.
   1. **Veri seçenekleri** ayarlarında **Açılışta yenile**'yi işaretleyin.

      **Özet tablo seçeneklerini ayarlama** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Şimdi bu dosyayı tasarımcı şablon dosyanız olarak kaydedebilirsiniz.

1. Yeni veri eklenmesi ve özet tablonun kaynak verisinin değiştirilmesi.
   1. Tasarımcı şablon oluşturulduktan sonra, özet tablonun kaynak verisini değiştirmek için aşağıdaki kodu kullanın.

Aşağıdaki örnek kodu çalıştırarak pivot tablosunun kaynak verisini değiştirin.

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

            // Instantiating a Workbook object using uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Populating new data to the worksheet cells
            worksheet.cells.get("A9").value = "Golf";
            worksheet.cells.get("B9").value = "Qtr4";
            worksheet.cells.get("C9").value = 7000;

            // Changing named range "DataSource"
            const range = worksheet.cells.createRange(0, 0, 9, 3);
            range.name = "DataSource";

            // Saving the modified Excel file
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
