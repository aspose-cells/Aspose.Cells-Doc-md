---
title: Excel のテーマと色
type: docs
weight: 100
url: /ja/net/excel-themes-and-colors/
---
## **Excel のテーマと色**

テーマは、ワークブックで使用される名前付きスタイル、グラフィック効果、およびその他のオブジェクトで統一された外観を提供します。たとえば、Accent1 スタイルは、Office テーマと Apex テーマでは異なって見えます。多くの場合、ドキュメントのテーマを適用してから、必要に応じて修正します。

Aspose.Cells は、テーマと色をカスタマイズするための機能を提供します。

### **テーマの色の取得と設定**

以下は、テーマの色を実装するいくつかのメソッドとプロパティです。

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): 前景色の設定に使用します。
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): 背景色の設定に使用します。
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): 文字色の設定に使用します。
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): テーマの色を取得するために使用されます。
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): テーマの色を設定するために使用します。

次の例は、テーマの色を取得および設定する方法を示しています。

次の例では、テンプレート XLSX ファイルを使用し、さまざまなテーマ カラー タイプの色を取得し、色を変更して、Microsoft Excel ファイルを保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

#### **テーマをカスタマイズする**

次の例は、目的の色でカスタム テーマを適用する方法を示しています。 Microsoft Excel 2007 で手動で作成されたサンプル テンプレート ファイルを使用します。

次の例では、テンプレート XLSX ファイルを読み込み、さまざまなテーマ カラー タイプの色を定義し、カスタム カラーを適用して、Excel ファイルを保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

#### **テーマの色を使用する**

次の例では、(ブックの) 既定のテーマの色の種類に基づいて、セルの前景色とフォントの色を適用します。また、Excel ファイルをディスクに保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

## **先行トピック**
- [Excel ファイルからテーマ データを抽出する](/cells/ja/net/extract-theme-data-from-excel-file/)
