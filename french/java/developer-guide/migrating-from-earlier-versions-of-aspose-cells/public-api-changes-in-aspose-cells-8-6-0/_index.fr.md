---
title: Changements de l API publique dans Aspose.Cells 8.6.0
type: docs
weight: 200
url: /fr/java/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.5.2 à 8.6.0 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes publiques et mises à jour, [classes ajoutées, etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-6-0/), mais aussi une description de tout changement de comportement en coulisse dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Prise en charge de la manipulation de métadonnées sans créer un objet de Workbook**
Cette version de l'API Aspose.Cells for Java a exposé deux nouvelles classes, à savoir WorkbookMetadata et MetadataOptions, ainsi qu'une nouvelle énumération MetadataType qui permet désormais de manipuler les propriétés du document (métadonnées) sans créer d'instance de Workbook. La classe WorkbookMetadata est légère et fournit un mécanisme très facile à utiliser et efficace pour [lire, écrire et mettre à jour les propriétés du document sans affecter les performances globales](/cells/fr/java/using-workbookmetadata/). 

Voici le scénario d'utilisation simple.

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
### **Propriété HtmlSaveOptions.ExportFrameScriptsAndProperties ajoutée**
Aspose.Cells for Java 8.6.0 a exposé la propriété HtmlSaveOptions.ExportFrameScriptsAndProperties qui peut être utilisée pour influencer la création de scripts supplémentaires lors de la conversion des feuilles de calcul au format HTML. Avec les paramètres par défaut, les API Aspose.Cells exportent la feuille de calcul au format HTML comme le fait l'application Excel, c'est-à-dire que le HTML résultant contient les trames et les commentaires conditionnels, qui détectent le type de navigateur et ajustent la mise en page en conséquence. La valeur par défaut de la propriété HtmlSaveOptions.ExportFrameScriptsAndProperties est true, ce qui signifie que l'exportation est effectuée selon les normes d'Excel. Si la propriété est définie sur false, l'API ne [générera pas les scripts liés aux trames et aux commentaires conditionnels](/cells/fr/java/disable-exporting-frame-scripts-and-document-properties/). Dans ce cas, le HTML résultant peut être correctement visualisé dans n'importe quel navigateur, mais il ne peut pas être réimporté à l'aide des API Aspose.Cells.

Voici le scénario d'utilisation simple.

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
### **Propriété Shape.MarcoName ajoutée**
Aspose.Cells for Java 8.6.0 a exposé la propriété Shape.MarcoName qui peut être utilisée pour [attribuer un module VBA à un contrôle de formulaire](/cells/fr/java/assign-macro-code-to-form-control/) tel qu'un bouton afin de fournir l'interaction. La propriété est de type chaîne et peut donc accepter le nom du module et l'attribuer au contrôle.

Voici le scénario d'utilisation simple.

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
### **Propriété OoxmlSaveOptions.UpdateZoom ajoutée**
Avec la publication de la v8.6.0, l'API Aspose.Cells for Java a exposé la propriété OoxmlSaveOptions.UpdateZoom qui peut être utilisée pour mettre à jour le zoom PageSetup si les propriétés PageSetup.FitToPagesWide et/ou PageSetup.FitToPagesTall ont été utilisées pour contrôler la mise à l'échelle de la feuille de calcul.
{{< app/cells/assistant language="java" >}}
