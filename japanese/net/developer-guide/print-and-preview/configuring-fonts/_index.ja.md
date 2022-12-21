---
title: スプレッドシートをレンダリングするためのフォントの構成
type: docs
weight: 10
url: /ja/net/configuring-fonts-for-rendering-spreadsheets/
---
## **考えられる使用シナリオ**

Aspose.Cells API は、スプレッドシートを画像形式でレンダリングしたり、PDF および XPS 形式に変換したりする機能を提供します。変換の忠実度を最大化するには、スプレッドシートで使用されるフォントがオペレーティング システムのデフォルトのフォント ディレクトリで使用できる必要があります。必要なフォントが存在しない場合、Aspose.Cells API は必要なフォントを使用可能なフォントに置き換えようとします。

## **フォントの選択**

以下は、Aspose.Cells API が舞台裏でたどるプロセスです。

1. API は、スプレッドシートで使用されている正確なフォント名に一致するファイル システム上のフォントを見つけようとします。
1.  API がまったく同じ名前のフォントを見つけられない場合、ワークブックの**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)**財産。
1.  API がブックの下に定義されているフォントを見つけられない場合**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)**プロパティで指定されたフォントを使用しようとします。**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**また**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)**財産。
1.  API で定義されているフォントが見つからない場合**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**また**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)**プロパティで指定されたフォントを使用しようとします。**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)**財産。
1.  API で定義されているフォントが見つからない場合**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)**プロパティを使用すると、使用可能なすべてのフォントから最適なフォントを選択しようとします。
1. 最後に、API がファイル システムでフォントを見つけられない場合、Arial を使用してスプレッドシートをレンダリングします。

## **カスタム フォント フォルダの設定**

Aspose.Cells API は、オペレーティング システムの既定のフォント ディレクトリで必要なフォントを検索します。必要なフォントがシステムのフォント ディレクトリにない場合、API はカスタム (ユーザー定義) ディレクトリを検索します。の**[FontConfigs](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs)**クラスは、以下に詳述するように、カスタム フォント ディレクトリを設定する多くの方法を公開しています。

1. **[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)**: この方法は、設定するフォルダーが 1 つしかない場合に便利です。
1. **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**: この方法は、フォントが複数のフォルダーに存在し、すべてのフォントを 1 つのフォルダーにまとめるのではなく、すべてのフォルダーを個別に設定したい場合に便利です。
1. **[FontConfigs.SetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources)**: このメカニズムは、ユーザーが複数のフォルダー、単一のフォント ファイル、またはバイト配列からフォント データからフォントを読み込みたい場合に便利です。

{{% alert color="primary" %}}

両方**[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)** & **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**メソッドはブール型の 2 番目のパラメーターを受け入れます。通過**真実** 番目のパラメーターは、フォント ファイルのサブフォルダーを検索するように Aspose.Cells API に指示するためです。

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

アプリケーションの開始時に上記のいずれかの方法を使用してください。 Aspose.Cells API の他のオブジェクトを呼び出す前。

{{% /alert %}} {{% alert color="primary" %}}

上記のすべての方法を使用してフォント ソースを設定すると、最後の設定のみが有効になります。

{{% /alert %}}

## **フォント置換メカニズム**

 Aspose.Cells API は、レンダリング目的で代替フォントを指定する機能も提供します。このメカニズムは、変換が必要なマシンで必要なフォントが利用できない場合に役立ちます。ユーザーは、元々必要だったフォントの代わりに、フォント名のリストを提供できます。これを実現するために、Aspose.Cells API は**[FontConfigs.SetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes)** 2 つのパラメータを受け取るメソッド。最初のパラメータの型は**ストリング**これは、置換する必要があるフォントの名前である必要があります。 2 番目のパラメーターは型の配列です。**ストリング**.ユーザーは、元のフォント名 (最初のパラメーターで指定) の代わりに、フォント名のリストを提供できます。

簡単な使用シナリオを次に示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **情報収集**

上記のメソッドに加えて、Aspose.Cells API は、設定されているソースと置換に関する情報を収集する手段も提供しています。

1. **[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)**メソッドは型の配列を返します**[FontSourceBase](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase)**指定されたフォント ソースのリストが含まれています。ソースが設定されていない場合、**[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)**メソッドは空の配列を返します。
1. **[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)**メソッドは型のパラメータを受け入れます**ストリング**置換を設定したフォント名を指定できるようになりました。指定されたフォント名に代替が設定されていない場合は、**[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)**メソッドは null を返します。

## **先行トピック**
- [スプレッドシートを画像にレンダリングする際のデフォルト フォントの設定](/cells/ja/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [PdfSaveOptions と ImageOrPrintOptions の DefaultFont プロパティを優先するように設定する](/cells/ja/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [サポートされているフォント形式](/cells/ja/net/supported-font-formats/)
- [Worksheet to Image - レンダリング イメージのピクセル形式の設定](/cells/ja/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
