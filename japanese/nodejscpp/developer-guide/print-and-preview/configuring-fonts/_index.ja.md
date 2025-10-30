---
title: Node.jsを使用したスプレッドシートのレンダリング用フォントの構成例 C++経由
linktitle: スプレッドシートのレンダリングのためのフォントの設定
type: docs
weight: 10
url: /ja/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Aspose.Cells for Node.js via C++を使用してスプレッドシートのレンダリングに適したフォントの構成方法を学びます。最適な変換精度を保つためにフォントは利用可能である必要があります。
---

## **可能な使用シナリオ**

Aspose.Cells APIは、スプレッドシートを画像形式でレンダリングしたり、PDFやXPS形式に変換したりする機能を提供します。変換の精度を最大化するためには、スプレッドシートで使用されるフォントがOSの標準フォントディレクトリに存在する必要があります。必要なフォントがない場合、Aspose.Cells APIは利用可能なフォントに置き換えようとします。

## **フォントの選択**

Aspose.Cells API が裏で行うプロセスは以下の通りです。

1. API は、スプレッドシートで使用されている正確なフォント名と一致するフォントをファイルシステムで検索しようとします。
1. API が正確な同じ名前のフォントを見つけられない場合、ワークブックの [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) プロパティで指定されたデフォルトフォントを使用しようとします。
1. API がワークブックの [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) プロパティで定義されたフォントを見つけられない場合、[**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) または [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) プロパティで指定されたフォントを使用しようとします。
1. API が [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) または [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) プロパティで定義されたフォントを見つけられない場合、[**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--) プロパティで指定されたフォントを使用しようとします。
1. API が [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--) プロパティで定義されたフォントを見つけられない場合、利用可能なすべてのフォントから最適なフォントを選択しようとします。
1. 最終的に API がファイルシステムでフォントを見つけられない場合、Arial を使用してスプレッドシートをレンダリングします。

## **カスタムフォントフォルダの設定**

Aspose.Cells APIは、必要なフォントが存在しない場合の代替フォントの指定も可能です。ユーザーはフォント名のリストを用意して、元々必要だったフォントの代わりに指定できます。このために、Aspose.Cells APIは[**FontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs)メソッドを公開しており、これは2つのパラメータを受け取ります。最初のパラメータは**string**型で、置換するフォント名を指定します。2つ目のパラメータは**string**型の配列で、元のフォントの代わりに使用するフォント名のリストを提供します。

1.[**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-): このメソッドは1つのフォルダだけを設定する場合に有用です。
1.[**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-): このメソッドは、フォントが複数のフォルダに存在し、ユーザーがすべてのフォルダを単一のフォルダにまとめるのではなく、それぞれ別々に設定したい場合に有用です。
1.[**FontConfigs.setFontSources(FontSourceBase[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSources-fontsourcebasearray-): このメカニズムは、ユーザーが複数のフォルダからフォントを読み込む場合や、単一のフォントファイルやバイト配列からフォントデータを読み込みたい場合に有用です。

{{% alert color="primary" %}}

両方の[**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-)および[**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-)メソッドは、2番目のパラメータとしてBoolean型を受け付けます。2番目のパラメータに**true**を渡すと、Aspose.Cells APIはフォントファイルをサブフォルダーで検索します。

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Defining string variables to store paths to font folders & font file
const fontFolder1 = path.join(dataDir, "Arial");
const fontFolder2 = path.join(dataDir, "Calibri");
const fontFile = path.join(dataDir, "arial.ttf"); 

// Setting first font folder with SetFontFolder method
// Second parameter directs the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method
// Second parameter prohibits the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolders([fontFolder1, fontFolder2], false);

// Defining FolderFontSource
const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

// Defining FileFontSource
const sourceFile = new AsposeCells.FileFontSource(fontFile);

// Defining MemoryFontSource
const sourceMemory = new AsposeCells.MemoryFontSource(require("fs").readFileSync(fontFile));

// Setting font sources
AsposeCells.FontConfigs.setFontSources([sourceFolder, sourceFile, sourceMemory]);
```

{{% alert color="primary" %}}

上記のいずれかの方法を、アプリケーションの開始時に（つまり、Aspose.Cellsの他のオブジェクトを呼び出す前に）使用してください。

{{% /alert %}} {{% alert color="primary" %}}

フォントソースを設定するために上記のすべての方法を使用した場合、最後に設定したもののみが有効になります。

{{% /alert %}}

## **フォントの代替メカニズム**

Aspose.Cells API は、変換時に必要なフォントが利用できない場合に備えて、代替フォントを指定する機能も提供しています。ユーザーは、オリジナルのフォントの代わりに使用可能なフォント名のリストを指定できます。このために、Aspose.Cells API では [**FontConfigs.setFontSubstitutes(string, string[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSubstitutes-string-stringarray-) メソッドを公開しており、2つのパラメータを受け取ります。最初のパラメータは **string** 型で、代替フォントの名前を指定します。二つ目のパラメータは **string** の配列で、代替フォント名のリストを提供します。

以下は単純な使用シナリオです。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Substituting the Arial font with Times New Roman & Calibri
AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
```

## **情報収集**

上記の方法に加え、Aspose.Cells APIは設定されたソースと置換に関する情報を収集する手段も提供しています。

1. [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--)メソッドは、指定されたフォントソースのリストを含む[**FontSourceBase**](https://reference.aspose.com/cells/nodejs-cpp/fontsourcebase)型の配列を返します。ソースが設定されていない場合、[**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--)メソッドは空の配列を返します。
1. [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-)メソッドは、置換が設定されているフォント名を指定できる**string**型のパラメータを受け取ります。指定されたフォントに対して置換が設定されていない場合、[**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-)メソッドはnullを返します。

## **高度なトピック**
- [スプレッドシートを画像にレンダリングする際のデフォルトフォントの設定](/cells/ja/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [PdfSaveOptionsおよびImageOrPrintOptionsのDefaultFontプロパティを優先するために設定します](/cells/ja/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [サポートされるフォント形式](/cells/ja/nodejs-cpp/supported-font-formats/)
- [ワークシートを画像に変換 - レンダリングされた画像のピクセル形式を設定する](/cells/ja/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="nodejs-cpp" >}}
