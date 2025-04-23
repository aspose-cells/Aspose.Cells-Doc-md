---
title: Aspose.Cells 8.6.0 de Yapılan Genel API Değişiklikleri
type: docs
weight: 190
url: /tr/net/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

Bu belge, sürüm 8.5.2'den 8.6.0'a Aspose.Cells API'daki değişiklikleri açıklar ve modül / uygulama geliştiricileri için ilgi çekici olabilecek herhangi bir değişikliği içerir. Yeni ve güncellenmiş genel methodlar, eklenmiş sınıflar vb. gibi sadece yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'in arka plandaki davranışındaki herhangi bir değişikliğin de açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Belge Oluşturmadan Metaveri Manipülasyon Desteği**
Bu sürümde Aspose.Cells for .NET API, WorkbookMetadata ve MetadataOptions adlı iki yeni sınıfı ve belge özelliklerini (meta veri) oluşturma gereksinimi olmaksızın manipüle etmeye izin veren MetadataType adlı yeni bir numaralandırmayı ortaya çıkarmıştır. WorkbookMetadata sınıfı hafif ve kullanımı çok kolay, etkili bir mekanizma sağlar. Performansı etkilemeden belge özelliklerini okuma, yazma ve güncellemeyi sağlar.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet with WorkbookMetadata while specifying appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DocumentProperties);

WorkbookMetadata metadata = new WorkbookMetadata(filePath, options);

//Set some properties

metadata.CustomDocumentProperties.Add("test", "test");

//Save the metadata info to spreadsheet

metadata.Save(filePath);

{{< /highlight >}}


### **HtmlSaveOptions.ExportFrameScriptsAndProperties Özelliği Eklendi**
Aspose.Cells for .NET 8.6.0, spreadsheets'leri HTML biçimine dönüştürürken ek script'lerin oluşturulmasını etkileyebilen HtmlSaveOptions.ExportFrameScriptsAndProperties özelliğini ortaya çıkarmıştır. Varsayılan ayarlarla, Aspose.Cells API'leri, sonuçta HTML'nin çerçeveleri ve koşulsal yorumları içerdiği standart Excel uygulamasının yapacağı gibi, yani; sonuçta HTML, tarayıcı türünü algılar ve düzeni buna göre ayarlar. HtmlSaveOptions.ExportFrameScriptsAndProperties özelliğinin varsayılan değeri true'dur, yani; dönüşüm Excel standartlarına göre yapılır. Ancak, özellik false olarak ayarlanırsa, API [script'lerin ve koşulsal yorumların oluşturulmayacağı](/cells/tr/net/disable-exporting-frame-scripts-and-document-properties/) anlamına gelir. Bu durumda, sonuçta HTML herhangi bir tarayıcıda doğru şekilde görüntülenebilir, ancak Aspose.Cells API'leri kullanılarak içeri aktarılamaz.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.ExportFrameScriptsAndProperties = false;

//Save spreadsheet as HTML

book.Save("output.html", options);

{{< /highlight >}}


### **Shape.MarcoName Özelliği Eklendi**
Aspose.Cells for .NET 8.6.0, form kontrollerine (örneğin, bir Düğme) herhangi bir VBA modülünü [atamak için kullanılan Shape.MarcoName özelliğini ortaya çıkarmıştır](/cells/tr/net/assign-macro-to-form-control/). Özellik, bir dize türündedir, bu nedenle modül adını kabul eder ve kontrolle ilişkilendirir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access first default worksheet

Worksheet sheet = workbook.Worksheets[0];

//Add a module to the worksheet

int moduleIdx = workbook.VbaProject.Modules.Add(sheet);

//Access newly added module from the collection

VbaModule module = workbook.VbaProject.Modules[moduleIdx];

//Add code to the module

module.Codes =

    "Sub ShowMessage()" + "\r\n" +

    "    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

    "End Sub";

//Add a Button on the worksheet and set its various properties

Aspose.Cells.Drawing.Button button = sheet.Shapes.AddButton(2, 0, 2, 0, 28, 80);

button.Placement = Aspose.Cells.Drawing.PlacementType.FreeFloating;

button.Font.Name = "Tahoma";

button.Font.IsBold = true;

button.Font.Color = System.Drawing.Color.Blue;

button.Text = "Aspose";

//Assign the VBA module to the button

button.MacroName = sheet.Name + ".ShowMessage";

//Save the result

workbook.Save("output.xlsm");

{{< /highlight >}}


### **OoxmlSaveOptions.UpdateZoom Özelliği Eklendi**
v8.6.0 ile, Aspose.Cells for .NET API, OoxmlSaveOptions.UpdateZoom özelliğini PageSetup.Zoom'u güncellemek için ortaya çıkarmıştır. PageSetup.FitToPagesWide ve/veya PageSetup.FitToPagesTall özelliklerinin Worksheet ölçeklendirmesini kontrol etmek için kullanılabilir.
{{< app/cells/assistant language="csharp" >}}
