---
title: 異なるMicrosoft Excelバージョンのファイルを開く
type: docs
weight: 20
url: /ja/cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft Excel 95/97 - 2003、SpreadsheetML、Microsoft Excel 2007/2010/2013/2016/2019およびOffice 365のXLSXまたは暗号化されたExcelファイルなど、さまざまなMicrosoft Excelバージョンのファイルを開くことができます。

{{% /alert %}}

## **異なるMicrosoft Excelバージョンのファイルを開く**

アプリケーションは、異なるバージョンで作成されたMicrosoft Excelファイル（たとえば、Microsoft Excel 95、97、またはMicrosoft Excel 2007/2010/2013/2016/2019およびOffice 365など）を開くことができる必要がよくあります。 XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimitedまたはTSV、CSV、ODSなど複数の形式のファイルをロードする必要があります。コンストラクタを使用するか、[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスの[**SetFileFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/)メソッドを指定して、[**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)列挙型を使用して形式を指定します。

[**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)列挙型には、多くの事前定義ファイル形式が含まれています。 以下にその一部を示します。

|**ファイルの形式の種類**|**説明**|
| :- | :- |
|FileFormatType_CSV|CSVファイルを表します|
|FileFormatType_Excel97To2003|Excel 97-2003ファイルを表します|
|FileFormatType_Xlsx|Excel 2007/2010/2013/2016/2019およびOffice 365のXLSXファイルを表します|
|FileFormatType_Xlsm|Excel 2007/2010/2013/2016/2019およびOffice 365のXLSMファイルを表します|
|FileFormatType_Xltx|Excel 2007/2010/2013/2016/2019およびOffice 365のテンプレートXLTXファイルを表します|
|FileFormatType_Xltm|Excel 2007/2010/2013/2016/2019およびOffice 365のマクロが有効なXLTMファイルを表します|
|FileFormatType_Xlsb|Excel 2007/2010/2013/2016/2019およびOffice 365のバイナリXLSBファイルを表します|
|FileFormatType_SpreadsheetML|SpreadsheetMLファイルを表します|
|FileFormatType_Tsv|タブ区切り値ファイルを表します|
|FileFormatType_TabDelimited|タブ区切りテキストファイルを表します|
|FileFormatType_Ods|ODS ファイルを表します|
|FileFormatType_Html|HTML ファイルを表します|
|FileFormatType_MHtml|MHTML ファイルを表します|

### **Microsoft Excel 95/5.0 ファイルを開く**

Microsoft Excel 95/5.0 ファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) を使用し、読み込むテンプレートファイルの関連属性を [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) クラスに設定します。この機能のテスト用のサンプルファイルは、次のリンクからダウンロードできます:

[Excel95 File](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

### **Microsoft Excel 97 - 2003 ファイルを開く**

Microsoft Excel 97 - 2003 ファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) を使用し、読み込むテンプレートファイルの関連属性を [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) クラスに設定します。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 XLSX ファイルを開く**

Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 形式、つまり XLSX または XLSB を開くには、ファイルパスを指定します。また、 [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) を使用し、テンプレートファイルの関連属性/オプションを読み込む [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) クラスに設定できます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells は、パスワードで保護された Microsoft Excel 2007 年、2010 年、2013 年、2016 年、2019 年、Office 365 ファイルを開くこともサポートしています。


{{< app/cells/assistant language="cpp" >}}
