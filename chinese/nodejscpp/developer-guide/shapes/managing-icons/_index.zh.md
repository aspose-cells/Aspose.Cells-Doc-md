---  
title: 在Node.js中通过C++向工作表中添加图标  
linktitle: 管理图标  
type: docs  
weight: 100  
url: /zh/nodejs-cpp/insert-svg-to-excel/  
---  

## 在Aspose.Cells for Node.js via C++中向工作表添加图标

如果您需要使用[Aspose.Cells](https://products.aspose.com/cells/)在Excel文件中添加'图标'，那么本文档可以为您提供一些帮助。

对应于插入图标操作的Excel界面如下：

![](1.png)

- 选择要插入到工作表中的图标的位置
- 左键单击*插入*->*图标*
- 在打开的窗口中，选择上图中红色矩形所示的图标
- 左键单击 *插入*，它将被插入到Excel文件中。

效果如下:

![](2.png)

这里，我们准备了 *示例代码* 来帮助你使用 [Aspose.Cells](https://products.aspose.com/cells/) 插入图标。还包括必要的 [示例文件](sample.xlsx) 和图标 [资源文件](icon.zip)。我们使用Excel界面插入了一个图标，与 [资源文件](icon.zip) 在 [示例文件](sample.xlsx) 中具有相同的显示效果。

### Node.js

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Read icon resource file data
const fileName = path.join(dataDir, "icon.svg");
const bytes = fs.readFileSync(fileName).buffer;

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the icon to the worksheet
sheet.getShapes().addIcons(3, 0, 7, 0, 100, 100, bytes, null);

// Set a prompt message
const c = sheet.getCells().get(8, 7);
c.putValue("Insert via Aspose.Cells");
const s = c.getStyle();
s.getFont().setColor(AsposeCells.Color.Blue);
c.setStyle(s);

// Save. You can check your icon in this way.
workbook.save("sample2.xlsx", AsposeCells.SaveFormat.Xlsx);
```

当您在项目中执行上述代码时，将获得以下结果:

![](3.png)  

{{< app/cells/assistant language="nodejs-cpp" >}}
