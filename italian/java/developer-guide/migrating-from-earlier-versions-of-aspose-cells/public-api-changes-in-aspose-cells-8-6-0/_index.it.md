---
title: Cambiamenti nell API Pubblica in Aspose.Cells 8.6.0
type: docs
weight: 200
url: /it/java/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.5.2 a 8.6.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, [classi aggiunte ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-6-0/), ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per la manipolazione dei metadati senza creare un oggetto di Workbook**
Questa release dell'API Aspose.Cells for Java ha esposto due nuove classi, ovvero WorkbookMetadata e MetadataOptions insieme a una nuova enumerazione MetadataType che ora consente di manipolare le proprietà del documento (metadati) senza creare un'istanza del Workbook. La classe WorkbookMetadata è leggera e fornisce un meccanismo molto facile da usare ed efficiente per [leggere, scrivere e aggiornare le proprietà del documento senza influire sulle prestazioni complessive](/cells/it/java/using-workbookmetadata/). 

Di seguito è riportato il semplice scenario d'uso.

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
### **Aggiunta la proprietà HtmlSaveOptions.ExportFrameScriptsAndProperties**
Aspose.Cells for Java 8.6.0 ha esposto la proprietà HtmlSaveOptions.ExportFrameScriptsAndProperties che può essere utilizzata per influenzare la creazione di script aggiuntivi durante la conversione dei fogli elettronici in formato HTML. Con le impostazioni predefinite, le API Aspose.Cells esportano il foglio elettronico in formato HTML come fa l'applicazione Excel, cioè il file HTML risultante contiene i frame e i commenti condizionali, che rilevano il tipo di browser e regolano il layout di conseguenza. Il valore predefinito della proprietà HtmlSaveOptions.ExportFrameScriptsAndProperties è true, il che significa che l'esportazione viene effettuata secondo gli standard di Excel. Se la proprietà è impostata su false, l'API non [genererà gli script relativi ai frame e ai commenti condizionali](/cells/it/java/disable-exporting-frame-scripts-and-document-properties/). In questo caso, l'HTML risultante può essere visualizzato correttamente in qualsiasi browser, tuttavia non può essere importato di nuovo utilizzando le API Aspose.Cells.

Di seguito è riportato il semplice scenario d'uso.

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
### **Aggiunta la proprietà Shape.MarcoName**
Aspose.Cells for Java 8.6.0 ha esposto la proprietà Shape.MarcoName che può essere utilizzata per [assegnare un modulo VBA a un controllo di modulo](/cells/it/java/assign-macro-code-to-form-control/) come un pulsante al fine di fornire l'interazione. La proprietà è di tipo stringa quindi può accettare il nome del modulo e lo assegna al controllo.

Di seguito è riportato il semplice scenario d'uso.

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
### **Aggiunta la proprietà OoxmlSaveOptions.UpdateZoom**
Con il rilascio di v8.6.0, l'API Aspose.Cells for Java ha esposto la proprietà OoxmlSaveOptions.UpdateZoom che può essere utilizzata per aggiornare la proprietà PageSetup.Zoom se sono state utilizzate le proprietà PageSetup.FitToPagesWide e/o PageSetup.FitToPagesTall per controllare il ridimensionamento del foglio elettronico.
