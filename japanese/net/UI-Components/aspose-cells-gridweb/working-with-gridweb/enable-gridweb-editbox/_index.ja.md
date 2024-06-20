---
title: Aspose.Cells.GridWebのEditBoxを有効にする
type: docs
weight: 110
url: /ja/net/aspose-cells-gridweb/enable-gridweb-editbox/
keywords: GridWeb,editbox,フォーミュラバーを有効にする
description: この記事では、GridWebでフォーミュラバーまたは編集ボックスを使用する方法について紹介します。
---

{{% alert color="primary" %}} 

GridWebのEdit Box（Excelではフォーミュラバーと呼ばれる）は、コントロールの上部にレンダリングされるツールバーで、フォーカスされたセルの値を表示したり入力したり、データや式をコピーしたりすることができます。また、現在編集しているセルの名前も表示されます。枠をクリックした後やデータを書き込み始めたり等号（＝）を入力したときに、Edit Boxが有効になります。

{{% /alert %}} 
## **Aspose.Cells.GridWebのEdit Boxを設定する**
GridWebコントロールには、開発者が"True"に割り当てることができるShowCellEditBoxプロパティがあります。 この属性のデフォルト値はFalseです。 値を"True"に設定すると、GridWebコントロールの上部に編集ボックスが表示されます。

{{% alert color="primary" %}} 

To enable this feature, you need to import "jquery.js" file to your project and refer it in your .aspx page(s) to make it work. You may download the jQuery archive from <https://jqueryui.com/download/all/> and put the library file(s) into some folder in the project and add reference to the library file via <script> tag in your .aspx web form as following. All the latest jQuery versions are OK.

{{< highlight csharp >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**編集ボックス付きのGridWebコントロール** 

![todo:image_alt_text](enable-gridweb-editbox_1.png)
### **例**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
