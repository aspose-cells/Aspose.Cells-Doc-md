---
title: Différentes façons d enregistrer des fichiers
linktitle: Enregistrer des fichiers
type: docs
weight: 40
url: /fr/net/different-ways-to-save-files/
description: Aspose.Cells for .NET peut enregistrer des fichiers dans différents formats. Enregistrer des fichiers au format PDF. Enregistrer des fichiers au format HTML. Enregistrer des fichiers au format DOCX. Enregistrer des fichiers au format PPTX. Enregistrer des fichiers au format JSON. Enregistrer des fichiers au format MHTML.
keywords: Aspose.Cells Enregistrer Excel en PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML, etc. en utilisant C#, Enregistrer ou Convertir un classeur en PDF HTML JSON TXT SQL en C#.
---

{{% alert color="primary" %}}

Aspose.Cells rend possible la création et l'enregistrement de fichiers. Cet article explique les différentes façons dont les fichiers peuvent être enregistrés.

{{% /alert %}}

## **Différentes façons d'enregistrer des fichiers**

Aspose.Cells fournit la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel et fournit les propriétés et les méthodes nécessaires pour travailler avec des fichiers Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) fournit la méthode [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) utilisée pour enregistrer des fichiers Excel. La méthode [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) a de nombreuses surcharges qui sont utilisées pour enregistrer des fichiers de différentes manières.

Le format de fichier dans lequel le fichier est enregistré est décidé par l'énumération [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)

|**Types de formats de fichier**|**Description**|
| :- | :- |
|CSV|Représente un fichier CSV|
|Excel97To2003|Représente un fichier Excel 97 - 2003|
|Xlsx|Représente un fichier Excel 2007 XLSX|
|Xlsm|Représente un fichier Excel 2007 XLSM|
|Xltx|Représente un modèle Excel 2007 XLTX|
|Xltm|Représente un modèle activé par macro Excel 2007 XLTM|
|Xlsb|Représente un fichier XLSB binaire Excel 2007|
|SpreadsheetML|Représente un fichier XML de feuille de calcul|
|TSV|Représente un fichier de valeurs séparées par des tabulations|
|TabDelimited|Représente un fichier de texte à onglets|
|ODS|Représente un fichier ODS|
|Html|Représente un fichier HTML|
|MHtml|Représente un fichier MHTML|
|Pdf|Représente un fichier PDF|
|XPS|Représente un document XPS|
|TIFF|Représente le format de fichier TIFF (Tagged Image File Format)|

## **Comment enregistrer un fichier dans différents formats**

Pour enregistrer des fichiers dans un emplacement de stockage, spécifiez le nom du fichier (complet avec le chemin de stockage) et le format de fichier souhaité (à partir de l'énumération [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)) lors de l'appel de la méthode [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) de l'objet [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **Comment enregistrer un classeur au format PDF**
Le format de fichier Portable Document Format (PDF) est un type de document créé par Adobe dans les années 1990. Le but de ce format de fichier était d'introduire une norme de représentation de documents et d'autres matériels de référence dans un format indépendant du logiciel d'application, du matériel et du système d'exploitation. Le format de fichier PDF a la capacité de contenir des informations telles que du texte, des images, des hyperliens, des champs de formulaire, des médias riches, des signatures numériques, des pièces jointes, des métadonnées, des fonctionnalités géospatiales et des objets 3D qui peuvent devenir une partie du document source.

Les codes suivants montrent comment enregistrer le classeur au format fichier PDF avec Aspose.Cells:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **Comment enregistrer le classeur au format texte ou CSV**

Parfois, vous souhaitez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats texte (par exemple TXT, TabDelim, CSV, etc.), par défaut, à la fois Microsoft Excel et Aspose.Cells enregistrent uniquement le contenu de la feuille de calcul active.

L'exemple de code suivant explique comment enregistrer un classeur entier au format texte. Chargez le classeur source qui peut être n'importe quel fichier de feuille de calcul Microsoft Excel ou OpenOffice (donc XLS, XLSX, XLSM, XLSB, ODS, etc.) avec n'importe quel nombre de feuilles de calcul

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT

Vous pouvez modifier le même exemple pour enregistrer votre fichier au format CSV. Par défaut, [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator) est la virgule, donc ne spécifiez pas de séparateur si vous enregistrez en format CSV. Veuillez noter : si vous utilisez la version d’évaluation et même si la propriété [**TxtSaveOptions.ExportAllSheets**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/exportallsheets/) est définie à true, le programme n’exportera qu’une seule feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Comment enregistrer un fichier en fichiers de texte avec un séparateur personnalisé**

Les fichiers texte contiennent des données de feuille de calcul sans mise en forme. Le fichier est un type de fichier texte brut qui peut avoir des délimiteurs personnalisés entre ses données

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **Comment enregistrer un fichier dans un flux**

Pour enregistrer des fichiers dans un flux, créez un objet *MemoryStream* ou *FileStream* et enregistrez le fichier dans cet objet flux en appelant la méthode [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) de l'objet [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index). Spécifiez le format de fichier souhaité en utilisant l'énumération [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) lors de l'appel de la méthode [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **Comment enregistrer un fichier Excel en fichiers Html et Mht**
Aspose.Cells peut simplement enregistrer un fichier Excel, JSON, CSV ou d'autres fichiers qui peuvent être chargés par Aspose.Cells en tant que fichiers .html et .mht.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}


## **Comment enregistrer un fichier Excel au format OpenOffice (ODS, SXC, FODS, OTS)**
Nous pouvons enregistrer les fichiers au format open offce : ODS, SXC, FODS, OTS, etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **Comment enregistrer un fichier Excel en JSON ou XML**

JSON (JavaScript Object Notation) est un format de fichier standard ouvert pour le partage de données qui utilise un texte lisible par l'homme pour stocker et transmettre des données. Les fichiers JSON sont stockés avec l'extension .json. JSON nécessite moins de mise en forme et est une bonne alternative à XML. JSON est dérivé de JavaScript mais est un format de données indépendant du langage. La génération et l'analyse du JSON sont prises en charge par de nombreux langages de programmation modernes. application/json est le type de support utilisé pour JSON.

Aspose.Cells prend en charge l'enregistrement de fichiers en JSON ou XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **Sujets avancés**
- [Ajuster le niveau de compression du classeur](/cells/fr/net/adjust-workbook-compression-level/)
- [Enregistrer le classeur au format strict Open XML Spreadsheet](/cells/fr/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Enregistrer le fichier dans l'objet Response](/cells/fr/net/saving-file-to-response-object/)
{{< app/cells/assistant language="csharp" >}}
