---
title: Yanıt Nesnesine Dosya Kaydet
type: docs
weight: 50
url: /tr/net/saving-file-to-response-object/
---

{{% alert color="primary" %}}

Aspose.Cells, dosyaların manipüle edilmesini mümkün kılar. Bu makale, dosyaların bir yanıt nesnesine nasıl kaydedilebileceğini açıklar.

{{% /alert %}}

## **Yanıt Nesnesine Dosya Kaydetme**

Ayrıca, bir dosya dinamik olarak oluşturulup doğrudan istemci tarayıcısına gönderilmesi de mümkündür. Bunun için aşağıdaki parametreleri kabul eden [**Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5) yönteminin özel aşırı yüklenmiş sürümünü kullanın:

- ASP.NET [**HttpResponse**](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8) nesnesi.
- Dosya adı.
- Çıktı dosyasının içerik düzeni türü olan [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition).
- Dosya biçim türü olan [**SaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/saveoptions).

[**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition) numaralandırması, tarayıcıya gönderilen dosyanın doğrudan tarayıcıda kendisi veya .xls/.xlsx veya başka bir uzantıyla ilişkilendirilmiş bir uygulamada açılıp açılmamasının seçeneğini belirler.

Numaralama aşağıdaki önceden tanımlanmış kaydetme türlerini içerir:

|**Tür**|**Açıklama**|
| :- | :- |
|Ek|Elektronik tabloyu tarayıcıya gönderir ve .xls/.xlsx veya diğer uzantılarla ilişkilendirilmiş bir uygulamada bir eki olarak açar|
|İçeride|Belgeyi tarayıcıya gönderir ve elektronik tabloyu diske kaydetme veya tarayıcı içinde açma seçeneği sunar|

### **XLS Dosyaları**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **XLSX Dosyaları**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **PDF Dosyaları**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **Not**

Sistemi içermeyen "System.Web.HttpResponse" nesnesi sebebiyle,
Bu durum, Aspose.Cells .NET5 ve .Netstandard sürümlerinde bulunmadığı için, dosyayı akıma kaydetme işlemini yapmak için aşağıdaki kodlara başvurabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

