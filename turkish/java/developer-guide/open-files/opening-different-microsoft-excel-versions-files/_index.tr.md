---
title: Farklı Microsoft Excel Sürümlerini Açma
type: docs
weight: 20
url: /tr/java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel 95/97 - 2003, SpreadsheetML, Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX veya Şifreli Excel Dosyaları gibi çeşitli farklı Microsoft Excel Sürümlerini açabilir.

{{% /alert %}}

## **Farklı Microsoft Excel Sürümleri Dosyalarını Açma**

Bir uygulamanın genellikle farklı sürümlerde oluşturulmuş Microsoft Excel dosyalarını açabilmesi gerekebilir, örneğin, Microsoft Excel 95,97 veya Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 gibi. XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited veya TSV, CSV, ODS ve benzeri formatlardan birinde dosya yüklemek için, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfının [**setFileFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#FileFormat) yöntemini kullanın veya [**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType) numaralı numaralama ile formatı belirtin.

[**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType) numaralandırması birçok önceden tanımlanmış dosya biçimini içerir. Bunlardan bazıları aşağıda verilmiştir.

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

Microsoft Excel 95/5.0 dosyasını açmak için, ilgili özniteliği belirlemek için [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) sınıfı için [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) kullanın ve şablon dosyası yüklenecek. Bu özelliği test etmek için bir örnek dosya aşağıdaki bağlantıdan indirilebilir:

[Excel95 Dosyası](Excel95.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel95Files.java" >}}

### **Microsoft Excel 97 - 2003 Dosyalarını Açma**

Microsoft Excel 97 - 2003 dosyasını açmak için [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) kullanın ve ilgili özniteliği belirlemek için [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) sınıfı için [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) kullanın şablon dosyası yüklenecek.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel97-2003Files.java" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX Dosyalarını Açma**

Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 biçimini yani XLSX veya XLSB dosya yolunu belirtin. Ayrıca, şablon dosyası yüklenecek [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) sınıf için [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) ve ilgili öznitelik/seçeneklerini de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel2007Files.java" >}}

### **Şifreli Excel Dosyalarını Açma**

Microsoft Excel kullanarak şifreli dosyalar oluşturmak mümkündür. Şifreli bir dosyayı açmak için, [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) kullanın ve yüklenen şablon dosyası için öznitelikleri ve seçeneklerini ayarlayın (örneğin, bir parola verin). 
Bu özelliği test etmek için bir örnek dosya aşağıdaki bağlantıdan indirilebilir:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenEncryptedExcelFiles.java" >}}

Aspose.Cells ayrıca şifre korumalı Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 dosyalarını açmayı destekler.
{{< app/cells/assistant language="java" >}}
