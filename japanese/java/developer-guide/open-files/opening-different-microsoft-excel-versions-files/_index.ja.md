---
title: 異なる Microsoft Excel バージョンのファイルを開く
type: docs
weight: 20
url: /ja/java/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells は、Microsoft Excel 95/97 - 2003、SpreadsheetML、Opening Microsoft Excel 2007/2010/2013/2016/2019、Office 365 XLSX または暗号化された Excel ファイルなど、さまざまな Microsoft Excel バージョン ファイルを開くことができます。

{{% /alert %}}

## **異なる Microsoft Excel バージョンのファイルを開く**

多くの場合、アプリケーションは、異なるバージョンで作成された Microsoft Excel ファイルを開くことができる必要があります。たとえば、 Microsoft Excel 95,97、または Microsoft Excel 2007/2010/2013/2016/2019 と Office 365 です。 XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited または TSV、CSV、ODS など、いくつかの形式のいずれかでファイルをロードする必要がある場合があります。コンストラクターを使用するか、**[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**クラス'**[setFileFormat](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#FileFormat)**を使用してフォーマットを指定するメソッド**[FileFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType)**列挙。

の**[FileFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType)**列挙には、事前に定義された多くのファイル形式が含まれており、その一部を以下に示します。

|**ファイル形式の種類**|**説明**|
|:- |:- |
|CSV|CSV ファイルを表します|
|エクセル_97_TO_2003|Excel 97 - 2003 ファイルを表します|
|XLSX|Excel 2007/2010/2013/2016/2019 および Office 365 XLSX ファイルを表します|
|XLSM|Excel 2007/2010/2013/2016/2019 および Office 365 XLSM ファイルを表します|
|XLTX|Excel 2007/2010/2013/2016/2019 および Office 365 テンプレート XLTX ファイルを表します|
|XLTM|Excel 2007/2010/2013/2016/2019 および Office 365 マクロ有効 XLTM ファイルを表します|
|XLSB|Excel 2007/2010/2013/2016/2019 および Office 365 バイナリ XLSB ファイルを表します|
|SPREADSHEET_ML|SpreadsheetML ファイルを表します|
|TSV|タブ区切り値ファイルを表します|
|TAB_DELIMITED|タブ区切りのテキスト ファイルを表します|
|ODS|ODS ファイルを表します|
|HTML|HTML ファイルを表します|
|M_HTML|MHTML ファイルを表します|

### **Microsoft Excel 95/5.0 ファイルを開く**

Microsoft Excel 95/5.0 ファイルを開くには、**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**関連する属性を設定します**読み込みオプション**ロードするテンプレート ファイルのクラス。この機能をテストするためのサンプル ファイルは、次のリンクからダウンロードできます。

[Excel95 ファイル](Excel95.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel95Files.java" >}}

### **Microsoft Excel 97 - 2003 ファイルを開く**

Microsoft Excel 97 - 2003 ファイルを開くには、次を使用します。**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**関連する属性を設定します**読み込みオプション**ロードするテンプレート ファイルのクラス。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel97-2003Files.java" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 XLSX ファイルを開く**

Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 形式、つまり XLSX または XLSB を開くには、ファイル パスを指定します。使用することもできます**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**関連する属性/オプションを設定します**読み込みオプション**ロードするテンプレート ファイルのクラス。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel2007Files.java" >}}

### **暗号化された Excel ファイルを開く**

Microsoft Excel を使用して、暗号化された Excel ファイルを作成することができます。暗号化されたファイルを開くには、**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**ロードするテンプレート ファイルの属性とオプションを設定します (たとえば、パスワードを指定します)。
この機能をテストするためのサンプル ファイルは、次のリンクからダウンロードできます。

[暗号化された Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenEncryptedExcelFiles.java" >}}

Aspose.Cells は、パスワードで保護された Microsoft Excel 2007、2010、2013、2016、2019、Office 365 ファイルを開くこともサポートしています。
