---
title: Visual Studio での作業
type: docs
weight: 20
url: /ja/net/working-with-visual-studio/
---
{{% alert color="primary" %}} 

このトピックでは、Visual Studio.NET 2005 を使用して ASP.NET アプリケーションで Aspose.Cells.GridWeb を使用する方法について説明します。このトピックは、Aspose.Cells.GridWeb を使用する初心者レベルの開発者に役立ちます。

{{% /alert %}} 
## **Visual Studio 2013 を使用した Aspose.Cells.GridWeb の操作**
このトピックでは、Visual Studio 2013 でサンプル Web サイトを作成して、Aspose.Cells.GridWeb を使用する方法を示します。プロセスはステップに分かれています。
### **ステップ 1: 新しい Web サイトを作成する**
1. Visual Studio 2013 を開きます。
1. から**ファイル**メニュー、選択**新しいメニュー**、 それから**Webサイト**. 

![todo:画像_代替_文章](working-with-visual-studio_1.png)


[新しい Web サイト] ダイアログが開きます。

1. 選択する**ASP.NET Web フォーム サイト**Visual Studio にインストールされたテンプレートから。
1.  Web サイトの場所として HTTP モードを選択します。

![todo:画像_代替_文章](working-with-visual-studio_2.png)




1.  Web サイト ファイルを作成して保存する場所を指定します。
 1. クリック**ブラウズ**[新しい Web サイト] ダイアログで。

![todo:画像_代替_文章](working-with-visual-studio_3.png)



 [場所の選択] ダイアログが表示されます。

1. クリック**ローカル IIS**タブ。
IIS ルート フォルダーに格納されているすべてのフォルダーと Web アプリケーションが表示されます (例: C:\Inetpub\wwwroot)。

![todo:画像_代替_文章](working-with-visual-studio_4.png)




1. ここで、Web サイト ファイルが格納されるローカル IIS に新しい Web アプリケーションを作成します。
 [場所の選択] ダイアログでは、ローカル IIS で Web アプリケーションまたは仮想ディレクトリを作成および削除できます。 Web アプリケーションを作成するには、下図のようにボタンをクリックします。

![todo:画像_代替_文章](working-with-visual-studio_5.png)



デフォルト名 WebSite の新しい Web アプリケーションが作成されます。

1. Web アプリケーションの名前を変更します。名前を GridWebOn2013 に変更しました。
1. クリック**開ける**. 

![todo:画像_代替_文章](working-with-visual-studio_6.png)



 [新しい Web サイト] ダイアログに戻ります。 Web サイトの場所のパスはに設定されています<http://localhost/GridWebOn2013>. 

1. クリック**わかった**Visual Studio で Web サイトを作成できるようにします。

![todo:画像_代替_文章](working-with-visual-studio_7.png)
### **ステップ 2: Web ページのソースとデザイン ビューを確認する**
Visual Studio 2013 によって既定の Web サイトが作成されます。これには、ダミーのテキストとマークアップを含む default.aspx Web ページが含まれています。

**default.aspx ページのソース ビュー** 

![todo:画像_代替_文章](working-with-visual-studio_8.png)



すべての Web ページ (ASP.NET を含む) は、2 つのモードで開くことができます。 1 つは、開発者がソース コードにアクセスして変更できるようにするソース ビューです。 2 つ目のモードは、Web ページを WYSIWYG 方式でデザインするために使用できるデザイン ビューです。上のスクリーンショットは、default.aspx Web ページのソース ビューを示しています。デザイン ビューを表示するには、**デザイン**. 

**default.aspx ページのデザイン ビュー** 

![todo:画像_代替_文章](working-with-visual-studio_9.png)




Visual Studio によって追加された Default.aspx ページを削除し、新しい空の Default.aspx ページを追加します。

![todo:画像_代替_文章](working-with-visual-studio_10.png)
### **ステップ 3: Aspose.Cells.GridWeb を Web ページに追加する**
ツールボックスからドラッグするだけで、Aspose.Cells.GridWeb (または GridWeb) コントロールを Web ページに追加できます。

![todo:画像_代替_文章](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb をツールボックスに追加する方法がわからない場合は、 を参照してください。[Aspose.Cells グリッド コントロールを Visual Studio.NET と統合する](/cells/ja/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

GridWeb コントロールが Web ページにドロップされると、次のようにレンダリングされます。

![todo:画像_代替_文章](working-with-visual-studio_12.png)



### **ステップ 4: <!DOCTYPE> タグを変更する**
1. ソース ビューに切り替えて、次を見つけます。**<!DOCTYPE>**ソース コードのタグ:

**ASP.NET**

{{< highlight "csharp" >}}



<!DOCTYPE html>



{{< /highlight >}}

1. 完全なタグを選択します。

![todo:画像_代替_文章](working-with-visual-studio_13.png)




1. 保持、変更、または削除<!DOCTYPE>鬼ごっこ。
1. または、<!DOCTYPE>次のタグを付けます。

{{< highlight "csharp" >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **手順 5: Aspose.Cells.GridWeb コントロールのサイズ変更**
Web サイトにドラッグした後、GridWeb コントロールの幅と高さを変更できます。

デザイン ビューでは、GridWeb の幅と高さを変更できます。

![todo:画像_代替_文章](working-with-visual-studio_14.png)



### **ステップ 6: Aspose.Cells.GridWeb のプロパティの構成**
をクリックして、WYSIWYG で Aspose.Cells.GridWeb プロパティを構成します。**プロパティ** Visual Studio 2013 IDE の右側にあるボタン。
 [プロパティ] ダイアログが表示されます。

![todo:画像_代替_文章](working-with-visual-studio_15.png)



[プロパティ] ペインでは、GridWeb のルック アンド フィールや、GridWeb の動作を制御するその他のプロパティを構成できます。
### **ステップ 7: Aspose.Cells.GridWeb を含む最初の Web サイトを実行する**
Web サイトを構築して実行します。

1.  Ctrl+F5 を押すか をクリックして、Visual Studio から Web サイトを直接実行します。**デバッグを開始**. 

![todo:画像_代替_文章](working-with-visual-studio_16.png)

これで、GridWeb コントロールで遊んでみることができます。

**動作中の GridWeb コントロール** 

![todo:画像_代替_文章](working-with-visual-studio_17.png)
