---
title: Public API Changements dans Aspose.Cells 8.6.0
type: docs
weight: 200
url: /fr/java/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.5.2 à 8.6.0 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour,[classes ajoutées, etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-6-0/), mais aussi une description de tout changement de comportement dans les coulisses du Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Prise en charge de la manipulation des métadonnées sans créer d'objet de classeur**
Cette version de Aspose.Cells for Java API a exposé deux nouvelles classes, à savoir WorkbookMetadata & MetadataOptions, ainsi qu'une nouvelle énumération MetadataType qui permet désormais de manipuler les propriétés du document (métadonnées) sans créer d'instance de Workbook. La classe WorkbookMetadata est légère et fournit un mécanisme très facile à utiliser et efficace pour[lire, écrire et mettre à jour les propriétés du document sans affecter les performances globales](/cells/fr/java/using-workbookmetadata/). 

Voici le scénario d'utilisation simple.

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
### **Propriété HtmlSaveOptions.ExportFrameScriptsAndProperties ajoutée**
Aspose.Cells for Java 8.6.0 a exposé la propriété HtmlSaveOptions.ExportFrameScriptsAndProperties qui peut être utilisée pour influencer la création de scripts supplémentaires lors de la conversion des feuilles de calcul au format HTML. Avec les paramètres par défaut, les API Aspose.Cells exportent la feuille de calcul au format HTML lorsque l'application Excel effectue l'exportation, c'est-à-dire ; le HTML résultant contient les cadres et les commentaires conditionnels, qui détectent le type de navigateur et ajustent la mise en page en conséquence. La valeur par défaut de la propriété HtmlSaveOptions.ExportFrameScriptsAndProperties est true, c'est-à-dire ; l'exportation se fait selon les normes Excel. Si la propriété est définie sur false, le API ne sera pas[générer les scripts liés aux cadres et aux commentaires conditionnels](/cells/fr/java/disable-exporting-frame-scripts-and-document-properties/). Dans ce cas, le HTML résultant peut être visualisé correctement dans n'importe quel navigateur, cependant, il ne peut pas être réimporté à l'aide des API Aspose.Cells.

Voici le scénario d'utilisation simple.

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
### **Propriété Shape.MarcoName ajoutée**
Aspose.Cells for Java 8.6.0 a exposé la propriété Shape.MarcoName qui peut être utilisée pour[affecter un module VBA à un contrôle de formulaire](/cells/fr/java/assign-macro-code-to-form-control/) un tel bouton afin de fournir l'interaction. La propriété est de type chaîne, elle peut donc accepter le nom du module et l'attribuer au contrôle.

Voici le scénario d'utilisation simple.

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
### **Propriété OoxmlSaveOptions.UpdateZoom ajoutée**
Avec la version v8.6.0, le Aspose.Cells for Java API a exposé la propriété OoxmlSaveOptions.UpdateZoom qui peut être utilisée pour mettre à jour PageSetup.Zoom si les propriétés PageSetup.FitToPagesWide et/ou PageSetup.FitToPagesTall ont été utilisées pour contrôler la mise à l'échelle de la feuille de calcul.
