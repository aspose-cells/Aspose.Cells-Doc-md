---
title: 異なるMicrosoft Excelバージョンのファイルを開く
type: docs
weight: 20
url: /ja/python-net/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft Excel 95/97 - 2003、SpreadsheetML、Microsoft Excel 2007/2010/2013/2016/2019およびOffice 365のXLSXまたは暗号化されたExcelファイルなど、さまざまなMicrosoft Excelバージョンのファイルを開くことができます。

{{% /alert %}}

## **異なるMicrosoft Excelバージョンのファイルを開く**

アプリケーションはしばしば異なるバージョンで作成されたMicrosoft Excelファイルを開くことができる必要があります。たとえば、Microsoft Excel 95、97、またはMicrosoft Excel 2007/2010/2013/2016/2019およびOffice 365。XLS、XLSX、XLSM、XLSB、SpreadsheetML、タブ区切りまたはTSV、CSV、ODSなどのいくつかの形式でファイルをロードする必要があるかもしれません。**Workbook**クラスの**file_format**タイプ属性を指定するためにコンストラクターを使用します、または**FileFormatType**列挙を使用してファイル形式を指定します。

**FileFormatType**列挙には、以下に示すものを含む、多くの事前定義のファイル形式が含まれています。

|**ファイルの形式の種類**|**説明**|
| :- | :- |
|CSV|CSVファイルを表します|
|EXCEL_97_TO_2003|Excel 97 - 2003ファイルを表します。
|XLSX|Excel 2007/2010/2013/2016/2019およびOffice 365 XLSXファイルを表します|
|XLSM|Excel 2007/2010/2013/2016/2019およびOffice 365 XLSMファイルを表します|
|Xltx|はExcel 2007/2010/2013/2016/2019およびOffice 365テンプレートXLTXファイルを表します
|XLTM|Excel 2007/2010/2013/2016/2019およびOffice 365マクロ有効XLTMファイルを表します|
|XLSB|Excel 2007/2010/2013/2016/2019およびOffice 365バイナリXLSBファイルを表します|
|SPREADSHEET_ML|SpreadsheetMLファイルを表します|
|TSV|タブ区切り値ファイルを表します|
|TAB_DELIMITED|タブ区切りテキストファイルを表します|
|ODS|ODSファイルを表します|
|HTML|HTMLファイルを表します|
|M_HTML|MHTMLファイルを表します|

### **Microsoft Excel 95/5.0 ファイルを開く**

Microsoft Excel 95/5.0ファイルを開くには、**LoadOptions**を使用して、**LoadOptions**クラスの関連属性を設定します。この機能をテストするためのサンプルファイルは、以下のリンクからダウンロードできます。

[Excel95 File](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **Microsoft Excel 97 - 2003 ファイルを開く**

Microsoft Excel 97 - 2003ファイルを開くには、**LoadOptions**を使用して、**LoadOptions**クラスの関連属性を設定します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 XLSX ファイルを開く**

Microsoft Excel 2007/2010/2013/2016/2019およびOffice 365形式（XLSXまたはXLSB）を開くには、ファイルパスを指定します。**LoadOptions**を使用して、**LoadOptions**クラスの関連属性/オプションを設定することもできます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **暗号化されたExcelファイルを開く**

Microsoft Excelを使用して暗号化されたExcelファイルを作成することが可能です。 暗号化されたファイルを開くには、**LoadOptions**を使用し、読み込むテンプレートファイルの属性とオプション（たとえば、パスワードを設定）を設定します。
この機能のテスト用のサンプルファイルは、以下のリンクからダウンロードできます:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells は、パスワードで保護された Microsoft Excel 2007 年、2010 年、2013 年、2016 年、2019 年、Office 365 ファイルを開くこともサポートしています。


