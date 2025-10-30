---  
title: 共有ブックの修正履歴日数を更新して保持する方法（履歴ログの保持期間を維持） Node.jsとC++を使用して  
linktitle: 共有ワークブックのリビジョンログの履歴を保持する日数を更新  
type: docs  
weight: 80  
url: /ja/nodejs-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/  
description: Aspose.Cells for Node.js via C++を使用して、共有ワークブックで修正履歴の保存期間（日数）を更新する方法を学びます。  
---  

## **可能な使用シナリオ**

ワークブックを共有すると、以下のスクリーンショットのように「***変更履歴をN日間保持***」というオプションが表示されます。Aspose.Cells for Node.js via C++の [**WorksheetCollection.getDaysPreservingHistory()**](https://reference.aspose.com/cells/nodejs-cpp/revisionlogcollection/#getDaysPreservingHistory--) プロパティを使用して、履歴を保持する日数を更新できます。

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **共有ブックにおける修正履歴の歴史を保持したまま日数を更新する**

次のサンプルコードは空のワークブックを作成し、それを共有し、履歴を30日通常のところ7日に維持する日数で更新します。コードによって生成された[出力Excelファイル](60489773.xlsx)を参照してください。

## **サンプルコード**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Share the workbook
workbook.getSettings().setShared(true);

// Update DaysPreservingHistory of RevisionLogs
workbook.getWorksheets().getRevisionLogs().setDaysPreservingHistory(7);

// Save the workbook
workbook.save("outputShared_DaysPreservingHistory.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
