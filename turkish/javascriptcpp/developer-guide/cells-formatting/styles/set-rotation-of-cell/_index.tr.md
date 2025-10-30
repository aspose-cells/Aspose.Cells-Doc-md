---
title: Hücrenin metnini Nasıl Döndürülür
linktitle: Hücrenin metnini Nasıl Döndürülür  
type: docs  
weight: 80  
url: /tr/javascript-cpp/how-to-rotate-text-of-cell/  
description: Bir hücrenin metnini programatik olarak döndürmeyi Aspose.Cells for JavaScript kullanarak C++ ile nasıl yapacağınızı öğrenin.  
keywords: JavaScript via C++ kullanarak Hücre Metnini Döndürmek, Çalışma Kitabındaki hücre metnini programlamalı olarak döndürmek, çalışma kitabındaki hücre döndürme açısını programlamalı ayarlamak, JavaScript ile hücre metnini döndürme nasıl yapılır, excel de hücre metni döndürme  
---

## **Aspose.Cells for JavaScript ile C++ kullanarak Hücre Metnini Döndürmek**

Aspose.Cells, geliştiricilerin Excel tabloları üzerinde programlı çalışmasını sağlayan güçlü bir JavaScript bileşenidir. Aspose.Cells'in sunduğu özelliklerden biri, hücreleri döndürme yeteneğidir ve bu, metin yönünü özelleştirmenize ve verinizin görsel sunumunu iyileştirmenize olanak tanır. Bu belgede, Aspose.Cells kullanarak hücreleri nasıl döndüreceğinizi inceleyeceğiz.

## **Excel'de Hücrenin Metnini Döndürme**
Bir hücreyi Excel'de döndürmek için aşağıdaki adımları kullanabilirsiniz:
1. Excel'i açın ve döndürmek istediğiniz hücreyi veya hücre aralığını seçin.
1. Seçilen hücre(ler)e sağ tıklayın ve bağlam menüsünden "Hücreleri Biçimlendir"'i seçin. Alternatif olarak, Excel şeridinde "Ana Sayfa" sekmesine gidip "Hücreler" grubundaki "Biçimlamanın" açılır menüsüne tıklayıp "Hücreleri Biçimlendir"'i seçebilirsiniz.
1. "Hücreleri Biçimlendir" iletişim kutusunda, "Hizalama" sekmesine gidin.
1. "Yönlendirme" bölümünde, metni döndürebileceğiniz seçenekleri göreceksiniz. "Derece" kutusuna istenen dönme açısını doğrudan girebilirsiniz. Pozitif değerler metni saat yönünün tersine döndürür, negatif değerler ise saat yönünde döndürür.
<br>
![todo:image_alt_text](alignment.png)
1. İstenilen yönlendirmeyi seçtikten sonra, değişiklikleri uygulamak için "Tamam"'a tıklayın. Seçilen hücre(ler) artık seçtiğiniz dönme açısına veya yönlendirmeye göre dönecektir.

## **Aspose.Cells API kullanarak Hücrenin Metnini Döndürme**

[**Style.rotationAngle(number)**](https://reference.aspose.com/cells/javascript-cpp/style/#rotationAngle-number-) özelliği hücreleri döndürmeyi kolaylaştırır. Aspose.Cells'te hücreleri döndürmek için şu adımları izlemeniz gerekir:
1. Excel Çalışma Kitabını Yükle  
<br>
İlk olarak, mevcut bir Excel dosyasını açmak veya yeni bir tane oluşturmak için Workbook sınıfını kullanarak Excel çalışma kitabını yüklemeniz gerekir. 

1. Çalışma Sayfasına Eriş  
<br>
Çalışma kitabı yüklendikten sonra, hücreleri döndürmek istediğiniz çalışma sayfasına erişmeniz gerekir. Çalışma sayfasına endeksine veya adına göre erişebilirsiniz. 

1. Hücrenin metnini döndür  
<br>
Artık çalışma sayfasına erişiminiz olduğuna göre, istenen hücrelerin Stil objesini değiştirerek hücreleri döndürebilirsiniz. Stil objesi, dönme dahil çeşitli biçimlendirme seçeneklerini belirlemenizi sağlar. 

1. Çalışma Kitabını Kaydet  
<br>
Hücreleri döndürdükten sonra, değiştirilmiş çalışma kitabını Save metodunu kullanarak bir dosyaya veya akıma geri kaydedebilirsiniz.

## **JavaScript Örnek Kod**

Aşağıdaki kodu inceleyin, bir çalışma kitabı nesnesi oluşturur ve birkaç hücre için farklı dönüş açıları ayarlar. Ekran görüntüsü, örnek kodun çalıştırılmasının ardından sonucu gösterir.
<br>
<img src="rotation.png" width=80% />

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Rotate Text in Cells Example</h1>
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
            // Creating a new Workbook (blank)
            const workbook = new Workbook();

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Row index of the cell
            let row = 0;
            // Column index of the cell
            let column = 0; 

            let a1 = worksheet.cells.get(row, column);
            a1.putValue("a1 rotate text");
            let a1Style = a1.style;

            // Set the rotation angle in degrees
            a1Style.rotationAngle = 45; 
            a1.style = a1Style;

            // set Column index of the cell
            column = 1;
            let b1 = worksheet.cells.get(row, column);
            b1.putValue("b1 rotate text");
            let b1Style = b1.style;

            // Set the rotation angle in degrees
            b1Style.rotationAngle = 255;
            b1.style = b1Style;

            // set Column index of the cell
            column = 2;
            let c1 = worksheet.cells.get(row, column);
            c1.putValue("c1 rotate text");
            let c1Style = c1.style;

            // Set the rotation angle in degrees
            c1Style.rotationAngle = -90;
            c1.style = c1Style;

            // set Column index of the cell
            column = 3;
            let d1 = worksheet.cells.get(row, column);
            d1.putValue("d1 rotate text");
            let d1Style = d1.style;

            // Set the rotation angle in degrees
            d1Style.rotationAngle = -90;
            d1.style = d1Style;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
