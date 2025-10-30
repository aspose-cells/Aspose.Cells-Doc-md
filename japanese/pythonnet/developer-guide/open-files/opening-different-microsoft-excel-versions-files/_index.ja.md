---
title: 異なるMicrosoft Excelバージョンのファイルを開く
type: docs
weight: 20
url: /ja/python-net/opening-different-microsoft-excel-versions-files/
description: この記事は、Aspose.Cells for Python via .NET APIを使用して異なるExcelバージョンのファイルを開く方法を説明します。
keywords: Pythonで異なるMicrosoft Excelファイルを開くにはどうすればよいですか、暗号化されたExcelファイルを開くにはどうすればよいですか。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、Microsoft Excel 95/97 - 2003、SpreadsheetML、Microsoft Excel 2007/2010/2013/2016/2019、Office 365 XLSX、および暗号化されたExcelファイルなど、さまざまなMicrosoft Excelバージョンのファイルを開くことが可能です。

{{% /alert %}}

## **異なるMicrosoft Excelバージョンのファイルを開く方法**

アプリケーションは、たとえばMicrosoft Excel 95、97、Microsoft Excel 2007/2010/2013/2016/2019、およびOffice 365で作成されたMicrosoft Excelファイルを開くことができる必要があります。さまざまな形式のファイル、XLS、XLSX、XLSM、XLSB、SpreadsheetML、タブ区切りやTSV、CSV、ODSなどのいずれかの形式でファイルを読み込む必要があるかもしれません。コンストラクタを使用するか、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスの[**file_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/file_format)属性を指定して、[**FileFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformattype)列挙型を使用してフォーマットを指定します。

[**FileFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformattype)列挙型には、多くの事前定義ファイル形式が含まれています。 以下にその一部を示します。

|**ファイルの形式の種類**|**説明**|
| :- | :- |
|Csv|はCSVファイルを表します
|Excel97To2003|はExcel 97-2003ファイルを表します
|Xlsx|はExcel 2007/2010/2013/2016/2019およびOffice 365 XLSXファイルを表します
|Xlsm|はExcel 2007/2010/2013/2016/2019およびOffice 365 XLSMファイルを表します
|Xltx|はExcel 2007/2010/2013/2016/2019およびOffice 365テンプレートXLTXファイルを表します
|Xltm|はExcel 2007/2010/2013/2016/2019およびOffice 365マクロ有効なXLTMファイルを表します
|Xlsb|はExcel 2007/2010/2013/2016/2019およびOffice 365バイナリXLSBファイルを表します
|SpreadsheetML|はSpreadsheetMLファイルを表します
|Tsv|はタブ区切りの値ファイルを表します
|TabDelimited|はタブ区切りのテキストファイルを表します
|Ods|はODSファイルを表します
|Html|はHTMLファイルを表します
|Mhtml|はMHTMLファイルを表します

### **Microsoft Excel 95/5.0ファイルを開く**

Microsoft Excel 95/5.0 ファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) を使用し、読み込むテンプレートファイルの関連属性を [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) クラスに設定します。この機能のテスト用のサンプルファイルは、次のリンクからダウンロードできます:

[Excel95 File](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningMicrosoftExcel95Files-1.py" >}}

### **Microsoft Excel 97-2003ファイルを開く**

Microsoft Excel 97 - 2003 ファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) を使用し、読み込むテンプレートファイルの関連属性を [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) クラスに設定します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningMicrosoftExcel972003Files-1.py" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019およびOffice 365 XLSXファイルを開く**

Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 形式、つまり XLSX または XLSB を開くには、ファイルパスを指定します。また、 [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) を使用し、テンプレートファイルの関連属性/オプションを読み込む [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) クラスに設定できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningMicrosoftExcel2007XlsxFiles-1.py" >}}

### **暗号化されたExcelファイルを開く**

Microsoft Excelで暗号化されたファイルを作成することは可能です。暗号化されたファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions)を使用し、テンプレートファイルの属性とオプション（たとえばパスワードを指定）を設定します。
この機能のテスト用のサンプルファイルは、以下のリンクからダウンロードできます:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningEncryptedExcelFiles-1.py" >}}

Aspose.Cells は、パスワードで保護された Microsoft Excel 2007 年、2010 年、2013 年、2016 年、2019 年、Office 365 ファイルを開くこともサポートしています。


{{< app/cells/assistant language="python-net" >}}
