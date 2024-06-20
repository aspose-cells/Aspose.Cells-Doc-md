---
title: Aspose.Cells 8.6.0 de Yapılan Genel API Değişiklikleri
type: docs
weight: 200
url: /tr/java/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sının 8.5.2'den 8.6.0'a sürümünde modül/uygulama geliştiricilerinin ilgisini çekebilecek değişiklikleri açıklar. Yeni ve güncellenmiş genel yöntemler, [eklenen sınıflar vb.](/cells/tr/java/public-api-changes-in-aspose-cells-8-6-0/) yanı sıra Aspose.Cells'in arka plandaki davranışındaki herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Belge Oluşturmadan Metaveri Manipülasyon Desteği**
Bu Aspose.Cells for Java API sürümü, WorkbookMetadata ve MetadataOptions adında iki yeni sınıfı ve belge örneği oluşturmadan belge özelliklerini (meta veri) manipüle etmeyi sağlayan yeni bir Metaveri Türü adlı yeni bir numaralandırmayı açığa çıkardı. WorkbookMetadata sınıfı hafif ve [genel performansı etkilemeden belge özelliklerini okuma, yazma ve güncelleme imkanı sağlar](/cells/tr/java/using-workbookmetadata/). 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Open Workbook metadata while specifying the appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DOCUMENT_PROPERTIES);

WorkbookMetadata metaWorkbook = new WorkbookMetadata("sample.xlsx", options);

//Set some properties

metaWorkbook.getCustomDocumentProperties().add("test", "test");

//Save the metadata information to the spreadsheet file

metaWorkbook.save(filePath);

{{< /highlight >}}
### **HtmlSaveOptions.ExportFrameScriptsAndProperties Özelliği Eklendi**
Aspose.Cells for Java 8.6.0, HtmlSaveOptions.ExportFrameScriptsAndProperties özelliğini ortaya çıkardı; bu özellik, elektronik tabloların HTML biçimine dönüştürülürken ek scriptlerin oluşturulmasını etkilemek için kullanılabilir. Varsayılan ayarlarla, Aspose.Cells API'leri elektronik tabloyu Excel uygulamasının dışa aktarımı gibi HTML biçiminde dışa aktarır; yani sonuçta oluşan HTML, tarayıcı türünü algılayan ve düzeni buna göre ayarlayan çerçeveler ve koşullu yorumlar içerir. HtmlSaveOptions.ExportFrameScriptsAndProperties özelliğinin varsayılan değeri true'dur, bu da dışa aktarımın Excel standartlarına göre yapıldığı anlamına gelir. Eğer özellik false olarak ayarlanırsa, API çerçeveler ve koşullu yorumlarla ilgili scriptleri oluşturmayacak. Bu durumda oluşan HTML, herhangi bir tarayıcıda doğru şekilde görüntülenebilir, ancak Aspose.Cells API'leri kullanılarak içe aktarılamaz.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.setExportFrameScriptsAndProperties(false);

//Save spreadsheet as HTML

book.save("output.html", options)

{{< /highlight >}}
### **Shape.MarcoName Özelliği Eklendi**
Aspose.Cells for Java 8.6.0, Shape.MarcoName özelliğini ortaya çıkardı; bu özellik, bir Düğme gibi bir form kontrolüne bir VBA modülü atamak için kullanılabilir. Özellik, string tipindedir bu nedenle modül adını kabul edebilir ve denetim'e atar.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Create a new Workbook object

Workbook workbook = new Workbook();

//Get the instance of first default worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Add a new module to the first worksheet

int moduleIdx = workbook.getVbaProject().getModules().add(sheet);

//Get the instance of newly added module

VbaModule module = workbook.getVbaProject().getModules().get(moduleIdx);

//Add module code

module.setCodes("Sub ShowMessage()" + "\r\n" +

        "    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

        "End Sub");

//Create a new button to the worksheet and set its various properties

Button button = (Button) sheet.getShapes().addShape(MsoDrawingType.BUTTON, 2, 0, 2, 0, 28, 80);

button.setPlacement(PlacementType.FREE_FLOATING);

button.getFont().setName("Tahoma");

button.getFont().setBold(true);

button.getFont().setColor(Color.getBlue());

button.setText("Aspose");

//Assign the newly added module to the button

button.setMacroName(module.getName() + ".ShowMessage" );

//Save the spreadsheet in XLSM format

workbook.save("output.xlsm");

{{< /highlight >}}
### **OoxmlSaveOptions.UpdateZoom Özelliği Eklendi**
V8.6.0 sürümüyle beraber, Aspose.Cells for Java API'sı OoxmlSaveOptions.UpdateZoom özelliğini ortaya çıkarmıştır; bu özellik, SayfaDüzeni.Zoom'u güncellemek için kullanılabilir eğer SayfaDüzeni.FitToPagesWide ve/veya SayfaDüzeni.FitToPagesTall özellikleri, Çalışsayfa ölçeklendirmesini kontrol etmek üzere kullanılmışsa.
