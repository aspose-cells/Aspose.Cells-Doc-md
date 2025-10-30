---
title: Excel’i PDF’ye dönüştürürken Office Eklentilerini Render Edin, Node.js ve C++ kullanarak
linktitle: Excel i PDF e dönüştürürken Office Eklentilerini Oluşturma
type: docs
weight: 100
url: /tr/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Olası Kullanım Senaryoları**

Önceden, Aspose.Cells, Excel dosyası PDF formatına kaydedildiğinde Office Eklentilerini render edemiyordu. Artık Aspose.Cells düzgün şekilde render ediyor. Office Eklentilerini render etmek için herhangi bir özel yöntem veya özellik kullanmanız gerekmez. Sadece Excel dosyanızı PDF’ye kaydedin, Office Eklentileri otomatik olarak render edilir.

## **Excel'i PDF'e dönüştürürken Office Eklentilerini renderla**

Aşağıdaki örnek kod, Office Eklentilerini içeren [örnek Excel dosyasını](60489769.xlsx) kaydeder. Lütfen önceki sürümle (örneğin 17.11) oluşturulan çıktı PDF'yi ve yeni sürümle (örneğin 17.12 ve sonrası) oluşturulan çıktı PDF'yi inceleyin. Önceki sürüm çıktı PDF'si boştur, ancak yeni sürüm çıktı PDF'si Office Eklentisi'ni gösterir.

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderOfficeAdd-Ins.xlsx");
// Load the sample Excel file containing Office Add-Ins
const wb = new AsposeCells.Workbook(filePath);

// Save it to Pdf format
wb.save(`output-${AsposeCells.CellsHelper.getVersion()}.pdf`);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
