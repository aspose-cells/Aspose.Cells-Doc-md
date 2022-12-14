---
title: Farklı Microsoft Excel Sürüm Dosyalarını Açma
type: docs
weight: 20
url: /tr/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel 95/97 - 2003, SpreadsheetML, Açılış Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX veya Şifreli Excel Dosyaları gibi bir dizi farklı Microsoft Excel Sürümü Dosyasını açabilir.

{{% /alert %}}

## **Farklı Microsoft Excel Sürümlerinin Dosyalarını Açma**

 Bir uygulamanın genellikle farklı sürümlerde oluşturulan Microsoft Excel dosyalarını açabilmesi gerekir, örneğin Microsoft Excel 95,97 veya Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 . XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited veya TSV, CSV, ODS vb. dahil çeşitli biçimlerden herhangi birinde bir dosya yüklemeniz gerekebilir. Yapıcıyı kullanın veya**[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)** sınıf'**[SetFileFormat](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#aa74a10e0aa88e3a8386ea328165896dc)** kullanarak biçimi belirtmek için yöntem**[FileFormatType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**numaralandırma.
	
 bu**[FileFormatType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**numaralandırma, bazıları aşağıda verilen önceden tanımlanmış birçok dosya formatını içerir.

|**Dosya Biçimi Türleri**|**Tanım**|
|:- |:- |
|FileFormatType_CSV|Bir CSV dosyasını temsil eder|
|FileFormatType_Excel97To2003|Bir Excel 97 - 2003 dosyasını temsil eder|
|FileFormatType_Xlsx|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX dosyasını temsil eder|
|FileFormatType_Xlsm|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 XLSM dosyasını temsil eder|
|FileFormatType_Xltx|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 şablonu XLTX dosyasını temsil eder|
|FileFormatType_Xltm|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 makro özellikli XLTM dosyasını temsil eder|
|FileFormatType_Xlsb|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 ikili XLSB dosyasını temsil eder|
|FileFormatType_SpreadsheetML|Bir SpreadsheetML dosyasını temsil eder|
|FileFormatType_Tsv|Sekmeyle ayrılmış değerler dosyasını temsil eder|
|FileFormatType_TabDelimited|Sekmeyle Ayrılmış bir metin dosyasını temsil eder|
|FileFormatType_Ods|Bir ODS dosyasını temsil eder|
|FileFormatType_Html|Bir HTML dosyasını temsil eder|
|FileFormatType_MHtml|Bir MHTML dosyasını temsil eder|

### **Microsoft Excel 95/5.0 Dosyalarını Açma**

Microsoft Excel 95/5.0 dosyasını açmak için şunu kullanın:**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)**ve ilgili özniteliği ayarlayın.**ILoadOptions**yüklenecek şablon dosyası için sınıf. Bu özelliği test etmek için örnek bir dosya aşağıdaki bağlantıdan indirilebilir:

[Excel95 Dosyası](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files.cpp" >}}

### **Microsoft Excel 97 - 2003 Dosyalarını Açma**

 Microsoft Excel 97 - 2003 dosyasını açmak için şunu kullanın:**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** ve ilgili özniteliği ayarlayın.**ILoadOptions**yüklenecek şablon dosyası için sınıf.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files.cpp" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX Dosyalarını Açma**

 Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 biçimini yani XLSX veya XLSB'yi açmak için dosya yolunu belirtin. Ayrıca kullanabilirsin**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** ve ilgili özniteliği/seçenekleri ayarlayın.**ILoadOptions**yüklenecek şablon dosyası için sınıf.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files.cpp" >}}

Aspose.Cells, parola korumalı Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 dosyalarının açılmasını da destekler.


