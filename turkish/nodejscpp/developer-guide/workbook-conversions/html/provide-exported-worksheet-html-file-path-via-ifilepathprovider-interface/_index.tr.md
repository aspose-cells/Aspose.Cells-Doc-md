---
title: Node.js kullanarak C++ ile IFilePathProvider arayüzü aracılığıyla Dışa Aktarılan Sayfa HTML dosya yolunu sağlama
linktitle: IFilePathProvider arayüzü aracılığıyla dışa aktarılan çalışma sayfası HTML dosyası yolunu sağlayın
type: docs
weight: 70
url: /tr/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Olası Kullanım Senaryoları**
Birden fazla sayfaya sahip Excel dosyanız olduğunu ve her sayfayı ayrı HTML dosyasına dışa aktarmak istediğinizi varsayın. Eğer herhangi bir sayfada diğer sayfalara bağlantılar varsa, bu bağlantılar dışa aktarılmış HTML'de bozuk olur. Bu sorunu çözmek için, Aspose.Cells for Node.js via C++, [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider) arayüzünü sunar ve bu arayüzü uygulayarak bozuk bağlantıları düzeltebilirsiniz.

## **IFilePathProvider arayüzü aracılığıyla dışa aktarılan çalışma sayfası HTML dosya yolunu sağlayın**
Aşağıdaki kodda kullanılan örnek Excel dosyasını [indirin](5115213.zip) ve dışa aktarılmış HTML dosyalarını alın. Tüm dosyalar geçici dizin içerisindedir. Bunu C: sürücüsüne çıkartın. Bu durumda C:\Temp dizini olur. Ardından, Sheet1.html dosyasını tarayıcıda açın ve içindeki iki bağlantıya tıklayın. Bu bağlantılar, C:\Temp\OtherSheets dizini içindeki bu iki dışa aktarılmış HTML çalışma sayfasına işaret eder.

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

Aşağıdaki ekran görüntüsü, C:\Temp\Sheet1.html ve bağlantılarının nasıl göründüğünü göstermektedir

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Aşağıdaki ekran görüntüsü HTML kaynağını gösterir. Gördüğünüz gibi, bağlantılar artık C:\Temp\OtherSheets dizinine atıfta bulunuyor. Bu, [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider) arayüzü kullanılarak gerçekleştirildi.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **Örnek Kod**
Lütfen C:\Temp dizininin sadece örnekleme amaçlı olduğunu unutmayın. İstediğiniz herhangi bir dizini kullanabilir ve içerisine [örnek Excel dosyasını](5115211.xlsx) koyabilirsiniz. Ardından, sağlanan örnek kodu çalıştırın. Bu, diziniz içinde bir OtherSheets alt dizini oluşturacak ve içindeki ikinci ve üçüncü çalışma sayfalarını HTML olarak dışa aktaracaktır. Lütfen kodda bulunan dirPath değişkenini değiştirerek kendi tercih ettiğiniz dizine göre ayarlayın.

{{% alert color="primary" %}} 

Örnek kod, yalnızca Aspose.Cells lisansı ayarlandığında çalışacaktır. Lisansı ayarlamadan kodu çalıştırmaya çalışırsanız, sonsuz döngüye girer. Bu yüzden, lisansın ayarlandığını kontrol eden ve ayarlanmadığında mesaj yazdırıp durduracak bir kod ekledik. Lisans satın alabilir veya Aspose.Purchase takımıyla 30 günlük geçici lisans talep edebilirsiniz.

{{% /alert %}} 

Lütfen, bu satırları kodda yorum satırı haline getirirseniz, Sheet1.html içindeki bağlantılar bozulur ve tıklandığında Sheet2.html veya Sheet3.html açılmaz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// Implementation of IFilePathProvider interface
class FilePathProvider extends AsposeCells.IFilePathProvider
{
// Constructor
constructor() 
{
super();
}

// Gets the full path of the file by worksheet name when exporting worksheet to html separately.
// So the references among the worksheets could be exported correctly.
getFullName(sheetName) 
{
if (sheetName === "Sheet2")
{
return "file:///" + path.join("OtherSheets", "Sheet2.html");
} 
else if (sheetName === "Sheet3") 
{
return "file:///" + path.join("OtherSheets", "Sheet3.html");
}

return "";
}
}

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
// If you will comment this line, then hyperlinks will be broken
const options = new AsposeCells.HtmlSaveOptions();
options.setFilePathProvider(new FilePathProvider());
```

İşte, sağladığımız [örnek Excel dosyası](5115211.xlsx) ile çalıştırabileceğiniz tam örnek kod.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Implementation of IFilePathProvider interface
class FilePathProvider extends AsposeCells.IFilePathProvider
{
// Constructor
constructor() 
{
super();
}

// Gets the full path of the file by worksheet name when exporting worksheet to html separately.
// So the references among the worksheets could be exported correctly.
getFullName(sheetName) 
{
if (sheetName === "Sheet2")
{
return "file:///" + path.join("OtherSheets", "Sheet2.html");
} 
else if (sheetName === "Sheet3") 
{
return "file:///" + path.join("OtherSheets", "Sheet3.html");
}

return "";
}
}

// This is the directory path which contains the sample.xlsx file
const dirPath = path.join(__dirname, "data");

// because Aspose.Cells will always make the warning worksheet as active sheet in Evaluation mode.
//setLicense();

// Check if license is set, otherwise do not proceed
const wb = new AsposeCells.Workbook();
if (!wb.isLicensed()) {
console.log("You must set the license to execute this code successfully.");
} else {
// Test IFilePathProvider interface
testFilePathProvider();
}

function setLicense() {
const licPath = "Aspose.Cells.lic";

const lic = new AsposeCells.License();
lic.setLicense(licPath);

console.log(AsposeCells.CellsHelper.getVersion());
console.debug(AsposeCells.CellsHelper.getVersion());

process.chdir(dirPath);
}

function testFilePathProvider() {
// Create subdirectory for second and third worksheets
const otherSheetsDir = path.join(dirPath, "OtherSheets");
if (!fs.existsSync(otherSheetsDir)) {
fs.mkdirSync(otherSheetsDir);
}

// Load sample workbook from your directory
const wb = new AsposeCells.Workbook(path.join(dirPath, "Sample_filepath.xlsx"));

// Save worksheets to separate html files
// Because of IFilePathProvider, hyperlinks will not be broken.
for (let i = 0; i < wb.getWorksheets().getCount(); i++)
{
// Set the active worksheet to current value of variable i
wb.getWorksheets().setActiveSheetIndex(i);

// Create html save option
const options = new AsposeCells.HtmlSaveOptions();
options.setExportActiveWorksheetOnly(true);
// If you will comment this line, then hyperlinks will be broken
options.setFilePathProvider(new FilePathProvider());
// Sheet actual index which starts from 1 not from 0
const sheetIndex = i + 1;

let filePath = "";

// Save first sheet to same directory and second and third worksheets to subdirectory
if (i === 0) 
{
filePath = path.join(dirPath, "Sheet1.html");
} 
else 
{
filePath = path.join(otherSheetsDir, `Sheet${sheetIndex}_out.html`);
}

// Save the worksheet to html file
wb.save(filePath, options);
}
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
