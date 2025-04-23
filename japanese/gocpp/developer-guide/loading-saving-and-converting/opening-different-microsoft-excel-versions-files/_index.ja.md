---
title: 異なるMicrosoft Excelバージョンのファイルを開く
type: docs
weight: 20
url: /ja/go-cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft Excel 95/97 - 2003、SpreadsheetML、Microsoft Excel 2007/2010/2013/2016/2019およびOffice 365のXLSXまたは暗号化されたExcelファイルなど、さまざまなMicrosoft Excelバージョンのファイルを開くことができます。

{{% /alert %}}

## **異なるMicrosoft Excelバージョンのファイルを開く**

アプリケーションはしばしば、Microsoft Excel 95、97、またはMicrosoft Excel 2007/2010/2013/2016/2019やOffice 365で作成された異なるバージョンのMicrosoft Excelファイルを開く必要があります。ファイルを読み込む必要があるフォーマットは、多くの場合、XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimitedやTSV、CSV、ODSなどです。[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)クラスの[**SetFileFormat**](https://reference.aspose.com/cells/go-cpp/workbook/setfileformat/)メソッドを使用して、[**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/)列挙体を使ってフォーマットを指定します。

[**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/)列挙体には、多くの事前定義されたファイルフォーマットが含まれており、その一部は以下の通りです。

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

Microsoft Excel 95/5.0 ファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) を使用し、読み込むテンプレートファイルの関連属性を [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) クラスに設定します。この機能のテスト用のサンプルファイルは、次のリンクからダウンロードできます:

[Excel95 File](Excel95.xls)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel95Files.go" >}}

### **Microsoft Excel 97 - 2003 ファイルを開く**

Microsoft Excel 97 - 2003 ファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) を使用し、読み込むテンプレートファイルの関連属性を [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) クラスに設定します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel97-2003Files.go" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 XLSX ファイルを開く**

Microsoft Excel 2007/2010/2013/2016/2019 および Office 365 形式、つまり XLSX または XLSB を開くには、ファイルパスを指定します。また、 [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) を使用し、テンプレートファイルの関連属性/オプションを読み込む [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) クラスに設定できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel2007Files.go" >}}

Aspose.Cellsはまた、パスワード保護されたMicrosoft Excel 2007、2010、2013、2016、2019、およびOffice 365のファイルのオープンもサポートしています。
