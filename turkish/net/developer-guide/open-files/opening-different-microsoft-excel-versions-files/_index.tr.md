---
title: Farklı Microsoft Excel Sürüm Dosyalarını Açma
type: docs
weight: 20
url: /tr/net/opening-different-microsoft-excel-versions-files/
description: Bu makalede, Aspose.Cells for .NET API kullanılarak farklı Excel sürüm dosyalarının nasıl açılacağı açıklanmaktadır.
keywords: C# Open Different Microsoft Excel file, How do I open Encrypted Excel Files.
---
{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel 95/97 - 2003, SpreadsheetML, Açılış Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX gibi farklı Microsoft Excel Sürüm Dosyaları aralığını açabilir veya Şifrelenmiş Excel Dosyaları.

{{% /alert %}}

##  **Farklı Microsoft Excel Sürümlerine Sahip Dosyalar Nasıl Açılır**

 Bir uygulamanın genellikle farklı sürümlerde oluşturulan Microsoft Excel dosyalarını açabilmesi gerekir; örneğin, Microsoft Excel 95,97 veya Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 . XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited veya TSV, CSV, ODS vb. dahil olmak üzere çeşitli biçimlerden herhangi birinde bir dosya yüklemeniz gerekebilir. Yapıcıyı kullanın veya belirtin**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)**sınıf'**[FileFormat](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** kullanarak formatı belirten type niteliğini kullanın.**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**numaralandırma.

**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**numaralandırma, bazıları aşağıda verilen önceden tanımlanmış birçok dosya formatını içerir.

|**Dosya Formatı Türleri**|**Tanım**|
| :- | :- |
|CSV|CSV dosyasını temsil eder|
|Excel97To2003|Bir Excel 97 - 2003 dosyasını temsil eder|
|Xlsx|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX dosyasını temsil eder|
|Xlsm|Bir Excel 2007/2010/2013/2016/2019 ve Office 365 XLSM dosyasını temsil eder|
|Xltx|Excel 2007/2010/2013/2016/2019 ve Office 365 şablonu XLTX dosyasını temsil eder|
|Xltm|Excel 2007/2010/2013/2016/2019 ve Office 365 makro özellikli XLTM dosyasını temsil eder|
|Xlsb|Excel 2007/2010/2013/2016/2019 ve Office 365 ikili XLSB dosyasını temsil eder|
|SpreadsheetML|SpreadsheetML dosyasını temsil eder|
|Tsv|Sekmeyle ayrılmış değerler dosyasını temsil eder|
|TabDelimited|Sekmeyle Sınırlandırılmış metin dosyasını temsil eder|
|Oranlar|ODS dosyasını temsil eder|
|Html|HTML dosyasını temsil eder|
|Mhtml|MHTML dosyasını temsil eder|

###  **Microsoft Excel 95/5.0 Dosyalarını Aç**

Microsoft Excel 95/5.0 dosyasını açmak için şunu kullanın:**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**ve ilgili özniteliği ayarlayın**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**Yüklenecek şablon dosyasının sınıfı. Bu özelliği test etmeye yönelik örnek bir dosya aşağıdaki bağlantıdan indirilebilir:

[Excel95 Dosyası](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

###  **Microsoft Excel 97 - 2003 Dosyalarını Aç**

 Microsoft Excel 97 - 2003 dosyasını açmak için şunu kullanın:**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** ve ilgili özniteliği ayarlayın**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**Yüklenecek şablon dosyasının sınıfı.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

###  **Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX Dosyalarını açın**

Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 biçimini (XLSX veya XLSB) açmak için dosya yolunu belirtin. Ayrıca kullanabilirsin**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** ve ilgili özelliği/seçenekleri ayarlayın.**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**Yüklenecek şablon dosyasının sınıfı.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

###  **Şifrelenmiş Excel Dosyalarını Açma**

 Microsoft Excel'i kullanarak şifrelenmiş Excel dosyaları oluşturmak mümkündür. Şifrelenmiş bir dosyayı açmak için**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**ve yüklenecek şablon dosyası için niteliklerini ve seçeneklerini (örneğin, şifre verme) ayarlayın.
Bu özelliği test etmeye yönelik örnek bir dosya aşağıdaki bağlantıdan indirilebilir:

[Şifreli Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells ayrıca parola korumalı Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 dosyalarının açılmasını da destekler.


