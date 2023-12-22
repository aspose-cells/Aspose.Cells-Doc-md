---
title: Excel のテーマと色
type: docs
weight: 100
url: /ja/net/excel-themes-and-colors/
description: C# Aspose.Cells for .NET API で Excel カラー スキームを使用するコード
keywords: C# to Create and Apply Color Schemes, c# programmatically Create a Custom Color Scheme, programmatically how to Apply a Custom Color Scheme, c# how to Use Color Scheme in excel
---
##  **Excelでカラースキームを適用および作成する方法**
ドキュメント テーマを使用すると、Excel ドキュメントの色、フォント、グラフィック書式設定効果を簡単に調整し、迅速に更新できます。
テーマは、ワークブックで使用される名前付きスタイル、グラフィック効果、その他のオブジェクトを使用して統一された外観を提供します。たとえば、Accent1 スタイルは、Office テーマと Apex テーマでは見た目が異なります。多くの場合、ドキュメントのテーマを適用してから、希望どおりに修正します。

###  **Excelでカラースキームを適用する方法**
1. Excel を開き、Excel リボンの [ページ レイアウト] タブに移動します。
1. 「テーマ」セクションの「色」ボタンをクリックします。
<br>
<img src="color.png" width=70% />
1. 要件に一致するカラー パレットを選択するか、スキームの上にマウスを置くとライブ プレビューが表示されます。

###  **Excel でカスタム カラー スキームを作成する方法**
独自のカラーセットを作成して、ドキュメントに新鮮でユニークな外観を与えたり、組織のブランド基準に準拠したりすることができます。

1. Excel を開き、Excel リボンの [ページ レイアウト] タブに移動します。
1. 「テーマ」セクションの「色」ボタンをクリックします。
1. 「色のカスタマイズ...」ボタンをクリックします。
<br>
<img src="color2.png" width=70% />

1. [新しいテーマの色の作成] ダイアログ ボックスで、要素の横にある色のドロップダウンをクリックして、各要素の色を選択できます。パレットから色を選択することも、「その他の色」オプションを使用してカスタム色を定義することもできます。
<br>
<img src="color3.png" width=70% />
1. 必要な色をすべて選択した後、「名前」フィールドにカスタム カラー スキームの名前を入力します。

1. [保存] ボタンをクリックして、カスタム カラー スキームを保存します。カスタムの配色は、今後使用できるように [色] ドロップダウン メニューで利用できるようになります。

##  **Aspose.Cells で配色を作成して適用する方法**
Aspose.Cells は、テーマと色をカスタマイズする機能を提供します。

###  **Aspose.Cells でカスタム カラー テーマを作成する方法**
ファイル内でテーマの色が使用されている場合、各セルを個別に変更する必要はなく、テーマ内の色を変更するだけで済みます。

次の例は、希望の色のカスタム テーマを適用する方法を示しています。 Microsoft Excel 2007 で手動で作成したサンプル テンプレート ファイルを使用します。

次の例では、テンプレート XLSX ファイルをロードし、さまざまなテーマ カラー タイプの色を定義し、カスタム カラーを適用して、Excel ファイルを保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

###  **Aspose.Cells でテーマカラーを適用する方法**

次の例では、(ブックの) デフォルトのテーマの色の種類に基づいてセルの前景色とフォントの色を適用します。また、Excel ファイルをディスクに保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

###  **Aspose.Cells でテーマカラーを取得および設定する方法**
以下に、テーマの色を実装するいくつかのメソッドとプロパティを示します。

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): 前景色を設定するために使用されます。
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor)：背景色の設定に使用します。
- [**フォント.テーマの色**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor)：文字の色を設定します。
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): テーマカラーを取得するために使用されます。
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor)：テーマカラーを設定します。

次の例は、テーマの色を取得および設定する方法を示しています。

次の例では、テンプレート XLSX ファイルを使用し、さまざまなテーマ カラー タイプの色を取得し、色を変更して、Microsoft Excel ファイルを保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

##  **アドバンストトピック**
- [Excelファイルからテーマデータを抽出](/cells/ja/net/extract-theme-data-from-excel-file/)
