---  
title: Excel de uyumluluk denetleyicisini devre dışı bırakmak için Node.js kullanın  
linktitle: Excel de Uyumluluk Denetimini Devre Dışı Bırakma  
type: docs  
weight: 170  
url: /tr/nodejs-cpp/disable-compatibility-checker-in-excel/  
description: Aspose.Cells for Node.js via C++ API si aracılığıyla uyumluluk denetleyicisini devre dışı bırakmayı öğrenin.  
keywords: Node.js kullanarak Uyumluluk Denetleyicisini Devre Dışı Bırakın, Excel Uyumluluk Denetleyicisini Node.js de Devre Dışı Bırakma, Workbook ta Uyumluluk Denetleyicisini Devre Dışı Bırakın.  
---  

## Node.js'de Excel Çalışma Sayfalarında Uyumluluk Denetleyicisini Devre Dışı Bırakma  

{{% alert color="primary" %}}  
Microsoft Excel'in Uyumluluk Denetçisi, bir dosyayı önceki bir dosya biçiminde kaydedildiğinde işlevsellik sorunlarına veya sadelik kaybına neden olabilecek özellikleri tespit eder. Uyumluluk Denetçisi, Microsoft Office Excel 2007 ve Microsoft Excel 2010'un bir özelliğidir.  

Excel 2007 veya 2003'ten Excel 2007 veya 2010'a kaydederken, Uyumluluk Denetçisi, daha önceki sürüm tarafından desteklenmeyen özellikleri içeren bir dosya olup olmadığını kontrol etmek için çalışma kitabını tarar. Uyumluluk sorunları hakkında kararlar vermenize yardımcı olmak için, Uyumluluk Denetçisi, seçenekleri içeren iletişim kutuları görüntüler. Ayrıca, çalışma kitabındaki herhangi bir sorun hakkında bir rapor oluşturmak veya özelliği devre dışı bırakmak için de kullanılabilir.  

Bazen, belirli bir elektronik tablo için Uyumluluk Denetleyicisini devre dışı bırakmanız gerekebilir. Aspose.Cells API'leri ile bunu programlı olarak yapabilirsiniz, böylece kullanıcılar manuel olarak Microsoft Excel'de dosyayı yeniden kaydettiklerinde Uyumluluk Denetleyicisi ileti kutusu nedeniyle hayal kırıklığı yaşamaz veya karışıklık yaşamazlar.  
{{% /alert %}}  

## **Microsoft Excel'de Uyumluluk Denetleyicisini Nasıl Devre Dışı Bırakılır**  

Microsoft Excel'de Uyumluluk Denetçisini devre dışı bırakmak için (örneğin Microsoft Excel 2007/2010):  

- (Excel 2007) Office düğmesine tıklayın, **Hazırla**'yı tıklayın, ardından **Uyumluluk Denetleyicisini Çalıştır**'ı tıklayın ve **Bu çalışma kitabını kaydederken uyumluluğu kontrol et** seçeneğini temizleyin.  
- (Excel 2010) Dosya sekmesine tıklayın, sonra **Bilgi**'ye tıklayın, **Sorunları kontrol et**'i tıklayın, **Uyumluluğu Kontrol Et**'i tıklayın ve son olarak **Bu çalışbook'u kaydederken uyumluluğu kontrol et** seçeneğini temizleyin.  

## **Aspose.Cells API'ları kullanarak Uyumluluk Denetleyicisini Nasıl Devre Dışı Bırakılır**  

Microsoft Excel'in Uyumluluk Denetleyicisini devre dışı bırakmak için [**Workbook.getCheckCompatibility()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCheckCompatibility--) özelliğini **false** olarak ayarlayın.  

### **Kod Örnekleri**  

Aşağıdaki kod örnekleri, Aspose.Cells for Node.js via C++ ile Uyumluluk Denetleyicisini nasıl devre dışı bırakacağınızı gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Disable the compatibility checker
workbook.getSettings().setCheckCompatibility(false);

const outputFilePath = path.join(dataDir, "Output_BK_CompCheck.out.xlsx");
// Saving the Excel file
workbook.save(outputFilePath);
```  

