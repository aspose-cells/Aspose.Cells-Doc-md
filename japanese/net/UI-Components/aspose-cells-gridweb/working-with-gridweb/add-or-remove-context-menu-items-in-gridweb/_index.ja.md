---
title: GridWeb でコンテキスト メニュー項目を追加または削除する
type: docs
weight: 130
url: /ja/net/add-or-remove-context-menu-items-in-gridweb/
---
{{% alert color="primary" %}} 

ASP.NET マークアップまたは .NET コードを使用して、コンテキスト メニュー項目を追加できます。 .NET コードを使用してコンテキスト メニュー項目を削除することもできます。これらの目的には、GridWeb.CustomCommandButtons.Add() および GridWeb.CustomCommandButtons.Remove() または RemoveAt() メソッドを使用してください。

{{% /alert %}} 
## **ASP.NET マークアップを使用してコンテキスト メニュー項目を追加する**
次の ASP.NET マークアップは、GridWeb にコンテキスト メニュー項目を追加します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



上記のコンテキスト メニュー項目で GridWeb を作成する完全な ASP.NET マークアップを次に示します。 OnCustomCommand="GridWeb1_CustomCommand" 属性に注意してください。コンテキスト メニュー項目がクリックされたときに呼び出されるイベント ハンドラ名です。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



上記の ASP.NET マークアップを使用して追加した後のコンテキスト メニュー項目は次のようになります。

![todo:画像_代替_文章](add-or-remove-context-menu-items-in-gridweb_1.png)

これは、コンテキスト メニュー項目がクリックされたときに実行されるイベント ハンドラー コードです。コードは最初にコマンド名をチェックし、コマンドと一致する場合は、アクティブな GridWeb ワークシートのセル A1 にテキストを追加し、最初の列幅を 40 単位に設定してテキストを表示します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


これは、コンテキスト メニュー項目をクリックしたときの GridWeb の外観です。

![todo:画像_代替_文章](add-or-remove-context-menu-items-in-gridweb_2.png)
## **コードを使用して Aspose.Cells.GridWeb にコンテキスト メニュー項目を追加する**
このコードは、コードを使用して GridWeb 内にコンテキスト メニュー項目を追加する方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **コードを使用して Aspose.Cells.GridWeb のコンテキスト メニュー項目を削除する**
このコードは、CustomCommandButtons.Remove() および CustomCommandButtons.RemoveAt() メソッドを使用してコンテキスト メニュー項目を削除する方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
