---
title: Aspose.Cells 8.8.2 de Genel API Değişiklikleri
type: docs
weight: 290
url: /tr/java/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricileri için Aspose.Cells API'sinde 8.8.1'den 8.8.2'ye yapılan değişiklikleri açıklar. Yeni ve güncellenmiş genel yöntemler, eklenen ve kaldırılan sınıflar vb. yanı sıra Aspose.Cells arkasındaki davranışlardaki değişikliklerin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Boş Satır ve Sutunları Silerken Referansları Otomatik Güncelle**
Aspose.Cells for Java 8.8.2, Cells.deleteBlankRows & Cells.deleteBlankColumns yöntemlerinin aşırı yüklenmiş versiyonlarını ortaya çıkardı. Yeni yöntemler, DeleteOptions sınıfının bir örneğini kabul edebilir ve formüllerde, grafik serisi verilerinde vb. oluşabilecek durumları aşmak için kullanılabilir. DeleteOptions sınıfının şu anda yalnızca bir üyesi, UpdateReference adlı Boolean türünde bir özelliktir. Söz konusu özellik true olarak ayarlandığında ve DeleteOptions sınıfının Cells.deleteBlankRows & Cells.deleteBlankColumns yöntemlerine iletilen örnek, API içsel olarak formül referanslarını (varsa) ayarlayacaktır. 

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için lütfen [Güncellenmiş Referanslar İle Boş Satır ve Sutunları Silme](/cells/tr/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/) başlıklı detaylı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

Workbook book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

Worksheet sheet = book.getWorksheets().get(0);

//Access cells of the desired worksheet

Cells cells = sheet.getCells();

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.setUpdateReference(true);

//Delete all blank rows and columns

cells.deleteBlankColumns(options);

cells.deleteBlankRows(options);

{{< /highlight >}}
