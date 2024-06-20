---
title: Farklı Microsoft Excel Sürümlerini Açma
type: docs
weight: 20
url: /tr/python-net/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel 95/97 - 2003, SpreadsheetML, Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX veya Şifreli Excel Dosyaları gibi çeşitli farklı Microsoft Excel Sürümlerini açabilir.

{{% /alert %}}

## **Farklı Microsoft Excel Sürümleri Dosyalarını Açma**

Bir uygulamanın genellikle farklı sürümlerde oluşturulmuş Microsoft Excel dosyalarını açabilmesi gerekebilir, örneğin Microsoft Excel 95,97, veya Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 . Bir dosyayı XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited veya TSV, CSV, ODS ve benzeri birkaç formatta yüklemeye ihtiyacınız olabilir. **Workbook** sınıfının **file_format** tipi özelliğini belirtmek için **FileFormatType** numaralandırmasını kullanın ya da yapıcıyı kullanın.

**FileFormatType** numaralandırması aşağıda verilen türlerden bazılarını içermektedir.

|**Dosya Biçimi Türleri**|**Açıklama**|
| :- | :- |
|CSV|CSV dosyasını temsil eder|
|EXCEL_97_TO_2003|Excel 97 - 2003 dosyasını temsil eder|
|XLSX|Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX dosyasını temsil eder|
|XLSM|Excel 2007/2010/2013/2016/2019 ve Office 365 XLSM dosyasını temsil eder|
|Xltx|Excel 2007/2010/2013/2016/2019 ve Office 365 şablonu XLTX dosyasını temsil eder|
|XLTX|Excel 2007/2010/2013/2016/2019 ve Office 365 makro etkin XLTM dosyasını temsil eder|
|XLSB|Excel 2007/2010/2013/2016/2019 ve Office 365 binary XLSB dosyasını temsil eder|
|SPREADSHEET_ML|SpreadsheetML dosyasını temsil eder|
|TSV|Tab boşluklu değerler dosyasını temsil eder|
|TAB_DELIMITED|Tab Delimited metin dosyasını temsil eder|
|ODS|ODS dosyasını temsil eder|
|HTML|HTML dosyasını temsil eder|
|M_HTML|MHTML dosyasını temsil eder|

### **Microsoft Excel 95/5.0 Dosyalarını Açma**

Microsoft Excel 95/5.0 dosyasını açmak için **LoadOptions** kullanın ve yüklenecek şablon dosyası için **LoadOptions** sınıfının ilgili özniteliğini ayarlayın. Bu özelliği test etmek için örnek bir dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[Excel95 Dosyası](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **Microsoft Excel 97 - 2003 Dosyalarını Açma**

Microsoft Excel 97 - 2003 dosyasını açmak için **LoadOptions** kullanın ve yüklenecek şablon dosyası için **LoadOptions** sınıfının ilgili özniteliğini ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX Dosyalarını Açma**

Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 biçimini, yani XLSX veya XLSB'yi açmak için dosya yolunu belirtin. Ayrıca, yüklenecek şablon dosyası için **LoadOptions** kullanabilir ve **LoadOptions** sınıfının ilgili özniteliklerini/ayarlarını belirleyebilirsiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **Şifreli Excel Dosyalarını Açma**

Microsoft Excel kullanarak şifreli Excel dosyaları oluşturmak mümkündür. Şifreli bir dosyayı açmak için, yüklenecek şablon dosyası için **LoadOptions** kullanın ve özniteliklerini ve seçeneklerini belirleyin (örneğin, bir şifre verin).
Bu özelliği test etmek için bir örnek dosya aşağıdaki bağlantıdan indirilebilir:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells ayrıca şifre korumalı Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 dosyalarını açmayı destekler.


