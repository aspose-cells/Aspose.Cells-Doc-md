---
title: C++でさまざまなファイル保存方法
linktitle: ファイルを保存する
type: docs
weight: 40
url: /ja/cpp/different-ways-to-save-files/
description: Aspose.Cells for C++はさまざまなフォーマットにファイルを保存できます。PDFに保存。HTMLに保存。DOCXに保存。PPTXに保存。JSONに保存。MHTMLに保存。
keywords: Aspose.Cellsを使用してExcelをPDF、HTML、JSON、CSV、TXT、XML、DOCX、PPTX、MHT、MHTMLに保存または変換し、C++でワークブックをPDF、HTML、JSON、TXT、SQLに保存または変換します。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、様々な方法でファイルを作成して保存することができます。この記事ではファイルを保存するさまざまな方法について説明します。

{{% /alert %}}

## **ファイルを保存する異なる方法**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)を提供し、Excelファイルを操作するために必要なプロパティとメソッドを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスは、Excelファイルを保存するために使用される[**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドを提供します。[**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドには、さまざまな方法でファイルを保存するために使用される多くのオーバーロードがあります。

ファイルの保存形式は、[**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)列挙型によって決定されます。

|**ファイルの形式の種類**|**説明**|
| :- | :- |
|CSV|CSVファイルを表します|
|Excel97To2003|はExcel 97-2003ファイルを表します
|Xlsx|Excel 2007 XLSXファイルを表します|
|Xlsm|Excel 2007 XLSMファイルを表します|
|Xltx|Excel 2007テンプレートXLTXファイルを表します|
|Xltm|Excel 2007マクロ有効XLTMファイルを表します|
|Xlsb|Excel 2007バイナリXLSBファイルを表します|
|SpreadsheetML|スプレッドシートXMLファイルを表します|
|TSV|タブ区切り値ファイルを表します|
|TabDelimited|はタブ区切りのテキストファイルを表します
|ODS|ODSファイルを表します|
|Html|HTMLファイルを表します|
|MHtml|MHTMLファイルを表します|
|Pdf|PDFファイルを表します|
|XPS|XPSドキュメントを表します|
|TIFF|タグ付き画像ファイル形式（TIFF）を表します|

## **異なる形式でファイルを保存する方法**

