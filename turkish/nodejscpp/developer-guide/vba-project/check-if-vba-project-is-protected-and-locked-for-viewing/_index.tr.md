---
title: VBA Projesinin Korumalı ve Görüntülemeye Kapalı Olduğunu Node.js ile Kontrol Edin
linktitle: C# da Bir Çalışbookun VBA Projesinin Korunup Görüntüleme İçin Kilitli Olup Olmadığını Kontrol Et
type: docs
weight: 30
url: /tr/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Aspose.Cells for Node.js via C++ kullanarak bir Excel dosyasındaki VBA projesinin korumalı ve görüntülemeye kapalı olup olmadığını nasıl kontrol edeceğinizi öğrenin.
---

## Node.js'de VBA Projesinin Korunduğunu ve Görüntülemeye Kilitli olup olmadığını Kontrol Etme

 Aspose.Cells, bir Excel dosyasının VBA (Visual Basic for Applications) Projesinin korunduğunu ve görüntülemeye kilitlendiğini kontrol etmenize olanak tanır. Bunun için API, [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--) özelliği sağlar. Eğer korundusa, [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--) özelliği **true** döner.

## **Örnek Kod**

Aşağıdaki örnek kod, [örnek Excel dosyasını](43352065.xlsm) yükler ve Excel dosyasının VBA (Visual Basic for Applications) Projesinin korunduğunu ve görüntülemeye kilitli olup olmadığını kontrol eder. Lütfen referans için Konsol Çıktısına da bakınız.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const filePath = path.join(dataDir, "sampleCheckifVBAProjectisProtected.xlsm");
const workbook = new AsposeCells.Workbook(filePath);

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Whether "Lock project for viewing" is true or not.
console.log("Is VBA Project Locked for Viewing: " + vbaProject.getIslockedForViewing());
```

## **Konsol Çıktısı**

Sağlanan [örnek Excel dosyası](43352065.xlsm) ile yukarıdaki örnek kodun çalıştırılması durumunda elde edilen konsol çıkışı budur.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
