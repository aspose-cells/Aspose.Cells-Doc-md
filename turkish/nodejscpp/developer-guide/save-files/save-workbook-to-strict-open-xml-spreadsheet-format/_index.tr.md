---  
title: Node.js kullanarak C++ ile Sıkı Open XML Elektronik Tablo Formatında Çalışma Kitabını Kaydet  
linktitle: Sıkı Açık XML Elektronik Tablo Biçimine Çalışma Kitabını Kaydet  
type: docs  
weight: 150  
url: /tr/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/  
description: Aspose.Cells for Node.js via C++ kullanarak çalışma kitabını Sıkı Open XML Elektronik Tablo formatında nasıl kaydedeceğinizi öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Aspose.Cells for Node.js via C++, çalışma kitabını *Sıkı Open XML Elektronik Tablo* formatında kaydetmenizi sağlar. Bunu yapmak için, [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--) özelliğini sağlar. Değeri [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance) olarak ayarlanırsa, çıktı Excel dosyası Sıkı Open XML Elektronik Tablo formatında kaydedilir.  

## **Sıkı Açık XML Elektronik Tablo Biçimine Çalışma Kitabını Kaydet**  

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--) özelliğinin değerini [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance) olarak ayarlar ve [çıktı Excel dosyası](67338272.xlsx) olarak kaydeder. Çıktı Excel dosyasını Microsoft Excel'de açıp "Farklı Kaydet..." iletişim kutusunu açarsanız, formatını *Sıkı Open XML Elektronik Tablo* olarak göreceksiniz, bu ekran görüntüsünde gösterildiği gibi.  

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook.
const wb = new AsposeCells.Workbook();

// Specify - Strict Open XML Spreadsheet - Format.
wb.getSettings().setCompliance(AsposeCells.OoxmlCompliance.Iso29500_2008_Strict);

// Add message in cell B4 of first worksheet.
const b4 = wb.getWorksheets().get(0).getCells().get("B4");
b4.putValue("This Excel file has Strict Open XML Spreadsheet format.");

// Save to output Excel file.
wb.save("outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
