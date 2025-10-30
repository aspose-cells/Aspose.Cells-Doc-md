---  
title: Web Uzantıları  Office Eklentileri Node.js ile C++ üzerinden  
linktitle: Web Eklentileri  Ofis Eklentileri  
type: docs  
weight: 130  
url: /tr/nodejs-cpp/web-extensions-office-add-ins/  
---  

Web Eklentileri, Ofis belgelerindeki içerikle etkileşimde bulunarak Ofis uygulamalarını genişletir. Web Eklentileri, kullanıcı deneyimini ve üretkenliği artırmak için Ofis istemcisine ek işlevsellik ekler.

Aspose.Cells, Web Eklentileri ile çalışma kabiliyeti de sunar.

## **Web Eklentisi Ekleme**

Excel'de Web Eklentileri (Office Eklentileri) ekleyebilirsiniz, bunun için **Ekle** sekmesine tıklayın ve sonra **Mağaza**/**Ekle Eklentileri Al** bağlantısını tıklayın. Eklentiler kutusunda, istediğiniz eklentiyi arayın ve ekleyin.

Aspose.Cells, ayrıca [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) ve [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane) sınıflarını kullanarak Web Eklentileri ekleme özelliği sağlar. Aşağıdaki kod örneği, [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) ve [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane) sınıflarını kullanarak bir Excel dosyasına web eklentisi eklemeyi gösterir. Lütfen referans olarak kod tarafından oluşturulan [çıktı Excel dosyasına](89849869.xlsx) bakın.

### **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const outDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook();

const extensions = workbook.getWorksheets().getWebExtensions();
const taskPanes = workbook.getWorksheets().getWebExtensionTaskPanes();

const extensionIndex = extensions.add();
const taskPaneIndex = taskPanes.add();

const extension = extensions.get(extensionIndex);
extension.getReference().setId("wa104379955");
extension.getReference().setStoreName("en-US");
extension.getReference().setStoreType(AsposeCells.WebExtensionStoreType.OMEX);

const taskPane = taskPanes.get(taskPaneIndex);
taskPane.setIsVisible(true);
taskPane.setDockState("right");
taskPane.setWebExtension(extension);

workbook.save(path.join(outDir, "AddWebExtension_Out.xlsx"));
```

## **Web Eklentisi Bilgilerine Erişme**

Aspose.Cells, Excel dosyasındaki Web Eklentileri bilgisine erişim sağlar. Aşağıdaki kod örneği, [örnek Excel dosyasını](89849870.xlsx) yükleyerek web eklentisi bilgisine nasıl ulaşılacağını gösterir. Kod tarafından üretilen konsol çıktısına bakın.

### **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load sample Excel file
const filePath = path.join(sourceDir, "WebExtensionsSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const taskPanes = workbook.getWorksheets().getWebExtensionTaskPanes();

for (let i = 0; i < taskPanes.getCount(); i++) {
const taskPane = taskPanes.get(i);
console.log("Width: " + taskPane.getWidth());
console.log("IsVisible: " + taskPane.isVisible());
console.log("IsLocked: " + taskPane.isLocked());
console.log("DockState: " + taskPane.getDockState());
console.log("StoreName: " + taskPane.getWebExtension().getReference().getStoreName());
console.log("StoreType: " + taskPane.getWebExtension().getReference().getStoreType());
console.log("WebExtension.Id: " + taskPane.getWebExtension().getId());
}
```

### **Konsol Çıktısı**

{{< highlight javascript >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
