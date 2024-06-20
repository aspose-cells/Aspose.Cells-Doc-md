---
title: Excelファイルを開く
type: docs
weight: 10
url: /ja/net/aspose-cells-griddesktop/openg-an-excel-file/
keywords: GridDesktop、ファイルを開く
description: この記事では、GridDesktopでファイルを開く方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells Grid Suiteのユニークな機能の1つは、Excelファイルとの互換性です。このトピックでは、Aspose.Cells.GridDesktopコントロールを使用してWindowsアプリケーションでExcelファイルを開く方法を実演します。

{{% /alert %}} 
## **紹介**
Aspose.Cells.GridDesktopを使用してExcelファイルを開くには、GridDesktopコントロールを含むデスクトップアプリケーションを作成する必要があります。WindowsフォームにAspose.Cells.GridDesktopコントロールを追加する方法がわからない場合は、[Aspose.Cells.GridDesktopの使用方法](/cells/ja/net/how-to-use-aspose-cells-griddesktop/)を参照してください。

Aspose.Cells.GridDesktopは、Excelファイルを開くための次の異なる方法を提供します。

1. ファイルから開く
1. CSVファイルを開く
1. ストリームから開く
## **Excelファイルを開く**
この例では、デスクトップアプリケーションを作成し、以下の操作を行います。

- フォームにGridControlコントロールを追加します。
- 以下のテキストプロパティを設定したボタンを3つ追加します:
  - **Excelファイルを開く**
  - **CSVファイルを開く**
  - **ストリームから開く**
### **ファイルから開く**
Excelファイルの内容をAspose.Cells.GridDesktopコントロールにロードするには、コントロールのメソッドを呼び出してExcelファイルのパスを指定する必要があります。その後、Aspose.Cells.GridDesktopコントロールは指定されたパスからファイルを自動的に見つけてその内容を表示します。Excelファイルの内容をロードするコードスニペットは以下の例に示されています。**Excelファイルを開く**ボタンのClickイベントを作成し、以下のコードを貼り付けます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


上記のコードスニペットは、開発者が任意の方法で使用できます。たとえば、Windowsフォームの読み込み時に自動的にExcelファイルを読み込みたい場合は、このコードをフォームの読み込みイベントの下に追加することができます。
### **CSVファイルを開く**
Aspose.Cells.GridDesktopコントロールはCSVファイルの読み込みもサポートしています。**Open CSV File**ボタンのクリックイベントを作成し、以下のコードを中に貼り付けてください。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **ストリームから開く**
上記のディスカッションでファイルパスを使用してExcelファイルを読み込むことについて説明しましたが、Aspose.Cells.GridDesktopコントロールはストリームからExcelファイルを読み込むこともサポートしています。**Open from Stream**ボタンのクリックイベントを作成し、以下のコードを中に貼り付けてください。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



ファイルをストリームとして使用することは、このアプローチによりファイルアクセスや共有違反の問題を防ぐためにより良いアプローチです。このアプローチにより、ストリームを閉じることでファイルへのすべての接続を確実に閉じることができます。

{{% alert color="primary" %}} 

重要: Aspose.Cells.GridDesktopコントロールにはLoadFromExcelというメソッドも含まれており、これはExcelファイルの内容をGridに読み込むために使用されます。しかし、このメソッドは現在非推奨となっています。したがって、すべての開発者は、非推奨のものよりも堅牢で効率的なImportExcelFileメソッドを使用することが推奨されています。

{{% /alert %}}
