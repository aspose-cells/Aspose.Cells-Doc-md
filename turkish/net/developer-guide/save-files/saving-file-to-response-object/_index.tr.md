---
title: Dosyayı Yanıt Nesnesine Kaydetme
type: docs
weight: 50
url: /tr/net/saving-file-to-response-object/
---
{{% alert color="primary" %}}

Aspose.Cells, dosyaları değiştirmeyi mümkün kılar. Bu makalede, dosyaların bir yanıt nesnesine kaydedilebileceği çeşitli yollar açıklanmaktadır.

{{% /alert %}}

## **Dosyayı Yanıt Nesnesine Kaydetme**

 Dinamik olarak bir dosya oluşturmak ve onu doğrudan bir istemci tarayıcısına göndermek de mümkündür. Bunu yapmak için, programın aşırı yüklenmiş özel bir sürümünü kullanın.**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5)**aşağıdaki parametreleri kabul eden yöntem:

-  ASP.NET**[HttpResponse](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8)**nesne.
- Dosya adı.
- **[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**, çıktı dosyasının içerik düzenleme türü.
- **[SaveOptions](https://reference.aspose.com/cells/net/aspose.cells/saveoptions)**, dosya biçimi türü

 bu**[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**numaralandırma, tarayıcıya gönderilen dosyanın doğrudan tarayıcıda veya .xls/.xlsx veya başka bir uzantıyla ilişkili bir uygulamada kendi kendine açma seçeneği sunup sunmadığını belirler.

Numaralandırma, aşağıdaki önceden tanımlanmış kaydetme türlerini içerir:

|**Tip**|**Açıklama**|
|:- |:- |
|Ek|Elektronik tabloyu tarayıcıya gönderir ve bir uygulamada .xls/.xlsx veya diğer uzantılarla ilişkili bir ek olarak açılır.|
|Çizgide|Belgeyi tarayıcıya gönderir ve elektronik tabloyu diske kaydetme veya tarayıcıda açma seçeneği sunar|

### **XLS Dosyalar**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **XLSX Dosyalar**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **PDF Dosyalar**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **Not**

.NET5 ve .Netstandard'da "System.Web.HttpResponse" nesnesi bulunmadığından,
Yani bu fonksiyon Aspose.Cells .NET5 ve .Netstandard versiyonunda yoktur, dosyayı stream'e kaydetmek için aşağıdaki koda başvurabilir, ardından stream'e işlem yapabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

