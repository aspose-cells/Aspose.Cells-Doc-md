---  
title: Node.js ile C++ kullanarak Çalışma Sayfasına Simgeler Ekleyin  
linktitle: Simgeleri Yönetme  
type: docs  
weight: 100  
url: /tr/nodejs-cpp/insert-svg-to-excel/  
---  

## Aspose.Cells for Node.js via C++ numaralı çalışma sayfasına simgeler ekleyin

Eğer bir Excel dosyasına 'simgeler' eklemek için [Aspose.Cells](https://products.aspose.com/cells/) kullanmanız gerekiyorsa, bu belge size bazı yardımlar sağlayabilir.

Ekle simgesine karşılık gelen Excel arayüzü aşağıdaki gibidir:

![](1.png)

- Çalışma sayfasına eklemek istediğiniz simgenin konumunu seçin
- *Ekle*->*Simgeler*ü tıklayın
- Açılan pencerede, yukarıdaki resimde kırmızı dikdörtgen içindeki simgeyi seçin
- Sol tıklama *Ekle* seçimine tıklayın, Excel dosyasına eklenecektir.

Efekt aşağıdaki gibidir:

![](2.png)

Burada, simgeleri [Aspose.Cells](https://products.aspose.com/cells/) kullanarak eklemenize yardımcı olacak *örnek kod* hazırlandı. Ayrıca gerekli [örnek dosya](sample.xlsx) ve bir ikon [kaynak dosyası](icon.zip) bulunmaktadır. Aynı görüntü efektini vermek için Excel arayüzünü kullanarak, [kaynak dosyası](icon.zip) içinden bir ikon ekledik ve [örnek dosya](sample.xlsx).

### Node.js

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Read icon resource file data
const fileName = path.join(dataDir, "icon.svg");
const bytes = fs.readFileSync(fileName).buffer;

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the icon to the worksheet
sheet.getShapes().addIcons(3, 0, 7, 0, 100, 100, bytes, null);

// Set a prompt message
const c = sheet.getCells().get(8, 7);
c.putValue("Insert via Aspose.Cells");
const s = c.getStyle();
s.getFont().setColor(AsposeCells.Color.Blue);
c.setStyle(s);

// Save. You can check your icon in this way.
workbook.save("sample2.xlsx", AsposeCells.SaveFormat.Xlsx);
```

Yukarıdaki kodu projenizde çalıştırdığınızda aşağıdaki sonuçları elde edersiniz:

![](3.png)  

{{< app/cells/assistant language="nodejs-cpp" >}}
