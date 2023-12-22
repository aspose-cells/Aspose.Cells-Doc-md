---
title: Différentes façons de sauvegarder des fichiers
linktitle: Enregistrer les fichiers
type: docs
weight: 40
url: /fr/net/different-ways-to-save-files/
description: Aspose.Cells for .NET peut enregistrer des fichiers dans différents formats. Enregistrez les fichiers au PDF. Enregistrez les fichiers au HTML. Enregistrez les fichiers au DOCX. Enregistrez les fichiers au PPTX. Enregistrez les fichiers au JSON. Enregistrez les fichiers au MHTML.
keywords: Aspose.Cells Save Excel to PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML and so on using C#, Save or Convert Workbook to PDF HTML JSON TXT SQL in C#.
---
{{% alert color="primary" %}}

Aspose.Cells permet de créer et de sauvegarder des fichiers. Cet article explique les différentes manières dont les fichiers peuvent être enregistrés.

{{% /alert %}}

##  **Différentes façons de sauvegarder des fichiers**

 Aspose.Cells fournit le**[Cahier d'exercices](https://reference.aspose.com/cells/net/aspose.cells/workbook)** qui représente un fichier Excel Microsoft et fournit les propriétés et méthodes nécessaires pour travailler avec des fichiers Excel. Le**[Cahier d'exercices](https://reference.aspose.com/cells/net/aspose.cells/workbook)** la classe fournit le**[Enregistrer](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** méthode utilisée pour enregistrer les fichiers Excel. Le**[Enregistrer](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**La méthode comporte de nombreuses surcharges qui sont utilisées pour enregistrer des fichiers de différentes manières.

 Le format de fichier dans lequel le fichier est enregistré est déterminé par le**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**énumération

|**Types de formats de fichiers**|**Description**|
| :- | :- |
|CSV|Représente un fichier CSV|
|Excel97À2003|Représente un fichier Excel 97 - 2003|
|XLSX|Représente un fichier Excel 2007 XLSX|
|Xlsm|Représente un fichier Excel 2007 XLSM|
|XLTX|Représente un fichier de modèle Excel 2007 XLTX|
|XLTM|Représente un fichier XLTM prenant en charge les macros Excel 2007.|
|Xlsb|Représente un fichier binaire XLSB Excel 2007|
|SpreadsheetML|Représente un fichier XML de feuille de calcul|
|TSV|Représente un fichier de valeurs séparées par des tabulations|
|TabDelimited|Représente un fichier texte délimité par des tabulations|
|ODS|Représente un fichier ODS|
|HTML|Représente le(s) fichier(s) HTML|
|HTML|Représente un ou plusieurs fichiers MHTML|
|PDF|Représente un fichier PDF|
|XPS|Représente un document XPS|
|TIFF|Représente le format de fichier image balisé (TIFF)|

##  **Comment enregistrer un fichier dans différents formats**

Pour enregistrer des fichiers dans un emplacement de stockage, spécifiez le nom du fichier (avec le chemin de stockage) et le format de fichier souhaité (à partir du**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** énumération) lors de l'appel du**[Cahier d'exercices](https://reference.aspose.com/cells/net/aspose.cells/workbook)** objets**[Enregistrer](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**méthode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

##  **Comment enregistrer un classeur au format PDF**
Portable Document Format (PDF) est un type de document créé par Adobe dans les années 1990. Le but de ce format de fichier était d'introduire une norme pour la représentation des documents et autres documents de référence dans un format indépendant du logiciel d'application, du matériel ainsi que du système d'exploitation. Le format de fichier PDF a toute la capacité de contenir des informations telles que du texte, des images, des hyperliens, des champs de formulaire, des médias riches, des signatures numériques, des pièces jointes, des métadonnées, des caractéristiques géospatiales et des objets 3D qui peuvent faire partie du document source.

Les codes suivants montrent comment enregistrer le classeur sous forme de fichier PDF avec Aspose.Cells :
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

##  **Comment enregistrer un classeur au format texte ou CSV**

Parfois, vous souhaitez convertir ou enregistrer un classeur contenant plusieurs feuilles de calcul au format texte. Pour les formats de texte (par exemple TXT, TabDelim, CSV, etc.), par défaut Microsoft Excel et Aspose.Cells enregistrent uniquement le contenu de la feuille de calcul active.

L'exemple de code suivant explique comment enregistrer un classeur entier au format texte. Chargez le classeur source qui peut être n'importe quel fichier de feuille de calcul Excel ou OpenOffice Microsoft (donc XLS, XLSX, XLSM, XLSB, ODS et ainsi de suite) avec n'importe quel nombre de feuilles de calcul.

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT.

 Vous pouvez modifier le même exemple pour enregistrer votre fichier sous CSV. Par défaut,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**est une virgule, donc ne spécifiez pas de séparateur si vous enregistrez au format CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

##  **Comment enregistrer un fichier dans des fichiers texte avec un séparateur personnalisé**

Les fichiers texte contiennent des données de feuille de calcul sans formatage. Le fichier est une sorte de fichier texte brut qui peut avoir des délimiteurs personnalisés entre ses données.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

##  **Comment enregistrer un fichier dans un flux**

 Pour enregistrer des fichiers dans un flux, créez un*Flux de mémoire* ou*Flux de fichiers*objet et enregistrez le fichier dans cet objet de flux en appelant le**[Cahier d'exercices](https://reference.aspose.com/cells/net/aspose.cells/workbook)** objets**[Enregistrer](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** méthode. Spécifiez le format de fichier souhaité à l'aide du**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** énumération lors de l'appel du**[Enregistrer](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**méthode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

##  **Comment enregistrer un fichier Excel dans des fichiers HTML et Mht**
Aspose.Cells peut simplement enregistrer un fichier Excel, JSON, CSV ou d'autres fichiers qui pourraient être chargés par Aspose.Cells sous forme de fichiers .html et .mht.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

##  **Comment enregistrer un fichier Excel sur OpenOffice (ODS, SXC, FODS, OTS)**
Nous pouvons sauvegarder les fichiers au format open office : ODS, SXC, FODS, OTS etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

##  **Comment enregistrer un fichier Excel au format JSON ou XML**

JSON (JavaScript Object Notation) est un format de fichier standard ouvert pour le partage de données qui utilise du texte lisible par l'homme pour stocker et transmettre des données. Les fichiers JSON sont stockés avec l'extension .json. JSON nécessite moins de formatage et constitue une bonne alternative au XML. JSON est dérivé de JavaScript mais est un format de données indépendant du langage. La génération et l'analyse de JSON sont prises en charge par de nombreux langages de programmation modernes. application/json est le type de média utilisé pour JSON.

Aspose.Cells prend en charge l'enregistrement des fichiers au format JSON ou XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


##  **Sujets avancés**
- [Ajuster le niveau de compression du classeur](/cells/fr/net/adjust-workbook-compression-level/)
- [Enregistrer le classeur au format de feuille de calcul Open XML strict](/cells/fr/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Enregistrement du fichier dans l'objet de réponse](/cells/fr/net/saving-file-to-response-object/)
