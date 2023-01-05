---
title: ワークシートへのアクセス
type: docs
weight: 10
url: /ja/net/accessing-worksheet/
---
{{% alert color="primary" %}} 

ワークシートは、Excel ファイルの不可欠な部分です。実際、Excel ファイルは 1 つ以上のワークシートで構成されています。各ワークシートは、最大 65,536 行と 256 列のみで構成できます。 Excelファイルにデータを保持するワークシートです。

Aspose.Cells.GridDesktop は、既存および新規の Excel ファイルを作成および操作できるため、もちろん、Aspose.Cells.GridDesktop を使用してワークシートにアクセスする方法があります。このトピックでは、その方法について説明します。

{{% /alert %}} 
## **ワークシート インデックスの使用**
開発者は、以下の例に示すように、目的のワークシートのワークシート インデックスを使用して、任意のワークシートのインスタンスにアクセスできます。このアプローチは、Excel ファイル内の多数のワークシートを反復処理する場合に適しています。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **ワークシート名の使用**
ワークシートの名前がわかっている場合は、以下に示すように、その名前を使用してワークシートにアクセスできます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **アクティブなワークシートへのアクセス**
Excel ファイルに複数のワークシートが含まれる場合があります。ユーザーが作業している 1 つの htat は、アクティブなワークシートと呼ばれます。アクティブシートにアクセスできます。

アクティブなワークシートにアクセスするために、Aspose.Cells.GridDesktop には 2 つの方法があります。
### **AcriveSheetIndex プロパティの使用**
Aspose.Cells.GridDesktop コントロールを使用してアクティブなワークシートにアクセスする 1 つの方法は、GridDesktop コントロールの ActiveSheetIndex プロパティを使用することです。このプロパティを使用すると、Aspose.Cells.GridDesktop コントロールでアクティブなワークシートのインデックスを取得できます。次に、そのインデックスを使用して、以下に示すように従来の方法でワークシートにアクセスできます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **GetActiveWorksheet メソッドの使用**
もう 1 つの方法は、GridDesktop コントロールの GetActiveWorksheet メソッドを呼び出すことです。このメソッドは、以下に示すように、Aspose.Cells.GridDesktop コントロールで現在アクティブなワークシートの参照を提供します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
