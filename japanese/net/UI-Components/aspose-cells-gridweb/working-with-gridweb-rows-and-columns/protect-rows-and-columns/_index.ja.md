---
title: 行と列を保護する
type: docs
weight: 60
url: /ja/net/protect-rows-and-columns/
---
{{% alert color="primary" %}} 

このトピックでは、エンド ユーザーが実行するあらゆる種類のアクションから行と列のセルを保護するためのいくつかの手法について説明します。開発者は、行と列のセルを読み取り専用にするか、Aspose.Cells.GridWeb のコンテキスト メニュー オプションを制限するという 2 つの手法を使用して、この保護を実装できます。これらの手法の両方について、例を使用して以下で説明します。

{{% /alert %}} 
## **行と列で Cells を保護する**
### **行と列を読み取り専用にする**
ワークシートの行と列を保護する 1 つの方法は、セルを読み取り専用にすることです。その後、エンド ユーザーはそれらを削除できません。

行と列を読み取り専用にするには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. コレクション内の GridWorksheet にアクセスします。
1. 行または列の目的のセルを読み取り専用に設定します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **コンテキスト メニュー オプションの制限**
Aspose.Cells.GridWeb は、エンド ユーザーがコントロールで操作を実行するために使用できるコンテキスト メニューを提供します。このメニューには、セル、行、および列を操作するための多くのオプションが用意されています。

**完全なコンテキスト オプション** 

![todo:画像_代替_文章](protect-rows-and-columns_1.png)

コンテキスト メニューで使用できるオプションを制限することで、行と列に対するあらゆる種類のクライアント側操作を制限することができます。これは、GridWeb コントロールの EnableClientColumnOperations プロパティと EnableClientRowOperations プロパティを false に設定することで実行できます。 GridWeb コントロールの EnableClientFreeze プロパティを false に設定することで、ユーザーが行と列をフリーズするのを制限することもできます。

**行と列のオプションを制限した後のコンテキスト メニュー** 

![todo:画像_代替_文章](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
