---
title: Farklı Microsoft Excel Sürüm Dosyalarını Açma
type: docs
weight: 20
url: /tr/python-net/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel 95/97 - 2003, SpreadsheetML, Açılış Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX gibi farklı Microsoft Excel Sürümleri Dosyalarını açabilir.

{{% /alert %}}

## **Farklı Microsoft Excel Sürümlerinin Dosyalarını Açma**

 Bir uygulamanın genellikle farklı sürümlerde oluşturulan Microsoft Excel dosyalarını açabilmesi gerekir, örneğin Microsoft Excel 95,97 veya Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 . Bir dosyayı XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited veya TSV, CSV, ODS ve benzeri biçimlerden herhangi birinde yüklemeniz gerekebilir. Yapıcıyı kullanın veya**Çalışma kitabı** sınıf'**dosya formatı**kullanarak formatı belirten type özelliği**Dosya Biçimi Türü**numaralandırma.

 bu**Dosya Biçimi Türü**numaralandırma, bazıları aşağıda verilen önceden tanımlanmış birçok dosya formatını içerir.

|**Dosya Biçimi Türleri**|**Açıklama**|
|:- |:- |
|CSV|CSV dosyasını temsil eder|
|EXCEL_97_TO_2003|Bir Excel 97 - 2003 dosyasını temsil eder|
|XLSX|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX dosyasını temsil eder|
|XLSM|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 XLSM dosyasını temsil eder|
|Xltx|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 şablonu XLTX dosyasını temsil eder|
|XLTX|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 makro özellikli XLTM dosyasını temsil eder|
|XLSB|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 ikili XLSB dosyasını temsil eder|
|SPREADSHEET_ML|SpreadsheetML dosyasını temsil eder|
|TSV|Sekmeyle ayrılmış değerler dosyasını temsil eder|
|TAB_DELIMITED|Sekmeyle Ayrılmış bir metin dosyasını temsil eder|
|ODS|Bir ODS dosyasını temsil eder|
|HTML|Bir HTML dosyasını temsil eder|
|M_HTML|Bir MHTML dosyasını temsil eder|

### **Microsoft Excel 95/5.0 Dosyalarını Açma**

Microsoft Excel 95/5.0 dosyasını açmak için şunu kullanın:**Yükleme Seçenekleri**ve ilgili özniteliği ayarlayın.**Yükleme Seçenekleri**yüklenecek şablon dosyası için sınıf. Bu özelliği test etmek için örnek bir dosya aşağıdaki bağlantıdan indirilebilir:

[Excel95 Dosyası](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **Microsoft Excel 97 - 2003 Dosyalarını Açma**

 Microsoft Excel 97 - 2003 dosyasını açmak için şunu kullanın:**Yükleme Seçenekleri** ve ilgili özniteliği ayarlayın.**Yükleme Seçenekleri**yüklenecek şablon dosyası için sınıf.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX Dosyalarını Açma**

Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 biçimini, yani XLSX veya XLSB'i açmak için dosya yolunu belirtin. Ayrıca kullanabilirsiniz**Yükleme Seçenekleri** ve ilgili özniteliği/seçenekleri ayarlayın.**Yükleme Seçenekleri**yüklenecek şablon dosyası için sınıf.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **Şifrelenmiş Excel Dosyalarını Açma**

 Microsoft Excel kullanarak şifreli Excel dosyaları oluşturmak mümkündür. Şifrelenmiş bir dosyayı açmak için,**Yükleme Seçenekleri**ve yüklenecek şablon dosyası için niteliklerini ve seçeneklerini ayarlayın (örneğin, bir şifre verin).
Bu özelliği test etmek için örnek bir dosya aşağıdaki bağlantıdan indirilebilir:

[Şifreli Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells, parola korumalı Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 dosyalarının açılmasını da destekler.


