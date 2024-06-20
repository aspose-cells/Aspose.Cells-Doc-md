---
title: Visual Studioでの作業
type: docs
weight: 20
url: /ja/net/aspose-cells-gridweb/work-with-visual-studio/
keywords: GridWeb,visualstudio
description: この記事では、Visual StudioでGridWebを使用する方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックではVisual Studio.NET 2005を使用したASP.NETアプリケーションでAspose.Cells.GridWebを使用する方法について説明します。このトピックは、Aspose.Cells.GridWebを使用する初心者レベルの開発者に役立ちます。

{{% /alert %}} 
## **Visual Studio 2013を使用したAspose.Cells.GridWebの作業**
このトピックでは、Visual Studio 2013でサンプルのウェブサイトを作成することでAspose.Cells.GridWebを使用する方法を示します。プロセスはステップに分かれています。
### **ステップ1：新しいウェブサイトの作成**
1. Visual Studio 2013を開きます。
1. **ファイル**メニューから**新規メニュー**、その後**ウェブサイト**を選択します。 

![todo:image_alt_text](working-with-visual-studio_1.png)


新しいウェブサイトダイアログが開きます。 

1. インストールされているVisual Studioテンプレートから**ASP.NET Web Formsサイト**を選択します。
1. ウェブサイトの場所のHTTPモードを選択します。 

![todo:image_alt_text](working-with-visual-studio_2.png)




1. ウェブサイトのファイルが作成および保存される場所を指定します。 
   新しいウェブサイトダイアログで**参照**をクリックします。 

![todo:image_alt_text](working-with-visual-studio_3.png)



Choose Location ダイアログが表示されます。 

1. **Local IIS** タブをクリックします。
   IIS ルートフォルダに格納されているすべてのフォルダおよび Web アプリケーションが表示されます（例: C:\Inetpub\wwwroot）。 

![todo:image_alt_text](working-with-visual-studio_4.png)




1. ローカル IIS に新しい Web アプリケーションを作成して、Web サイトファイルを保存します。
   Choose Location ダイアログを使用して、ローカル IIS に Web アプリケーションまたは仮想ディレクトリを作成および削除できます。Web アプリケーションを作成するには、下の図に示されているようにボタンをクリックします。 

![todo:image_alt_text](working-with-visual-studio_5.png)



デフォルト名 WebSite の新しい Web アプリケーションが作成されます。 

1. Web アプリケーションの名前を変更します。GridWebOn2013 に名前を変更しました。
1. **開く** をクリックします。 

![todo:image_alt_text](working-with-visual-studio_6.png)



You return to the New Web Site dialog. The path of web site location is set to <http://localhost/GridWebOn2013>. 

1. **OK** をクリックして、Visual Studio に Web サイトを作成させます。 

![todo:image_alt_text](working-with-visual-studio_7.png)
### **手順 2: Web ページのソースビューおよびデザインビューを確認**
Visual Studio 2013 によってデフォルトの Web サイトが作成されます。ダミーテキストやマークアップが含まれた default.aspx Web ページが含まれています。 

**default.aspx ページのソースビュー** 

![todo:image_alt_text](working-with-visual-studio_8.png)



すべての Web ページ（ASP.NET を含む）は、2つのモードで開くことができます。1つは開発者がソースコードにアクセスして変更できるソースビューです。2番目のモードは WYSIWYG 方式で Web ページをデザインできるデザインビューです。上のスクリーンショットは、default.aspx Web ページのソースビューを示しています。デザインビューを表示するには、**デザイン** をクリックします。 

**default.aspx ページのデザインビュー** 

![todo:image_alt_text](working-with-visual-studio_9.png)




Visual Studio によって追加された Default.aspx ページを削除し、新しい空の Default.aspx ページを追加します。

![todo:image_alt_text](working-with-visual-studio_10.png)
### **手順 3: Aspose.Cells.GridWeb を Web ページに追加**
Aspose.Cells.GridWeb（または GridWeb）コントロールをツールボックスからドラッグして簡単に Web ページに追加できます。 

![todo:image_alt_text](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

Aspose.Cells.GridWeb をツールボックスに追加する方法についてわからない場合は、[Integrate Aspose.Cells Grid Controls with Visual Studio.NET](/cells/ja/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/) を参照してください。 

{{% /alert %}} 

GridWeb コントロールを Web ページにドロップすると、次のようにレンダリングされます: 

![todo:image_alt_text](working-with-visual-studio_12.png)



### **Step 4: Change the <!DOCTYPE> tag**
1. Switch to source view and find the following **<!DOCTYPE>** tag in the source code: 

**ASP.NET**

{{< highlight csharp >}}



<!DOCTYPE html>



{{< /highlight >}}

1. タグ全体を選択します。 

![todo:image_alt_text](working-with-visual-studio_13.png)




1. Retain, change or delete the <!DOCTYPE> tag.
1. Or modify the <!DOCTYPE> tag with the following one: 

{{< highlight csharp >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **手順 5: Aspose.Cells.GridWeb コントロールのサイズ変更**
Web サイトにドラッグした後で GridWeb コントロールの幅と高さを変更できます。 

デザインビューでは、GridWeb の幅と高さを変更できます。 

![todo:image_alt_text](working-with-visual-studio_14.png)



### **手順 6: Aspose.Cells.GridWeb のプロパティを構成**
Visual Studio 2013 IDE の右側にある **Properties** ボタンをクリックして、Aspose.Cells.GridWeb のプロパティを WYSIWYG で構成します。 
プロパティ ダイアログが表示されます。 

![todo:image_alt_text](working-with-visual-studio_15.png)



プロパティペインにより、GridWeb の外観やその他のプロパティを構成して、GridWeb の動作を制御することが可能となります。
### **手順 7: Aspose.Cells.GridWeb を含む最初の Web サイトを実行**
Web サイトをビルドして実行します。 

1. Ctrl+F5 を押すか、**デバッグの開始** をクリックして Visual Studio から Web サイトを直接実行します。 

![todo:image_alt_text](working-with-visual-studio_16.png)

今、GridWebコントロールでのプレイを開始できます。 

**GridWebコントロールの活用** 

![todo:image_alt_text](working-with-visual-studio_17.png)
