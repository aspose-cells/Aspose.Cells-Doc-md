---
title: スプレッドシートのレンダリングのためのフォントの設定
type: docs
weight: 10
url: /ja/python-net/configuring-fonts-for-rendering-spreadsheets/
---

## **可能な使用シナリオ**

Aspose.Cells for Python via .NETのAPIは、スプレッドシートを画像フォーマットにレンダリングしたり、PDFやXPSフォーマットに変換する機能を提供します。変換の忠実性を最大化するには、スプレッドシートで使用されるフォントがOSの標準フォントディレクトリにある必要があります。必要なフォントがない場合、Aspose.Cells for Python via .NETのAPIは利用可能なフォントで代替しようとします。

## **フォントの選択**

以下は、Aspose.Cells for Python via .NET APIが裏で実行する処理です。

1. API は、スプレッドシートで使用されている正確なフォント名と一致するフォントをファイルシステムで検索しようとします。
1. API が正確な同じ名前のフォントを見つけられない場合、ワークブックの [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) プロパティで指定されたデフォルトフォントを使用しようとします。
1. API がワークブックの [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) プロパティで定義されたフォントを見つけられない場合、[**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) または [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) プロパティで指定されたフォントを使用しようとします。
1. API が [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) または [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) プロパティで定義されたフォントを見つけられない場合、[**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name) プロパティで指定されたフォントを使用しようとします。
1. API が [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name) プロパティで定義されたフォントを見つけられない場合、利用可能なすべてのフォントから最適なフォントを選択しようとします。
1. 最終的に API がファイルシステムでフォントを見つけられない場合、Arial を使用してスプレッドシートをレンダリングします。

## **カスタムフォントフォルダの設定**

Aspose.Cells for Python via .NETのAPIは、必要なフォントをOSの既定フォントディレクトリから検索します。必要なフォントが見つからない場合は、カスタム（ユーザー定義）ディレクトリを検索します。[**FontConfigs**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs)クラスは、カスタムフォントディレクトリを設定するいくつかの方法を公開しています。詳細は以下に示します。

1.[**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/): このメソッドは1つのフォルダだけを設定する場合に有用です。
1.[**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/): このメソッドは、フォントが複数のフォルダに存在し、ユーザーがすべてのフォルダを単一のフォルダにまとめるのではなく、それぞれ別々に設定したい場合に有用です。
1.[**FontConfigs.set_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_sources/#list): このメカニズムは、ユーザーが複数のフォルダからフォントを読み込む場合や、単一のフォントファイルやバイト配列からフォントデータを読み込みたい場合に有用です。

{{% alert color="primary" %}}

[**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/)および[**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/)メソッドは、Boolean型の第2引数を受け取ります。第2引数に**true**を渡すと、Aspose.Cells for Python via .NETのAPIはサブフォルダ内のフォントファイルも検索します。

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-1.py" >}}

{{% alert color="primary" %}}

上記のいずれかのメソッドを、アプリケーションの開始時に呼び出してください。つまり、Aspose.Cells for Python via .NETのAPIの他のオブジェクトを呼び出す前に呼び出してください。

{{% /alert %}} {{% alert color="primary" %}}

フォントソースを設定するために上記のすべての方法を使用した場合、最後に設定したもののみが有効になります。

{{% /alert %}}

## **フォントの代替メカニズム**

Aspose.Cells for Python via .NETのAPIは、レンダリング目的のために代替フォントを指定する機能も提供しています。この仕組みは、変換を行うマシンに必要なフォントがない場合に役立ちます。ユーザーは、元のフォントの代わりにするフォント名のリストを提供できます。これを実現するため、Aspose.Cells for Python via .NETのAPIは、2つのパラメータを受け取る[**FontConfigs.set_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_substitutes/#str-list)メソッドを公開しています。最初のパラメータは**string**型で、置換に必要なフォント名です。2つ目のパラメータは**string**型のリストで、元のフォント名の代替となるフォント名のリストを提供できます。

以下は単純な使用シナリオです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-FontSubstitution.py" >}}

## **情報収集**

上記の方法に加えて、Aspose.Cells for Python via .NET APIは、設定されたソースや置換情報を収集する手段も提供しています。

1. [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#)メソッドは、指定されたフォントソースのリストを含む[**FontSourceBase**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsourcebase)型の配列を返します。ソースが設定されていない場合は、[**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#)メソッドは空の配列を返します。
1. [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str)メソッドは、指定されたフォント名の代替が設定されていることを許可する**string**型のパラメータを受け入れます。指定されたフォント名のための代替が設定されていない場合、[**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str)メソッドはnullを返します。

## **高度なトピック**
- [スプレッドシートを画像にレンダリングする際のデフォルトフォントの設定](/cells/ja/python-net/set-default-font-while-rendering-spreadsheet-to-images/)
- [PdfSaveOptionsおよびImageOrPrintOptionsのDefaultFontプロパティを優先するために設定します](/cells/ja/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [サポートされるフォント形式](/cells/ja/python-net/supported-font-formats/)
- [ワークシートを画像に変換 - レンダリングされた画像のピクセル形式を設定する](/cells/ja/python-net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)

