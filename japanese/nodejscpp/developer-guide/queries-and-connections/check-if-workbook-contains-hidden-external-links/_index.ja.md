---  
title: Node.js経由でC++を使ってWorkbookに隠された外部リンクが含まれているかどうかを確認する方法  
linktitle: ワークブックに非表示の外部リンクが含まれているかどうかを確認  
type: docs  
weight: 230  
url: /ja/nodejs-cpp/check-if-workbook-contains-hidden-external-links/  
description: Aspose.Cells for Node.js via C++を使って、ワークブックに隠された外部リンクがあるかどうかを確認する方法を学びます。  
---  

## **可能な使用シナリオ**  
時折、ワークブックには隠されていてMicrosoft Excelで閲覧できない外部リンクが含まれていることがあります。Aspose.Cellsは、表示されているか隠されているかに関わらず、すべての外部リンクを取得します。ただし、[ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--)プロパティを使用して、外部リンクが表示されているかどうかを確認できます。

## **ワークブックに非表示の外部リンクが含まれる [ソースExcelファイル](5115413.xlsx) をロードする以下のサンプルコードでは、Microsoft Excelで表示されない非表示の外部リンクが含まれています。 [ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) および [ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) プロパティを出力した後、[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible) プロパティを出力します。以下のコンソール出力では、すべての外部リンクが非表示であることがわかります。**  
次のサンプルコードは、隠された外部リンクを含む[ソースExcelファイル](5115413.xlsx)をロードします。これらのリンクはMicrosoft Excelでは閲覧できませんが、ワークブック内に存在しています。[ExternalLink.getDataSource()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#getDataSource--)と[ExternalLink.isReferred()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isReferred--)プロパティを出力した後、[ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--)プロパティも出力します。以下のコンソール出力では、その外部リンクはすべて不可視であることがわかります。

### **サンプルコード**  
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

### **コンソール出力**  
与えられた [サンプルExcelファイル](5115413.xlsx) で上記のサンプルコードを実行した場合の、コンソール出力は次のとおりです。

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
{{< app/cells/assistant language="nodejs-cpp" >}}
