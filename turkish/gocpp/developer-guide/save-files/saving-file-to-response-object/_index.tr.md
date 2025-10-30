---
title: Dosyayı Yanıt Nesnesine kaydetmek Golang ile C++ kullanarak
linktitle: Yanıt Nesnesine Dosya Kaydet
type: docs
weight: 50
url: /tr/go-cpp/saving-file-to-response-object/
description: Aspose.Cells for C++ kullanarak dosyaları dinamik şekilde kaydetmeyi ve doğrudan istemci tarayıcısına göndermeyi öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, dosyaların manipüle edilmesini mümkün kılar. Bu makale, dosyaların bir yanıt nesnesine nasıl kaydedilebileceğini açıklar.

{{% /alert %}}

## **Yanıt Nesnesine Dosya Kaydetme**

Ayrıca, bir dosya dinamik olarak oluşturulup doğrudan istemci tarayıcısına gönderilmesi de mümkündür. Bunun için aşağıdaki parametreleri kabul eden [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/) yönteminin özel aşırı yüklenmiş sürümünü kullanın:

- **HttpResponse** nesnesi.
- Dosya adı.
- Çıktı dosyasının içerik düzeni türü olan [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/).
- [**SaveOptions**](https://reference.aspose.com/cells/go-cpp/saveoptions/), dosya biçim tipi.

[**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/) numaralandırması, tarayıcıya gönderilen dosyanın doğrudan tarayıcıda kendisi veya .xls/.xlsx veya başka bir uzantıyla ilişkilendirilmiş bir uygulamada açılıp açılmamasının seçeneğini belirler.

Numaralama aşağıdaki önceden tanımlanmış kaydetme türlerini içerir:

|**Tür**|**Açıklama**|
| :- | :- |
|Ek|Elektronik tabloyu tarayıcıya gönderir ve .xls/.xlsx veya diğer uzantılarla ilişkilendirilmiş bir uygulamada bir eki olarak açar|
|İçeride|Belgeyi tarayıcıya gönderir ve elektronik tabloyu diske kaydetme veya tarayıcı içinde açma seçeneği sunar|

### **XLS Dosyaları**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject.go" >}}
### **XLSX Dosyaları**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-1.go" >}}
### **PDF Dosyaları**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-2.go" >}}
### **Not**

Sistemi içermeyen "System.Web.HttpResponse" nesnesi sebebiyle,
Bu durum, Aspose.Cells .NET5 ve .Netstandard sürümlerinde bulunmadığı için, dosyayı akıma kaydetme işlemini yapmak için aşağıdaki kodlara başvurabilirsiniz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-3.go" >}}
