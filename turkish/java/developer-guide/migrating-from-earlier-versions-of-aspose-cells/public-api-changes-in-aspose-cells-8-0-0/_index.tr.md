---
title: Aspose.Cells 8.0.0 daki Genel API Değişiklikler
type: docs
weight: 20
url: /tr/java/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

Bu sayfa, Aspose.Cells 8.0.0'da tanıtılan genel API değişikliklerini listeler. Yeni ve eskimiş genel yöntemlerin yanı sıra, mevcut kodu etkileyebilecek Aspose.Cells'in arkasındaki davranışlarda yapılan herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **YükOptions ve WorkbookSettings'e MemorySetting eklendi**
Kullanım düşüncesi için bellek kullanımı seçeneklerini sunma amacıyla Aspose.Cells for Java'nin v8.0.0'inden itibaren. MemorySetting özelliği artık LoadOptions ve WorkbookSettings sınıflarında mevcuttur.
### **Örnek**
Büyük boyuta sahip bir Excel dosyasını (optimize edilmiş modda) nasıl okuyacağınızı gösterir.

**Java**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Büyük bir Veri Setini optimize edilmiş modda bir çalışsayfa içine nasıl yazacağınızı gösterir.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

[Büyük Dosyalar İle Çalışırken Belleği Optimize Etme](/cells/tr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/) başlıklı detaylı makaleyi kontrol edin.

{{% /alert %}}
## **Satır ve Hücre uygulamaları değişti**
Önceki sürümlerde, Satır ve Hücre nesneleri, ilgili çalışsayfadaki karşılık gelen satırı ve hücreyi temsil etmek üzere bellekte tutulurdu. Bellek performansı düşünüldüğünde, şimdi Satır ve Hücrenin yalnızca özellikleri ve verileri bellekte tutulacaktır. Bu nedenle Satır ve Hücre nesnesi, mezkur özelliklerin bir kapsayıcısı haline gelmiştir.
### **Örnek**
Artık Hücre ve Satır nesnelerini nasıl karşılaştıracağınızı gösterir.

**Java**

{{< highlight csharp >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

Satır ve Hücre nesneleri, çağrıya göre örneklendirildiğinden, bunlar Çalışsayfa bileşeni tarafından bellekte tutulmayacak ve yönetilmeyecektir.
### **Örnek**
Örneğin, 8.0.0 ve sonraki sürümlerde aşağıdaki kod örneği geçersiz sonuçlar döndürecektir,

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

Yeni sürümle birlikte Hücre nesnesi geçersiz hale gelecek veya istenmeyen bir değere sahip A2'ye yönlendirilecektir. Bu tür durumları önlemek için, doğru sonucu almak için Satır veya Hücre nesnelerini tekrar hücre koleksiyonundan alın.

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection artık CollectionBase'den miras almıyor çünkü iç listesinde Satır nesnesi bulunmuyor.

{{% /alert %}}
## **Hücre.StringValue Davranışı Değişti**
Önceki sürümlerde, özel desen _ hücre değerlerini biçimlendirirken dikkate alınmazdı, * karakteri ise daima biçimlendirilmiş sonuçta bir karakter üretirdi. Bu sürümden itibaren, _ ve * özel karakterlerini işleme mantığını değiştirdik ve biçimlendirilmiş sonucun Excel uygulamasının sonucuyla aynı olmasını sağladık. Örneğin, özel hücre formatı olan"_(\$* #,##0.00_)" değerini 123 olarak temsil ettiğinde sonuç "$ 123.00" idi. Yeni sürümlerle birlikte, Hücre.StringValue sonucu "$123.00" olacaktır ki bu da Excel uygulamasının, hücreyi metin olarak kopyalarken veya CSV'ye dışa aktarırken sergilediği davranışla aynıdır.
## **PdfSaveOptions'a CreatedTime Eklendi**
Artık PdfSaveOptions sınıfını kullanarak çalışsayfayı PDF olarak kaydederken PDF oluşturma zamanını alabilir veya ayarlayabilirsiniz.
## **Çalışsayfasında Boolean özelliği ShowFormulas yeni sürümlerde kullanılabilir.**
Artık Kullanıcılar, Çalışsayfa tarafından sunulan ShowFormulas özelliği kullanarak belirli bir çalışsayfanın formül ve değer görünümü arasında geçiş yapabilirler.
## **FileFormatType'a Ooxml Eklendi**
Şifreli Office açık XML dosyasını (örneğin XLSX, DOCX, PPTX vb.) temsil etmek için FileFormatType sınıfına yeni bir sabit Ooxml eklenmiştir.
## **AutoFilter'ın FilterColumnCollection'ı Eski Kullanımdan Kaldırıldı**
Aspose.Cells for Java ile getFilterColumnCollection yöntemi eskimiş olarak işaretlendi. Bunun yerine AutFilter.getFilterColumns yönteminin kullanılması önerilir.
## **SeriesCollection.SecondCatergoryData, SeriesCollection.SecondCategoryData ile Değiştirildi**
Ser SeriesCollection.getSecondCatergoryData yönteminde yazım hatasını düzeltildi. Bundan sonra SeriesCollection.getSecondCategoryData yöntemini kullanabilirsiniz, orijinal method artık eskimiş olarak işaretlendi.
