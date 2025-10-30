---
title: Node.js ve C++ kullanarak ActiveX ComboBox Kontrolünü Güncelleyin
linktitle: ActiveX ComboBox Kontrolünü Güncelle
type: docs
weight: 170
url: /tr/nodejs-cpp/update-activex-combobox-control/
description: Aspose.Cells for Node.js via C++ kullanarak ActiveX ComboBox Kontrolünün değerlerini nasıl okuyup yazacağınızı öğrenin. 
---

## **Olası Kullanım Senaryoları**
 ActiveX ComboBox Kontrolünün değerlerini Aspose.Cells for Node.js via C++ kullanarak okuyabilir veya yazabilirsiniz. Lütfen ActiveX Kontrolüne [Shape.getActiveXControl()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) özelliği aracılığıyla erişin ve türünü [ActiveXControlBase.getType()](https://reference.aspose.com/cells/nodejs-cpp/activexcontrolbase/#getType--) özelliğiyle kontrol edin, bu değer [ControlType.ComboBox](https://reference.aspose.com/cells/nodejs-cpp/controltype/) olmalı ve ardından onu [ComboBoxActiveXControl](https://reference.aspose.com/cells/nodejs-cpp/comboboxactivexcontrol/) nesnesine dönüştürün, ve çeşitli özelliklerini okuyup değiştirebilirsiniz.

Lütfen aşağıdaki örnek kodda kullanılan [örnek excel dosyasını](5115124.xlsx) indirin.
## **ActiveX ComboBox Kontrolünü Güncelleme**
Aşağıdaki ekran görüntüsü, [örnek excel dosyası](5115124.xlsx) üzerinde örnek kodun etkisini göstermektedir. Görebileceğiniz gibi, AktifX ComboBox değeri "Bu bir combo box kontrolüdür" olarak güncellenmiştir.

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Örnek Kod**
[örnek excel dosyası](5115124.xlsx) içinde bulunan AktifX ComboBox Kontrolünün değerini güncelleyen aşağıdaki örnek kodu takip edin.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SourceFile_activex.xlsx");
// Create a workbook
const wb = new AsposeCells.Workbook(filePath);

// Access first shape from first worksheet
const shape = wb.getWorksheets().get(0).getShapes().get(0);

// Access ActiveX ComboBox Control and update its value
if (shape.getActiveXControl() != null)
{
// Access Shape ActiveX Control
const c = shape.getActiveXControl();

if (c instanceof AsposeCells.ComboBoxActiveXControl)
{
// Type cast ActiveXControl into ComboBoxActiveXControl and change its value
const comboBoxActiveX = new AsposeCells.ComboBoxActiveXControl(c);
comboBoxActiveX.setValue("This is combo box control with updated value.");

}

}

// Save the workbook
const outputFilePath = path.join(dataDir, "OutputFile_out.xlsx");
wb.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
