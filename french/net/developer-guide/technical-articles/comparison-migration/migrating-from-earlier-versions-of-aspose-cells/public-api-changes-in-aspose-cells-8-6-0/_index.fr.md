---
title: Changements de l API publique dans Aspose.Cells 8.6.0
type: docs
weight: 190
url: /fr/net/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.5.2 à la 8.6.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, [classes ajoutées, etc.](/cells/fr/net/public-api-changes-in-aspose-cells-8-6-0/), mais aussi une description de tout changement dans le comportement en arrière-plan d'Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Prise en charge de la manipulation de métadonnées sans créer un objet de Workbook**
Cette version de l'API Aspose.Cells for .NET a exposé deux nouvelles classes, à savoir WorkbookMetadata & MetadataOptions ainsi qu'une nouvelle énumération MetadataType qui permet désormais de manipuler les propriétés du document (métadonnées) sans créer d'instance de Workbook. La classe WorkbookMetadata est légère et fournit un mécanisme très facile à utiliser, efficace pour [lire, écrire et mettre à jour les propriétés du document sans impacter les performances globales](/cells/fr/net/using-workbookmetadata/).

Voici le scénario d'utilisation simple.

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


### **Propriété HtmlSaveOptions.ExportFrameScriptsAndProperties ajoutée**
Aspose.Cells for .NET 8.6.0 a exposé la propriété HtmlSaveOptions.ExportFrameScriptsAndProperties qui peut être utilisée pour influencer la création de scripts supplémentaires lors de la conversion des feuilles de calcul au format HTML. Avec les paramètres par défaut, les APIs Aspose.Cells exportent la feuille de calcul au format HTML comme le fait l'application Excel, c'est-à-dire; le HTML résultant contient les cadres et les commentaires conditionnels, qui détectent le type de navigateur et ajustent la mise en page en conséquence. La valeur par défaut de la propriété HtmlSaveOptions.ExportFrameScriptsAndProperties est true, ce qui signifie que l'exportation est effectuée selon les normes Excel. Cependant, si la propriété est définie sur false, l'API ne [générera pas les scripts liés aux cadres et aux commentaires conditionnels](/cells/fr/net/disable-exporting-frame-scripts-and-document-properties/). Dans ce cas, le HTML résultant peut être visualisé correctement dans n'importe quel navigateur, mais il ne peut pas être réimporté à l'aide des APIs Aspose.Cells.

Voici le scénario d'utilisation simple.

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


### **Propriété Shape.MarcoName ajoutée**
Aspose.Cells for .NET 8.6.0 a exposé la propriété Shape.MarcoName qui peut être utilisée pour [attribuer n'importe quel module VBA à un contrôle de formulaire](/cells/fr/net/assign-macro-to-form-control/) tel qu'un Bouton afin de fournir l'interaction. La propriété est de type chaîne de caractères et peut donc accepter le nom du module et l'assigner au contrôle.

Voici le scénario d'utilisation simple.

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


### **Propriété OoxmlSaveOptions.UpdateZoom ajoutée**
Avec la version 8.6.0, l'API Aspose.Cells for .NET a exposé la propriété OoxmlSaveOptions.UpdateZoom qui peut être utilisée pour mettre à jour la propriété PageSetup.Zoom si les propriétés PageSetup.FitToPagesWide et/ou PageSetup.FitToPagesTall ont été utilisées pour contrôler la mise à l'échelle de la feuille de calcul.
{{< app/cells/assistant language="csharp" >}}
