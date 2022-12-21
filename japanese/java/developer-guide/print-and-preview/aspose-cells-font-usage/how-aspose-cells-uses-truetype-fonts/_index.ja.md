---
title: Aspose.Cells の TrueType フォントの使用方法
type: docs
weight: 10
url: /ja/java/how-aspose-cells-uses-truetype-fonts/
---
{{% alert color="primary" %}}

Aspose.Cells では、スプレッドシートを PDF、XPS、画像などの形式にレンダリングするときに TrueType フォントが必要です。

Aspose.Cells がスプレッドシートをレンダリングするとき、スプレッドシートで使用されている TrueType フォントへのアクセスが必要です。これは、PDF、XPS、および画像の生成中の通常の方法であり、変換されたドキュメントまたは画像がどのビューアでも同一に見えるようにします。

{{% /alert %}}

## **フォントについて**

### **フォントの可用性と代替**

スプレッドシートは、Arial、Times New Roman、Verdana などのさまざまなフォントを使用してフォーマットできます。 Aspose.Cells がスプレッドシートをレンダリングするとき、スプレッドシートで使用されているフォントを選択しようとします。ただし、正確なフォントが利用できない場合があるため、代わりに Aspose.Cells で類似のフォントを使用する必要があります。

以下は、Aspose.Cells が舞台裏でたどるプロセスです。

1. Aspose.Cells は、スプレッドシートで使用されている正確なフォント名に一致するファイル システム上のフォントを見つけようとします。
1. Aspose.Cells がまったく同じ名前のフォントを見つけられない場合、Workbook の DefaultStyle.Font プロパティで指定された既定のフォントを使用しようとします。
1. Aspose.Cells は、ブックの DefaultStyle.Font プロパティで定義されたフォントを見つけられない場合、使用可能なすべてのフォントから最適なフォントを選択しようとします。
1. 最後に、Aspose.Cells がファイル システムでフォントを見つけられない場合、Arial を使用してスプレッドシートをレンダリングします。

### **Aspose.Cells がフォントを探す場所**

Aspose.Cells は、ファイル システムで TrueType フォントを自動的に見つけようとします。ほとんどの場合、Aspose.Cell のデフォルトの動作に頼って TrueType フォントを見つけることができますが、FontConfigs.setFontFolder ファクトリ メソッドを使用して TrueType フォントを含むフォルダーを指定する必要がある場合があります。

### **典型的なフォント関連の問題と解決策**

この表は、Aspose.Cells を使用してスプレッドシートを PDF にレンダリングするときに発生する可能性のある問題とその解決策の一部を示しています。

{{% alert color="primary" %}}

フォントをコピーするときは、ほとんどのフォントが著作権で保護されていることに注意してください。まず、フォントのライセンスを事前に見つけて、別のマシンに自由に転送できることを確認してください。

{{% /alert %}}

|**問題** |**理由** |**解決** |
|:- |:- |:- |
|レンダリングされたドキュメントのレイアウトとフォントは、元のドキュメントとは異なります。| TureType フォントがデフォルトで存在しない Linux または Mac OS で Aspose.Cells を使用しているため、Aspose.Cells はコンピューター上のフォントを見つけることができません。|Windows マシンから TrueType フォント ファイルをコピーするか、TrueType フォント パッケージをインストールします。 FontConfigs.setFontFolder ファクトリ メソッドを使用して、フォント ファイルの場所を指定します。|

{{% alert color="primary" %}}

の詳細記事をチェック

- [Linux に TrueType フォントを配置する方法](/cells/ja/java/how-to-install-truetype-fonts-on-linux/).
- [TrueType フォントの場所を指定する方法](/cells/ja/java/how-to-specify-truetype-fonts-location/).
- [フォントの置換が発生したときに警告を表示する方法](/cells/ja/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
