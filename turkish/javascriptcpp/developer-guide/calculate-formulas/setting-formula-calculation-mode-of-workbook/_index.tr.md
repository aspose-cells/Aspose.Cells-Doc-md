---
title: Workbook un Formül Hesaplama Modunu JavaScript ile C++ kullanarak ayarlama
linktitle: Çalışbook un Formül Hesaplama Modunu Ayarlama
description: Bu makale, Microsoft Excel de workbook un formül hesaplama modunu Aspose.Cells for JavaScript ile C++ kullanarak nasıl ayarlayacağınızı anlatmaktadır. Var olan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells in sağladığı özellikleri kullanarak formül hesaplama modunu ayarlayabilir ve sonucu alabilirsiniz. Son olarak, değiştirilmiş Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, çalışma kitabı, formül hesaplama modu, ayarlar, C++ üzerinden JavaScript
type: docs
weight: 110
url: /tr/javascript-cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}  
Microsoft Excel, formül hesaplama modunu, yani formüllerin nasıl hesaplandığını ayarlamanıza izin verir. Üç olası değer bulunmaktadır:  

- Otomatik - bir şey değiştirildiğinde ve her bir çalışma kitabı açıldığında yeniden hesapla.  
- Otomatik, veri tabloları hariç - bir şey değiştirildiğinde yeniden hesapla, ancak veri tablolarını dışarıda bırak.  
- Manuel - kullanıcı açıkça istediğinde (F9 veya CTRL+ALT+F9'a basarak) veya çalışma kitabı kaydedildiğinde sadece yeniden hesapla.  
{{% /alert %}}  

Microsoft Excel'de formül hesaplama modunu ayarlamak için:  

1. **Formüller**'i seçin, ardından **Hesaplama Seçenekleri**'ni seçin.  
1. Seçeneklerden birini seçin.  

Aspose.Cells for JavaScript ile C++ ayrıca [**FormulaSettings.calculationMode**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#calculationMode--) mod özelliği kullanılarak **Formül Hesaplama Modu** ayarlamanıza olanak sağlar. Bunu aşağıdaki değerlerden biri olan [**CalcModeType**](https://reference.aspose.com/cells/javascript-cpp/calcmodetype) enum'una atayabilirsiniz:  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

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
            // Creating a workbook
            const workbook = new Workbook();

            // Set the Formula Calculation Mode to Manual
            workbook.settings.formulaSettings.calculationMode = AsposeCells.CalcModeType.Manual;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
