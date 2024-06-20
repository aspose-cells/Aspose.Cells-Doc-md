---
title: ワークシートへのアクセス
type: docs
weight: 10
url: /ja/net/aspose-cells-griddesktop/access-worksheet/
keywords: GridDesktop、worksheet
description: この記事では、GridDesktopでワークシートを操作する方法について紹介します。
---

{{% alert color="primary" %}} 

ワークシートはExcelファイルの中でも重要な部分です。 実際、Excelファイルは1つ以上のワークシートで構成されています。 各ワークシートは最大で65,536行と256列で構成されています。 Excelファイルでデータを保持するのはワークシートです。

Aspose.Cells.GridDesktopは既存のExcelファイルを作成および操作できるため、Aspose.Cells.GridDesktopを使用してワークシートにアクセスする方法もあります。 このトピックではその手順について説明します。

{{% /alert %}} 
## **ワークシートのインデックスを使用する**
開発者は、例に示されているように任意のワークシートのワークシートインデックスを使用して、Aspose.Cells.GridDesktopのインスタンスにアクセスできます。このアプローチは、Excelファイル内の複数のワークシートを反復処理するために適しています。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **ワークシートの名前を使用する**
ワークシートの名前がわかっている場合、次に示すようにその名前を使用してワークシートにアクセスすることができます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **アクティブワークシートへのアクセス**
Excelファイルには複数のワークシートが含まれる可能性があります。ユーザーが作業しているワークシートはアクティブワークシートと呼ばれます。アクティブシートにアクセスすることができます。

アクティブワークシートへのアクセスには、Aspose.Cells.GridDesktopが2つのアプローチを提供します
### **ActiveSheetIndexプロパティを使用する**
Aspose.Cells.GridDesktopコントロールを使用してアクティブなワークシートにアクセスする方法の1つは、GridDesktopコントロールのActiveSheetIndexプロパティを使用することです。このプロパティを使用すると、Aspose.Cells.GridDesktopコントロール内のアクティブなワークシートのインデックスを取得することができます。そのインデックスを使用して、次に示すようにワークシートにアクセスすることができます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **GetActiveWorksheetメソッドを使用する**
もう一つのアプローチは、GridDesktopコントロールのGetActiveWorksheetメソッドを呼び出すことです。このメソッドは、Aspose.Cells.GridDesktopコントロールで現在アクティブなワークシートの参照を提供します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
