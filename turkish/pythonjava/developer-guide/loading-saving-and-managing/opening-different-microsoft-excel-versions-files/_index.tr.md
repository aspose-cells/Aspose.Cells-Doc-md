---
title: Farklı Microsoft Excel Sürümlerini Açma
type: docs
weight: 20
url: /tr/python-java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel 95/97 - 2003, SpreadsheetML, Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX veya Şifreli Excel Dosyaları gibi çeşitli farklı Microsoft Excel Sürümlerini açabilir.

{{% /alert %}}

## **Farklı Microsoft Excel Sürümleri Dosyalarını Açma**

Bir uygulamanın genellikle farklı sürümlerde oluşturulmuş Microsoft Excel dosyalarını açabilmesi gerekmektedir, örneğin, Microsoft Excel 95, 97 veya Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365. XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited veya TSV, CSV, ODS vb. gibi çeşitli formatlardan birinde bir dosyayı yüklemeniz gerekebilir. Formatı belirtmek için yapıcıyı kullanın veya [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) sınıfının [**setFileFormat**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#FileFormat) yöntemini belirtmek için [**FileFormatType**](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType) numaralı numaralandırmasını kullanın.

[**FileFormatType**](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType) numaralandırması birçok önceden tanımlanmış dosya biçimini içerir. Bunlardan bazıları aşağıda verilmiştir.

|**Dosya Biçimi Türleri**|**Açıklama**|
| :- | :- |
|CSV|CSV dosyasını temsil eder|
|EXCEL_97_TO_2003|Excel 97 - 2003 dosyasını temsil eder|
|XLSX|Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX dosyasını temsil eder|
|XLSM|Excel 2007/2010/2013/2016/2019 ve Office 365 XLSM dosyasını temsil eder|
|XLTX|Excel 2007/2010/2013/2016/2019 ve Office 365 şablon XLTX dosyasını temsil eder|
|XLTM|Excel 2007/2010/2013/2016/2019 ve Office 365 makro etkin XLTM dosyasını temsil eder|
|XLSB|Excel 2007/2010/2013/2016/2019 ve Office 365 binary XLSB dosyasını temsil eder|
|SPREADSHEET_ML|SpreadsheetML dosyasını temsil eder|
|TSV|Tab boşluklu değerler dosyasını temsil eder|
|TAB_DELIMITED|Tab Delimited metin dosyasını temsil eder|
|ODS|ODS dosyasını temsil eder|
|HTML|HTML dosyasını temsil eder|
|M_HTML|MHTML dosyasını temsil eder|

### **Microsoft Excel 95/5.0 Dosyalarını Açma**

Microsoft Excel 95/5.0 dosyasını açmak için, [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) kullanın ve yüklenecek olan şablon dosyası için **Yükleme Seçenekleri** sınıfının ilgili özniteliğini ayarlayın. Bu özelliği test etmek için bir örnek dosya aşağıdaki bağlantıdan indirilebilir:

[Excel95 Dosyası](Excel95.xls)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel95Files.py" >}}

### **Microsoft Excel 97 - 2003 Dosyalarını Açma**

Microsoft Excel 97 - 2003 dosyasını açmak için, [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) kullanın ve yüklenecek olan şablon dosyası için **Yükleme Seçenekleri** sınıfının ilgili özniteliğini ayarlayın.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel97-2003Files.py" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX Dosyalarını Açma**

Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 formatında, yani XLSX veya XLSB formatında bir dosyayı açmak için dosya yolunu belirtin. Ayrıca [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) kullanabilir ve yüklenecek şablon dosyasının ilişkili öznitelik/ayarlarını **LoadOptions** sınıfına ayarlayabilirsiniz.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel2007Files.py" >}}

### **Şifreli Excel Dosyalarını Açma**

Microsoft Excel kullanarak şifreli dosyalar oluşturmak mümkündür. Şifreli bir dosyayı açmak için, [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) kullanın ve yüklenen şablon dosyası için öznitelikleri ve seçeneklerini ayarlayın (örneğin, bir parola verin).
Bu özelliği test etmek için bir örnek dosya aşağıdaki bağlantıdan indirilebilir:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells ayrıca şifre korumalı Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 dosyalarını açmayı destekler.


