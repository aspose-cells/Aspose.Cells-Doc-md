---
title: Büyük Elektronik Tabloları Yüklerken java.lang.OutOfMemoryError Hatasını Düzeltme
type: docs
weight: 20
url: /tr/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---
{{% alert color="primary" %}} 

 Çalışma Kitabı oluşturucusunun büyük elektronik tabloları yüklerken java.lang.OutOfMemoryError hatası vermesi oldukça olasıdır. Bu istisna, kullanılabilir belleğin elektronik tabloyu belleğe tamamen yüklemek için yetersiz olduğunu, bu nedenle elektronik tablonun etkinleştirilirken yüklenmesi gerektiğini gösterir.[Bellek Tercihleri](/cells/tr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 
## **Büyük e-tablo yüklenirken java.lang.OutOfMemoryError nasıl düzeltilir?**
Aspose.Cells API'ler, elektronik tabloları yüklerken ve işlerken bellek tüketimini optimize etmek için Bellek Tercihleri sağlar. Bu seçenekler, aşağıda gösterildiği gibi, Workbook nesnesinde büyük veri kümeleri içeren büyük elektronik tabloların verimli bir şekilde yüklenmesine de yardımcı olur.

**Java**

{{< highlight "csharp" >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
