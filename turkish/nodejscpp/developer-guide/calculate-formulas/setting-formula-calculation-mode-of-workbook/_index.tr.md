---  
title: Node.js kullanarak C++ ile Çalışma Kitabının Formül Hesaplama Modunu Ayarlama  
linktitle: Çalışbook un Formül Hesaplama Modunu Ayarlama  
description: Bu makale, Microsoft Excel de Çalışma Kitabının formül hesaplama modunu Aspose.Cells for Node.js via C++ ile nasıl ayarlayacağınızı anlatmaktadır. Var olan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemi kullanarak formül hesaplama modunu belirleyebilir ve sonucu alabilirsiniz. Son olarak, değiştirilen Excel dosyasını diske kaydederiz.  
keywords: Aspose.Cells, Excel, çalışma kitabı, formül hesaplama modu, ayarlar, C++ ile Node.js  
type: docs  
weight: 110  
url: /tr/nodejs-cpp/setting-formula-calculation-mode-of-workbook/  
---  

{{% alert color="primary" %}}  
Microsoft Excel, formül hesaplama modunu, yani formüllerin nasıl hesaplandığını ayarlamanıza izin verir. Üç olası değer bulunmaktadır:  

- Otomatik - bir şey değiştirildiğinde ve her bir çalışma kitabı açıldığında yeniden hesapla.  
- Otomatik, veri tabloları hariç - bir şey değiştirildiğinde yeniden hesapla, ancak veri tablolarını dışarıda bırak.  
- Manuel - kullanıcı açıkça istediğinde (F9 veya CTRL+ALT+F9'a basarak) veya çalışma kitabı kaydedildiğinde sadece yeniden hesapla.  
{{% /alert %}}  

Microsoft Excel'de formül hesaplama modunu ayarlamak için:  

1. **Formüller**'i seçin, ardından **Hesaplama Seçenekleri**'ni seçin.  
1. Seçeneklerden birini seçin.  

Aspose.Cells for Node.js via C++ ayrıca [**FormulaSettings.getCalculationMode()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getCalculationMode--) modu özelliği kullanılarak **Formül Hesaplama Modu** nu ayarlamanıza izin verir. Aşağıdaki değerlerden biri olan [**CalcModeType**](https://reference.aspose.com/cells/nodejs-cpp/calcmodetype) enum'una atayabilirsiniz:  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Set the Formula Calculation Mode to Manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
