---
title: Farklı Microsoft Excel Sürüm Dosyalarını Açma
type: docs
weight: 20
url: /tr/net/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel 95/97 - 2003, SpreadsheetML, Açılış Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX veya Şifreli Excel Dosyaları gibi bir dizi farklı Microsoft Excel Sürümü Dosyasını açabilir.

{{% /alert %}}

## **Farklı Microsoft Excel Sürümlerinin Dosyalarını Açma**

Bir uygulamanın genellikle farklı sürümlerde oluşturulan Microsoft Excel dosyalarını açabilmesi gerekir, örneğin Microsoft Excel 95,97 veya Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 . XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited veya TSV, CSV, ODS vb. dahil çeşitli biçimlerden herhangi birinde bir dosya yüklemeniz gerekebilir. Yapıcıyı kullanın veya**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)** sınıf'**[DosyaFormat](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** kullanarak formatı belirten type özelliği**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**numaralandırma.

 bu**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**numaralandırma, bazıları aşağıda verilen önceden tanımlanmış birçok dosya formatını içerir.

|**Dosya Biçimi Türleri**|**Tanım**|
|:- |:- |
|Csv|Bir CSV dosyasını temsil eder|
|Excel97To2003|Bir Excel 97 - 2003 dosyasını temsil eder|
|Xlsx|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX dosyasını temsil eder|
|Xlsm|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 XLSM dosyasını temsil eder|
|Xltx|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 şablonu XLTX dosyasını temsil eder|
|Xltm|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 makro özellikli XLTM dosyasını temsil eder|
|Xlsb|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 ikili XLSB dosyasını temsil eder|
|E-tabloML|Bir SpreadsheetML dosyasını temsil eder|
|Tsv|Sekmeyle ayrılmış değerler dosyasını temsil eder|
|Sekmeyle Sınırlandırılmış|Sekmeyle Ayrılmış bir metin dosyasını temsil eder|
|Oranlar|Bir ODS dosyasını temsil eder|
|html|Bir HTML dosyasını temsil eder|
|Mhtml|Bir MHTML dosyasını temsil eder|

### **Microsoft Excel 95/5.0 Dosyalarını Açma**

Microsoft Excel 95/5.0 dosyasını açmak için şunu kullanın:**[Yükleme Seçenekleri](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**ve ilgili özniteliği ayarlayın.**[Yükleme Seçenekleri](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**yüklenecek şablon dosyası için sınıf. Bu özelliği test etmek için örnek bir dosya aşağıdaki bağlantıdan indirilebilir:

[Excel95 Dosyası](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **Microsoft Excel 97 - 2003 Dosyalarını Açma**

 Microsoft Excel 97 - 2003 dosyasını açmak için şunu kullanın:**[Yükleme Seçenekleri](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** ve ilgili özniteliği ayarlayın.**[Yükleme Seçenekleri](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**yüklenecek şablon dosyası için sınıf.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX Dosyalarını Açma**

 Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 biçimini yani XLSX veya XLSB'yi açmak için dosya yolunu belirtin. Ayrıca kullanabilirsin**[Yükleme Seçenekleri](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** ve ilgili özniteliği/seçenekleri ayarlayın.**[Yükleme Seçenekleri](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**yüklenecek şablon dosyası için sınıf.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **Şifrelenmiş Excel Dosyalarını Açma**

 Microsoft Excel kullanarak şifreli Excel dosyaları oluşturmak mümkündür. Şifrelenmiş bir dosyayı açmak için,**[Yükleme Seçenekleri](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**ve yüklenecek şablon dosyası için niteliklerini ve seçeneklerini ayarlayın (örneğin, bir şifre verin).
Bu özelliği test etmek için örnek bir dosya aşağıdaki bağlantıdan indirilebilir:

[Şifreli Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells, parola korumalı Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 dosyalarının açılmasını da destekler.


