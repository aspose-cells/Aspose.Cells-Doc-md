---
title: Genel API Aspose.Cells 8.0.1'deki değişiklikler
type: docs
weight: 20
url: /tr/net/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

Bu sayfa, Aspose.Cells 8.0.1'de tanıtılan genel API değişikliklerini listeler. Yalnızca yeni ve eskimiş genel yöntemleri değil, aynı zamanda Aspose.Cells'deki perde arkasındaki mevcut kodu etkileyebilecek davranış değişikliklerinin açıklamasını da içerir. Bir gerileme olarak görülebilen ve mevcut davranışı değiştiren herhangi bir davranış özellikle önemlidir ve burada belgelenmiştir.

{{% /alert %}} 
## **Cells Sınıfına MemorySetting Özelliği Eklendi**
Cells sınıfı, hücre verileri için bellek kullanımını optimize etmek ve dolayısıyla genel bellek maliyetini azaltmak için kullanılabilen MemorySetting özelliğini kullanıma sundu. Aşağıdaki örnek, optimize edilmiş modda bir çalışma sayfasına büyük bir verinin nasıl yazılacağını gösterir.

**C#**

{{< highlight "csharp" >}}

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

Bellek ayarları, Çalışma Kitabı nesnesi tarafından otomatik olarak oluşturulan varsayılan sayfa için çalışmayacaktır. Mevcut sayfaların hafıza ayarlarını değiştirmek için lütfen herhangi bir veri işleme yapmadan önce hafıza ayarını manuel olarak uygulayın.

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Büyük Veri Kümeleriyle Çalışırken Belleği Optimize Etme](/cells/tr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
