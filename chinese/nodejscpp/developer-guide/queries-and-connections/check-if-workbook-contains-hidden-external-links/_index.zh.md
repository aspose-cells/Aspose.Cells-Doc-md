---  
title: 检查工作簿是否包含隐藏的外部链接，使用Node.js和C++  
linktitle: 检查工作簿是否包含隐藏的外部链接  
type: docs  
weight: 230  
url: /zh/nodejs-cpp/check-if-workbook-contains-hidden-external-links/  
description: 学习如何使用Aspose.Cells for Node.js via C++检查工作簿是否包含隐藏的外部链接。  
---  

## **可能的使用场景**  
有时候，工作簿包含隐藏且在Microsoft Excel中无法查看的外部链接。Aspose.Cells会检索所有外部链接，无论它们是否可见。不过，你可以查看[ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--)属性，判断外部链接是否可见。

## **检查工作簿是否包含隐藏的外部链接**  
以下示例代码加载包含隐藏外部链接的[源Excel文件](5115413.xlsx)。这些链接在Excel中无法查看，但存在于工作簿中。在打印了[ExternalLink.getDataSource()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#getDataSource--)和[ExternalLink.isReferred()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isReferred--)属性后，还会打印[ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--)属性。在下面的控制台输出中，你会看到所有外部链接都不可见。

### **示例代码**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the external link collection of the workbook
const links = workbook.getWorksheets().getExternalLinks();

// Print all the external links and check their IsVisible property
for (let i = 0; i < links.getCount(); i++) {
console.log("Data Source: " + links.get(i).getDataSource());
console.log("Is Referred: " + links.get(i).getIsReferred());
console.log("Is Visible: " + links.get(i).getIsVisible());
console.log();
}
```  

### **控制台输出**  
这是执行给定[源Excel文件](5115413.xlsx)时上述示例代码的控制台输出。

{{< highlight java >}}  
 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls  

Is Referred: True  

Is Visible: False  
{{< /highlight >}}  
