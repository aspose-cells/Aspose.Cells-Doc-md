---
title: Node.js kullanarak Form Kontrolüne Makro Atama
linktitle: Form Kontrolüne Makro Atama
type: docs
weight: 60
url: /tr/nodejs-cpp/assign-macro-to-form-control/
description: Aspose.Cells for Node.js via C++ kullanarak bir Macro Kodunu Button gibi Form Kontrolüne nasıl atayacağınızı öğrenin. 
keywords: Form Kontrolüne Makro Atama Node.js, Makro Kodunu Form Kontrolüne Node.js, Entegre Makro ve XLSM Node.js ile C++
---

{{% alert color="primary" %}}

Aspose.Cells, Düğme gibi Bir Form Kontrolüne bir Makro Kodu atamanıza izin verir. Lütfen çalışma kitabının içindeki Form Kontrolüne yeni bir Makro Kodu atamak için [**Shape.getMacroName()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getMacroName--) özelliğini kullanın.

{{% /alert %}}

Aşağıdaki örnek kod yeni bir çalışma kitabı oluşturur, bir Makro Kodunu Bir Form Düğmesine atar ve sonucu XLSM formatında kaydeder. Microsoft Excel'de çıktı XLSM dosyasını açtığınızda, aşağıdaki makro kodunu göreceksiniz.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Node.js'de Form Kontrolüne Makro Atama**

İşte Makro Koduyla çıktı XLSM dosyası oluşturmaya örnek kod.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);

const moduleIdx = workbook.getVbaProject().getModules().add(sheet);
const module = workbook.getVbaProject().getModules().get(moduleIdx);
module.setCodes(
"Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub"
);

const button = sheet.getShapes().addButton(2, 0, 2, 0, 28, 80);
button.setPlacement(AsposeCells.PlacementType.FreeFloating);
button.getFont().setName("Tahoma");
button.getFont().setIsBold(true);
button.getFont().setColor(AsposeCells.Color.Blue);
button.setText("Aspose");

button.setMacroName(sheet.getName() + ".ShowMessage");

const outputFilePath = path.join(dataDir, "Output.out.xlsm");
workbook.save(outputFilePath);
```
