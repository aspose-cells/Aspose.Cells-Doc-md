---
title: 異なる Microsoft Excel バージョンのファイルを開く
type: docs
weight: 20
url: /ja/net/opening-different-microsoft-excel-versions-files/
description: この記事では、Aspose.Cells for .NET API を使用して、異なる Excel バージョンのファイルを開く方法について説明します。
keywords: C# Open Different Microsoft Excel file, How do I open Encrypted Excel Files.
---
{{% alert color="primary" %}}

Aspose.Cells は、Microsoft Excel 95/97 - 2003、SpreadsheetML、opening Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 XLSX または En など、さまざまな Microsoft Excel バージョン ファイルを開くことができます。暗号化された Excel ファイル。

{{% /alert %}}

##  **異なる Microsoft Excel バージョンのファイルを開く方法**

多くの場合、アプリケーションは、さまざまなバージョンで作成された Microsoft Excel ファイル (たとえば、 Microsoft Excel 95、97、または Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 ) を開くことができなければなりません。 XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited または TSV、CSV、ODS など、いくつかの形式のいずれかでファイルをロードする必要がある場合があります。コンストラクターを使用するか、**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**クラス'**[ファイル形式](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** type 属性を使用して形式を指定します。**[ファイル形式タイプ](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**列挙。

の**[ファイル形式タイプ](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**列挙には、事前定義されたファイル形式が多数含まれており、その一部を以下に示します。

|**ファイル形式の種類**|**説明**|
| :- | :- |
|CSV|CSV ファイルを表します|
|Excel97To2003|Excel 97 ～ 2003 ファイルを表します|
|XLSX|Excel 2007/2010/2013/2016/2019 および Office 365 XLSX ファイルを表します|
|Xlsm|Excel 2007/2010/2013/2016/2019 および Office 365 XLSM ファイルを表します|
|Xltx|Excel 2007/2010/2013/2016/2019 および Office 365 テンプレート XLTX ファイルを表します|
|Xltm|Excel 2007/2010/2013/2016/2019 および Office 365 マクロが有効な XLTM ファイルを表します|
|Xlsb|Excel 2007/2010/2013/2016/2019 および Office 365 バイナリ XLSB ファイルを表します|
|SpreadsheetML|SpreadsheetML ファイルを表します|
|ツブ|タブ区切り値ファイルを表します|
|TabDelimited|タブ区切りテキストファイルを表します|
|オッズ|ODS ファイルを表します|
|HTML|HTML ファイルを表します|
|Mhtml|MHTML ファイルを表します|

###  **Microsoft Excel 95/5.0 ファイルを開く**

Microsoft Excel 95/5.0 ファイルを開くには、次を使用します。**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**関連する属性を設定します。**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**ロードするテンプレートファイルのクラス。この機能をテストするためのサンプル ファイルは、次のリンクからダウンロードできます。

[Excel95ファイル](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

###  **Microsoft Excel 97 - 2003 ファイルを開く**

Microsoft Excel 97 - 2003 ファイルを開くには、次を使用します。**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**関連する属性を設定します。**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**ロードするテンプレートファイルのクラス。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

###  **Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 XLSX ファイルを開く**

Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 形式、つまり XLSX または XLSB を開くには、ファイル パスを指定します。も使用できます**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**関連する属性/オプションを設定します。**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**ロードするテンプレートファイルのクラス。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

###  **暗号化された Excel ファイルを開く**

Microsoft Excel を使用して、暗号化された Excel ファイルを作成することができます。暗号化されたファイルを開くには、**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**ロードするテンプレート ファイルの属性とオプション (パスワードを与えるなど) を設定します。
この機能をテストするためのサンプル ファイルは、次のリンクからダウンロードできます。

[暗号化されたExcel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells は、パスワードで保護された Microsoft Excel 2007、2010、2013、2016、2019、Office 365 ファイルを開くこともサポートしています。


