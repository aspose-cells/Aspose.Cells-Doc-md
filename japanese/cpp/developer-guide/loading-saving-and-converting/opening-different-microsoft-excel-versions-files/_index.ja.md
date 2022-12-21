---
title: 異なる Microsoft Excel バージョンのファイルを開く
type: docs
weight: 20
url: /ja/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells は、Microsoft Excel 95/97 - 2003、SpreadsheetML、Opening Microsoft Excel 2007/2010/2013/2016/2019、Office 365 XLSX または暗号化された Excel ファイルなど、さまざまな Microsoft Excel バージョン ファイルを開くことができます。

{{% /alert %}}

## **異なる Microsoft Excel バージョンのファイルを開く**

多くの場合、アプリケーションは、異なるバージョンで作成された Microsoft Excel ファイルを開くことができる必要があります。たとえば、 Microsoft Excel 95,97、または Microsoft Excel 2007/2010/2013/2016/2019 と Office 365 です。 XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited または TSV、CSV、ODS など、いくつかの形式のいずれかでファイルをロードする必要がある場合があります。コンストラクターを使用するか、**[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)**クラス'**[SetFileFormat](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#aa74a10e0aa88e3a8386ea328165896dc)**を使用してフォーマットを指定するメソッド**[FileFormatType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**列挙。
	
の**[FileFormatType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**列挙には、事前に定義された多くのファイル形式が含まれており、その一部を以下に示します。

|**ファイル形式の種類**|**説明**|
|:- |:- |
|FileFormatType_CSV|CSV ファイルを表します|
|FileFormatType_Excel97To2003|Excel 97 - 2003 ファイルを表します|
|FileFormatType_Xlsx|Excel 2007/2010/2013/2016/2019 および Office 365 XLSX ファイルを表します|
|FileFormatType_Xlsm|Excel 2007/2010/2013/2016/2019 および Office 365 XLSM ファイルを表します|
|FileFormatType_Xltx|Excel 2007/2010/2013/2016/2019 および Office 365 テンプレート XLTX ファイルを表します|
|FileFormatType_Xltm|Excel 2007/2010/2013/2016/2019 および Office 365 マクロ有効 XLTM ファイルを表します|
|FileFormatType_Xlsb|Excel 2007/2010/2013/2016/2019 および Office 365 バイナリ XLSB ファイルを表します|
|FileFormatType_SpreadsheetML|SpreadsheetML ファイルを表します|
|FileFormatType_Tsv|タブ区切り値ファイルを表します|
|FileFormatType_TabDelimited|タブ区切りのテキスト ファイルを表します|
|FileFormatType_Ods|ODS ファイルを表します|
|FileFormatType_Html|HTML ファイルを表します|
|FileFormatType_MHtml|MHTML ファイルを表します|

### **Microsoft Excel 95/5.0 ファイルを開く**

Microsoft Excel 95/5.0 ファイルを開くには、**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)**関連する属性を設定します**ILoadOptions**ロードするテンプレート ファイルのクラス。この機能をテストするためのサンプル ファイルは、次のリンクからダウンロードできます。

[Excel95 ファイル](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files.cpp" >}}

### **Microsoft Excel 97 - 2003 ファイルを開く**

Microsoft Excel 97 - 2003 ファイルを開くには、次を使用します。**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)**関連する属性を設定します**ILoadOptions**ロードするテンプレート ファイルのクラス。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files.cpp" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 XLSX ファイルを開く**

Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 形式、つまり XLSX または XLSB を開くには、ファイル パスを指定します。使用することもできます**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)**関連する属性/オプションを設定します**ILoadOptions**ロードするテンプレート ファイルのクラス。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files.cpp" >}}

Aspose.Cells は、パスワードで保護された Microsoft Excel 2007、2010、2013、2016、2019、Office 365 ファイルを開くこともサポートしています。


