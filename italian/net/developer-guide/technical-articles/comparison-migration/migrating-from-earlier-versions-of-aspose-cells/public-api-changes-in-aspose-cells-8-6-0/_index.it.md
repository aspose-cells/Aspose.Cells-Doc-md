---
title: Pubblico API Modifiche Aspose.Cells 8.6.0
type: docs
weight: 190
url: /it/net/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.5.2 alla 8.6.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati,[classi aggiunte ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-6-0/), ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per la manipolazione dei metadati senza creare un oggetto della cartella di lavoro**
Questa versione di Aspose.Cells for .NET API ha esposto due nuove classi, WorkbookMetadata e MetadataOptions, insieme a una nuova enumerazione MetadataType che ora consente di manipolare le proprietà del documento (metadati) senza creare un'istanza di Workbook. La classe WorkbookMetadata è leggera e fornisce un meccanismo molto facile da usare ed efficiente per[leggere, scrivere e aggiornare le proprietà del documento senza influire sulle prestazioni complessive](/cells/it/net/using-workbookmetadata/).

Di seguito è riportato il semplice scenario di utilizzo.

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


### **Proprietà HtmlSaveOptions.ExportFrameScriptsAndProperties aggiunta**
Aspose.Cells for .NET 8.6.0 ha esposto la proprietà HtmlSaveOptions.ExportFrameScriptsAndProperties che può essere utilizzata per influenzare la creazione di script aggiuntivi durante la conversione dei fogli di calcolo nel formato HTML. Con le impostazioni predefinite, le API Aspose.Cells esportano il foglio di calcolo nel formato HTML mentre l'applicazione Excel esegue l'esportazione, ovvero; il risultante HTML contiene i frame e i commenti condizionali, che rilevano il tipo di browser e regolano il layout di conseguenza. Il valore predefinito della proprietà HtmlSaveOptions.ExportFrameScriptsAndProperties è true, ovvero; l'esportazione avviene secondo gli standard di Excel. Tuttavia, se la proprietà è impostata su false, API non lo farà[generare gli script relativi ai frame e ai commenti condizionali](/cells/it/net/disable-exporting-frame-scripts-and-document-properties/). In questo caso, il risultante HTML può essere visualizzato correttamente in qualsiasi browser, tuttavia non può essere reimportato utilizzando le API Aspose.Cells.

Di seguito è riportato il semplice scenario di utilizzo.

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


### **Proprietà Shape.MarcoName aggiunto**
Aspose.Cells for .NET 8.6.0 ha esposto la proprietà Shape.MarcoName che può essere utilizzata per[assegnare qualsiasi modulo VBA a un controllo del modulo](/cells/it/net/assign-macro-to-form-control/) tale pulsante per fornire l'interazione. La proprietà è di tipo stringa quindi può accettare il nome del modulo e assegnarlo al controllo.

Di seguito è riportato il semplice scenario di utilizzo.

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


### **Proprietà OoxmlSaveOptions.UpdateZoom aggiunta**
Con il rilascio di v8.6.0, Aspose.Cells for .NET API ha esposto la proprietà OoxmlSaveOptions.UpdateZoom che può essere utilizzata per aggiornare PageSetup.Zoom se le proprietà PageSetup.FitToPagesWide e/o PageSetup.FitToPagesTall sono state utilizzate per controllare il ridimensionamento del foglio di lavoro.
