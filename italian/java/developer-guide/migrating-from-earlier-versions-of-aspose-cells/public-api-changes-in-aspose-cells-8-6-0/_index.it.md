---
title: Pubblico API Modifiche Aspose.Cells 8.6.0
type: docs
weight: 200
url: /it/java/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.5.2 alla 8.6.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati,[classi aggiunte ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-6-0/), ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per la manipolazione dei metadati senza creare un oggetto della cartella di lavoro**
Questa versione di Aspose.Cells for Java API ha esposto due nuove classi, WorkbookMetadata e MetadataOptions, insieme a una nuova enumerazione MetadataType che ora consente di manipolare le proprietà del documento (metadati) senza creare un'istanza di Workbook. La classe WorkbookMetadata è leggera e fornisce un meccanismo molto facile da usare ed efficiente per[leggere, scrivere e aggiornare le proprietà del documento senza influire sulle prestazioni complessive](/cells/it/java/using-workbookmetadata/). 

Di seguito è riportato il semplice scenario di utilizzo.

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
### **Proprietà HtmlSaveOptions.ExportFrameScriptsAndProperties aggiunta**
Aspose.Cells for Java 8.6.0 ha esposto la proprietà HtmlSaveOptions.ExportFrameScriptsAndProperties che può essere utilizzata per influenzare la creazione di script aggiuntivi durante la conversione dei fogli di calcolo nel formato HTML. Con le impostazioni predefinite, le API Aspose.Cells esportano il foglio di calcolo nel formato HTML mentre l'applicazione Excel esegue l'esportazione, ovvero; il risultante HTML contiene i frame e i commenti condizionali, che rilevano il tipo di browser e regolano il layout di conseguenza. Il valore predefinito della proprietà HtmlSaveOptions.ExportFrameScriptsAndProperties è true, ovvero; l'esportazione avviene secondo gli standard di Excel. Se la proprietà è impostata su false, API non lo farà[generare gli script relativi ai frame e ai commenti condizionali](/cells/it/java/disable-exporting-frame-scripts-and-document-properties/). In questo caso, il risultante HTML può essere visualizzato correttamente in qualsiasi browser, tuttavia non può essere reimportato utilizzando le API Aspose.Cells.

Di seguito è riportato il semplice scenario di utilizzo.

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
### **Proprietà Shape.MarcoName aggiunto**
Aspose.Cells for Java 8.6.0 ha esposto la proprietà Shape.MarcoName che può essere utilizzata per[assegnare un modulo VBA a un controllo del modulo](/cells/it/java/assign-macro-code-to-form-control/) tale pulsante per fornire l'interazione. La proprietà è di tipo stringa quindi può accettare il nome del modulo e assegnarlo al controllo.

Di seguito è riportato il semplice scenario di utilizzo.

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
### **Proprietà OoxmlSaveOptions.UpdateZoom aggiunta**
Con il rilascio di v8.6.0, Aspose.Cells for Java API ha esposto la proprietà OoxmlSaveOptions.UpdateZoom che può essere utilizzata per aggiornare PageSetup.Zoom se le proprietà PageSetup.FitToPagesWide e/o PageSetup.FitToPagesTall sono state utilizzate per controllare il ridimensionamento del foglio di lavoro.
