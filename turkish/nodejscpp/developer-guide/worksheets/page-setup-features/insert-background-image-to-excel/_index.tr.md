---
title: Node.js ve C++ kullanarak Excel e Arka Plan Resmi Ekleme
linktitle: Excel e Arka Plan Görüntüsü Ekleme
type: docs
weight: 90
url: /tr/nodejs-cpp/insert-background-image-to-excel/
description: "Aspose.Cells for Node.js via C++ kullanarak Excel e arka plan resmi nasıl eklenir."
---

{{% alert color="primary" %}} 

Bir çalışma sayfasına resim ekleyerek çalışma sayfasını daha çekici hale getirebilirsiniz. Bu özellik, çalışma sayfasındaki verileri engellemeden arka plana hafif bir ipucu ekleyen özel bir kurumsal grafik veya resminiz varsa oldukça etkili olabilir. Aspose.Cells API'sini kullanarak bir sayfa için arka plan resmi ayarlayabilirsiniz.

{{% /alert %}} 

## **Microsoft Excel'de Sayfa Arka Planını Ayarlama**

Microsoft Excel'de bir sayfanın arka plan görüntüsünü ayarlamak için (örneğin, Microsoft Excel 2019 için):

1. **Sayfa Düzeni** menüsünden **Sayfa Ayarı** seçeneğini bulun ve ardından **Arka Plan** seçeneğine tıklayın.
1. Tablonun arka plan resmini ayarlamak için bir resim seçin.

   **Tablo arka planı ayarlama**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Aspose.Cells for Node.js via C++ ile Sayfa Arka Planı ayarlama**

Aşağıdaki kod, bir akıştaki bir resim kullanarak arka plan resmini ayarlar.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const backgroundImagePath = path.join(dataDir, "background.jpg");

// Create a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Set the background image for the worksheet.
sheet.setBackgroundImage(fs.readFileSync(backgroundImagePath).buffer);

// Save the Excel file
workbook.save("outputBackImageSheet.xlsx");

// Save the HTML file
workbook.save("outputBackImageSheet.html", AsposeCells.SaveFormat.Html);
```

## İlgili Makaleler

- [ODS Dosyalarında Arkaplanla Çalışma](/cells/tr/nodejs-cpp/working-with-background-in-ods-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}