ファイルを保存するには、[**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)列挙型からの所望のファイル形式を指定して、[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)オブジェクトの[**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドを呼び出す際にファイル名（保存先パスを含む）を指定します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xls";

    // Load your source workbook
    Workbook workbook(filePath);

    // Save in Excel 97 to 2003 format
    workbook.Save(outDir + u".output.xls");
    // OR
    XlsSaveOptions xlsSaveOptions;
    workbook.Save(outDir + u".output.xls", xlsSaveOptions);

    // Save in Excel2007 xlsx format
    workbook.Save(outDir + u".output.xlsx", SaveFormat::Xlsx);

    // Save in Excel2007 xlsb format
    workbook.Save(outDir + u".output.xlsb", SaveFormat::Xlsb);

    // Save in ODS format
    workbook.Save(outDir + u".output.ods", SaveFormat::Ods);

    // Save in Pdf format
    workbook.Save(outDir + u".output.pdf", SaveFormat::Pdf);

    // Save in Html format
    workbook.Save(outDir + u".output.html", SaveFormat::Html);

    // Save in SpreadsheetML format
    workbook.Save(outDir + u".output.xml", SaveFormat::SpreadsheetML);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **WorkbookをPDFに保存する方法**
Portable Document Format（PDF）は、1990年代にAdobeによって作成されたドキュメントの一種です。このファイル形式の目的は、アプリケーションソフトウェア、ハードウェア、およびオペレーティングシステムに依存しない形式で、文書やその他のリファレンス資料を表現するための標準を導入することでした。PDFファイル形式には、テキスト、画像、ハイパーリンク、フォームフィールド、リッチメディア、デジタル署名、添付ファイル、メタデータ、地理空間機能、3Dオブジェクトなどの情報を含めるための完全な機能があります。

Aspose.CellsでWorkbookをPDFファイルに保存する方法のコードは次のとおりです:
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the Workbook object
    Workbook workbook;

    // Set value to Cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"Hello World!");

    // Save the workbook to PDF
    workbook.Save(u"pdf1.pdf");

    // Save as Pdf format compatible with PDFA-1a
    PdfSaveOptions saveOptions;
    saveOptions.SetCompliance(PdfCompliance::PdfA1a);

    workbook.Save(u"pdfa1a.pdf", saveOptions);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **WorkbookをテキストまたはCSV形式で保存する方法**

時々、複数のワークシートを含むワークブックをテキスト形式に変換または保存したい場合があります。テキスト形式（たとえば、TXT、TabDelim、CSVなど）の場合、デフォルトでMicrosoft ExcelおよびAspose.Cellsの両方はアクティブなワークシートの内容のみを保存します。

以下のコード例では、ワークブック全体をテキスト形式で保存する方法について説明しています。任意のMicrosoft ExcelまたはOpenOfficeスプレッドシートファイル（XLS、XLSX、XLSM、XLSB、ODSなど）を読み込み、任意の数のワークシートを含めることができます。

コードを実行すると、ワークブックのすべてのシートのデータがTXT形式に変換されます。

同じ例を修正して、CSV形式でファイルを保存することも可能です。デフォルトでは、区切り文字はカンマ（,）ですので、CSV形式で保存する場合は区切り文字を指定しないでください。注意点として、評価版を使用している場合でも `[**TxtSaveOptions.GetExportAllSheets()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getexportallsheets/)` プロパティがtrueに設定されている場合でも、プログラムは一つのワークシートだけをエクスポートします。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output text file
    U16String outputFilePath = outDir + u"out.txt";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook data saved to text file successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **カスタム区切り記号を使用してテキストファイルにファイルを保存する方法**

テキストファイルには書式がないスプレッドシートデータが含まれます。ファイルは、データ間にいくつかのカスタマイズされた区切り記号があるプレーンテキストファイルの種類です。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';');

    // Save the file with the options
    wb.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **ストリームにファイルを保存する方法**

ファイルをストリームに保存するには、*MemoryStream*または*FileStream*オブジェクトを作成し、[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)オブジェクトの[**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドを呼び出してそのストリームオブジェクトにファイルを保存します。[**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドを呼び出す際に、所望のファイル形式を[**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)列挙型を使用して指定します。

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```

## **ExcelファイルをHTMLとMHTファイルに保存する方法**
Aspose.Cellsは、単にExcelファイル、JSON、CSVなどのファイルを.htmlおよび.mhtファイルとして簡単に保存できます。
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    Workbook workbook(inputFilePath);

    // Save file to MHTML format
    U16String outputFilePath(u"out.mht");
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully to MHTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **ExcelファイルをOpenOffice（ODS、SXC、FODS、OTS）に保存する方法**
ファイルを開いた形式で保存できます：ODS、SXC、FODS、OTSなど。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file
    workbook.Save(u"Out.ods");

    // Save as sxc file
    workbook.Save(u"Out.sxc");

    // Save as fods file
    workbook.Save(u"Out.fods");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **ExcelファイルをJSONまたはXMLに保存する方法**

JSON（JavaScript Object Notation）は、人間が読めるテキストを使用してデータを格納および送信するためのオープンな標準ファイル形式です。 JSONファイルは.json拡張子で保存されます。 JSONはより少ないフォーマットが必要であり、XMLの良い代替手段です。 JSONはJavaScriptに由来していますが、言語に依存しないデータ形式です。 JSONの生成と解析は、多くの現代のプログラミング言語でサポートされています。 application/jsonはJSONに使用されるメディアタイプです。

Aspose.CellsはファイルをJSONまたはXMLに保存することをサポートしています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output json file
    U16String outputFilePath = outDir + u"book1.json";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **高度なトピック**
- [ワークブックの圧縮レベルを調整](/cells/ja/cpp/adjust-workbook-compression-level/)
- [ストリクトなOpen XMLスプレッドシート形式でワークブックを保存](/cells/ja/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [レスポンスオブジェクトへのファイルの保存](/cells/ja/cpp/saving-file-to-response-object/)
{{< app/cells/assistant language="cpp" >}}
