---
title: Aspose.Cells for Node.js via C++ kullanarak ActiveX Kontrolleri Ekle
linktitle: Aspose.Cells Kullanarak AktifX Kontrolleri Ekleme
type: docs
weight: 260
url: /tr/nodejs-cpp/add-activex-controls-using-aspose-cells/
description: Aspose.Cells for Node.js via C++ kullanarak bir çalışma sayfasına ActiveX kontrolleri nasıl eklenir öğrenin. 
---

{{% alert color="primary" %}}

 Aspose.Cells kullanarak [**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-) yöntemiyle ActiveX kontrolleri ekleyebilirsiniz. Bu yöntem, bir parametre [**ControlType**](https://reference.aspose.com/cells/nodejs-cpp/controltype/) alır ve bu, hangi tür ActiveX kontrolünün bir çalışma sayfasına eklenmesi gerektiğini belirtir. Aşağıdaki değerleri içerir.

- ControlType.CheckBox
- ControlType.ComboBox
- ControlType.CommandButton
- ControlType.Image
- ControlType.Label
- ControlType.ListBox
- ControlType.RadioButton
- ControlType.ScrollBar
- ControlType.SpinButton
- ControlType.TextBox
- ControlType.ToggleButton
- ControlType.Unknown

ActiveX kontrolü şekil koleksiyonuna eklendikten sonra, [**Shape.getActiveXControl()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) özelliği aracılığıyla ActiveX kontrol nesnesine erişebilir ve ardından çeşitli özelliklerini ayarlayabilirsiniz.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells kullanarak Toggle Button AktifX Kontrolü ekler.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const sheet = wb.getWorksheets().get(0);

// Add Toggle Button ActiveX Control inside the Shape Collection
const s = sheet.getShapes().addActiveXControl(AsposeCells.ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

// Access the ActiveX control object and set its linked cell property
const c = s.getActiveXControl();
c.setLinkedCell("A1");

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "AddActiveXControls_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
