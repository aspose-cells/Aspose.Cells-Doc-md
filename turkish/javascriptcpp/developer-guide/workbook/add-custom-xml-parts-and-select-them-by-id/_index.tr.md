```markdown
---
title: Özel XML Parçaları Ekleyin ve ID ye Göre Seçin, C++ ile JavaScript kullanarak
linktitle: Özel XML Parçalarını Ekleyin ve ID leri ile Seçin
type: docs
weight: 70
url: /tr/javascript-cpp/add-custom-xml-parts-and-select-them-by-id/
description: Excel belgelerine özel XML parçaları nasıl eklenir ve ID ye göre nasıl seçilir öğrenin, Aspose.Cells for JavaScript kullanarak C++ ile.
---

## **Olası Kullanım Senaryoları**  

Özel XML Parçaları, Microsoft Excel belgeleri içinde saklanan XML verileridir ve bu belgelerle ilgilenen uygulamalar tarafından kullanılır. Şu anda bunları Microsoft Excel kullanıcı arayüzü kullanarak doğrudan eklemenin bir yolu yoktur. Ancak, bunları programlı olarak çeşitli yollarla ekleyebilirsiniz, örneğin VSTO kullanarak, Aspose.Cells kullanarak vb. Lütfen Aspose.Cells API kullanarak Özel XML Parçası eklemek istiyorsanız [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--) koleksiyonunu kullanın. Ayrıca, ID'sini [**CustomXmlPart.iD**](https://reference.aspose.com/cells/javascript-cpp/customxmlpart/#iD--) özelliği ile ayarlayabilirsiniz. Benzer şekilde, ID'ye göre Özel XML Parçasını seçmek için [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--) koleksiyonunu kullanabilirsiniz.  

## **Özel XML Parçalarını ekleyin ve ID'leri ile seçin**  

Aşağıdaki örnek kod ilk olarak [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--) koleksiyonunu kullanarak dört adet Özel XML Parçası ekler. Daha sonra, onların ID'lerini [**CustomXmlPart.iD**](https://reference.aspose.com/cells/javascript-cpp/customxmlpart/#iD--) özelliği ile ayarlar. Son olarak, eklenen Özel XML Parçasından birini [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--) koleksiyonunu kullanarak bulur veya seçer. Ayrıca, aşağıda verilen kodun konsol çıktılarına da bakınız.  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add and Select Custom XML Parts Example</title>
    </head>
    <body>
        <h1>Add and Select Custom XML Parts Example</h1>
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

            // Loads the workbook which contains hidden external links
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Some data in the form of byte array.
            // Please use correct XML and Schema instead.
            const btsData = new Uint8Array([1, 2, 3]);
            const btsSchema = new Uint8Array([1, 2, 3]);

            // Create four custom xml parts.
            wb.customXmlParts.add(btsData, btsSchema);
            wb.customXmlParts.add(btsData, btsSchema);
            wb.customXmlParts.add(btsData, btsSchema);
            wb.customXmlParts.add(btsData, btsSchema);

            // Assign ids to custom xml parts.
            wb.customXmlParts.get(0).id = "Fruit";
            wb.customXmlParts.get(1).id = "Color";
            wb.customXmlParts.get(2).id = "Sport";
            wb.customXmlParts.get(3).id = "Shape";

            // Specify search custom xml part id.
            let srchID = "Fruit";
            srchID = "Color";
            srchID = "Sport";

            // Search custom xml part by the search id.
            const cxp = wb.customXmlParts.selectByID(srchID);

            // Print the found or not found message on console and UI.
            if (cxp.isNull()) {
                console.log(`Not Found: CustomXmlPart ID ${srchID}`);
                document.getElementById('result').innerHTML = `<p style="color: red;">Not Found: CustomXmlPart ID ${srchID}</p>`;
            } else {
                console.log(`Found: CustomXmlPart ID ${srchID}`);
                document.getElementById('result').innerHTML = `<p style="color: green;">Found: CustomXmlPart ID ${srchID}</p>`;
            }

            // Save the modified workbook and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            console.log("AddCustomXMLPartsAndSelectThemByID executed successfully.");
        });
    </script>
</html>
```  

## **Konsol Çıktısı**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  
 ```
