---
title: Aspose.CellsがTrueTypeフォントを使用する方法
type: docs
weight: 10
url: /ja/java/how-aspose-cells-uses-truetype-fonts/
---

{{% alert color="primary" %}}

Aspose.Cellsは、スプレッドシートをPDF、XPS、イメージなどの形式にレンダリングする際にTrueTypeフォントが必要です。

Aspose.Cellsがスプレッドシートをレンダリングする際、スプレッドシートで使用されているTrueTypeフォントにアクセスする必要があります。これは、PDF、XPS、イメージの生成中に一般的な取り組みであり、変換されたドキュメントやイメージがどのビューアにとっても同じように表示されることを保証します。

{{% /alert %}}

## **フォントについて**

### **フォントの利用可能性と代替**

スプレッドシートはArial、Times New Roman、Verdanaなどさまざまなフォントを使用してフォーマットされる場合があります。Aspose.Cellsがスプレッドシートをレンダリングする際、スプレッドシートで使用されているフォントを選択しようとします。しかし、正確なフォントが利用できない場合もありますので、Aspose.Cellsは代わりの似たフォントを選択する必要があります。

下記は、Aspose.Cellsが裏で行うプロセスです。

1. Aspose.Cellsは、スプレッドシートで使用されている正確なフォント名と一致するフォントをファイルシステムで探そうとします。
1. Aspose.Cellsが正確なフォント名のフォントを見つけられない場合、ワークブックのDefaultStyle.Fontプロパティで指定されたデフォルトフォントを使用しようとします。
1. Aspose.CellsがワークブックのDefaultStyle.Fontプロパティで定義されたフォントを見つけられない場合、利用可能なすべてのフォントから最も適したフォントを選択しようとします。
1. 最終的に、Aspose.Cellsがファイルシステムでフォントを見つけられない場合、スプレッドシートをArialでレンダリングします。

### **Aspose.Cellsがフォントを探す場所**

Aspose.Cellsは自動的にファイルシステム上のTrueTypeフォントを見つけようとします。ほとんどの場合、Aspose.Cellsのデフォルト動作に依存できますが、TrueTypeフォントが含まれるフォルダをFontConfigs.setFontFolderファクトリメソッドを使用して明示的に指定する必要がある場合もあります。

### **典型的なフォント関連の問題と解決策**

典型的なフォント関連の問題と解決策

{{% alert color="primary" %}}

フォントをコピーする際には、ほとんどのフォントが著作権があります。フォントのライセンスを事前に見つけ、他のマシンに自由に転送できることを確認してください。 

{{% /alert %}}

|**問題** |**理由** |**解決策** |
| :- | :- | :- |
|レンダリングされたドキュメントのレイアウトやフォントが元のものと異なる。 |Aspose.CellsをLinuxやMac OSで使用しており、デフォルトではTrueTypeフォントが存在しないため、Aspose.Cellsがコンピューター上のフォントを見つけられない。 |WindowsマシンからTrueTypeフォントファイルをコピーするか、TrueTypeフォントの場所を指定するためにFontConfigs.setFontFolderファクトリメソッドを使用してフォントファイルの場所を指定してください。|

{{% alert color="primary" %}}

詳細な記事は次の場所を確認してください

- [LinuxにTrueTypeフォントを配置する方法](/cells/ja/java/how-to-install-truetype-fonts-on-linux/)
- [TrueTypeフォントの場所を指定する方法](/cells/ja/java/how-to-specify-truetype-fonts-location/)
- [フォントの代替が発生した際に警告を取得する方法](/cells/ja/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
