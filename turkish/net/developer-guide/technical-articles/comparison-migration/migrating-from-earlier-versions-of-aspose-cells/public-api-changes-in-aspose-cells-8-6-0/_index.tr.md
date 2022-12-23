---
title: Genel API Aspose.Cells 8.6.0'daki değişiklikler
type: docs
weight: 190
url: /tr/net/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 Bu belge, Aspose.Cells API sürüm 8.5.2'den 8.6.0'a modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-6-0/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **Çalışma Kitabı Nesnesi Oluşturmadan Meta Veri Manipülasyonu Desteği**
Aspose.Cells for .NET API'in bu sürümü, WorkbookMetadata & MetadataOptions adlı iki yeni sınıfı ve artık bir Workbook örneği oluşturmadan belge özelliklerini (meta veriler) manipüle etmeye izin veren yeni bir MetadataType numaralandırmasını ortaya çıkardı. WorkbookMetadata sınıfı hafiftir ve kullanımı çok kolay, etkili bir mekanizma sağlar.[genel performansı etkilemeden belge özelliklerini okuyun, yazın ve güncelleyin](/cells/tr/net/using-workbookmetadata/).

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet with WorkbookMetadata while specifying appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DocumentProperties);

WorkbookMetadata metadata = new WorkbookMetadata(filePath, options);

//Set some properties

metadata.CustomDocumentProperties.Add("test", "test");

//Save the metadata info to spreadsheet

metadata.Save(filePath);

{{< /highlight >}}


### **Özellik HtmlSaveOptions.ExportFrameScriptsAndProperties Eklendi**
Aspose.Cells for .NET 8.6.0, elektronik tabloları HTML biçimine dönüştürürken ek komut dosyalarının oluşturulmasını etkilemek için kullanılabilecek HtmlSaveOptions.ExportFrameScriptsAndProperties özelliğini kullanıma sundu. Varsayılan ayarlarla, Aspose.Cells API'leri, Excel uygulamasının dışa aktarımı yaptığı gibi elektronik tabloyu HTML biçiminde dışa aktarır, yani; ortaya çıkan HTML, tarayıcı türünü algılayan ve düzeni buna göre ayarlayan çerçeveleri ve koşullu yorumları içerir. HtmlSaveOptions.ExportFrameScriptsAndProperties özelliğinin varsayılan değeri true'dur, yani; dışa aktarma Excel standartlarına göre yapılır. Ancak özellik false olarak ayarlanırsa API[çerçeveler ve koşullu yorumlarla ilgili komut dosyalarını oluşturun](/cells/tr/net/disable-exporting-frame-scripts-and-document-properties/). Bu durumda, ortaya çıkan HTML herhangi bir tarayıcıda doğru bir şekilde görüntülenebilir, ancak Aspose.Cells API'leri kullanılarak geri alınamaz.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.ExportFrameScriptsAndProperties = false;

//Save spreadsheet as HTML

book.Save("output.html", options);

{{< /highlight >}}


### **Özellik Shape.MarcoName Eklendi**
Aspose.Cells for .NET 8.6.0, kullanılabilecek Shape.MarcoName özelliğini kullanıma sundu.[herhangi bir VBA modülünü bir form kontrolüne atayın](/cells/tr/net/assign-macro-to-form-control/) etkileşimi sağlamak için böyle bir Düğme. Özellik string türündedir, bu nedenle modül adını kabul edebilir ve onu kontrole atar.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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


### **Özellik OoxmlSaveOptions.UpdateZoom Eklendi**
v8.6.0'ın piyasaya sürülmesiyle, Aspose.Cells for .NET API, Çalışma Sayfası ölçeklendirmesini kontrol etmek için PageSetup.FitToPagesWide ve/veya PageSetup.FitToPagesTall özellikleri kullanılmışsa PageSetup.Zoom'u güncellemek için kullanılabilecek OoxmlSaveOptions.UpdateZoom özelliğini kullanıma sundu.
