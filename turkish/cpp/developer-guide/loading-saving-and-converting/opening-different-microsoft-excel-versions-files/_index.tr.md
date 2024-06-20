---
title: Farklı Microsoft Excel Sürümlerini Açma
type: docs
weight: 20
url: /tr/cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel 95/97 - 2003, SpreadsheetML, Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX veya Şifreli Excel Dosyaları gibi çeşitli farklı Microsoft Excel Sürümlerini açabilir.

{{% /alert %}}

## **Farklı Microsoft Excel Sürümleri Dosyalarını Açma**

Bir uygulamanın genellikle farklı sürümlerde oluşturulmuş Microsoft Excel dosyalarını açabilmesi gerekmektedir, örneğin, Microsoft Excel 95, 97 veya Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365. XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited veya TSV, CSV, ODS vb. gibi çeşitli formatlardan birinde bir dosyayı yüklemeniz gerekebilir. Formatı belirtmek için yapıcıyı kullanın veya [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfının [**SetFileFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/) yöntemini belirtmek için [**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/) numaralı numaralandırmasını kullanın.

[**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/) numaralandırması birçok önceden tanımlanmış dosya biçimini içerir. Bunlardan bazıları aşağıda verilmiştir.

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

Microsoft Excel 95/5.0 dosyasını açmak için, ilgili özniteliği belirlemek için [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) sınıfı için [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) kullanın ve şablon dosyası yüklenecek. Bu özelliği test etmek için bir örnek dosya aşağıdaki bağlantıdan indirilebilir:

[Excel95 Dosyası](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

### **Microsoft Excel 97 - 2003 Dosyalarını Açma**

Microsoft Excel 97 - 2003 dosyasını açmak için [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) kullanın ve ilgili özniteliği belirlemek için [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) sınıfı için [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) kullanın şablon dosyası yüklenecek.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX Dosyalarını Açma**

Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 biçimini yani XLSX veya XLSB dosya yolunu belirtin. Ayrıca, şablon dosyası yüklenecek [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) sınıf için [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) ve ilgili öznitelik/seçeneklerini de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells ayrıca şifre korumalı Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 dosyalarını açmayı destekler.


