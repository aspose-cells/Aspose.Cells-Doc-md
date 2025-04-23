---
title: 異なるMicrosoft Excelバージョンのファイルを開く
type: docs
weight: 20
url: /ja/java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft Excel 95/97 - 2003、SpreadsheetML、Microsoft Excel 2007/2010/2013/2016/2019およびOffice 365のXLSXまたは暗号化されたExcelファイルなど、さまざまなMicrosoft Excelバージョンのファイルを開くことができます。

{{% /alert %}}

## **異なるMicrosoft Excelバージョンのファイルを開く**

アプリケーションは、異なるバージョンで作成されたMicrosoft Excelファイル（たとえば、Microsoft Excel 95、97、Microsoft Excel 2007/2010/2013/2016/2019およびOffice 365）を開くことができる必要があります。ファイルを異なる形式（XLS、XLSX、XLSM、XLSB、SpreadsheetML、タブ区切りまたはTSV、CSV、ODSなど）で読み込む必要があるかもしれません。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスのコンストラクタ、または[**setFileFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#FileFormat)メソッドを使用して、[**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType)列挙型を使用して形式を指定します。

[**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType)列挙型には、多くの事前定義ファイル形式が含まれています。 以下にその一部を示します。

|**ファイルの形式の種類**|**説明**|
| :- | :- |
|CSV|CSVファイルを表します|
|EXCEL_97_TO_2003|Excel 97 - 2003ファイルを表します。
|XLSX|Excel 2007/2010/2013/2016/2019およびOffice 365 XLSXファイルを表します|
|XLSM|Excel 2007/2010/2013/2016/2019およびOffice 365 XLSMファイルを表します|
|XLTX|Excel 2007/2010/2013/2016/2019およびOffice 365テンプレートXLTXファイルを表します|
|XLTM|Excel 2007/2010/2013/2016/2019およびOffice 365マクロ有効なXLTMファイルを表します|
|XLSB|Excel 2007/2010/2013/2016/2019およびOffice 365バイナリXLSBファイルを表します|
|SPREADSHEET_ML|SpreadsheetMLファイルを表します|
|TSV|タブ区切り値ファイルを表します|
|TAB_DELIMITED|タブ区切りテキストファイルを表します|
|ODS|ODSファイルを表します|
|HTML|HTMLファイルを表します|
|M_HTML|MHTMLファイルを表します|

### **Microsoft Excel 95/5.0 ファイルを開く**

Microsoft Excel 95/5.0 ファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) を使用し、読み込むテンプレートファイルの関連属性を [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) クラスに設定します。この機能のテスト用のサンプルファイルは、次のリンクからダウンロードできます:

[Excel95 File](Excel95.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel95Files.java" >}}

### **Microsoft Excel 97 - 2003 ファイルを開く**

Microsoft Excel 97 - 2003 ファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) を使用し、読み込むテンプレートファイルの関連属性を [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) クラスに設定します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel97-2003Files.java" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 XLSX ファイルを開く**

Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 形式、つまり XLSX または XLSB を開くには、ファイルパスを指定します。また、 [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) を使用し、テンプレートファイルの関連属性/オプションを読み込む [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) クラスに設定できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel2007Files.java" >}}

### **暗号化されたExcelファイルを開く**

Microsoft Excelで暗号化されたファイルを作成することは可能です。暗号化されたファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)を使用し、テンプレートファイルの属性とオプション（たとえばパスワードを指定）を設定します。 
この機能のテスト用のサンプルファイルは、以下のリンクからダウンロードできます:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenEncryptedExcelFiles.java" >}}

Aspose.Cells は、パスワードで保護された Microsoft Excel 2007 年、2010 年、2013 年、2016 年、2019 年、Office 365 ファイルを開くこともサポートしています。
{{< app/cells/assistant language="java" >}}
