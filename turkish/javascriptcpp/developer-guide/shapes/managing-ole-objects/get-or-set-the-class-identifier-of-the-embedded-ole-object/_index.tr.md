---
title: JavaScript ve C++ kullanarak Gömülü OLE Nesnesinin Sınıf Tanımlayıcısını Al veya Ayarla
linktitle: Gömülü OLE Nesnesinin Sınıf Kimliğini Alın veya Ayarlayın
type: docs
weight: 200
url: /tr/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Aspose.Cells kullanarak JavaScript te gömülü OLE nesnelerinin sınıf tanımlayıcısını nasıl alır veya ayarlarsınız öğrenin.
---

## **Olası Kullanım Senaryoları**  
Aspose.Cells, gömülü OLE nesnesinin sınıf tanımlayıcısını alıp veya ayarlamak için kullanabileceğiniz [OleObject.classIdentifier](https://reference.aspose.com/cells/javascript-cpp/oleobject/#classIdentifier--) özelliği sağlar. OLE nesnesinin sınıf tanımlayıcıları aslında GUID'ler yani Evrensel Benzersiz Tanımlayıcılar'dır. GUID her zaman 16 bayttır; bu yüzden sınıf tanımlayıcıları da 16 bayttır. Sıklıkla Windows Rehberi içinde bulunurlar ve istemci uygulaması içindeki çeşitli gömülü kaynaklar içeren OLE nesneleri nasıl açılacağında hakkında bilgi sağlarlar.

## **Gömülü Çalışmayan Elemanın Sınıf Tanımlayıcısını Al veya Ayarla**  
Aşağıdaki ekran görüntüsü, gömülü PowerPoint OLE nesnesi içeren örnek Excel dosyasından (5115190.xls) alınan OLE nesnesinin sınıf tanımlayıcısı yani GUID'yi gösterir.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **Örnek Kod**  
Lütfen aşağıdaki örnek kodu, [örnek Excel dosyası](5115190.xls) ile çalıştırıldığında ve konsol çıktısı alınırken görebileceğiniz, OLE nesnesinin sınıf tanımlayıcısını veya GUID'yi gösteren çıktı ile birlikte inceleyin. Yazdırılan GUID, ekran görüntüsünde gösterildiği gibi aynıdır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract OLE Object Class Identifier (GUID)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access its first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first ole object inside the worksheet
            const oleObject = worksheet.oleObjects.get(0);

            // Convert 16-bytes array into GUID
            const bytes = new Uint8Array(oleObject.classIdentifier);
            const guid = bytes.reduce((acc, byte) => acc + String.fromCharCode(byte), '');

            // Print the GUID
            console.log(guid.toUpperCase());
            resultDiv.innerHTML = `<p style="color: green;">GUID: ${guid.toUpperCase()}</p>`;
        });
    </script>
</html>
```  
### **Konsol Çıktısı**  
Yukarıdaki örnek kodun, [örnek Excel dosyası](5115190.xls) kullanılarak çalıştırıldığında aldığı konsol çıktısı.

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}
