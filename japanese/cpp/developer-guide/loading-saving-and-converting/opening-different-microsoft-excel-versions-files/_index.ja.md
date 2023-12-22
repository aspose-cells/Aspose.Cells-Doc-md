---
title: 異なる Microsoft Excel バージョンのファイルを開く
type: docs
weight: 20
url: /ja/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells は、Microsoft Excel 95/97 - 2003、SpreadsheetML、opening Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 XLSX または En など、さまざまな Microsoft Excel バージョン ファイルを開くことができます。暗号化された Excel ファイル。

{{% /alert %}}

##  **異なる Microsoft Excel バージョンのファイルを開く**

多くの場合、アプリケーションは、さまざまなバージョンで作成された Microsoft Excel ファイル (たとえば、 Microsoft Excel 95、97、または Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 ) を開くことができなければなりません。 XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited または TSV、CSV、ODS など、いくつかの形式のいずれかでファイルをロードする必要がある場合があります。コンストラクターを使用するか、**[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)**クラス'**[SetFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/)**を使用して形式を指定するメソッド**[ファイル形式タイプ](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**列挙。
	
の**[ファイル形式タイプ](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**列挙には、事前定義されたファイル形式が多数含まれており、その一部を以下に示します。

|**ファイル形式の種類**|**説明**|
| :- | :- |
|ファイル形式タイプ_CSV|CSV ファイルを表します|
|ファイル形式タイプ_Excel97To2003|Excel 97 ～ 2003 ファイルを表します|
|ファイル形式タイプ_Xlsx|Excel 2007/2010/2013/2016/2019 および Office 365 XLSX ファイルを表します|
|ファイル形式タイプ_Xlsm|Excel 2007/2010/2013/2016/2019 および Office 365 XLSM ファイルを表します|
|ファイル形式タイプ_Xltx|Excel 2007/2010/2013/2016/2019 および Office 365 テンプレート XLTX ファイルを表します|
|FileFormatType_Xltm|Excel 2007/2010/2013/2016/2019 および Office 365 マクロが有効な XLTM ファイルを表します|
|ファイル形式タイプ_Xlsb|Excel 2007/2010/2013/2016/2019 および Office 365 バイナリ XLSB ファイルを表します|
|ファイル形式タイプ_スプレッドシートML|SpreadsheetML ファイルを表します|
|ファイル形式タイプ_Tsv|タブ区切り値ファイルを表します|
|FileFormatType_TabDelimited|タブ区切りテキストファイルを表します|
|FileFormatType_Ods|ODS ファイルを表します|
|FileFormatType_Html|HTML ファイルを表します|
|FileFormatType_MHtml|MHTML ファイルを表します|

###  **Microsoft Excel 95/5.0 ファイルを開く**

Microsoft Excel 95/5.0 ファイルを開くには、次を使用します。**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**関連する属性を設定します。**ロードオプション**ロードするテンプレートファイルのクラス。この機能をテストするためのサンプル ファイルは、次のリンクからダウンロードできます。

[Excel95ファイル](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

###  **Microsoft Excel 97 - 2003 ファイルを開く**

Microsoft Excel 97 - 2003 ファイルを開くには、次を使用します。**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**関連する属性を設定します。**ロードオプション**ロードするテンプレートファイルのクラス。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

###  **Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 XLSX ファイルを開く**

Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 形式、つまり XLSX または XLSB を開くには、ファイル パスを指定します。も使用できます**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**関連する属性/オプションを設定します。**ロードオプション**ロードするテンプレートファイルのクラス。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells は、パスワードで保護された Microsoft Excel 2007、2010、2013、2016、2019、Office 365 ファイルを開くこともサポートしています。


