---
title: Excelのテーマと色
type: docs
weight: 100
url: /ja/python-net/excel-themes-and-colors/
description: C#コードでExcelカラースキームをAspose.Cells for Python via .NET APIと連携させて使用する例
keywords: C#での色のスキームの作成と適用、プログラム的にカスタムカラースキームの作成、プログラム的にカスタムカラースキームの適用方法、Excelでのカラースキームの使用方法
---

## **Excelでのカラースキームの適用と作成方法**
ドキュメントテーマを使用すると、Excelドキュメントの色、フォント、グラフィックの書式効果を簡単に調整し、迅速に更新できます。 
テーマは名前付きスタイル、グラフィカル効果、ブックの他のオブジェクトを使用して統一された外観を提供します。たとえば、OfficeテーマとApexテーマでは、Accent1スタイルは異なる外観になります。よくあるのは、ドキュメントテーマを適用してから、必要に応じて修正することです。

### **Excelでのカラースキームの適用方法**
1. Excelを開き、「ページレイアウト」タブに移動します。
1. 「テーマ」セクションの「カラー」ボタンをクリックします。
<br>
<img src="color.png" width=70% />
1. 要件に合ったカラーパレットを選択するか、スキームにマウスを重ねてライブプレビューを表示します。

### **Excelでのカスタムカラースキームの作成方法**
ドキュメントに新鮮で独自の外観を与えるために独自のカラーセットを作成するか、組織のブランド規準に準拠します。

1. Excelを開き、「ページレイアウト」タブに移動します。
1. 「テーマ」セクションの「カラー」ボタンをクリックします。
1. 「カスタムカラーのカスタマイズ...」ボタンをクリックします。
<br>
<img src="color2.png" width=70% />

1. 「新しいテーマの色の作成」ダイアログボックスで、各要素の色を選択できます。
<br>
<img src="color3.png" width=70% />
1. 必要な色をすべて選択した後、「名前」フィールドにカスタムカラースキームの名前を入力します。

1. 「保存」ボタンをクリックしてカスタムカラースキームを保存します。カスタムカラースキームは今後の使用のために「カラー」ドロップダウンメニューで利用可能になります。

## **Aspose.Cells for Python via .NETでカラー スキームを作成および適用する方法**
Aspose.Cells for Python via .NETは、テーマや色のカスタマイズ機能を提供します。

### **Aspose.Cells for Python via .NETでカスタムカラーテーマを作成する方法**
ファイルでテーマカラーが使用されている場合、各セルを個々に変更する必要はありません。テーマの色を修正するだけで済みます。

使用例では、希望の色でカスタムテーマを適用する方法が示されています。Microsoft Excel 2007 で手動で作成されたサンプルテンプレートファイルを使用します。

使用例では、テンプレートXLSXファイルを読み込み、さまざまなテーマカラータイプの色を定義し、カスタムカラーを適用してExcelファイルを保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CustomizeThemes-1.py" >}}

### **Aspose.Cells for Python via .NETでテーマカラーを適用する方法**

使用例では、セルの前景色とフォント色を、ブックのデフォルトテーマの色タイプに基づいて適用します。また、Excelファイルをディスクに保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UtilizeThemeColors-1.py" >}}

### **Aspose.Cells for Python via .NETでテーマカラーの取得と設定方法**
 テーマカラーを実装するいくつかのメソッドとプロパティが以下に示されています。

- [**Style.foreground_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_theme_color)：前景色を設定するために使用されます。
- [**Style.background_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_theme_color)：背景色を設定するために使用されます。
- [**Font.theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/theme_color)：フォントの色を設定するために使用されます。
- [**Workbook.get_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_theme_color)：テーマカラーを取得するために使用されます。
- [**Workbook.set_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/set_theme_color)：テーマカラーを設定するために使用されます。

使用例では、テーマカラーを取得および設定する方法が示されています。

使用例では、テンプレートXLSXファイルを使用して、さまざまなテーマカラータイプの色を取得し、色を変更し、Microsoft Excelファイルを保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetSetThemeColors-1.py" >}}

## **高度なトピック**
- [Excelファイルからテーマデータを抽出](/cells/ja/python-net/extract-theme-data-from-excel-file/)

