---
title: Node.js ve C++ kullanarak ActiveX Kontrolünü Kaldır
linktitle: AktifX Kontrolü Kaldır
type: docs
weight: 1000
url: /tr/nodejs-cpp/remove-activex-control/
description: Aspose.Cells for Node.js via C++ kullanarak çalışma kitaplarından ActiveX kontrolünü nasıl kaldıracağınızı öğrenin.
---

## **ActiveX Kontrolü Kaldırma**

Aspose.Cells, dosyalardan ActiveX Kontrolü kaldırma yeteneği sağlar. Bunun için API [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--) yöntemini sunar. Aşağıdaki kod parçası, [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#removeActiveXControl--) yöntemini kullanarak ActiveX Kontrolü kaldırmayı gösterir.

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create a workbook
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleUpdateActiveXComboBoxControl.xlsx"));

// Access first shape from first worksheet
const shape = wb.getWorksheets().get(0).getShapes().get(0);

// Access ActiveX ComboBox Control and update its value
if (shape.getActiveXControl() != null) {
// Remove Shape ActiveX Control
shape.removeActiveXControl();
}

// Save the workbook
wb.save(path.join(outputDir, "RemoveActiveXControl_our.xlsx"));
``` 

{{< app/cells/assistant language="nodejs-cpp" >}}
