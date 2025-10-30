---
title: Çalışma Kitaplarında Koşullu Biçimlendirme Uygulama
linktitle: Çalışma Kitaplarında Koşullu Biçimlendirme Uygulama
description: JavaScript aracılığıyla C++ kullanarak Aspose.Cells kütüphanesini, hücrelerin görünümünü daha iyi kontrol etmek için çalışma sayfalarında koşullu biçimlendirme uygulamada nasıl kullanacağınızı gösterir.
keywords: Aspose.Cells, Koşullu Biçimlendirme, JavaScript aracılığıyla C++, Çalışma Sayfası, Biçimlendirme
type: docs
weight: 130
url: /tr/javascript-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Bu makale, bir çalışma sayfasındaki hücre aralığına koşullu biçimlendirme eklemenin detaylı bir anlayışını sağlamak amacıyla tasarlanmıştır.

Koşullu biçimlendirme, Microsoft Excel'de gelişmiş bir özelliktir ve bir hücrenin değerine veya bir formülün değerine bağlı olarak biçimlendirme uygulamanıza olanak tanır. Örneğin, bir hücrenin arka planı, negatif bir değeri vurgulamak için kırmızı olabilir veya pozitif bir değer için metin rengi yeşil olabilir. Hücrenin değeri biçim koşulunu karşıladığında, biçim uygulanır. Hücrenin değeri biçim koşulunu karşılamadığında, hücrenin varsayılan biçimlendirmesi kullanılır.

Microsoft Office Automation ile koşullu biçimlendirme uygulamak mümkündür ancak bunun dezavantajları vardır. Örneğin, güvenlik, istikrar, ölçeklenebilirlik ve hız gibi çeşitli nedenler ve sorunlar bulunmaktadır. Başka bir çözüm bulma ana nedeni, Microsoft'un kendisinin yazılım çözümleri için Office Automation'a kesinlikle karşı çıkmasıdır.

Bu makale, Aspose.Cells API kullanarak web uygulaması oluşturmada, hücrelere koşullu biçimlendirme eklemede en basit satırları kullanma yöntemini gösterir.

{{% /alert %}}

## **Hücre Değerine Bağlı Olarak Koşullu Biçimlendirme Uygulamak İçin Aspose.Cells Kullanma**

1. **Aspose.Cells'ı İndirin ve Kurun**.
   1. Aspose.Cells for JavaScript'i C++ ile indirin.
1. Geliştirme bilgisayarınıza kurun.
   Kurulduğunda, tüm Aspose bileşenleri değerlendirme modunda çalışır. Değerlendirme modunun süresiz bir sınırlaması yoktur ve yalnızca üretilen belgelere filigran enjekte eder.
1. **Bir proje oluşturun.**
   JavasScript projenize başlamak için başlatın. Bu örnek, tarayıcı tabanlı web uygulamasında kullanımı göstermektedir.
1. **Referanslar Ekleyin**.
   Projeye Aspose.Cells referansı ekleyin, örneğin kütüphaneyi şu şekilde dahil ederek:
   ```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Conditional Formatting Example</title>
    </head>
    <body>
        <h1>Apply Conditional Formatting Based on Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FormatConditionType, OperatorType, CellArea, Color } = AsposeCells;

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
            const worksheet = workbook.worksheets.get(0);

            // Add conditional formatting collection
            const cfCollection = worksheet.conditionalFormattings;
            const idx = cfCollection.add();
            const formatConditionCollection = cfCollection.get(idx);

            // Define the cell area to apply conditional formatting (A1)
            const area = CellArea.createCellArea(0, 0, 0, 0); // fromRow, fromCol, toRow, toCol
            formatConditionCollection.addArea(area);

            // Add a condition: Cell Value > 100
            const conditionIndex = formatConditionCollection.addCondition(
                FormatConditionType.CellValue,
                OperatorType.Greater,
                "100",
                null
            );

            const formatCondition = formatConditionCollection.get(conditionIndex);

            // Modify the style for the condition: bold and red font
            const style = formatCondition.style;
            if (!style.font) {
                style.font = {};
            }
            style.font.bold = true;
            style.font.color = Color.fromArgb(255, 255, 0, 0); // ARGB red

            // Assign modified style back (property assignment pattern)
            formatCondition.style = style;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'conditional_formatting_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied to cell A1 (value &gt; 100). Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Yukarıdaki kod yürütüldüğünde, çıktı dosyasının (output.xls) ilk çalışma sayfasındaki “A1” hücresine koşullu biçimlendirme uygulanır. A1 hücresine uygulanan koşullu biçimlendirme, hücre değere bağlıdır. A1 hücresinin değeri 50 ile 100 arasında ise, koşullu biçimlendirme nedeniyle arka plan rengi kırmızı olur.

## **Aspose.Cells Kullanarak Formül Değerine Bağlı Olarak Koşullu Biçimlendirme Uygulama**

1. Formül Uygun Olarak Koşullu Biçimlendirme Uygulama (Kod Parçası)
   Aşağıda verilen kod, görevi gerçekleştirmek için kullanılan koddur. B3'e koşullu biçimlendirme uygular.
