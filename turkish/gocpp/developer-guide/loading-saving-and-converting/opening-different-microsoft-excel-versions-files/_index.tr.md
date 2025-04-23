---
title: Farklı Microsoft Excel Sürümlerini Açma
type: docs
weight: 20
url: /tr/go-cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel 95/97 - 2003, SpreadsheetML, Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX veya Şifreli Excel Dosyaları gibi çeşitli farklı Microsoft Excel Sürümlerini açabilir.

{{% /alert %}}

## **Farklı Microsoft Excel Sürümleri Dosyalarını Açma**

Bir uygulama, farklı sürümlerde oluşturulmuş Microsoft Excel dosyalarını açabilmelidir, örneğin Microsoft Excel 95,97 veya Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365. Bir dosyayı birkaç farklı formatta yüklemeniz gerekebilir, bunlar arasında XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited veya TSV, CSV, ODS ve diğerleri bulunur. Bunu yapmak için, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfının yapıcı veya [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) metodunu ve [**SetFileFormat**](https://reference.aspose.com/cells/go-cpp/workbook/setfileformat/) yöntemini kullanarak formatı [**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/) sınıfı ile belirtin.

[**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/) demetinde, aşağıda bazıları verilen birçok önceden tanımlanmış dosya formatı bulunur.

|**Dosya Biçimi Türleri**|**Açıklama**|
| :- | :- |
|FileFormatType_CSV|Bir CSV dosyasını temsil eder|
|FileFormatType_Excel97To2003|Excel 97 - 2003 dosyasını temsil eder|
|FileFormatType_Xlsx|Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX dosyasını temsil eder|
|FileFormatType_Xlsm|Excel 2007/2010/2013/2016/2019 ve Office 365 XLSM dosyasını temsil eder|
|FileFormatType_Xltx|Excel 2007/2010/2013/2016/2019 ve Office 365 şablonu XLTX dosyasını temsil eder|
|FileFormatType_Xltm|Excel 2007/2010/2013/2016/2019 ve Office 365 makro etkin XLTM dosyasını temsil eder|
|FileFormatType_Xlsb|Excel 2007/2010/2013/2016/2019 ve Office 365 ikili XLSB dosyasını temsil eder|
|FileFormatType_SpreadsheetML|Bir SpreadsheetML dosyasını temsil eder|
|FileFormatType_Tsv|Bir Sekmeyle ayrılmış değerler dosyasını temsil eder|
|FileFormatType_TabDelimited|Bir Sekmeyle Ayrılmış metin dosyasını temsil eder|
|FileFormatType_Ods|Bir ODS dosyasını temsil eder|
|FileFormatType_Html|Bir HTML dosyasını temsil eder|
|FileFormatType_MHtml|Bir MHTML dosyasını temsil eder|

### **Microsoft Excel 95/5.0 Dosyalarını Açma**

Microsoft Excel 95/5.0 dosyasını açmak için, ilgili özniteliği belirlemek için [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) sınıfı için [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) kullanın ve şablon dosyası yüklenecek. Bu özelliği test etmek için bir örnek dosya aşağıdaki bağlantıdan indirilebilir:

[Excel95 Dosyası](Excel95.xls)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel95Files.go" >}}

### **Microsoft Excel 97 - 2003 Dosyalarını Açma**

Microsoft Excel 97 - 2003 dosyasını açmak için [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) kullanın ve ilgili özniteliği belirlemek için [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) sınıfı için [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) kullanın şablon dosyası yüklenecek.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel97-2003Files.go" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX Dosyalarını Açma**

Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 biçimini yani XLSX veya XLSB dosya yolunu belirtin. Ayrıca, şablon dosyası yüklenecek [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) sınıf için [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) ve ilgili öznitelik/seçeneklerini de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel2007Files.go" >}}

Aspose.Cells, ayrıca şifreyle korunan Microsoft Excel 2007, 2010, 2013, 2016, 2019 ve Office 365 dosyalarını açmayı destekler.
