---
title: Modifications de l API publique dans Aspose.Cells 8.8.3
type: docs
weight: 300
url: /fr/java/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.8.2 à la version 8.8.3 qui pourraient intéresser les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes publiques mises à jour, les classes ajoutées et supprimées, etc., mais aussi une description des changements de comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Prise en charge des contrôles ActiveX**
Aspose.Cells for Java 8.8.3 a exposé la méthode addActiveXControl qui permet d'ajouter un contrôle ActiveX à la ShapeCollection. La méthode susmentionnée nécessite 7 paramètres pour spécifier le type de contrôle, l'emplacement pour placer le contrôle et la taille du contrôle. Le type peut être spécifié à l'aide de l'énumération ControlType avec les valeurs possibles suivantes.

1. ControlType.CHECK_BOX
1. ControlType.COMBO_BOX
1. ControlType.COMMAND_BUTTON
1. ControlType.IMAGE
1. ControlType.LABEL
1. ControlType.LIST_BOX
1. ControlType.RADIO_BUTTON
1. ControlType.SCROLL_BAR
1. ControlType.SPIN_BUTTON
1. ControlType.TEXT_BOX
1. ControlType.TOGGLE_BUTTON
1. ControlType.UNKNOWN

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Ajout de contrôles ActiveX à la feuille de calcul](/cells/fr/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Add Toggle Button ActiveX Control to the ShapeCollection at specified location

Shape shape = sheet.getShapes().addActiveXControl(ControlType.TOGGLE_BUTTON, 4, 0, 4, 0, 100, 30);

//Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.getActiveXControl();

control.setLinkedCell("A1");

//Save the result on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Méthode LoadOptions.setPaperSize ajoutée**
Aspose.Cells for Java 8.8.3 permet de définir la taille de papier d'impression par défaut à partir des paramètres de l'imprimante par défaut tout en utilisant la méthode LoadOptions.setPaperSize récemment exposée comme démontré ci-dessous. Veuillez noter que le paramètre d'entrée de la méthode susmentionnée est la valeur de l'énumération PaperSizeType contenant les tailles de papier prédéfinies.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Charger des feuilles de calcul avec une taille de papier spécifiée](/cells/fr/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Méthode Cell.getCharacters(flag) ajoutée**
Les API Aspose.Cells permettent d'obtenir les objets caractères sous forme de tableau FontSetting en utilisant la méthode Cell.getCharacters. Avec cette version, l'API Aspose.Cells for Java a exposé une version surchargée de la méthode Cell.getCharacters qui pourrait accepter un booléen en paramètre, indiquant si le style de tableau doit être appliqué sur la cellule si la cellule fait partie d'un ListObject.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access cells collection of the first worksheet

Cells cells = sheet.getCells();

//Access particular cell from a ListObject

//Assuming A1 resides in a ListObject

Cell cell = cells.get("A1");

//Get all Characters objects from the cell

FontSetting[] characters = cell.getCharacters(true);

{{< /highlight >}}
### **Propriété ajoutée OleObject.AutoLoad**
Aspose.Cells for Java 8.8.3 a exposé la propriété OleObject.AutoLoad qui permet de rafraîchir l'image de l'objet OleObject si le contenu / les données de l'objet sous-jacent ont été modifiés. Lorsque ladite propriété est définie sur true, elle force l'application Excel à rafraîchir l'image de l'objet OleObject lorsque la feuille de calcul résultante est chargée.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Rafraîchir automatiquement les objets OleObjects](/cells/fr/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access OleObjectCollection from first worksheet

OleObjectCollection oleObjects = sheet.getOleObjects();

//Access a OleObject from the collection

OleObject oleObject = oleObjects.get(0);

//Set AutoLoad to true

oleObject.setAutoLoad(true);

{{< /highlight >}}
### **Propriété ajoutée HTMLLoadOptions.SupportDivTag**
Aspose.Cells for Java 8.8.3 a exposé la propriété HTMLLoadOptions.SupportDivTag qui permet d'analyser les balises DIV incorporées dans les balises TD lors du chargement de fichiers / extraits HTML dans le modèle d'objet Aspose.Cells. La propriété de type booléen a la valeur par défaut false.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Prendre en charge les balises DIV internes lors du chargement d'HTML](/cells/fr/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Store the HTML snippet in a variable

String export_html = "<html>"

\+ "<body>"

\+ " <table>"

\+ "     <tr>"

\+ "         <td>"

\+ "             <div>This is some Text.</div>"

\+ "             <div>"

\+ "                 <div>"

\+ "                     <span>This is some more Text</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>abc@abc.com</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>1234567890</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>ABC DEF</span>"

\+ "                 </div>"

\+ "             </div>"

\+ "             <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>"

\+ "         </td>"

\+ "         <td>"

\+ "             <img src='ASpose_logo_100x100.png' />"

\+ "         </td>"

\+ "     </tr>"

\+ " </table>"

\+ "</body>"

\+ "</html>";

//Convert HTML string to InputStream

InputStream stream = new ByteArrayInputStream(export_html.getBytes(StandardCharsets.UTF_8));

//Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

// Set SupportDivTag property to true

loadOptions.setSupportDivTag(true);

//Create workbook object from the HTML using load options

Workbook book = new Workbook(stream, loadOptions);

//Save the spreadsheet on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Propriété ajoutée HtmlSaveOptions.ExportGridLines**
Aspose.Cells for Java 8.8.3 a exposé la propriété HtmlSaveOptions.ExportGridLines qui permet de rendre les lignes de grille lors de l'exportation de feuilles de calcul au format HTML. La propriété de type booléen a la valeur par défaut false, cependant, lorsqu'elle est définie sur true, l'API rend les lignes de grille pour la plage de données disponible au format HTML.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Rendre les lignes de grille au format HTML](/cells/fr/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Propriété ajoutée ListObject.Comment**
Les API Aspose.Cells permettent maintenant d'obtenir et de définir les commentaires pour une instance de ListObject. Afin de fournir ladite fonctionnalité, les API Aspose.Cells ont exposé la propriété ListObject.Comment.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Ajouter des commentaires pour ListObjects](/cells/fr/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first ListObject from the collection of ListObjects

ListObject listObject = sheet.getListObjects().get(0);

//Set comments for the ListObject

listObject.setComment("Comments");

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}
## **APIs supprimées**
### **Méthode Workbook.decrypt supprimée**
La propriété en question a été marquée comme obsolète il y a quelque temps. Cette version l'a complètement supprimée de l'API publique. Il est conseillé de définir la propriété WorkbookSettings.Password à null afin d'atteindre le même objectif.
{{< app/cells/assistant language="java" >}}
