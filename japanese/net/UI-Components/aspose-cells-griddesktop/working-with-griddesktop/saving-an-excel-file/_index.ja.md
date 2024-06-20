---
title: Excelファイルを保存する
type: docs
weight: 20
url: /ja/net/aspose-cells-griddesktop/save-an-excel-file/
keywords: GridDesktop、save、file
description: この記事では、GridDesktopでファイルを保存する方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktopコントロールを使用すると、新しいExcelファイルを作成するだけでなく、既存のファイルを管理することもできます。しかし、どちらの場合もAspose.Cells.GridDesktopのコンテンツをExcelファイルとして保存する必要があります。したがって、今回は、ユーザーがGridのコンテンツをExcelファイルとして保存する方法について知るための話題です。

{{% /alert %}} 
## **紹介**
Aspose.Cells.GridDesktopコントロールのコンテンツをExcelファイルとして保存するには、Aspose.Cells.GridDesktopは以下のメソッドを提供しています。

1. **ファイルとして保存**
1. **ストリームとして保存**
## **ファイルを保存**
デスクトップアプリケーションを作成し、フォームにGridControlコントロールと2つのボタンを追加します。ボタンのテキストプロパティをそれぞれ **Save as File** と **Save as Stream** に設定してください。
### **ファイルとして保存する**
**Save as File** ボタンのクリックイベントを作成し、以下のコードを中に貼り付けてください。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

重要: Aspose.Cells.GridDesktopコントロールにはSaveToExcelというメソッドも含まれており、これはExcelファイルへのGridデータの保存に使用されます。しかし、このメソッドも現在非推奨となっています。したがって、すべての開発者は、非推奨のものよりも堅牢で効率的なExportExcelFileメソッドを使用することが推奨されています。

{{% /alert %}} 
### **ストリームとして保存する**
開発者がGridのコンテンツをストリーム（例えばMemoryStream）に保存する必要がある場合があります。このタスクを容易にするために、Aspose.Cells.GridDesktopコントロールはGridデータをストリームに保存するのをサポートしています。**Save as Stream** ボタンのクリックイベントを作成し、以下のコードを中に貼り付けてください。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

重要: Microsoft ExcelはExcelシートに最大で65,536行と256列を含めることができます。Aspose.Cells.GridDesktopも同じ標準に従っています。Aspose.Cells.GridDesktopコントロールでは、標準制限を超える行数や列数を作成することができますが、GridデータをExcelファイルに保存する際に例外がスローされます。つまり、Aspose.Cells.GridDesktopを使用してExcelファイルに保存できるのは65,536行と256列に含まれるデータのみです。

{{% /alert %}}
