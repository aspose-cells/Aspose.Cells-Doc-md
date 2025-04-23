---
title: Aspose.Cells 8.0.0 daki Genel API Değişiklikler
type: docs
weight: 10
url: /tr/net/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

Bu sayfa, Aspose.Cells 8.0.0'da tanıtılan genel API değişikliklerini listeler. Yeni ve eskimiş genel yöntemlerin yanı sıra, mevcut kodu etkileyebilecek Aspose.Cells'in arkasındaki davranışlarda yapılan herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **YükOptions ve WorkbookSettings'e MemorySetting eklendi**
Aspose.Cells for .NET sürümünden itibaren, performans düşünceleri için bellek kullanımı seçenekleri sağladık. MemorySetting özelliği şimdi LoadOptions ve WorkbookSettings sınıflarında mevcuttur.
##### **Örnek**
Büyük boyuta sahip bir Excel dosyasını (optimize edilmiş modda) nasıl okuyacağınızı gösterir.

**C#**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Büyük bir Veri Setini optimize edilmiş modda bir çalışsayfa içine nasıl yazacağınızı gösterir.

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

Lütfen [Büyük Veri Dosyaları ve Büyük Veri Kümeleri ile Çalışırken Belleği Optimizasyonu](/cells/tr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/) hakkında detaylı makaleyi kontrol edin.

{{% /alert %}}
## **Satır ve Hücre uygulamaları değişti**
Önceki sürümlerde, Satır ve Hücre nesneleri, ilgili çalışsayfadaki karşılık gelen satırı ve hücreyi temsil etmek üzere bellekte tutulurdu. Bellek performansı düşünüldüğünde, şimdi Satır ve Hücrenin yalnızca özellikleri ve verileri bellekte tutulacaktır. Bu nedenle Satır ve Hücre nesnesi, mezkur özelliklerin bir kapsayıcısı haline gelmiştir.
### **Örnek**
Artık Hücre ve Satır nesnelerini nasıl karşılaştıracağınızı gösterir.

**C#**

{{< highlight csharp >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

Satır ve Hücre nesneleri, çağrıya göre örneklendirildiğinden, bunlar Çalışsayfa bileşeni tarafından bellekte tutulmayacak ve yönetilmeyecektir.
### **Örnek**
Örneğin, 8.0.0 ve sonraki sürümlerde aşağıdaki kod örneği geçersiz sonuçlar döndürecektir,

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



Yeni sürümle birlikte Hücre nesnesi geçersiz hale gelecek veya istenmeyen bir değere sahip A2'ye yönlendirilecektir. Bu tür durumları önlemek için, doğru sonucu almak için Satır veya Hücre nesnelerini tekrar hücre koleksiyonundan alın.

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection artık CollectionBase'den miras almıyor çünkü iç listesinde Satır nesnesi bulunmuyor.

{{% /alert %}}
## **Hücre.StringValue Davranışı Değişti**
Önceki sürümlerde, özel desen _ hücre değerlerini biçimlendirirken dikkate alınmazdı, * özel karakteri her zaman biçimli sonuca bir karakter üretirdi. Bu sürümden itibaren, hücre değerlerinde _ ve * özel karakterleri işlemek için mantığı değiştirdik, bu sayede biçimli sonucun Excel uygulamasıyla aynı hale gelmesini sağladık. Örneğin, "_(\$* #,##0.00_)" özel hücre biçimi, 123 değerini "$ 123.00" sonucunu üretirdi. Yeni sürümlerle, Hücre.StringValue sonucu "$123.00" olarak biçimlendirilmiş olacaktır ki bu Excel uygulamasının hücreyi metne kopyalarken veya CSV'ye dönüştürürken sergilediği davranışa benzer.
## **PdfSaveOptions'a CreatedTime Eklendi**
Artık PdfSaveOptions sınıfını kullanarak çalışsayfayı PDF olarak kaydederken PDF oluşturma zamanını alabilir veya ayarlayabilirsiniz.
## **Çalışsayfasında Boolean özelliği ShowFormulas yeni sürümlerde kullanılabilir.**
Artık Kullanıcılar, Formül göstermek için Worksheet tarafından sunulan Boolean ShowFormulas özelliğini kullanabilir.
## **FileFormatType'a Ooxml Eklendi**
Şifreli Office açık XML dosyasını (örneğin XLSX, DOCX, PPTX vb.) temsil etmek için FileFormatType sınıfına yeni bir sabit Ooxml eklenmiştir.
## **AutoFilter'ın FilterColumnCollection'ı Eski Kullanımdan Kaldırıldı**
Aspose.Cells for Java ile FilterColumnCollection özelliği eski olarak işaretlendi. Bunun yerine AuotFilter.FilterColumns özelliğinin kullanılması önerilir.
## **SeriesCollection.SecondCatergoryData, SeriesCollection.SecondCategoryData ile Değiştirildi**
Temelde SeriesCollection.SecondCatergoryData özelliğindeki yazım hatasını düzelttik. Artık SeriesCollection.SecondCategoryData özelliğini kullanabilirken, orijinal SeriesCollection.SecondCatergoryData özelliği eski olarak işaretlenmiştir.
{{< app/cells/assistant language="csharp" >}}
