---
title: Genel API Aspose.Cells 8.6.0'daki değişiklikler
type: docs
weight: 200
url: /tr/java/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 Bu belge, Aspose.Cells API sürüm 8.5.2'den 8.6.0'a modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/java/public-api-changes-in-aspose-cells-8-6-0/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **Çalışma Kitabı Nesnesi Oluşturmadan Meta Veri Manipülasyonu Desteği**
Aspose.Cells for Java API'in bu sürümü, WorkbookMetadata & MetadataOptions adlı iki yeni sınıfı ve artık bir Workbook örneği oluşturmadan belge özelliklerini (meta veriler) değiştirmeye izin veren yeni bir MetadataType numaralandırmasını ortaya çıkardı. WorkbookMetadata sınıfı hafiftir ve kullanımı çok kolay, etkili bir mekanizma sağlar.[genel performansı etkilemeden belge özelliklerini okuyun, yazın ve güncelleyin](/cells/tr/java/using-workbookmetadata/). 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Open Workbook metadata while specifying the appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DOCUMENT_PROPERTIES);

WorkbookMetadata metaWorkbook = new WorkbookMetadata("sample.xlsx", options);

//Set some properties

metaWorkbook.getCustomDocumentProperties().add("test", "test");

//Save the metadata information to the spreadsheet file

metaWorkbook.save(filePath);

{{< /highlight >}}
### **Özellik HtmlSaveOptions.ExportFrameScriptsAndProperties Eklendi**
Aspose.Cells for Java 8.6.0, elektronik tabloları HTML biçimine dönüştürürken ek komut dosyalarının oluşturulmasını etkilemek için kullanılabilecek HtmlSaveOptions.ExportFrameScriptsAndProperties özelliğini kullanıma sundu. Varsayılan ayarlarla, Aspose.Cells API'leri, Excel uygulamasının dışa aktarımı yaptığı gibi elektronik tabloyu HTML biçiminde dışa aktarır, yani; ortaya çıkan HTML, tarayıcı türünü algılayan ve düzeni buna göre ayarlayan çerçeveleri ve koşullu yorumları içerir. HtmlSaveOptions.ExportFrameScriptsAndProperties özelliğinin varsayılan değeri true'dur, yani; dışa aktarma Excel standartlarına göre yapılır. Özellik false olarak ayarlanırsa API[çerçeveler ve koşullu yorumlarla ilgili komut dosyalarını oluşturun](/cells/tr/java/disable-exporting-frame-scripts-and-document-properties/). Bu durumda, ortaya çıkan HTML herhangi bir tarayıcıda doğru bir şekilde görüntülenebilir, ancak Aspose.Cells API'leri kullanılarak geri alınamaz.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.setExportFrameScriptsAndProperties(false);

//Save spreadsheet as HTML

book.save("output.html", options)

{{< /highlight >}}
### **Özellik Shape.MarcoName Eklendi**
Aspose.Cells for Java 8.6.0, kullanılabilecek Shape.MarcoName özelliğini kullanıma sundu.[form kontrolüne VBA modülü atama](/cells/tr/java/assign-macro-code-to-form-control/) etkileşimi sağlamak için böyle bir Düğme. Özellik string türündedir, bu nedenle modül adını kabul edebilir ve onu kontrole atar.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

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
### **Özellik OoxmlSaveOptions.UpdateZoom Eklendi**
v8.6.0'ın piyasaya sürülmesiyle, Aspose.Cells for Java API, Çalışma Sayfası ölçeklendirmesini kontrol etmek için PageSetup.FitToPagesWide ve/veya PageSetup.FitToPagesTall özellikleri kullanılmışsa PageSetup.Zoom'u güncellemek için kullanılabilecek OoxmlSaveOptions.UpdateZoom özelliğini kullanıma sundu.
