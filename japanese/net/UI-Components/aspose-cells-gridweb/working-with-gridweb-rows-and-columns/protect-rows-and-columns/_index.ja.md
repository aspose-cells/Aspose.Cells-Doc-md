---
title: 行と列の保護
type: docs
weight: 60
url: /ja/net/aspose-cells-gridweb/protect-rows-and-columns/
keywords: GridWeb,保護
description: この記事では、GridWebで行や列を保護する方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、開発者が行や列のセルをエンドユーザーによるアクションから保護するためのいくつかのテクニックについて説明します。セルを読み取り専用にすることで、削除を防ぐことができます。また、Aspose.Cells.GridWebのコンテキストメニューオプションを制限することで保護を実装することができます。これらのテクニックについては、例を使用して以下で詳しく説明します。

{{% /alert %}} 
## **行と列のセルを保護する**
### **行と列を読み取り専用にする**
ワークシートの行や列を保護する方法の一つは、セルを読み取り専用にすることです。そのため、エンドユーザーがそれらを削除することはできません。

行や列を読み取り専用にするには:

1. Web フォームに Aspose.Cells.GridWeb コントロールを追加します。
1. コレクション内の GridWorksheet にアクセスします。
1. 行または列のセルを読み取り専用に設定します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **コンテキストメニューオプションの制限**
Aspose.Cells.GridWeb は、ユーザーがコントロール上で操作を実行するために使用できるコンテキストメニューを提供します。このメニューには、セル、行、および列を操作するための多くのオプションが用意されています。

**完全なコンテキストオプション** 

![todo:image_alt_text](protect-rows-and-columns_1.png)

コンテキストメニューで利用可能なオプションを制限することで、行や列に対するクライアント側の操作を制限することが可能です。これは、GridWeb コントロールの EnableClientColumnOperations および EnableClientRowOperations プロパティを false に設定することで行うことができます。また、GridWeb コントロールの EnableClientFreeze プロパティを false に設定することで、ユーザーが行や列を固定することを制限することも可能です。

**行と列のオプションを制限した後のコンテキストメニュー** 

![todo:image_alt_text](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
