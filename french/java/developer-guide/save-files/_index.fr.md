---
title: Enregistrement de fichiers Excel aux formats CSV, PDF et autres
linktitle: Enregistrer les fichiers
type: docs
weight: 20
url: /fr/java/saving-excel-files-to-csv-pdf-and-other-formats/
---
{{% alert color="primary" %}}

**Aspose.Cells** permet aux développeurs de créer des fichiers Excel à partir de zéro à l'aide de son API flexible. Une fois que vous avez créé des fichiers Excel, vous devez également enregistrer votre classeur (fichier). Aspose.Cells fournit une variété de façons d'enregistrer ces fichiers. Dans cette rubrique, nous discuterons de toutes les manières possibles qui peuvent être adoptées par les développeurs pour enregistrer leurs fichiers.

{{% /alert %}}

## **Différentes façons d'enregistrer vos fichiers**

 Aspose.Cells API fournit une classe nommée[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)qui représente un fichier Excel et fournit toutes les propriétés et méthodes nécessaires dont les développeurs peuvent avoir besoin pour travailler avec leurs fichiers Excel. Le[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la classe offre une[**sauvegarder**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) méthode utilisée pour enregistrer les fichiers Excel. Le[**sauvegarder**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) a de nombreuses surcharges qui sont utilisées pour enregistrer des fichiers Excel de différentes manières.

 Les développeurs peuvent également spécifier le format de fichier dans lequel leurs fichiers doivent être enregistrés. Les fichiers peuvent être enregistrés dans plusieurs formats tels que XLS, SpreadsheetML, CSV, Tab Delimited, Tab-separated values TSV, XPS et bien d'autres. Ces formats de fichier sont spécifiés à l'aide de la[**Enregistrer le format**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) énumération.

[**Enregistrer le format**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)énumération contient de nombreux formats de fichiers prédéfinis (que vous pouvez choisir) comme suit :

|**Types de formats de fichiers**|**Description**|
|:- |:- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API tente de détecter le format approprié à partir de l'extension de fichier spécifiée dans le premier paramètre de la méthode de sauvegarde|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|Représente un fichier CSV|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Représente un fichier Office Open XML SpreadsheetML|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|Représente le fichier XLSM basé sur XML|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Représente un fichier de modèle Excel|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Représente un fichier de modèle Excel compatible avec les macros|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Représente un fichier Excel XLAM|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|Représente un fichier de valeurs séparées par des tabulations|
|[**ONGLET DÉLIMITÉ**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|Représente un fichier texte délimité par des tabulations|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|Représente un ou plusieurs fichiers HTML|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|Représente un ou plusieurs fichiers MHTML|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|Représente un fichier de feuille de calcul OpenDocument|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Représente un fichier XLS qui est le format par défaut pour les révisions Excel 1997 à 2003|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|Représente un fichier SpreadSheetML|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Représente un fichier Excel 2007 binaire XLSB|
|[**INCONNUE**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Représente un format non reconnu, ne peut pas être enregistré.|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|Représente un document PDF|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|Représente un fichier XML Paper Specification (XPS)|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Représente un fichier Tagged Image File Format (TIFF)|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|Représente un fichier XML Scalable Vector Graphics (SVG)|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Représente le format d'échange de données.|
|[**NOMBRES**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Représente un fichier de nombres.|
|[**MARKDOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Représente un document de démarque.|
**Normalement, il existe deux façons d'enregistrer des fichiers Excel comme suit :**

1. **Enregistrer le fichier à un emplacement**
1. **Enregistrement du fichier dans un flux**

## **Enregistrement du fichier à un emplacement**

Si les développeurs ont besoin d'enregistrer leurs fichiers dans un emplacement de stockage, ils peuvent simplement spécifier le nom du fichier (avec son chemin de stockage complet) et le format de fichier souhaité (en utilisant le[**Enregistrer le format**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) énumération) en appelant le[**sauvegarder**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) méthode de[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)objet.

**Exemple:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Enregistrement du classeur au format texte ou CSV**

Parfois, vous souhaitez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats de texte (par exemple TXT, TabDelim, CSV etc.), par défaut, Microsoft Excel et Aspose.Cells enregistrent uniquement le contenu de la feuille de calcul active.

L'exemple de code suivant explique comment enregistrer un classeur entier au format texte. Chargez le classeur source qui peut être n'importe quel fichier de feuille de calcul Excel ou OpenOffice Microsoft (donc XLS, XLSX, XLSM, XLSB, ODS, etc.) avec n'importe quel nombre de feuilles de calcul.

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT.

Vous pouvez modifier le même exemple pour enregistrer votre fichier au CSV. Par défaut,[**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) est une virgule, ne spécifiez donc pas de séparateur si vous enregistrez au format CSV.

**Exemple:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Enregistrement de fichiers texte avec un séparateur personnalisé**

Les fichiers texte contiennent des données de feuille de calcul sans formatage. Le fichier est une sorte de fichier texte brut qui peut avoir des délimiteurs personnalisés entre ses données.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Enregistrement d'un fichier dans un flux**

 Si les développeurs ont besoin d'enregistrer leurs fichiers sur un**Flux** alors ils doivent créer un**FileOutputStream** objet, puis enregistrez le fichier dans celui-ci**Flux** objet en appelant le[**sauvegarder**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) méthode de[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) objet. Les développeurs peuvent également spécifier le format de fichier souhaité (à l'aide de la[**Enregistrer le format**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) énumération) en appelant le[**sauvegarder**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) méthode.

**Exemple:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Enregistrement du fichier dans un autre format**

### **XLS Fichiers**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX Fichiers**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF Fichiers**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **Définir l'option ContentCopyForAccessibility**

 Avec le[**PdfEnregistrerOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) classe, vous pouvez obtenir ou définir le PDF[**AccessibilitéExtraireContenu**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent)option pour contrôler l'accès au contenu dans le PDF converti. Cela signifie qu'il permet au logiciel de lecteur d'écran d'utiliser le texte dans le fichier PDF pour lire le fichier PDF. Vous pouvez le désactiver en appliquant un mot de passe de modification des autorisations et en désélectionnant les deux éléments dans la capture d'écran[ici](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Exporter les propriétés personnalisées vers PDF**

Avec le[**PdfEnregistrerOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) classe, vous pouvez exporter les propriétés personnalisées du classeur source vers le PDF.[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport) L'énumérateur est fourni pour spécifier la manière dont les propriétés sont exportées. Ces propriétés peuvent être observées dans Adobe Acrobat Reader en cliquant sur Fichier, puis sur l'option Propriétés, comme indiqué dans l'image suivante. Le fichier modèle "sourceWithCustProps.xlsx" peut être téléchargé[ici](sourceWithCustProps.xlsx)pour tester et produire le fichier PDF "outSourceWithCustProps" est disponible[ici](outSourceWithCustProps.pdf)pour analyse.

![tâche : image_autre_texte](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Convertir un classeur Excel en Markdown**

Le Aspose.Cells API prend en charge l'exportation de feuilles de calcul au format Markdown. Pour exporter la feuille de calcul active vers Markdown, passez[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)comme deuxième paramètre de[**Classeur.Enregistrer**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)) méthode. Vous pouvez également utiliser[**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions)classe pour spécifier des paramètres supplémentaires pour l'exportation de la feuille de calcul vers Markdown.

L'exemple de code suivant illustre l'exportation d'une feuille de calcul active vers Markdown à l'aide de[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)membre de l'énumération. Veuillez consulter le[fichier Markdown de sortie](Book1.txt)généré par le code pour référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **Sujets avancés**
- [Ajuster le niveau de compression du classeur](/cells/fr/java/adjust-workbook-compression-level/)
- [Conversion du classeur en différents formats](/cells/fr/java/converting-workbook-to-different-formats/)
- [Enregistrer le classeur au format de feuille de calcul Open XML strict](/cells/fr/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Suivre la progression de la conversion d'Excel vers TIFF](/cells/fr/java/track-conversion-progress-of-excel-to-tiff/)
- [Suivre la progression de la conversion des documents](/cells/fr/java/track-document-conversion-progress/)
