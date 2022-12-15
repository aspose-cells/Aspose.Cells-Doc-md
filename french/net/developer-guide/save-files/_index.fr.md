---
title: Différentes façons d'enregistrer des fichiers
linktitle: Enregistrer les fichiers
type: docs
weight: 40
url: /fr/net/different-ways-to-save-files/
---
{{% alert color="primary" %}}

Aspose.Cells permet de créer et de sauvegarder des fichiers. Cet article explique les différentes façons dont les fichiers peuvent être enregistrés.

{{% /alert %}}

## **Différentes façons d'enregistrer des fichiers**

 Aspose.Cells fournit le**[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook)** qui représente un fichier Excel Microsoft et fournit les propriétés et les méthodes nécessaires pour travailler avec des fichiers Excel. La**[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook)** la classe fournit la**[Enregistrer] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** méthode utilisée pour enregistrer les fichiers Excel. La**[Enregistrer] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**La méthode a de nombreuses surcharges qui sont utilisées pour enregistrer des fichiers de différentes manières.

 Le format de fichier dans lequel le fichier est enregistré est déterminé par le**[Enregistrer le format] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)**énumération

|**Types de formats de fichiers**|**La description**|
|:- |:- |
|CSV|Représente un fichier CSV|
|Excel97To2003|Représente un fichier Excel 97 - 2003|
|Xlsx|Représente un fichier Excel 2007 XLSX|
|Xlsm|Représente un fichier Excel 2007 XLSM|
|XLTX|Représente un fichier XLTX de modèle Excel 2007|
|Xltm|Représente un fichier Excel 2007 prenant en charge les macros XLTM|
|Xlsb|Représente un fichier XLSB binaire Excel 2007|
|TableurML|Représente un fichier XML de feuille de calcul|
|VST|Représente un fichier de valeurs séparées par des tabulations|
|Onglet délimité|Représente un fichier texte délimité par des tabulations|
|SAO|Représente un fichier ODS|
|HTML|Représente le(s) fichier(s) HTML|
|MHtml|Représente un ou plusieurs fichiers MHTML|
|PDF|Représente un fichier PDF|
|XPS|Représente un document XPS|
|TIFF|Représente le format de fichier d'image balisé (TIFF)|

## **Enregistrement du fichier sous différents formats**

 Pour enregistrer des fichiers dans un emplacement de stockage, spécifiez le nom du fichier (complet avec le chemin de stockage) et le format de fichier souhaité (à partir du**[Enregistrer le format] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)**énumération) lors de l'appel du**[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook)** objets**[Enregistrer] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**méthode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **Enregistrer le classeur au format PDF**
Portable Document Format (PDF) est un type de document créé par Adobe dans les années 1990. Le but de ce format de fichier était d'introduire une norme pour la représentation des documents et autres documents de référence dans un format indépendant du logiciel d'application, du matériel ainsi que du système d'exploitation. Le format de fichier PDF a la pleine capacité de contenir des informations telles que du texte, des images, des hyperliens, des champs de formulaire, des médias enrichis, des signatures numériques, des pièces jointes, des métadonnées, des fonctionnalités géospatiales et des objets 3D qui peuvent faire partie du document source.

Les codes suivants montrent comment enregistrer le classeur en tant que fichier pdf avec Aspose.Cells :
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **Enregistrement du classeur au format texte ou CSV**

Parfois, vous souhaitez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats de texte (par exemple TXT, TabDelim, CSV, etc.), par défaut, Microsoft Excel et Aspose.Cells enregistrent uniquement le contenu de la feuille de calcul active.

L'exemple de code suivant explique comment enregistrer un classeur entier au format texte. Chargez le classeur source qui peut être n'importe quel fichier de feuille de calcul Excel ou OpenOffice Microsoft (c'est-à-dire XLS, XLSX, XLSM, XLSB, ODS, etc.) avec n'importe quel nombre de feuilles de calcul.

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT.

 Vous pouvez modifier le même exemple pour enregistrer votre fichier au format CSV. Par défaut,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**est une virgule, donc ne spécifiez pas de séparateur si vous enregistrez au format CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Enregistrement de fichiers texte avec un séparateur personnalisé**

Les fichiers texte contiennent des données de feuille de calcul sans formatage. Le fichier est une sorte de fichier texte brut qui peut avoir des délimiteurs personnalisés entre ses données.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **Enregistrement d'un fichier dans un flux**

 Pour enregistrer des fichiers dans un flux, créez un*MemoryStream* ou*FileStream* objet et enregistrez le fichier dans cet objet de flux en appelant le**[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook)** objets**[Enregistrer] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** méthode. Spécifiez le format de fichier souhaité à l'aide de la**[Enregistrer le format] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)** énumération lors de l'appel du**[Enregistrer] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**méthode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **Enregistrement de fichiers en tant que fichiers Html et Mht**
Aspose.Cells peut simplement enregistrer un fichier Excel, JSON, CSV ou d'autres fichiers qui pourraient être chargés par Aspose.Cells en tant que fichiers .html et .mht.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

## **Enregistrement sous OpenOffice (ODS, SXC, FODS, OTS)**
Nous pouvons enregistrer les fichiers au format open office : ODS, SXC, FODS, OTS etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **Enregistrement du fichier Excel au format JSON ou XML**

JSON (JavaScript Object Notation) est un format de fichier standard ouvert pour le partage de données qui utilise du texte lisible par l'homme pour stocker et transmettre des données. Les fichiers JSON sont stockés avec l'extension .json. JSON nécessite moins de formatage et constitue une bonne alternative au XML. JSON est dérivé de JavaScript mais est un format de données indépendant du langage. La génération et l'analyse de JSON sont prises en charge par de nombreux langages de programmation modernes. application/json est le type de média utilisé pour JSON.

Aspose.Cells prend en charge l'enregistrement de fichiers au format JSON ou XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **Sujets avancés**
- [Ajuster le niveau de compression du classeur](/cells/fr/net/adjust-workbook-compression-level/)
- [Enregistrer le classeur au format de feuille de calcul Open XML strict](/cells/fr/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Enregistrement du fichier dans l'objet de réponse](/cells/fr/net/saving-file-to-response-object/)
