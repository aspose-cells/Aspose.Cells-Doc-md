---
title: Excelのテーマと色
type: docs
weight: 130
url: /ja/java/excel-2007-themes-and-colors/
---

{{% alert color="primary" %}}

テーマは、ブックで使用される名前付きスタイル、グラフィカルエフェクト、およびその他のオブジェクトとともに統一された外観を提供します。たとえば、Accent1スタイルは Office と Apexのテーマで異なる外観になります。通常、ドキュメントテーマを適用し、必要に応じて修正します。

Microsoft Excelでテーマを適用する

![todo:image_alt_text](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **テーマカラーを取得および設定する**

Aspose.Cells APIでは、テーマと色をカスタマイズするための機能が提供されます。以下は、テーマカラーを実装するいくつかのメソッドとプロパティです。

- Style.ForegroundThemeColorプロパティは、前景色を設定するために使用できます。
- Style.BackgroundThemeColorプロパティは、背景色を設定するために使用できます。
- Font.ThemeColorプロパティは、フォントの色を設定するために使用できます。
- Workbook.getThemeColorメソッドを使用してテーマカラーを取得できます。
- Workbook.setThemeColorメソッドを使用してテーマカラーを設定できます。

使用例では、テーマカラーを取得および設定する方法が示されています。

使用例では、テンプレートXLSXファイルを使用して、さまざまなテーマカラータイプの色を取得し、色を変更し、Microsoft Excelファイルを保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **テーマのカスタマイズ**

以下の例は、独自の色を使用してカスタムテーマを適用する方法を示しています。この例では、Microsoft Excel 2007で手動で作成したサンプルテンプレートファイルを使用しています。

**テンプレートCustomThemeColor.xlsxファイル**

![todo:image_alt_text](excel-2007-themes-and-colors_2.png)

使用例では、テンプレートXLSXファイルを読み込み、さまざまなテーマカラータイプの色を定義し、カスタムカラーを適用してExcelファイルを保存します。

**カスタマイズされたテーマカラーを使用した生成されたファイル**

![todo:image_alt_text](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **テーマカラーの使用**

使用例では、セルの前景色とフォント色を、ブックのデフォルトテーマの色タイプに基づいて適用します。また、Excelファイルをディスクに保存します。

コードを実行すると、次の出力が生成されます。

**ワークシートのD3セルに適用されたテーマカラー** 

![todo:image_alt_text](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **高度なトピック**
- [Excelファイルからテーマデータを抽出](/cells/ja/java/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="java" >}}
