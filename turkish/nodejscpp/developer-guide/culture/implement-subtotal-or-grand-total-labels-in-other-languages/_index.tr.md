---  
title: Node.js ve C++ kullanarak Diğer Dillerde Alt Toplam veya Genel Toplam Etiketleri uygulayın  
linktitle: Diğer Dillerde Alt Toplam veya Genel Toplam Etiketi Uygula  
type: docs  
weight: 50  
url: /tr/nodejs-cpp/implement-subtotal-or-grand-total-labels-in-other-languages/  
---  

## **Olası Kullanım Senaryoları**  

Bazen, Çin, Japon, Arapça, Hintçe gibi İngilizce olmayan dillerde alt toplam ve genel toplam etiketlerini göstermek istersiniz. Aspose.Cells for Node.js via C++, bunu [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) sınıfını ve [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/) özelliğini kullanarak yapmanıza olanak tanır. Bu konuda [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) sınıfının nasıl kullanılacağına ilişkin makaleye bakabilirsiniz.  

- [Özel Ara Toplamların Kullanımı ve Pasta Grafiği Etiketleri İçin GlobalizationSettings Sınıfını Kullanma](/cells/tr/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)  

## ** Diğer Dillerde Alt Toplam veya Genel Toplam Etiketi Uygula**  

Aşağıdaki örnek kod, [örnek excel dosyasını](5115151.xlsx) yükler ve Çin dilinde alt toplam ve genel toplam isimlerini uygular. Lütfen, bu kodun oluşturduğu [çıktı Excel dosyasını](5115152.xlsx) referans olarak kontrol edin. Önce [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) sınıfını oluşturur ve kodumuzda kullanırız.  

```javascript
const AsposeCells = require("aspose.cells.node");

class GlobalizationSettingsImp extends AsposeCells.GlobalizationSettings {
// This function will return the sub total name
getTotalName(functionType) {
return "Chinese Total - 可能的用法";
}

// This function will return the grand total name
getGrandTotalName(functionType) {
return "Chinese Grand Total - 可能的用法";
}
}
```  

Şimdi yukarıda oluşturulan sınıfı aşağıdaki gibi kodda kullanın:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Set the globalization setting to change subtotal and grand total names
const globalizationSettings = new AsposeCells.GlobalizationSettings();
workbook.getSettings().setGlobalizationSettings(globalizationSettings);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Apply subtotal on A1:B10
const cellArea = AsposeCells.CellArea.createCellArea("A1", "B10");
worksheet.getCells().subtotal(cellArea, 0, AsposeCells.ConsolidationFunction.Sum, [2, 3, 4]);

// Set the width of the first column
worksheet.getCells().setColumnWidth(0, 40);

// Save the output excel file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
