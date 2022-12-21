---
title: Excel のテーマと色
type: docs
weight: 130
url: /ja/java/excel-2007-themes-and-colors/
---
{{% alert color="primary" %}}

テーマは、ワークブックで使用される名前付きスタイル、グラフィック効果、およびその他のオブジェクトで統一された外観を提供します。たとえば、Accent1 スタイルは、Office テーマと Apex テーマでは異なって見えます。多くの場合、ドキュメントのテーマを適用してから、必要に応じて修正します。

**Microsoft Excel でのテーマの適用**

![todo:画像_代替_文章](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **テーマの色の取得と設定**

Aspose.Cells API は、テーマと色をカスタマイズするための機能を提供します。以下は、テーマの色を実装するいくつかのメソッドとプロパティです。

- Style.ForegroundThemeColor プロパティを使用して前景色を設定できます。
- Style.BackgroundThemeColor プロパティを使用して、背景色を設定できます。
- Font.ThemeColor プロパティを使用して、フォントの色を設定できます。
- Workbook.getThemeColor メソッドを使用して、テーマの色を取得できます。
- Workbook.setThemeColor メソッドを使用して、テーマの色を設定できます。

次の例は、テーマの色を取得および設定する方法を示しています。

次の例では、テンプレート XLSX ファイルを使用し、さまざまなテーマの色の種類の色を取得し、色を変更して、Microsoft Excel ファイルを保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **テーマのカスタマイズ**

次の例は、目的の色でカスタム テーマを適用する方法を示しています。この例では、Microsoft Excel 2007 で手動で作成されたサンプル テンプレート ファイルを使用しています。

**テンプレート CustomThemeColor.xlsx ファイル**

![todo:画像_代替_文章](excel-2007-themes-and-colors_2.png)

次の例では、テンプレート XLSX ファイルを読み込み、さまざまなテーマ カラー タイプの色を定義し、カスタム カラーを適用して、Excel ファイルを保存します。

**テーマの色をカスタマイズして生成されたファイル**

![todo:画像_代替_文章](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **テーマの色の使用**

次の例では、(ブックの) 既定のテーマの色の種類に基づいて、セルの前景色とフォントの色を適用します。また、Excel ファイルをディスクに保存します。

コードを実行すると、次の出力が生成されます。

**ワークシートの D3 セルに適用されるテーマの色** 

![todo:画像_代替_文章](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **先行トピック**
- [Excel ファイルからテーマ データを抽出する](/cells/ja/java/extract-theme-data-from-excel-file/)
