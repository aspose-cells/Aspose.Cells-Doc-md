---
title: Farklı Microsoft Excel Sürümleri Dosyalarını Açın
type: docs
weight: 20
url: /tr/net/opening-different-microsoft-excel-versions-files/
description: Bu makale, Aspose.Cells for .NET API sı kullanarak farklı excel sürümleri dosyalarını açmayı açıklar.
keywords: C# Farklı Microsoft Excel Dosyasını Açma, Şifreli Excel Dosyalarını Nasıl Açarım.
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel 95/97 - 2003, SpreadsheetML, Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX veya Şifreli Excel Dosyaları gibi çeşitli farklı Microsoft Excel Sürümlerini açabilir.

{{% /alert %}}

## **Farklı Microsoft Excel Sürümleri Dosyalarını Açma**

Bir uygulamanın genellikle farklı sürümlerde oluşturulmuş Microsoft Excel dosyalarını açabilmesi gerekir, örneğin, Microsoft Excel 95,97 veya Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365. Belirli birkaç formattan herhangi birinde dosya yüklemeniz gerekebilir, bunlar arasında XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited veya TSV, CSV, ODS ve benzerleri bulunur. Formatı belirleyen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının [**FileFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat) tip özelliğini veya [**FileFormatType**](https://reference.aspose.com/cells/net/aspose.cells/fileformattype) sıralamasını belirten özellikleri belirtmek için kullanılır.

[**FileFormatType**](https://reference.aspose.com/cells/net/aspose.cells/fileformattype) numaralandırması birçok önceden tanımlanmış dosya biçimini içerir. Bunlardan bazıları aşağıda verilmiştir.

|**Dosya Biçimi Türleri**|**Açıklama**|
| :- | :- |
|Csv|CSV dosyasını temsil eder|
|Excel97To2003|Excel 97 - 2003 dosyasını temsil eder|
|Xlsx|Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX dosyasını temsil eder|
|Xlsm|Excel 2007/2010/2013/2016/2019 ve Office 365 XLSM dosyasını temsil eder|
|Xltx|Excel 2007/2010/2013/2016/2019 ve Office 365 şablonu XLTX dosyasını temsil eder|
|Xltm|Excel 2007/2010/2013/2016/2019 ve Office 365 makro etkin XLTM dosyasını temsil eder|
|Xlsb|Excel 2007/2010/2013/2016/2019 ve Office 365 binary XLSB dosyasını temsil eder|
|SpreadsheetML|SpreadsheetML dosyasını temsil eder|
|Tsv|TSV dosyasını temsil eder|
|TabDelimited|Tab Delimited metin dosyasını temsil eder|
|Ods|ODS dosyasını temsil eder|
|Html|HTML dosyasını temsil eder|
|Mhtml|MHTML dosyasını temsil eder|

### **Microsoft Excel 95/5.0 Dosyalarını Aç**

Microsoft Excel 95/5.0 dosyasını açmak için, ilgili özniteliği belirlemek için [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) sınıfı için [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) kullanın ve şablon dosyası yüklenecek. Bu özelliği test etmek için bir örnek dosya aşağıdaki bağlantıdan indirilebilir:

[Excel95 Dosyası](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **Microsoft Excel 97 - 2003 Dosyalarını Aç**

Microsoft Excel 97 - 2003 dosyasını açmak için [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) kullanın ve ilgili özniteliği belirlemek için [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) sınıfı için [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) kullanın şablon dosyası yüklenecek.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX Dosyalarını Aç**

Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 biçimini yani XLSX veya XLSB dosya yolunu belirtin. Ayrıca, şablon dosyası yüklenecek [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) sınıf için [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) ve ilgili öznitelik/seçeneklerini de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **Şifreli Excel Dosyalarını Aç**

Microsoft Excel kullanarak şifreli dosyalar oluşturmak mümkündür. Şifreli bir dosyayı açmak için, [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) kullanın ve yüklenen şablon dosyası için öznitelikleri ve seçeneklerini ayarlayın (örneğin, bir parola verin).
Bu özelliği test etmek için bir örnek dosya aşağıdaki bağlantıdan indirilebilir:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells ayrıca şifre korumalı Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 dosyalarını açmayı destekler.


{{< app/cells/assistant language="csharp" >}}
