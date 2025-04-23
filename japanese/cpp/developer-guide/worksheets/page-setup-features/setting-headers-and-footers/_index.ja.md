---
title: ヘッダーとフッターの設定（C++）
linktitle: ヘッダーとフッターの設定
type: docs
weight: 30
url: /ja/cpp/setting-headers-and-footers/
description: この記事では、C++ APIまたはライブラリのスクリプトコマンドを使用して、Excelのワークシートのヘッダーとフッターに画像をプログラムで挿入する方法を説明します。
keywords: Excelのヘッダーとフッターに画像を挿入するC++コード、スクリプトコマンドによる設定
---

{{% alert color="primary" %}}

ヘッダーとフッターはそれぞれ上部の余白の下に表示されるテキスト行です。ワークシートにもヘッダーやフッターを追加することができます。ヘッダーやフッターには、ページ番号、著者名、トピック名、または日付と時刻などの有用な情報を表示することができます。ヘッダーとフッターはページ設定の設定を使用して管理されます。

{{% /alert %}}

## **ヘッダーとフッタの設定**

Aspose.Cells はランタイムでワークシートにヘッダーやフッターを追加することができますが、印刷のために事前に設計されたファイルでヘッダーとフッターを手動で設定することをお勧めします。Microsoft Excel を GUI ツールとして使用して、ヘッダーやフッターを設定して手間と開発時間を節約することができます。Aspose.Cells はそのファイルをインポートして設定を保存することができます。

ヘッダーやフッターをランタイムで追加するために、Aspose.Cells は特別な API 呼び出しとスクリプトコマンドを提供しています。

### **スクリプトコマンド**

スクリプトコマンドは、ヘッダーやフッターのフォーマットを設定する特別なコマンドです。

|**スクリプトコマンド**|**説明**|
| :- | :- |
|&P|現在のページ番号
|&G|画像
|&N|ページの総数
|&D|現在の日付
|&T|現在の時刻
|&A|ワークシート名
|&F|パスを除いたファイル名
|&&Text|は &Text を表示します。例： &&WO は &WO と表示されます|
|&"\<FontName>"|フォント名を表します。例: &"Arial"
|&"\<FontName>, \<FontStyle>"|スタイル付きのフォント名を表します。例: &"Arial,Bold"
|&\<FontSize>|フォントサイズを表します。例：「&14abc」。ただし、このコマンドの後にヘッダーに印刷されるプレーンな数字が続く場合、その数字はフォントサイズとスペースで区切る必要があります。例：「&14 123」。|

### **ヘッダーやフッタの設定**

[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) クラスは、ワークシートにヘッダーやフッターを追加するために使用される [**SetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheader/) と [**SetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooter/) という二つのメソッドを提供します。これらのメソッドは2つのパラメーターのみを取ります。

- **Section** – ヘッダーやフッターを配置するセクション。左、中央、右の3つのセクションがあり、それぞれ0、1、2で表されます。
- **Script** – ヘッダーやフッターのために使用するスクリプト。このスクリプトにはヘッダーやフッターをフォーマットするためのスクリプトコマンドが含まれます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook excel;

    // Get the first worksheet's PageSetup
    PageSetup pageSetup = excel.GetWorksheets().Get(0).GetPageSetup();

    // Set worksheet name at the left section of the header
    pageSetup.SetHeader(0, u"&A");

    // Set current date and time at the central section of the header with custom font
    pageSetup.SetHeader(1, u"&\"Times New Roman,Bold\"&D-&T");

    // Set current file name at the right section of the header with custom font
    pageSetup.SetHeader(2, u"&\"Times New Roman,Bold\"&12&F");

    // Set a string at the left section of the footer with custom font for part of the string
    pageSetup.SetFooter(0, u"Hello World! &\"Courier New\"&14 123");

    // Set the current page number at the central section of the footer
    pageSetup.SetFooter(1, u"&P");

    // Set page count at the right section of the footer
    pageSetup.SetFooter(2, u"&N");

    // Save the workbook
    excel.Save(u"SetHeadersAndFooters_out.xls");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **ヘッダーやフッターに画像を挿入**

[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) クラスには、ヘッダーやフッターに画像を追加するために使用される [**SetHeaderPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheaderpicture/) と [**SetFooterPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooterpicture/) という追加のメソッドがあります。これらのメソッドは以下のパラメーターを取ります。

- **Section** – 画像が配置されるヘッダーやフッターセクション。左、中央、右の3つのセクションがあり、それぞれ0、1、2で表されます。
- **バイト配列** – グラフィカルデータ（バイナリデータはバイト配列のバッファに書き込む必要があります）。

以下のコードを実行し、ファイルを開いた後、ワークシートのヘッダーを確認してください。

1. **ファイル** メニューから **ページ設定** を選択します。ダイアログが表示されます。
1. **ヘッダー/フッター** タブを選択します。

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Creating a Workbook object
    Workbook workbook;

    // Creating a string variable to store the url of the logo/picture
    U16String logo_url = srcDir + u"aspose-logo.jpg";

    // Declaring a FileStream object
    ifstream inFile;

    // Declaring a byte array
    vector<uint8_t> binaryData;

    // Opening the logo/picture in the stream
    inFile.open(logo_url.ToUtf8(), ios::binary);

    if (inFile.is_open())
    {
        // Get the size of the file
        inFile.seekg(0, ios::end);
        size_t fileSize = inFile.tellg();
        inFile.seekg(0, ios::beg);

        // Resize the byte array to the size of the file
        binaryData.resize(fileSize);

        // Read the file into the byte array
        inFile.read(reinterpret_cast<char*>(binaryData.data()), fileSize);

        // Creating a PageSetup object to get the page settings of the first worksheet of the workbook
        PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

        // Convert std::vector to Aspose::Cells::Vector
        Aspose::Cells::Vector<uint8_t> asposeBinaryData(binaryData.data(), static_cast<int32_t>(binaryData.size()));

        // Setting the logo/picture in the central section of the page header
        pageSetup.SetHeaderPicture(1, asposeBinaryData);

        // Setting the script for the logo/picture
        pageSetup.SetHeader(1, u"&G");

        // Setting the Sheet's name in the right section of the page header with the script
        pageSetup.SetHeader(2, u"&A");

        // Saving the workbook
        workbook.Save(outDir + u"InsertImageInHeaderFooter_out.xls");

        // Closing the FileStream object
        inFile.close();
    }
    else
    {
        cerr << "Failed to open the image file." << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
