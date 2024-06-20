---
title: Aspose.Cells 8.0.1 de Genel API Değişiklikleri
type: docs
weight: 20
url: /tr/net/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Bu sayfa, Aspose.Cells 8.0.1'de tanıtılan genel API değişikliklerini listeleyen bir sayfadır. Bu, sadece yeni ve eskimiş genel yöntemleri değil, aynı zamanda mevcut kodları etkileyebilecek Aspose.Cells arka planındaki davranışlardaki herhangi değişikliklerin bir açıklamasını içerir. Mevcut davranışı değiştiren herhangi bir davranış özellikle önemli olup burada dökümante edilmektedir.

{{% /alert %}} 
## **MemorySetting Özelliği Cells Sınıfına Eklendi**
Cells sınıfı, hücre verilerinin bellek kullanımını optimize etmek için kullanılabilecek MemorySetting özelliğini açığa çıkardı, bu sayede genel bellek maliyetini azaltabilir.

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.Settings.MemorySetting = MemorySetting.MemoryPreference;

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.Worksheets[0].Cells;

cells.MemorySetting = MemorySetting.MemoryPreference;

//Input large dataset into the cells of the worksheet

//Your code goes here

{{< /highlight >}}

Bellek ayarları, Workbook nesnesi tarafından otomatik olarak oluşturulan varsayılan sayfa için çalışmaz. Varolan sayfaların bellek ayarlarını değiştirmek için lütfen veri manipülasyonu yapmadan önce bellek ayarını manuel olarak uygulayın.

{{% alert color="primary" %}} 

Lütfen [Büyük Veri Kümeleri ile Çalışırken Belleği Optimizasyonu](/cells/tr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/) hakkında detaylı makaleyi kontrol edin.

{{% /alert %}}
