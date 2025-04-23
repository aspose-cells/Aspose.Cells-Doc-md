---  
title: Excelのテーマと色
linktitle: Excelのテーマと色  
type: docs  
weight: 100  
url: /ja/nodejs-cpp/excel-themes-and-colors/  
description: Aspose.Cells for Node.js via C++を使用したカスタムカラースキームの使い方を学びます。  
keywords: Node.jsでカラースキームを作成および適用、プログラムでカスタムカラースキームを作成、プログラムでカスタムカラースキームをNode.jsで適用、Excelで色スキームを使用する方法  
---  

## **Excelでのカラースキームの適用と作成方法**  
ドキュメントテーマを使用すると、Excelドキュメントの色、フォント、グラフィックの書式効果を簡単に調整し、迅速に更新できます。  
テーマは、名前付きスタイル、グラフィック効果、他のオブジェクトを使用してブックの外観を統一します。例えば、Accent1スタイルはOfficeテーマとApexテーマで異なって見えます。多くの場合、ドキュメントテーマを適用し、その後必要に応じて修正します。  

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

## **Aspose.Cellsでのカラースキームの作成と適用方法**  
Aspose.Cellsにはテーマと色をカスタマイズする機能が提供されています。  

### **Aspose.Cellsでのカスタムカラーテーマの作成方法**  
テーマカラーをファイル内で使用する場合、各セルを個別に変更する必要はなく、テーマの色だけを変更すればよいです。  

使用例では、希望の色でカスタムテーマを適用する方法が示されています。Microsoft Excel 2007 で手動で作成されたサンプルテンプレートファイルを使用します。  

以下の例では、テンプレートXLSXファイルを読み込み、異なるテーマカラータイプの色を定義し、カスタム色を適用してExcelファイルを保存します。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-CreateCustomColorTheme.js" >}}



### **Aspose.Cells でテーマカラーを適用する方法**  
以下の例では、セルの前景色とフォント色をデフォルトのテーマ（ワークブック）のカラータイプに基づいて適用し、Excelファイルをディスクに保存します。  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-ApplyThemeColors.js" >}}


### **Aspose.Cells でテーマカラーを取得および設定する方法**  
テーマカラーを実装するいくつかのメソッドとプロパティが以下に示されています。  

- [**Style.setForegroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundThemeColor-themecolor-): 前景色の設定に使用します。  
- [**Style.setBackgroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundThemeColor-themecolor-): 背景色の設定に使用します。  
- [**Font.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setThemeColor-themecolor-): フォント色の設定に使用します。  
- [**Workbook.getThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getThemeColor-themecolortype-): テーマ色を取得するために使用します。  
- [**Workbook.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#setThemeColor-themecolortype-color-): テーマ色を設定するために使用します。  

使用例では、テーマカラーを取得および設定する方法が示されています。  

以下の例では、テンプレートXLSXファイルを使用し、異なるテーマカラータイプの色を取得、色を変更し、Microsoft Excelファイルを保存します。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetAndSetThemeColors.js" >}}


## **高度なトピック**  
- [Excelファイルからテーマデータを抽出](/cells/ja/nodejs-cpp/extract-theme-data-from-excel-file/)  

