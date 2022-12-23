---
title: Genel API Aspose.Cells 8.0.0'daki değişiklikler
type: docs
weight: 20
url: /tr/java/public-api-changes-in-aspose-cells-8-0-0/
---
{{% alert color="primary" %}} 

Bu sayfa, Aspose.Cells 8.0.0'da tanıtılan genel API değişikliklerini listeler. Yalnızca yeni ve eski genel yöntemleri değil, aynı zamanda Aspose.Cells'deki perde arkasındaki mevcut kodu etkileyebilecek davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **LoadOptions & WorkbookSettings'e MemorySetting eklendi**
Aspose.Cells for Java v8.0.0'dan başlayarak, performans değerlendirmeleri için bellek kullanım seçeneklerini sağladık. MemorySetting özelliği artık LoadOptions & WorkbookSettings sınıflarında mevcuttur.
### **Örnek vermek**
Optimize edilmiş modda (büyük boyutlu) bir Excel dosyasının nasıl okunacağını gösterir.

**Java**

{{< highlight "csharp" >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Optimize edilmiş modda büyük Veri Kümesinin bir çalışma sayfasına nasıl yazılacağını gösterir.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Büyük Dosyayla Çalışırken Belleği Optimize Etme](/cells/tr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)s.

{{% /alert %}}
## **Row & Cell uygulamaları değişti**
 Önceki sürümlerde, Satır ve Cell nesneleri, bir Çalışma Sayfasında karşılık gelen satır ve hücreyi temsil etmek için bellekte tutuluyordu. Aynı örnek her seferinde iade edildi**Satır Koleksiyonu[int dizini]** veya**Cells[int satır, int sütun]** alındı. Bellek performansının dikkate alınması için, bundan sonra yalnızca Row ve Cell'in özellikleri ve verileri bellekte tutulacaktır. Dolayısıyla, Row & Cell nesnesi, bahsedilen özelliklerin sarmalayıcısı haline geldi.
### **Örnek vermek**
Bundan sonra Cell ve Row nesnelerinin nasıl karşılaştırılacağını gösterir.

**Java**

{{< highlight "csharp" >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

Row ve Cell nesneleri çağrıya göre başlatıldığından, Cells bileşeni tarafından bellekte tutulmayacak ve yönetilmeyecektir. Bu nedenle bazı ekleme ve silme işlemlerinden sonra Satır & Sütun indeksleri güncellenemeyebilir veya daha da kötüsü bu nesneler geçersiz hale gelebilir.
### **Örnek vermek**
Örneğin, aşağıdaki kod parçacığı 8.0.0 ve üzerini kullanarak geçersiz sonuçlar verecektir,

**Java**

{{< highlight "csharp" >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

Yeni sürümle Cell nesnesi geçersiz hale gelecek veya bazı istenmeyen değerlerle A2'ye atıfta bulunacaktır. Böyle bir durumla karşılaşmamak için, doğru sonucu almak için hücreler koleksiyonundan Row veya Cell nesnelerini tekrar alın.

**Java**

{{< highlight "csharp" >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection, iç listesinde Row nesnesi olmadığından artık CollectionBase'i devralmaz.

{{% /alert %}}
## **Cell.StringValue Davranışı Değiştirildi**
 Önceki sürümlerde özel desen_hücre değerleri biçimlendirilirken göz ardı edildi, burada * özel karakteri her zaman biçimlendirilmiş sonuçta bir karakter üretti. Bu sürümden itibaren, mantığı özel karakterleri işlemek için değiştirdik._ ve* biçimlendirilmiş sonucu Excel uygulamasındakiyle aynı yapmak için. Örneğin, özel hücre biçimi "_(\$* #,##0.00_)", 123 değerini temsil etmek için kullanıldığında sonucu "$ 123.00" olarak üretti. Yeni sürümlerde, Cell.StringValue sonucu, Excel uygulamasının hücreyi kopyalarken sergilediği davranışla aynı olan "$123.00" olarak içerecektir. metin göndermek veya CSV'e aktarmak.
## **PdfSaveOptions'a CreatedTime eklendi**
Artık kullanıcılar, PdfSaveOptions sınıfını kullanırken e-tabloyu PDF'e kaydederken PDF oluşturma zamanını alabilir veya ayarlayabilir.
## **Çalışma Sayfasına Formülleri Göster eklendi**
Şu andan itibaren kullanıcılar, belirli bir çalışma sayfasının görünümü ve formülü arasında geçiş yapmak için Worksheet tarafından sunulan ShowFormulas Boolean özelliğini kullanabilir.
## **FileFormatType'a Ooxml eklendi**
FileFormatType sınıfına, XLSX, DOCX, PPTX ve daha fazlası gibi şifrelenmiş Office açık XML dosyasını temsil etmesi için yeni bir Ooxml sabiti eklendi.
## **AutoFilter'ın Eski FilterColumnCollection'ı**
Aspose.Cells for Java ile getFilterColumnCollection yöntemi geçersiz olarak işaretlendi. Bunun yerine AuotFilter.getFilterColumns yönteminin kullanılması önerilir.
## **SeriesCollection.SecondCategoryData, SeriesCollection.SecondCategoryData ile değiştirildi**
SeriesCollection.getSecondCatergoryData için yöntem adındaki yazım hatası hatasını temel olarak düzelttik. SeriesCollection.getSecondCategoryData yöntemini bundan sonra kullanabilirsiniz, oysa orijinal SeriesCollection.getSecondCatergoryData yöntemi geçersiz olarak işaretlendi.
