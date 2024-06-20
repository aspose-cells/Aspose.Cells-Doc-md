---
title: スプレッドシートのレンダリングのためのフォントの設定
type: docs
weight: 10
url: /ja/net/configuring-fonts-for-rendering-spreadsheets/
---

## **可能な使用シナリオ**

Aspose.Cells API は、スプレッドシートを画像形式でレンダリングしたり、PDF & XPS 形式に変換したりする機能を提供します。変換の精度を最大限にするためには、スプレッドシートで使用されているフォントがオペレーティングシステムのデフォルトのフォントディレクトリに存在する必要があります。必要なフォントが存在しない場合、Aspose.Cells API は代替のフォントを使用しようとします。

## **フォントの選択**

Aspose.Cells API が裏で行うプロセスは以下の通りです。

1. API は、スプレッドシートで使用されている正確なフォント名と一致するフォントをファイルシステムで検索しようとします。
1. API が正確な同じ名前のフォントを見つけられない場合、ワークブックの [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) プロパティで指定されたデフォルトフォントを使用しようとします。
1. API がワークブックの [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) プロパティで定義されたフォントを見つけられない場合、[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) または [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) プロパティで指定されたフォントを使用しようとします。
1. API が [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) または [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) プロパティで定義されたフォントを見つけられない場合、[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname) プロパティで指定されたフォントを使用しようとします。
1. API が [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname) プロパティで定義されたフォントを見つけられない場合、利用可能なすべてのフォントから最適なフォントを選択しようとします。
1. 最終的に API がファイルシステムでフォントを見つけられない場合、Arial を使用してスプレッドシートをレンダリングします。

## **カスタムフォントフォルダの設定**

Aspose.CellsのAPIは、必要なフォントをオペレーティングシステムのデフォルトフォントディレクトリで検索します。必要なフォントがシステムのフォントディレクトリにない場合は、APIはカスタム（ユーザー定義）ディレクトリを検索します。[**FontConfigs**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs)クラスでは、以下に詳細を示しますが、カスタムフォントディレクトリを設定するためのいくつかの方法を公開しています。

1.[**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder): このメソッドは1つのフォルダだけを設定する場合に有用です。
1.[**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders): このメソッドは、フォントが複数のフォルダに存在し、ユーザーがすべてのフォルダを単一のフォルダにまとめるのではなく、それぞれ別々に設定したい場合に有用です。
1.[**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources): このメカニズムは、ユーザーが複数のフォルダからフォントを読み込む場合や、単一のフォントファイルやバイト配列からフォントデータを読み込みたい場合に有用です。

{{% alert color="primary" %}}

両方の[**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)および[**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)メソッドは、2番目のパラメータとしてBoolean型を受け付けます。2番目のパラメータに**true**を渡すと、Aspose.Cells APIはフォントファイルをサブフォルダーで検索します。

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

上記のいずれかの方法を、アプリケーションの開始時に（つまり、Aspose.Cellsの他のオブジェクトを呼び出す前に）使用してください。

{{% /alert %}} {{% alert color="primary" %}}

フォントソースを設定するために上記のすべての方法を使用した場合、最後に設定したもののみが有効になります。

{{% /alert %}}

## **フォントの代替メカニズム**

Aspose.CellsのAPIは、レンダリングに使用する代替フォントを指定する機能も提供します。このメカニズムは、必要なフォントが変換を行うマシンに存在しない場合に役立ちます。ユーザーは元々必要なフォントの代替として、フォント名のリストを提供することができます。これを実現するために、Aspose.CellsのAPIは、2つのパラメータを受け入れる[**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes)メソッドを公開しています。最初のパラメータは**string**型であり、代替が必要なフォントの名前でなければなりません。2番目のパラメータは**string**型の配列です。ユーザーは、最初のパラメータで指定されたオリジナルのフォント名の代替として、フォント名のリストを提供することができます。

以下は単純な使用シナリオです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **情報収集**

上記の方法に加えて、Aspose.Cells APIには設定されているソースと代替に関する情報を収集する手段も提供されています。

1. [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)メソッドは、指定されたフォントソースのリストを含む[**FontSourceBase**](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase)型の配列を返します。ソースが設定されていない場合は、[**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)メソッドは空の配列を返します。
1. [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)メソッドは、指定されたフォント名の代替が設定されていることを許可する**string**型のパラメータを受け入れます。指定されたフォント名のための代替が設定されていない場合、[**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)メソッドはnullを返します。

## **高度なトピック**
- [スプレッドシートを画像にレンダリングする際のデフォルトフォントの設定](/cells/ja/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [PdfSaveOptionsおよびImageOrPrintOptionsのDefaultFontプロパティを優先するために設定します](/cells/ja/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [サポートされるフォント形式](/cells/ja/net/supported-font-formats/)
- [ワークシートを画像に変換 - レンダリングされた画像のピクセル形式を設定する](/cells/ja/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
