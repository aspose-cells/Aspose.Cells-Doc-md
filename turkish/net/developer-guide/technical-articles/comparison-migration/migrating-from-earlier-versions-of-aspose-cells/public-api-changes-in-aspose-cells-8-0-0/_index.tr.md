---
title: Genel API Aspose.Cells 8.0.0'daki değişiklikler
type: docs
weight: 10
url: /tr/net/public-api-changes-in-aspose-cells-8-0-0/
---
{{% alert color="primary" %}} 

Bu sayfa, Aspose.Cells 8.0.0'da tanıtılan genel API değişikliklerini listeler. Yalnızca yeni ve eski genel yöntemleri değil, aynı zamanda Aspose.Cells'deki perde arkasındaki mevcut kodu etkileyebilecek davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **LoadOptions & WorkbookSettings'e MemorySetting eklendi**
Aspose.Cells for .NET v8.0.0'dan başlayarak, performans değerlendirmeleri için bellek kullanım seçeneklerini sağladık. MemorySetting özelliği artık LoadOptions & WorkbookSettings sınıflarında mevcuttur.
##### **Örnek**
Optimize edilmiş modda (büyük boyutlu) bir Excel dosyasının nasıl okunacağını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Optimize edilmiş modda büyük Veri Kümesinin bir çalışma sayfasına nasıl yazılacağını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Büyük Dosyayla Çalışırken Belleği Optimize Etme](/cells/tr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **Row & Cell uygulamaları değişti**
 Önceki sürümlerde, Satır ve Cell nesneleri, bir Çalışma Sayfasında karşılık gelen satır ve hücreyi temsil etmek için bellekte tutuluyordu. Aynı örnek her seferinde iade edildi**Satır Koleksiyonu[int dizini]** veya**Cells[int satır, int sütun]** alındı. Bellek performansının dikkate alınması için, bundan sonra yalnızca Row ve Cell'in özellikleri ve verileri bellekte tutulacaktır. Dolayısıyla, Row & Cell nesnesi, bahsedilen özelliklerin sarmalayıcısı haline geldi.
### **Örnek**
Bundan sonra Cell ve Row nesnelerinin nasıl karşılaştırılacağını gösterir.

**C#**

{{< highlight "csharp" >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

Row ve Cell nesneleri çağrıya göre başlatıldığından, Cells bileşeni tarafından bellekte tutulmayacak ve yönetilmeyecektir. Bu nedenle bazı ekleme ve silme işlemlerinden sonra Satır & Sütun indeksleri güncellenemeyebilir veya daha da kötüsü bu nesneler geçersiz hale gelebilir.
### **Örnek**
Örneğin, aşağıdaki kod parçacığı 8.0.0 ve üzerini kullanarak geçersiz sonuçlar verecektir,

**C#**

{{< highlight "csharp" >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



Yeni sürümle Cell nesnesi geçersiz hale gelecek veya bazı istenmeyen değerlerle A2'ye atıfta bulunacaktır. Böyle bir durumla karşılaşmamak için, doğru sonucu almak için hücreler koleksiyonundan Row veya Cell nesnelerini tekrar alın.

**C#**

{{< highlight "csharp" >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection, iç listesinde Row nesnesi olmadığından artık CollectionBase'i devralmaz.

{{% /alert %}}
## **Cell.StringValue Davranışı Değiştirildi**
 Önceki sürümlerde özel desen_hücre değerleri biçimlendirilirken göz ardı edildi, burada * özel karakteri her zaman biçimlendirilmiş sonuçta bir karakter üretti. Bu sürümden itibaren, mantığı özel karakterleri işlemek için değiştirdik._ ve* biçimlendirilmiş sonucu Excel uygulamasındakiyle aynı yapmak için. Örneğin, özel hücre biçimi "_(\$* #,##0.00_)", 123 değerini temsil etmek için kullanıldığında sonucu "$ 123.00" olarak üretti. Yeni sürümlerde, Cell.StringValue sonucu, Excel uygulamasının hücreyi kopyalarken sergilediği davranışla aynı olan "$123.00" olarak içerecektir. metin veya CSV'ye dışa aktarma.
## **PdfSaveOptions'a CreatedTime eklendi**
Artık kullanıcılar, PdfSaveOptions sınıfını kullanırken elektronik tabloyu PDF'ye kaydederken PDF oluşturma süresini alabilir veya ayarlayabilir.
## **Çalışma Sayfasına Formülleri Göster eklendi**
Artık kullanıcılar, belirli bir çalışma sayfasının görünümünü formülden değere değiştirmek için Worksheet tarafından sunulan ShowFormulas Boolean özelliğini kullanabilir.
## **FileFormatType'a Ooxml eklendi**
XLSX, DOCX, PPTX ve daha fazlası gibi şifrelenmiş Office açık XML dosyasını temsil etmesi için FileFormatType sınıfına yeni bir sabit Ooxml eklenmiştir.
## **AutoFilter'ın Eski FilterColumnCollection'ı**
Aspose.Cells for Java ile, FilterColumnCollection özelliği geçersiz olarak işaretlendi. Bunun yerine AuotFilter.FilterColumns özelliğinin kullanılması önerilir.
## **SeriesCollection.SecondCategoryData, SeriesCollection.SecondCategoryData ile değiştirildi**
SeriesCollection.SecondCatergoryData için özellik adındaki yazım hatası hatasını temel olarak düzelttik. SeriesCollection.SecondCategoryData özelliğini şu andan itibaren kullanabilirsiniz, oysa orijinal SeriesCollection.SecondCatergoryData özelliği geçersiz olarak işaretlendi.
