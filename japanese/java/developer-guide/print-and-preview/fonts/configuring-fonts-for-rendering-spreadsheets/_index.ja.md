---
title: スプレッドシートのレンダリングのためのフォントの設定
type: docs
weight: 10
url: /ja/java/configuring-fonts-for-rendering-spreadsheets/
---

## **可能な使用シナリオ**

Aspose.Cells API は、スプレッドシートを画像形式でレンダリングしたり、PDF & XPS 形式に変換したりする機能を提供します。変換の精度を最大限にするためには、スプレッドシートで使用されているフォントがオペレーティングシステムのデフォルトのフォントディレクトリに存在する必要があります。必要なフォントが存在しない場合、Aspose.Cells API は代替のフォントを使用しようとします。

## **フォントの選択**

Aspose.Cells API が裏で行うプロセスは以下の通りです。

1. API は、スプレッドシートで使用されている正確なフォント名と一致するフォントをファイルシステムで検索しようとします。
1. API が正確な同じ名前のフォントを見つけられない場合、ワークブックの [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) プロパティで指定されたデフォルトフォントを使用しようとします。
1. API がワークブックの [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) プロパティで定義されたフォントを見つけられない場合、[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) または [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) プロパティで指定されたフォントを使用しようとします。
1. API が [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) または [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) プロパティで定義されたフォントを見つけられない場合、[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) プロパティで指定されたフォントを使用しようとします。
1. API が [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) プロパティで定義されたフォントを見つけられない場合、利用可能なすべてのフォントから最適なフォントを選択しようとします。
1. 最終的に API がファイルシステムでフォントを見つけられない場合、Arial を使用してスプレッドシートをレンダリングします。

{{% alert color="primary" %}}

一般的に、Aspose.CellsのAPIはWindows、Linux、MacOSのデフォルトのフォントディレクトリをスキャンします。 [Aspose.Cells for Java 24.7](https://releases.aspose.com/cells/java/release-notes/2024/aspose-cells-for-java-24-7-release-notes/)以降、APIはデフォルトでOfficeキャッシュのクラウドフォントディレクトリもスキャンします。

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.CellsのAPIは例外なく、常にOSのデフォルトフォントディレクトリをスキャンします。ただし、JVM引数**-DAspose.Cells.FontDirExc="YourFontDir"**を設定した場合は除きます。その場合、APIはOSのデフォルトフォントディレクトリのスキャンをスキップし、指定されたパスのみを検索します。

{{% /alert %}}

## **カスタムフォントフォルダの設定**

Aspose.Cells APIは必要なフォントを取得するために、オペレーティングシステムのデフォルトのフォントディレクトリを検索します。システムのフォントディレクトリに必要なフォントがない場合、APIはカスタム（ユーザー定義）ディレクトリを検索します。[**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs)クラスでは、以下に詳細に述べられているように、カスタムフォントディレクトリを設定するためのいくつかの方法が公開されています。

1.[**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder-java.lang.String-boolean-): このメソッドは1つのフォルダだけを設定する場合に有用です。
1.[**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders-java.lang.String[]-boolean-): このメソッドは、フォントが複数のフォルダに存在し、ユーザーがすべてのフォルダを単一のフォルダにまとめるのではなく、それぞれ別々に設定したい場合に有用です。
1.[**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources-com.aspose.cells.FontSourceBase[]-): このメカニズムは、ユーザーが複数のフォルダからフォントを読み込む場合や、単一のフォントファイルやバイト配列からフォントデータを読み込みたい場合に有用です。

{{% alert color="primary" %}}

[**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder-java.lang.String-boolean-)および[**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders-java.lang.String[]-boolean-)の両メソッドは、ブール型の2番目のパラメーターを受け入れます。2番目のパラメーターとして**true**を渡すと、Aspose.Cells APIはフォントファイルのサブフォルダーを検索します。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

上記のいずれかの方法をアプリケーションの開始時に使用してください。つまり、Aspose.Cells APIの他のオブジェクトを呼び出す前に使用してください。

{{% /alert %}} {{% alert color="primary" %}}

上記の方法のいずれよりも複数の方法を使用してフォントソースを設定した場合、最後の設定のみが有効になります。

{{% /alert %}}

## **フォントの代替メカニズム**

Aspose.Cells APIは、レンダリングのための代替フォントを指定する機能も提供します。このメカニズムは、必要なフォントが変換を行うマシンに存在しない場合に役立ちます。ユーザーはオリジナルの必要なフォントの代わりとしてフォント名のリストを指定できます。このために、Aspose.Cells APIはFontConfigs.setFontSubstitutesメソッドを公開しており、これは2つのパラメーターを受け入れます。1つ目のパラメーターは**String**型であり、代替する必要のあるフォントの名前でなければなりません。2つ目のパラメーターは**String**型の配列でなければなりません。ユーザーはオリジナルのフォントに代わる代替としてのフォント名のリストを提供することができます。

以下は単純な使用シナリオです。

{{< highlight java >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

## **情報収集**

上記の方法に加えて、Aspose.Cells APIには設定されているソースと代替に関する情報を収集する手段も提供されています。

1.[**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--): このメソッドは、指定されたフォントソースのリストを含む[**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource)型の配列を返します。ソースが設定されていない場合、[**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--)メソッドは空の配列を返します。
1.[**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes-java.lang.String-): このメソッドは**String**型のパラメーターを受け入れます。これを使用して設定したフォント名を指定することができます。指定されたフォント名に対する代替が設定されていない場合、[**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes-java.lang.String-)メソッドはnullを返します。
{{< app/cells/assistant language="java" >}}
