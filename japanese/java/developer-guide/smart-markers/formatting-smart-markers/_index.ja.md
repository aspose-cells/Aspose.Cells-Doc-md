---
title: SmartMarkersのフォーマット設定
type: docs
weight: 20
url: /ja/java/formatting-smart-markers/
---

## **スタイル属性のコピー**
スマートマーカーtagsを持つセルのスタイルをコピーする場合には、そのためにスマートマーカーtagsのCopyStyle属性を使用することができます。
### **スマートマーカーを含むセルからスタイルをコピーするための簡単な例です。この例では、A2およびB2のセルに2つのマーカーが使用されています。セルB2に貼り付けられたマーカーはCopyStyle属性を使用していますが、セルA2のマーカーは使用していません。簡単な書式設定（たとえばフォントの色を**赤**に設定し、セルの塗りつぶし色を**イエロー**に設定します）。**
この例では、A2およびB2のセルに2つのマーカーを持つシンプルなテンプレートMicrosoft Excelファイルが使用されています。セルB2に貼り付けられたマーカーはCopyStyle属性を使用し、一方、セルA2のマーカーは使用していません。簡単なフォーマット（例：フォントの色を**赤**に設定し、セルの背景色を**黄**に設定）を適用します。

この例では、セルにいくつかのマーカーが含まれる[テンプレートファイル](template1.xlsx)が使用されます。コードを実行すると、Aspose.Cellsは列Bのすべてのレコードにフォーマットをコピーしますが、列Aのフォーマットは保持しません。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-UsingCopyStyleAttribute-1.java" >}}


## **カスタムラベルの追加**
### **紹介**
Smart Markersのグループ化データ機能を使用する場合、時々サマリー行に独自のカスタムラベルを追加する必要があります。また、列の名前をそのラベルと連結したい場合があります。例えば、"注文の小計" のように. Aspose.Cells はラベルと LabelPosition 属性を提供しているため、グループ化データの Smart Markers にカスタムラベルを配置し、サマリー行と連結することができます。
### **Smart Markers内の小計行にカスタムラベルを追加**
この例では、セルにいくつかのマーカーが含まれる[テンプレートファイル](template.xlsx)が使用されます。コードを実行すると、Aspose.Cellsはグルーピングデータのサマリー行にカスタムラベルを追加します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-AddCustomLabels-1.java" >}}
{{< app/cells/assistant language="java" >}}
