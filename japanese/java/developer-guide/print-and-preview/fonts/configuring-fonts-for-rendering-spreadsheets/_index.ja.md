---
title: スプレッドシートをレンダリングするためのフォントの構成
type: docs
weight: 10
url: /ja/java/configuring-fonts-for-rendering-spreadsheets/
---
## **考えられる使用シナリオ**

Aspose.Cells API は、スプレッドシートを画像形式で表示したり、PDF および XPS 形式に変換したりする機能を提供します。変換の忠実度を最大化するには、スプレッドシートで使用されるフォントがオペレーティング システムのデフォルトのフォント ディレクトリで使用できる必要があります。必要なフォントが存在しない場合、Aspose.Cells API は必要なフォントを使用可能なフォントに置き換えようとします。

## **フォントの選択**

以下は、Aspose.Cells API が舞台裏でたどるプロセスです。

1. API は、スプレッドシートで使用されている正確なフォント名に一致するファイル システム上のフォントを見つけようとします。
1.  API がまったく同じ名前のフォントを見つけられない場合、ワークブックの[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font)財産。
1.  API がブックの下に定義されているフォントを見つけられない場合[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font)プロパティで指定されたフォントを使用しようとします。[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont)また[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont)財産。
1.  API で定義されているフォントが見つからない場合[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont)また[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont)プロパティで指定されたフォントを使用しようとします。[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName)財産。
1.  API で定義されているフォントが見つからない場合[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName)プロパティを使用すると、使用可能なすべてのフォントから最適なフォントを選択しようとします。
1. 最後に、API がファイル システムでフォントを見つけられない場合、Arial を使用してスプレッドシートをレンダリングします。

{{% alert color="primary" %}}

 Aspose.Cells API は、1 つの例外を除いて、常にオペレーティング システムのデフォルトのフォント ディレクトリをスキャンします。 JVM引数の場合**-DAspose.Cells.FontDirExc="YourFontDir"**設定されています。その場合、Aspose.Cells API はオペレーティング システムのデフォルト フォント ディレクトリのスキャンをスキップし、前述の JVM 引数で指定されたパスのみを検索します。

{{% /alert %}}

## **カスタム フォント フォルダの設定**

Aspose.Cells API は、オペレーティング システムの既定のフォント ディレクトリで必要なフォントを検索します。必要なフォントがシステムのフォント ディレクトリにない場合、API はカスタム (ユーザー定義) ディレクトリを検索します。の[**FontConfig**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs)クラスは、以下に詳述するように、カスタム フォント ディレクトリを設定する多くの方法を公開しています。

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)): この方法は、設定するフォルダーが 1 つしかない場合に便利です。
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)): この方法は、フォントが複数のフォルダーに存在し、すべてのフォントを 1 つのフォルダーにまとめるのではなく、すべてのフォルダーを個別に設定したい場合に便利です。
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): このメカニズムは、ユーザーが複数のフォルダーまたは単一のフォント ファイルからフォントをロードしたり、バイト配列からフォント データをロードしたい場合に便利です。

{{% alert color="primary" %}}

両方[**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) & [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean) メソッドはブール型の 2 番目のパラメーターを受け入れます。通過**真実**番目のパラメーターとして、Aspose.Cells API に、サブフォルダーでフォント ファイルを検索するように指示します。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

アプリケーションの開始時に上記のいずれかの方法を使用してください。 Aspose.Cells API の他のオブジェクトを呼び出す前。

{{% /alert %}} {{% alert color="primary" %}}

上記の方法を複数使用してフォント ソースを設定した場合、最後の設定のみが有効になります。

{{% /alert %}}

## **フォント置換メカニズム**

Aspose.Cells API は、レンダリング目的で代替フォントを指定する機能も提供します。このメカニズムは、変換が必要なマシンで必要なフォントが利用できない場合に役立ちます。ユーザーは、元々必要だったフォントの代わりに、フォント名のリストを提供できます。これを実現するために、Aspose.Cells API は、2 つのパラメーターを受け入れる FontConfigs.setFontSubstitutes メソッドを公開しました。最初のパラメータの型は**弦**これは、置換する必要があるフォントの名前である必要があります。 2 番目のパラメーターは型の配列です。**弦**.ユーザーは、元のフォント (最初のパラメーターで指定) の代替としてフォント名のリストを提供できます。

簡単な使用シナリオを次に示します。

{{< highlight "java" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

## **情報収集**

上記のメソッドに加えて、Aspose.Cells API は、設定されているソースと置換に関する情報を収集する手段も提供しています。

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources() ): このメソッドは型の配列を返します[**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource)指定されたフォント ソースのリストが含まれています。ソースが設定されていない場合、[**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources()) メソッドは空の配列を返します。
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String) ): このメソッドは型のパラメータを受け入れます**弦**置換を設定したフォント名を指定できるようになりました。指定されたフォント名に代替が設定されていない場合は、[**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)) メソッドは null を返します。
