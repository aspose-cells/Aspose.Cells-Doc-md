---
title: Aspose.Cells 8.0.1 de Genel API Değişiklikleri
type: docs
weight: 30
url: /tr/java/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Bu sayfa, Aspose.Cells 8.0.1'de tanıtılan genel API değişikliklerini listeleyen bir sayfadır. Bu, sadece yeni ve eskimiş genel yöntemleri değil, aynı zamanda mevcut kodları etkileyebilecek Aspose.Cells arka planındaki davranışlardaki herhangi değişikliklerin bir açıklamasını içerir. Mevcut davranışı değiştiren herhangi bir davranış özellikle önemli olup burada dökümante edilmektedir.

{{% /alert %}} 
## **MemorySetting Özelliği, Cells Sınıfına Eklendi**
Cells sınıfı, hücre verilerinin bellek kullanımını optimize etmek için kullanılabilecek setMemorySetting ve getMemorySetting yöntemlerini açığa çıkardı. Aşağıdaki örnek, optimize edilmiş modda geniş bir veri kümesini çalışsayfaya yazmanın nasıl yapılacağını göstermektedir.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.getWorksheets().get(0).getCells();

cells.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large dataset into the cells of the worksheet.

//Your code goes here

{{< /highlight >}}

{{% alert color="primary" %}} 

Bellek ayarları, Workbook tarafından otomatik olarak oluşturulan varsayılan sayfa için çalışmaz. Var olan sayfaların bellek ayarlarını değiştirmek için, veri manipülasyonu yapmadan önce bellek ayarlarını manuel olarak uygulayınız. 

{{% /alert %}} {{% alert color="primary" %}} 

[Büyük Veri Kümeleriyle Çalışırken Belleği Optimize Etme](/cells/tr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/) konusundaki detaylı makaleyi kontrol edin

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
