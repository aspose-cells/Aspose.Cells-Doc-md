---
title: Farklı Microsoft Excel Sürüm Dosyalarını Açma
type: docs
weight: 20
url: /tr/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel 95/97 - 2003, SpreadsheetML, Açılış Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX gibi farklı Microsoft Excel Sürüm Dosyaları aralığını açabilir veya Şifrelenmiş Excel Dosyaları.

{{% /alert %}}

##  **Farklı Microsoft Excel Sürümlerindeki Dosyaları Açma**

 Bir uygulamanın genellikle farklı sürümlerde oluşturulan Microsoft Excel dosyalarını açabilmesi gerekir; örneğin, Microsoft Excel 95,97 veya Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 . XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited veya TSV, CSV, ODS vb. dahil olmak üzere çeşitli biçimlerden herhangi birinde bir dosya yüklemeniz gerekebilir. Yapıcıyı kullanın veya belirtin**[Çalışma Kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)**sınıf'**[SetFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/)** kullanarak formatı belirtme yöntemini kullanın.**[FileFormatType](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**numaralandırma.
	
**[FileFormatType](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**numaralandırma, bazıları aşağıda verilen önceden tanımlanmış birçok dosya formatını içerir.

|**Dosya Formatı Türleri**|**Tanım**|
| :- | :- |
|FileFormatType_CSV|CSV dosyasını temsil eder|
|FileFormatType_Excel97To2003|Bir Excel 97 - 2003 dosyasını temsil eder|
|FileFormatType_Xlsx|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX dosyasını temsil eder|
|FileFormatType_Xlsm|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 XLSM dosyasını temsil eder|
|FileFormatType_Xltx|Excel 2007/2010/2013/2016/2019 ve Office 365 şablonu XLTX dosyasını temsil eder|
|FileFormatType_Xltm|Excel 2007/2010/2013/2016/2019 ve Office 365 makro özellikli XLTM dosyasını temsil eder|
|FileFormatType_Xlsb|Excel 2007/2010/2013/2016/2019 ve Office 365 ikili XLSB dosyasını temsil eder|
|FileFormatType_SpreadsheetML|SpreadsheetML dosyasını temsil eder|
|FileFormatType_Tsv|Sekmeyle ayrılmış değerler dosyasını temsil eder|
|FileFormatType_TabDelimited|Sekmeyle Sınırlandırılmış metin dosyasını temsil eder|
|FileFormatType_Ods|ODS dosyasını temsil eder|
|FileFormatType_Html|HTML dosyasını temsil eder|
|FileFormatType_MHtml|MHTML dosyasını temsil eder|

###  **Microsoft Excel 95/5.0 Dosyalarını Açma**

Microsoft Excel 95/5.0 dosyasını açmak için şunu kullanın:**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**ve ilgili özniteliği ayarlayın**Yük Seçenekleri**Yüklenecek şablon dosyasının sınıfı. Bu özelliği test etmeye yönelik örnek bir dosya aşağıdaki bağlantıdan indirilebilir:

[Excel95 Dosyası](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

###  **Microsoft Excel 97 - 2003 Dosyalarını Açma**

 Microsoft Excel 97 - 2003 dosyasını açmak için şunu kullanın:**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)** ve ilgili özniteliği ayarlayın**Yük Seçenekleri**Yüklenecek şablon dosyasının sınıfı.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

###  **Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX Dosyalarının Açılması**

Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 biçimini (XLSX veya XLSB) açmak için dosya yolunu belirtin. Ayrıca kullanabilirsin**[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)** ve ilgili özelliği/seçenekleri ayarlayın.**Yük Seçenekleri**Yüklenecek şablon dosyasının sınıfı.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells ayrıca parola korumalı Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 dosyalarının açılmasını da destekler.


