---
title: GridWebにスタイルを適用する
type: docs
weight: 20
url: /ja/net/aspose-cells-gridweb/apply-styles-to-gridweb/
keywords: GridWeb, style, styles
description: この記事では、GridWebでスタイルを適用または設定する方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWebにはデフォルトの外観がありますが、外観を変更することも可能です。Aspose.Cells.GridWebは、開発者が外観を完全に制御するためにいくつかのプロパティを提供しています。このトピックでは、その中のいくつかのプロパティについて説明します。

{{% /alert %}} 
## **Aspose.Cells.GridWebにプリセットまたはカスタムスタイルを適用する**
### **プリセットスタイル**
開発者の手間を省くために、Aspose.Cells.GridWebはいくつかのプリセットスタイルを提供しています。リストからスタイルを選択して適用するだけです。

|**スタイル**|**色の配色**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
特定のスタイルが選択されると、GridWebコントロール全体の外観が変わります。開発者は、デザイン時にGridに適用するプリセットスタイルを選択できますが、Aspose.Cells.GridWebの柔軟なAPIを使用してランタイムでこのタスクを達成することもできます。

{{% alert color="primary" %}} 

Aspose.Cells.GridWebコントロールはGridWebクラスによって表されます。

{{% /alert %}} 

プリセットスタイルを選択するには：

1. Aspose.Cells.GridWebコントロールをwebフォームに追加します。
1. コントロールに適用するプリセットスタイルを選択します。

GridWebコントロールは、開発者が任意のプリセットスタイルを割り当てることができるPresetStyleプロパティを提供します。

以下のコードスニペットの出力は以下に示されています。 

Colorful1スタイルが適用されたGridWebコントロール 

![todo:image_alt_text](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **ヘッダーバースタイル**
GridWebコントロールを見ると、2つのヘッダーバーがあることに気づきます。1つは列用（すなわちA、B、C、Dなど）、もう1つは行用（すなわち1、2、3、4など）です。Aspose.Cells.GridWebは、これらのヘッダーバーの外観を制御することができます。開発者はデザイン時または実行時にヘッダーバーのスタイルを設定することができます。

{{% alert color="primary" %}} 

GridWebコントロールは、コントロールの両方のヘッダーバーにスタイルを適用するHeaderBarStyleプロパティを提供します。

{{% /alert %}} 

以下の例のコードの出力はこちらに示されています。 

ヘッダーバーの変更されたスタイル 

![todo:image_alt_text](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **タブバースタイル**
タブバーのスタイルを設定することができます。 

アクティブおよび非アクティブなタブバーの変更されたスタイル 

![todo:image_alt_text](apply-styles-to-gridweb_3.png)

上記の図では、Sheet4がアクティブなタブであるため、その外観が他のタブと異なることが、以下の例のコードで定義されています。





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **再利用可能なカスタマイズされたスタイルファイル**
Aspose.Cells.GridWebは、外観やスタイル設定をファイルに保存する機能もサポートしています。GridWebコントロールの外観プロパティをすべて設定した後、これらのプロパティまたは設定をディスクファイルに保存することができます。このアプローチは、開発者が古いスタイルの構成を1つ1つ設定するのではなく、スタイルファイルから再利用することで時間と労力を節約するために非常に便利です。
### **スタイルファイルの保存**
スタイルプロパティの設定が完了したら、GridWebコントロールのSaveCustomStyleFileメソッドを呼び出すことで、自分のスタイル構成設定をXMLファイルの形式で保存することができます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

保存されたスタイルファイルはXML形式なので、開発者は任意のテキストエディタでこのファイルを編集することもできます。

{{% /alert %}} 
### **スタイルファイルの読み込み**
既存のスタイルファイルからGridWebコントロールにスタイル設定を適用するには、開発者はControlのCustomStyleFileNameプロパティにスタイルファイルのパスを設定することができます。ただし、その前に、コントロールのPresetStyleプロパティをCustomに設定する必要があります。その理由は、スタイルファイルがすでに開発者によって定義されたカスタムスタイル情報を含んでいるためです。

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb Designerを使用してスタイルファイルを読み込むまたは保存することも可能です。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

重要：GridWebコントロールにスタイルファイルを読み込んでも、コントロールのセルの書式設定には影響しません。

{{% /alert %}} 
### **XMLスタイルテンプレートの標準形式**
{{< highlight java >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}
