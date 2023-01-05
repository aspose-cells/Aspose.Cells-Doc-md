---
title: Public API Changements dans Aspose.Cells 8.8.3
type: docs
weight: 290
url: /fr/net/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.8.2 à 8.8.3 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Prise en charge des contrôles ActiveX**
Aspose.Cells for .NET 8.8.3 a exposé la méthode AddActiveXControl qui permet d'ajouter un contrôle ActiveX à la ShapeCollection. La méthode susmentionnée nécessite 7 paramètres pour spécifier le type de contrôle, l'emplacement pour placer le contrôle et la taille du contrôle. Le type peut être spécifié à l'aide de l'énumération ControlType avec les valeurs possibles suivantes.

1. ControlType.CheckBoxControlType.CheckBox
1. ControlType.ComboBoxControlType.ComboBox
1. ControlType.CommandButtonControlType.CommandButtonControlType.CommandButtonControlType.CommandButton
1. ControlType.Image
1. ControlType.LabelControlType.Label
1. ControlType.ListBoxControlType.ListBox
1. ControlType.RadioButtonControlType.RadioButtonControlType.RadioButtonControlType.RadioButton
1. ControlType.ScrollBarControlType.ScrollBar
1. ControlType.SpinButtonControlType.SpinButtonControlType.SpinButtonControlType.SpinButtonControlType.SpinButtonControlType.SpinButtonControlType.SpinButton
1. ControlType.TextBox
1. ControlType.ToggleButtonControlType.ToggleButtonControlType.ToggleButton
1. ControlType.UnknownControlType.Unknown

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Ajout de contrôles ActiveX à la feuille de calcul](/cells/fr/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Add Toggle Button ActiveX Control to the ShapeCollection at specified location

var shape = sheet.Shapes.AddActiveXControl(ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

// Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.ActiveXControl;

control.LinkedCell = "A1";

// Save the result on disc

book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **Ajout de la méthode LoadOptions.SetPaperSize**
Aspose.Cells for .NET 8.8.3 permet de définir le format de papier d'impression par défaut à partir du paramètre par défaut de l'imprimante tout en utilisant la méthode LoadOptions.SetPaperSize nouvellement exposée, comme illustré ci-dessous. Veuillez noter que le paramètre d'entrée de la méthode susmentionnée est la valeur de l'énumération PaperSizeType contenant les formats de papier prédéfinis.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Charger des feuilles de calcul avec le format de papier spécifié](/cells/fr/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Ajout de la méthode Cell.GetCharacters(flag)**
Les API Aspose.Cells permettent d'obtenir les objets caractères sous forme de tableau FontSetting en utilisant la méthode Cell.GetCharacters. Avec cette version, le Aspose.Cells for .NET API a exposé une version surchargée du Cell.GetCharacters qui pourrait accepter Boolean comme paramètre, indiquant si le style de tableau doit être appliqué sur la cellule si la cellule fait partie d'un ListObject.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access cells collection of the first worksheet

var cells = sheet.Cells;

// Access particular cell from a ListObject

// Assuming A1 resides in a ListObject

var cell = cells["A1"];

// Get all Characters objects from the cell

var characters = cell.GetCharacters(true);

{{< /highlight >}}


### **Ajout de la propriété OleObject.AutoLoad**
Aspose.Cells for .NET 8.8.3 a exposé la propriété OleObject.AutoLoad qui permet de rafraîchir l'image de l'OleObject si le contenu/les données de l'objet sous-jacent ont été modifiés. La propriété susmentionnée, lorsqu'elle est définie sur true, force l'application Excel à actualiser l'image de l'OleObject lorsque la feuille de calcul résultante est chargée.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Actualiser automatiquement les OleObjects](/cells/fr/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access OleObjectCollection from first worksheet

var oleObjects = sheet.OleObjects;

// Access a OleObject from the collection

var oleObject = oleObjects[0];

// Set AutoLoad to true

oleObject.AutoLoad = true;

{{< /highlight >}}


### **Ajout de la propriété HTMLLoadOptions.SupportDivTag**
Aspose.Cells for .NET 8.8.3 a exposé la propriété HTMLLoadOptions.SupportDivTag qui permet d'analyser les balises DIV intégrées dans les balises TD lors du chargement des fichiers/extraits HTML dans le modèle d'objet Aspose.Cells. La propriété de type booléen a la valeur par défaut de false.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Prise en charge des balises DIV internes lors du chargement HTML](/cells/fr/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 // Store the HTML snippet in a variable

var export_html = @"

<html>

<body>

    <table>

        <tr>

            <td>

                <div>This is some Text.</div>

                <div>

                    <div>

                        <span>This is some more Text</span>

                    </div>

                    <div>

                        <span>abc@abc.com</span>

                    </div>

                    <div>

                        <span>1234567890</span>

                    </div>

                    <div>

                        <span>ABC DEF</span>

                    </div>

                </div>

                <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>

            </td>

            <td>

                <img src='ASpose_logo_100x100.png' />

            </td>

        </tr>

    </table>

</body>

</html>";

// Create an instance of MemoryStream and load the contents of the HTML

using (var stream = new MemoryStream(System.Text.Encoding.UTF8.GetBytes(export_html)))

{

    // Create an instance of HTMLLoadOptions

    var loadOptions = new HTMLLoadOptions(LoadFormat.Html);

    // Set SupportDivTag property to true

    loadOptions.SupportDivTag = true;

    // Create workbook object from the HTML using load options

    var book = new Workbook(stream, loadOptions);

    // Auto fit rows and columns of first worksheet

    var sheet = book.Worksheets[0];

    sheet.AutoFitRows();

    sheet.AutoFitColumns();

    // Save the spreadsheet on disc

    book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}


### **Ajout de la propriété HtmlSaveOptions.ExportGridLines**
Aspose.Cells for .NET 8.8.3 a exposé la propriété HtmlSaveOptions.ExportGridLines qui permet de restituer les lignes de la grille lors de l'exportation de la feuille de calcul au format HTML. La propriété de type booléen a la valeur par défaut de false, cependant, lorsqu'elle est définie sur true, le API restitue les lignes de grille pour la plage de données disponible au format HTML.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Rendu des lignes de grille à HTML](/cells/fr/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Ajout de la propriété ListObject.Comment**
Aspose.Cells Les API permettent désormais d'obtenir et de définir les commentaires d'une instance de ListObject. Afin de fournir la fonctionnalité susmentionnée, les API Aspose.Cells ont exposé la propriété ListObject.Comment.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Ajout de commentaires pour ListObjects](/cells/fr/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first ListObject from the collection of ListObjects

var listObject = sheet.ListObjects[0];

// Set comments for the ListObject

listObject.Comment = "Comments";

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Ajout de la propriété GridWeb.SessionStorePath**
Aspose.Cells.GridWeb for .NET 8.8.3 a exposé la propriété SessionStorePath qui permet d'obtenir ou de définir le chemin du magasin de session lorsque le mode de session est ViewState. La propriété susmentionnée obtient ou définit le chemin relatif vers le répertoire de base de l'application Web actuelle.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Spécifier le chemin des fichiers de session temporaires](/cells/fr/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.
## **API supprimées**
### **Suppression de la méthode Workbook.Decrypt**
Ladite propriété a été marquée obsolète il y a quelque temps. Cette version l'a complètement supprimé du public API. Il est conseillé de définir la propriété WorkbookSettings.Password sur null afin d'atteindre le même objectif.
