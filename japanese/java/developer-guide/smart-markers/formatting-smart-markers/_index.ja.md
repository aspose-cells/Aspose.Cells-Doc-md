---
title: スマートマーカーの書式設定
type: docs
weight: 20
url: /ja/java/formatting-smart-markers/
---
##  **スタイル属性のコピー**
スマート マーカーを使用するときに、スマート マーカー タグを含むセルのスタイルをコピーしたい場合があります。この目的には、スマート マーカーのタグの CopyStyle 属性を使用できます。
###  **スマート マーカーを使用して Cells からスタイルをコピーする**
この例では、A2 セルと B2 セルに 2 つのマーカーがある単純なテンプレート Microsoft Excel ファイルを使用します。セル B2 に貼り付けられたマーカーは CopyStyle 属性を使用しますが、セル A2 のマーカーは使用しません。単純な書式設定を適用します (たとえば、フォントの色を**赤**セルの塗りつぶしの色を *黄色** に設定します)。

この例では、[テンプレートファイル](template1.xlsx)コードを実行すると、Aspose.Cells は列 B のすべてのレコードに書式設定をコピーしますが、列 A の書式設定は保持しません。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-UsingCopyStyleAttribute-1.java" >}}


##  **カスタムラベルの追加**
###  **序章**
スマート マーカーのデータのグループ化機能を使用しているときに、独自のカスタム ラベルを概要行に追加する必要がある場合があります。また、「注文の小計」など、列の名前とそのラベルを連結することもできます。 Aspose.Cells は Label 属性と LabelPosition 属性を提供するため、グループ化データの小計行と連結しながらスマート マーカーにカスタム ラベルを配置できます。
###  **カスタム ラベルを追加してスマート マーカーの小計行と連結する**
この例では、[テンプレートファイル](template.xlsx)細胞内にいくつかのマーカーが存在します。コードを実行すると、Aspose.Cells はグループ化されたデータの概要行にいくつかのカスタム ラベルを追加します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-AddCustomLabels-1.java" >}}
