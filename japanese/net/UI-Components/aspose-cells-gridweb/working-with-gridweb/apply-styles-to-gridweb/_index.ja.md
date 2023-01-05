---
title: スタイルを GridWeb に適用する
type: docs
weight: 20
url: /ja/net/apply-styles-to-gridweb/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb には独自のデフォルトのルック アンド フィールがありますが、外観を変更することができます。 Aspose.Cells.GridWeb は、開発者がその外観を完全に制御できるように、いくつかのプロパティを提供します。このトピックでは、これらのプロパティのいくつかについて説明します。

{{% /alert %}} 
## **Aspose.Cells.GridWeb へのプリセット スタイルまたはカスタム スタイルの適用**
### **プリセット スタイル**
開発者の労力を節約するために、Aspose.Cells.GridWeb にはいくつかのプリセット スタイルが用意されています。スタイルを適用するには、リストからスタイルを選択するだけです。

|**スタイル**|**カラースキーム**|
|:- |:- |
|標準|銀|
|カラフル1|ローズ|
|カラフル2|青い|
|プロフェッショナル1|シアン|
|プロフェッショナル2|シアン再び|
|トラディショナル1|暗い|
|トラディショナル2|グレー|
|カスタム|カスタマイズされた|
特定のスタイルが選択されると、GridWeb コントロールの全体的な外観が変更されます。開発者は、設計時にグリッドに適用するプリセット スタイルを選択できますが、このタスクは、Aspose.Cells.GridWeb の柔軟な API を使用して実行時に実行することもできます。

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb コントロールは GridWeb クラスで表されます。

{{% /alert %}} 

プリセット スタイルを選択するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. コントロールに適用するプリセット スタイルを選択します。

GridWeb コントロールは、開発者が任意のプリセット スタイルを割り当てることができる PresetStyle プロパティを提供します。

以下のコード スニペットの出力を以下に示します。

**Colorful1 スタイルが適用された GridWeb コントロール** 

![todo:画像_代替_文章](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **ヘッダー バーのスタイル**
GridWeb コントロールを見ると、2 つのヘッダー バーがあることがわかります。 1 つは列 (A、B、C、D など) 用で、もう 1 つは行 (1、2、3、4 など) 用です。 Aspose.Cells.GridWeb を使用すると、開発者はこれらのヘッダー バーの外観を制御できます。開発者は、設計時または実行時にヘッダー バーのスタイルを設定できます。

{{% alert color="primary" %}} 

GridWeb コントロールは、コントロールの両方のヘッダー バーにスタイルを適用する HeaderBarStyle プロパティを提供します。

{{% /alert %}} 

以下のコード例の出力を次に示します。

**ヘッダー バーの変更されたスタイル** 

![todo:画像_代替_文章](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **タブバーのスタイル**
タブバーのスタイルを設定できます。

**アクティブおよび非アクティブのタブ バーの変更されたスタイル** 

![todo:画像_代替_文章](apply-styles-to-gridweb_3.png)

上の図では、Sheet4 がアクティブなタブであるため、以下のコード例で定義されているように、その外観は他のタブとは異なります。





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **再利用可能なカスタマイズされたスタイル ファイル**
Aspose.Cells.GridWeb は、その外観またはスタイル設定をファイルに保存することもサポートしています。 GridWeb コントロールのすべての外観プロパティを設定したら、これらのプロパティまたは設定をディスク ファイルに保存できます。このアプローチは、コントロールのすべてのスタイル (または外観) プロパティを 1 つずつ設定する代わりに、スタイル ファイルから古いスタイル構成を再利用することで、開発者が時間と労力を節約するのに非常に役立ちます。
### **スタイルファイルの保存**
スタイル プロパティの設定が完了したら、GridWeb コントロールの SaveCustomStyleFile メソッドを呼び出して、スタイル構成設定を XML ファイルの形式で保存できます (これは、スタイル ファイルが XML ファイルとして保存されているためです)。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

保存されたスタイル ファイルは XML 形式であるため、開発者は必要に応じてこのファイルを任意のテキスト エディタで編集することもできます。

{{% /alert %}} 
### **スタイルファイルを読み込んでいます**
既存のスタイル ファイルから GridWeb コントロールにスタイル設定を適用するために、開発者はスタイル ファイルのパスをコントロールの CustomStyleFileName プロパティに設定できます。ただし、それを行う前に、コントロールの PresetStyle プロパティを Custom に設定する必要があります。そのスタイル ファイルには、開発者によって既に定義されているカスタム スタイル情報が含まれているためです。

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb Designer を使用してスタイル ファイルをロードまたは保存することもできます。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

重要: スタイル ファイルを GridWeb コントロールにロードしても、コントロールのセルの書式設定には影響しません。

{{% /alert %}} 
### **XML スタイル テンプレートの標準形式**
{{< highlight "java" >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}
