---
title: Node.js ile C++ kullanarak Excel Dosyası Yüklerken Uyarıları Alın
linktitle: Excel Dosyası Yüklenirken Uyarıları Al
type: docs
weight: 110
url: /tr/nodejs-cpp/get-warnings-while-loading-excel-file/
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyasını yüklerken uyarıları nasıl yakalayacağınızı öğrenin. Bozuk ama yüklenebilir çalışma kitaplarını etkili şekilde yönetin.
---

## **Olası Kullanım Senaryoları**

Bazen kullanıcı, biraz bozuk fakat yüklenebilir olan bir çalışma kitabını yüklemeye çalışır. Bu durumlarda, Aspose.Cells yükleme sırasında uyarılar fırlatır. Bu uyarıları, [**IWarningCallback**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback) arayüzünü uygulayarak ve [**LoadOptions.getWarningCallback()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getWarningCallback--) özelliğini ayarlayarak yakalayabilirsiniz.

## **Excel Dosyası Yüklenirken Uyarıları Al**

Aşağıdaki örnek kod, Excel dosyasını yüklerken uyarıları nasıl alacağınızı gösterir. Kod, [**DuplicateDefinedName**](https://reference.aspose.com/cells/nodejs-cpp/warningtype) uyarısı veren [örnek Excel dosyasını](sampleDuplicateDefinedName.xlsx) yükler. Bu uyarı, [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback/#warning-warninginfo-) yöntemiyle yakalanır ve uyarı mesajlarını konsolda yazdırır. Daha sonra çalışma kitabı [çıktı excel dosyasına](outputDuplicateDefinedName.xlsx) kaydedilir. Eğer örnek Excel dosyasını Microsoft Excel'de açarsanız, bu uyarıyı görürsünüz; ekran görüntüsünde gösterildiği gibi. Lütfen aşağıdaki kodun konsol çıktısını da kontrol edin, daha iyi anlamak için.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Örnek Kod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Implement IWarningCallback interface to catch warnings while loading workbook
class WarningCallback extends AsposeCells.IWarningCallback {
    warning(warningInfo) {
        if (warningInfo.getType() === AsposeCells.WarningType.DuplicateDefinedName) {
            console.log("Duplicate Defined Name Warning: " + warningInfo.getDescription());
        }
    }
}

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create load options and set the WarningCallback property 
// to catch warnings while loading workbook
const options = new AsposeCells.LoadOptions();
options.setWarningCallback(new WarningCallback());

// Load the source excel file
const book = new AsposeCells.Workbook(path.join(dataDir, "sampleDuplicateDefinedName.xlsx"), options);

// Save the workbook 
book.save(path.join(dataDir, "outputDuplicateDefinedName.xlsx"));
```

## **Konsol Çıktısı**

Yukarıdaki kodun, verilen [örnek excel dosyası](sampleDuplicateDefinedName.xlsx) ile çalıştırıldığında konsol çıktısı şöyledir.

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
