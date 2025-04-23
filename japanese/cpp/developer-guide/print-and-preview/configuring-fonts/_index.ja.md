---
title: フォント設定によるスプレッドシートのレンダリング（C++）
linktitle: スプレッドシートのレンダリングのためのフォントの設定
type: docs
weight: 10
url: /ja/cpp/configuring-fonts-for-rendering-spreadsheets/
description: Aspose.Cells for C++を使用して、スプレッドシートを画像、PDF、XPS形式にレンダリングするためのフォント設定方法を学びます。
---

## **可能な使用シナリオ**

Aspose.CellsのAPIは、スプレッドシートを画像形式にレンダリングしたり、PDFやXPSに変換したりする機能を提供します。変換精度を最大化するためには、スプレッドシートで使用されるフォントがオペレーティングシステムのデフォルトフォントディレクトリに存在する必要があります。必要なフォントが存在しない場合、Aspose.Cellsは利用可能なフォントで置き換えを試みます。

## **フォントの選択**

以下は、Aspose.Cells APIが裏で実行するプロセスです：

1. API は、スプレッドシートで使用されている正確なフォント名と一致するフォントをファイルシステムで検索しようとします。
1. APIが正確な名前のフォントを見つけられない場合、Workbookの[**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)プロパティで指定された既定のフォントを使用しようとします。
1. APIがWorkbookの[**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)プロパティで定義されたフォントを見つけられない場合、[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/)または[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)プロパティで指定されたフォントを使用しようとします。
1. APIが[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/)または[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)プロパティで定義されたフォントを見つけられない場合、[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/)プロパティで指定されたフォントを使用しようとします。
1. [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/)プロパティで定義されたフォントを見つけられない場合、利用可能なすべてのフォントから最も適したフォントを選択しようとします。
1. 最終的に、APIがファイルシステム上のフォントを見つけられない場合、スプレッドシートをArialを使用してレンダリングします。

## **カスタムフォントフォルダの設定**

Aspose.Cells APIは、必要なフォントをオペレーティングシステムの既定のフォントディレクトリから検索します。必要なフォントがシステムのフォントディレクトリにない場合、APIはカスタム（ユーザー定義）ディレクトリを検索します。[**FontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/)クラスは、以下の詳細な方法でカスタムフォントディレクトリを設定する手段を提供します：

1.[**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/): このメソッドは1つのフォルダだけを設定する場合に有用です。
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/)：この方法は、複数のフォルダにフォントが存在し、すべてのフォルダを個別に設定したい場合に便利です。
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsources/)：この仕組みは、複数のフォルダ、単一のフォントファイル、またはバイト配列からフォントデータをロードしたい場合に役立ちます。

{{% alert color="primary" %}}

[**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/)および[**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/)の両方のメソッドは、Boolean型の第2パラメータを受け取ります。第2パラメータに**true**を渡すと、Aspose.Cells APIはサブフォルダ内のフォントファイルを検索します。

{{% /alert %}}

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

Vector<uint8_t> GetDataFromFile(const U16String& file)
{
    std::string f = file.ToUtf8();
    // open a file 
    std::ifstream fileStream(f, std::ios::binary);

    if (!fileStream.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    // Get file size
    fileStream.seekg(0, std::ios::end);
    std::streampos fileSize = fileStream.tellg();
    fileStream.seekg(0, std::ios::beg);

    // Read file contents into uint8_t array
    uint8_t* buffer = new uint8_t[fileSize];
    fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
    fileStream.close();

    Vector<uint8_t>data(buffer, fileSize);
    delete[] buffer;

    return data;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String fontFolder1 = srcDir + u"Arial";
    U16String fontFolder2 = srcDir + u"Calibri";
    U16String fontFile = srcDir + u"arial.ttf";

    FontConfigs::SetFontFolder(fontFolder1, true);

    Vector<U16String> fontFolders{ fontFolder1 , fontFolder2 };

    FontConfigs::SetFontFolders(fontFolders, false);

    FolderFontSource sourceFolder(fontFolder1, false);
    FileFontSource sourceFile(fontFile);
    Vector<uint8_t> fontData = GetDataFromFile(fontFile);
    MemoryFontSource sourceMemory(fontData);

    Vector<FontSourceBase> fontSources{ sourceFolder ,sourceFile ,sourceMemory };

    FontConfigs::SetFontSources(fontSources);

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

上記のいずれかの方法をアプリケーションの開始時に、つまり他のAspose.Cells APIオブジェクトを呼び出す前に使用してください。

{{% /alert %}}

{{% alert color="primary" %}}

フォントソースを設定するために上記のすべての方法を使用した場合、最後に設定したもののみが有効になります。

{{% /alert %}}

## **フォントの代替メカニズム**

Aspose.Cells APIはまた、レンダリング目的の代替フォントを指定する機能も提供しています。この仕組みは、変換を行うマシンに必要なフォントがない場合に役立ちます。ユーザーは、必要なフォント名のリストを代替フォントとして提供できます。このために、Aspose.Cells APIは[**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsubstitutes/)メソッドを公開しており、2つのパラメータを受け取ります。最初のパラメータは**string**型で、置換が必要なフォント名を指定します。2つ目のパラメータは**string**型の配列で、元のフォント名（最初のパラメータに指定）に代わるフォント名のリストを提供できます。

簡単な使用例はこちら：

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Substituting the Arial font with Times New Roman & Calibri
    Vector<U16String> substituteFonts{ u"Times New Roman", u"Calibri" };
    FontConfigs::SetFontSubstitutes(u"Arial", substituteFonts);

    Aspose::Cells::Cleanup();
}
```

## **情報収集**

上記の方法に加え、Aspose.Cells APIは設定されたフォントの情報や代替設定を収集する手段も提供しています：

1. [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/)メソッドは、指定されたフォントソースのリストを含む[**FontSourceBase**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsourcebase/)型の配列を返します。フォントソースが設定されていない場合、[**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/)メソッドは空の配列を返します。
1. [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/)メソッドは、置換設定がされたフォント名を指定できる**string**型のパラメータを受け取ります。指定したフォント名に対する置換設定がない場合、[**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/)メソッドはnullを返します。

## ** 高度なトピック**
- [スプレッドシートを画像にレンダリングする際のデフォルトフォントの設定](/cells/ja/cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [PdfSaveOptionsおよびImageOrPrintOptionsのDefaultFontプロパティを優先するために設定します](/cells/ja/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [サポートされるフォント形式](/cells/ja/cpp/supported-font-formats/)
