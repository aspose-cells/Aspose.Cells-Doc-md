---
title: Public API Changements dans Aspose.Cells 8.8.3
type: docs
weight: 300
url: /fr/java/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.8.2 à 8.8.3 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Prise en charge des contrôles ActiveX**
Aspose.Cells for Java 8.8.3 a exposé la méthode addActiveXControl qui permet d'ajouter un contrôle ActiveX à la ShapeCollection. La méthode susmentionnée nécessite 7 paramètres pour spécifier le type de contrôle, l'emplacement pour placer le contrôle et la taille du contrôle. Le type peut être spécifié à l'aide de l'énumération ControlType avec les valeurs possibles suivantes.

1. Type de contrôle.CHECK_BOX
1. ControlType.COMBO_BOX
1. Type de contrôle.COMMAND_BUTTON
1. ControlType.IMAGE
1. ControlType.LABEL
1. Type de contrôle.LIST_BOX
1. Type de contrôle.RADIO_BUTTON
1. ControlType.SCROLL_BAR
1. Type de contrôle.SPIN_BUTTON
1. ControlType.TEXT_BOX
1. Type de contrôle.TOGGLE_BUTTON
1. ControlType.UNKNOWN

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Ajout de contrôles ActiveX à la feuille de calcul](/cells/fr/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

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
### **Ajout de la méthode LoadOptions.setPaperSize**
Aspose.Cells for Java 8.8.3 permet de définir la taille du papier d'impression par défaut à partir du paramètre par défaut de l'imprimante tout en utilisant la méthode LoadOptions.setPaperSize nouvellement exposée, comme illustré ci-dessous. Veuillez noter que le paramètre d'entrée de la méthode susmentionnée est la valeur de l'énumération PaperSizeType contenant les formats de papier prédéfinis.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Charger des feuilles de calcul avec le format de papier spécifié](/cells/fr/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Ajout de la méthode Cell.getCharacters(flag)**
Les API Aspose.Cells permettent d'obtenir les objets caractères sous forme de tableau FontSetting en utilisant la méthode Cell.getCharacters. Avec cette version, le Aspose.Cells for Java API a exposé une version surchargée du Cell.getCharacters qui pourrait accepter Boolean comme paramètre, indiquant si le style de tableau doit être appliqué sur la cellule si la cellule fait partie d'un ListObject.

**Java**

{{< highlight "csharp" >}}

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

FontSetting[]characters = cell.getCharacters(true);

{{< /highlight >}}
### **Ajout de la propriété OleObject.AutoLoad**
Aspose.Cells for Java 8.8.3 a exposé la propriété OleObject.AutoLoad qui permet de rafraîchir l'image de l'OleObject si le contenu/les données de l'objet sous-jacent ont été modifiés. La propriété susmentionnée, lorsqu'elle est définie sur true, force l'application Excel à actualiser l'image de l'OleObject lorsque la feuille de calcul résultante est chargée.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Actualiser automatiquement les OleObjects](/cells/fr/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

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
### **Ajout de la propriété HTMLLoadOptions.SupportDivTag**
Aspose.Cells for Java 8.8.3 a exposé la propriété HTMLLoadOptions.SupportDivTag qui permet d'analyser les balises DIV intégrées dans les balises TD lors du chargement de fichiers/extraits HTML dans le modèle d'objet Aspose.Cells. La propriété de type booléen a la valeur par défaut de false.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Prise en charge des balises DIV internes lors du chargement du code HTML](/cells/fr/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

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
### **Ajout de la propriété HtmlSaveOptions.ExportGridLines**
Aspose.Cells for Java 8.8.3 a exposé la propriété HtmlSaveOptions.ExportGridLines qui permet de restituer les lignes de la grille lors de l'exportation de la feuille de calcul au format HTML. La propriété de type booléen a la valeur par défaut de false, cependant, lorsqu'elle est définie sur true, le API restitue les lignes de grille pour la plage de données disponible au format HTML.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Rendre les lignes de la grille en HTML](/cells/fr/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Ajout de la propriété ListObject.Comment**
Aspose.Cells Les API permettent désormais d'obtenir et de définir les commentaires d'une instance de ListObject. Afin de fournir la fonctionnalité susmentionnée, les API Aspose.Cells ont exposé la propriété ListObject.Comment.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Ajout de commentaires pour ListObjects](/cells/fr/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

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
## **API supprimées**
### **Suppression de la méthode Workbook.decrypt**
Ladite propriété a été marquée obsolète il y a quelque temps. Cette version l'a complètement supprimé du public API. Il est conseillé de définir la propriété WorkbookSettings.Password sur null afin d'atteindre le même objectif.
