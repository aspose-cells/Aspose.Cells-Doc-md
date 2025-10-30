---
title: XML i JavaScript ve C++ kullanarak Excel çalışma kitabına içe aktarın
linktitle: XML Haritaları
type: docs
weight: 210
url: /tr/javascript-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: XML dosyalarından verileri Excel e Aspose.Cells for JavaScript kullanarak içe aktarın.
---

{{% alert color="primary" %}}

Aspose.Cells, [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-) yöntemi kullanılarak çalışma kitabı içindeki XML haritasını içe aktarmanıza olanak tanır. XML Map'i aşağıdaki adımlarla Microsoft Excel kullanarak içe aktarabilirsiniz:

- **Geliştirici** sekmesini seçin
- XML bölümünde **İçe Aktar**'ı tıklayın ve gerekli adımları izleyin.

İçe aktarma işlemini tamamlamak için XML verilerinizi sağlamanız gerekecektir. Test için kullanabileceğiniz [örnek XML verileri](5115037.txt) burada bulunmaktadır.

{{% /alert %}}

## **Microsoft Excel kullanarak XML Haritası İçe Aktarma**

Aşağıdaki ekran görüntüsü, Microsoft Excel kullanarak XML Haritası İçe Aktarma işlemini göstermektedir.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Aspose.Cells for JavaScript kullanarak XML Eşlemesini içe aktar**

Aşağıdaki örnek kod, [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-). faydalanmak için nasıl kullanılacağını göstermektedir. Bu, [çıktı excel dosyasını](5115036.xlsx) üretmektedir, bu, ekran görüntüsünde gösterilmiştir.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Import XML</title>
    </head>
    <body>
        <h1>Import XML into Workbook Example</h1>
        <input type="file" id="xmlInput" accept=".xml,.txt" />
        <button id="runExample">Import XML and Save</button>
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
            const fileInput = document.getElementById('xmlInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an XML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const xmlText = await file.text();

            // Create a workbook
            const workbook = new Workbook();

            // Import your XML Map data starting from cell A1 on Sheet1
            workbook.importXml(xmlText, "Sheet1", 0, 0);

            // Save workbook to XLSX and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">XML imported and workbook saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **İleri konular**
- [XmlMapCollection.add() yöntemi kullanarak çalışma kitabı içine XML Map ekleyin](/cells/tr/javascript-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Çalışma Kitabı içinde XML Haritasına bağlı XML Verilerini Dışa Aktar](/cells/tr/javascript-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [XML Haritasının Kök Eleman Adını Bul](/cells/tr/javascript-cpp/find-the-root-element-name-of-xml-map/)
- [Hücreleri XML Haritası Elemanlarına Bağla](/cells/tr/javascript-cpp/link-cells-to-xml-map-elements/)
