---
title: Modifications de l API publique dans Aspose.Cells 8.8.3
type: docs
weight: 290
url: /fr/net/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.8.2 à la version 8.8.3 qui pourraient intéresser les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes publiques mises à jour, les classes ajoutées et supprimées, etc., mais aussi une description des changements de comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Prise en charge des contrôles ActiveX**
Aspose.Cells for .NET 8.8.3 a exposé la méthode AddActiveXControl qui permet d'ajouter un contrôle ActiveX à la ShapeCollection. La méthode mentionnée ci-dessus nécessite 7 paramètres pour spécifier le type de contrôle, l'emplacement pour placer le contrôle et la taille du contrôle. Le type peut être spécifié en utilisant l'énumération ControlType avec les valeurs possibles suivantes.

1. ControlType.CheckBox
1. ControlType.ComboBox
1. ControlType.CommandButton
1. ControlType.Image
1. ControlType.Label
1. ControlType.ListBox
1. ControlType.RadioButton
1. ControlType.ScrollBar
1. ControlType.SpinButton
1. ControlType.TextBox
1. ControlType.ToggleButton
1. ControlType.Unknown

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Ajout de contrôles ActiveX à la feuille de calcul](/cells/fr/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

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


### **Méthode LoadOptions.SetPaperSize ajoutée**
Aspose.Cells for .NET 8.8.3 permet de définir la taille de papier d'impression par défaut à partir des paramètres de l'imprimante par défaut tout en utilisant la méthode LoadOptions.SetPaperSize nouvellement exposée comme démontré ci-dessous. Veuillez noter que le paramètre d'entrée de la méthode mentionnée ci-dessus est la valeur de l'énumération PaperSizeType contenant les tailles de papier prédéfinies.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Chargement de feuilles de calcul avec une taille de papier spécifiée](/cells/fr/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Méthode ajoutée Cell.GetCharacters(flag)**
Les API Aspose.Cells permettent d'obtenir les objets de caractères sous forme de tableau FontSetting en utilisant la méthode Cell.GetCharacters. Avec cette version, l'API Aspose.Cells for .NET a exposé une version surchargée de la méthode Cell.GetCharacters qui pourrait accepter un booléen en tant que paramètre, indiquant si le style de tableau doit être appliqué sur la cellule si la cellule fait partie d'un ListObject.

**C#**

{{< highlight csharp >}}

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


### **Propriété ajoutée OleObject.AutoLoad**
Aspose.Cells for .NET 8.8.3 a exposé la propriété OleObject.AutoLoad qui permet de rafraîchir l'image OleObject si le contenu/données de l'objet sous-jacent a été modifié. Lorsque ladite propriété est définie sur true, elle force l'application Excel à rafraîchir l'image OleObject lorsque la feuille de calcul résultante est chargée.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Actualiser automatiquement les OleObjects](/cells/fr/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

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


### **Propriété ajoutée HTMLLoadOptions.SupportDivTag**
Aspose.Cells for .NET 8.8.3 a exposé la propriété HTMLLoadOptions.SupportDivTag qui permet de parser les balises DIV intégrées dans les balises TD lors du chargement de fichiers/snippets HTML dans le modèle d'objet Aspose.Cells. La propriété de type booléen a la valeur par défaut false.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Prise en charge des balises DIV internes lors du chargement HTML](/cells/fr/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

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


### **Propriété ajoutée HtmlSaveOptions.ExportGridLines**
Aspose.Cells for .NET 8.8.3 a exposé la propriété HtmlSaveOptions.ExportGridLines qui permet de rendre les lignes de grille lors de l'exportation de feuilles de calcul au format HTML. La propriété de type booléen a la valeur par défaut false, cependant, lorsqu'elle est définie sur true, l'API rend les lignes de grille pour la plage de données disponible au format HTML.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Afficher les lignes de grille en HTML](/cells/fr/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Propriété ajoutée ListObject.Comment**
Les API Aspose.Cells permettent maintenant d'obtenir et de définir les commentaires pour une instance de ListObject. Afin de fournir ladite fonctionnalité, les API Aspose.Cells ont exposé la propriété ListObject.Comment.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Ajouter des commentaires pour les ListObjects](/cells/fr/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

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


### **Propriété ajoutée GridWeb.SessionStorePath**
Aspose.Cells.GridWeb pour .NET 8.8.3 a exposé la propriété SessionStorePath qui permet de récupérer ou définir le chemin de stockage de session lorsque le mode de session est ViewState. La propriété susmentionnée récupère ou définit le chemin relatif vers le répertoire de base de l'application Web actuelle.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Spécifier le chemin pour les fichiers de session temporaires](/cells/fr/net/specificer-le-chemin-où-gridweb-stocke-les-fichiers-de-session-temporaires/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.
## **APIs supprimées**
### **Méthode Workbook.Decrypt supprimée**
La propriété en question a été marquée comme obsolète il y a quelque temps. Cette version l'a complètement supprimée de l'API publique. Il est conseillé de définir la propriété WorkbookSettings.Password à null afin d'atteindre le même objectif.
