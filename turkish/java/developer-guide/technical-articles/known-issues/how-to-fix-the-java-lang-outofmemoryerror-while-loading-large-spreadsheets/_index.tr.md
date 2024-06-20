---
title: Java da Büyük Elektronik Tabloları Yüklerken java.lang.OutOfMemoryError ı Nasıl Düzeltebilirim
type: docs
weight: 20
url: /tr/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---

{{% alert color="primary" %}} 

Çalışma kitabı yapıcı büyük elektronik tabloları yüklerken java.lang.OutOfMemoryError hatası atabilir. Bu istisna, mevcut belleğin elektronik tabloyu tamamen belleğe yüklemek için yetersiz olduğunu önerir, bu nedenle elektronik tablo [Bellek Tercihleri](/cells/tr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/) etkinleştirilerek yüklenmelidir.

{{% /alert %}} 
## **Büyük elektronik tabloları yüklerken java.lang.OutOfMemoryError hatasını nasıl çözebilirim**
Aspose.Cells API'ları, elektronik tabloların yüklenmesi ve işlenmesi sırasında bellek tüketimini optimize etmek için Bellek Tercihleri sağlar. Bu seçenekler ayrıca, Workbook nesnesindeki dev veri setlerine sahip büyük elektronik tabloların etkili bir şekilde yüklenmesine yardımcı olur. 

**Java**

{{< highlight csharp >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
