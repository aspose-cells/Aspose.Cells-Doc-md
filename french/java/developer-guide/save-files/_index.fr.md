---
title: Enregistrement des fichiers Excel au format CSV, PDF et autres formats
linktitle: Enregistrer des fichiers
type: docs
weight: 20
url: /fr/java/saving-excel-files-to-csv-pdf-and-other-formats/
---

{{% alert color="primary" %}}

**Aspose.Cells** permet aux développeurs de créer des fichiers Excel à partir de zéro en utilisant son API flexible. Une fois que vous créez des fichiers Excel, vous devrez également enregistrer votre classeur (fichier). Aspose.Cells offre une variété de façons d'enregistrer ces fichiers. Dans ce sujet, nous discuterons de toutes ces façons possibles qui peuvent être adoptées par les développeurs pour enregistrer leurs fichiers.

{{% /alert %}}

## **Différentes façons d'enregistrer vos fichiers**

L'API Aspose.Cells fournit une classe nommée [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) qui représente un fichier Excel et fournit toutes les propriétés et les méthodes nécessaires que les développeurs peuvent avoir besoin pour travailler avec leurs fichiers Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) fournit une méthode [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) qui est utilisée pour enregistrer des fichiers Excel. La méthode [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) a de nombreuses surcharges qui sont utilisées pour enregistrer des fichiers Excel de différentes manières.

Les développeurs peuvent également spécifier le format de fichier dans lequel leurs fichiers doivent être enregistrés. Les fichiers peuvent être enregistrés dans plusieurs formats tels que XLS, SpreadsheetML, CSV, délimité par tabulation, valeurs séparées par des tabulations TSV, XPS et bien d'autres. Ces formats de fichiers sont spécifiés à l'aide de l'énumération [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat).

L'énumération [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) contient de nombreux formats de fichiers prédéfinis (qui peuvent être choisis par vous) comme suit :

|**Types de formats de fichier**|**Description**|
| :- | :- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|L'API essaie de détecter le format approprié à partir de l'extension de fichier spécifiée dans le premier paramètre de la méthode d'enregistrement|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|Représente un fichier CSV|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Représente un fichier Office Open XML SpreadsheetML|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|Représente un fichier XLSM basé sur XML|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Représente un fichier de modèle Excel|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Représente un fichier de modèle activé pour les macros Excel|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Représente un fichier XLAM Excel|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|Représente un fichier de valeurs séparées par des tabulations|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|Représente un fichier texte délimité par des tabulations|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|Représente un fichier(s) HTML|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|Représente un fichier(s) MHTML|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|Représente un fichier de feuille de calcul OpenDocument|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Représente un fichier XLS qui est le format par défaut pour les révisions d'Excel 1997 à 2003|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|Représente un fichier SpreadSheetML|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Représente un fichier XLSB binaire Excel 2007|
|[**UNKNOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Représente un format non reconnu, ne peut pas être enregistré.|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|Représente un document PDF|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|Représente un fichier de spécification de papier XML (XPS)|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Représente un fichier au format TIFF (Tagged Image File Format)|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|Représente un fichier SVG (Scalable Vector Graphics) basé sur XML|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Représente un format d'échange de données.|
|[**NUMBERS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Représente un fichier de numéros.|
|[**MARKDOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Représente un document Markdown.|
**Normalement, il existe deux façons d'enregistrer des fichiers Excel comme suit:**

1. **Enregistrer le fichier à un emplacement quelconque**
1. **Enregistrer le fichier dans un flux**

## **Enregistrer le fichier à un emplacement quelconque**

Si les développeurs ont besoin d'enregistrer leurs fichiers dans un emplacement de stockage, ils peuvent simplement spécifier le nom du fichier (avec son chemin de stockage complet) et le format de fichier souhaité (en utilisant l'énumération [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)) lors de l'appel de la méthode [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) de l'objet [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook).

**Exemple :**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Enregistrer le classeur au format texte ou CSV**

Parfois, vous voulez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats texte (par exemple TXT, TabDelim, CSV, etc.), à la fois Microsoft Excel et Aspose.Cells enregistrent par défaut le contenu de la feuille de calcul active uniquement.

L'exemple de code suivant explique comment enregistrer un classeur entier au format texte. Chargez le classeur source qui peut être n'importe quel fichier de feuille de calcul Microsoft Excel ou OpenOffice (donc XLS, XLSX, XLSM, XLSB, ODS, etc.) avec n'importe quel nombre de feuilles de calcul

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT.

Vous pouvez modifier le même exemple pour enregistrer votre fichier au format CSV. Par défaut, [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) est une virgule, donc ne spécifiez pas de séparateur lors de l'enregistrement au format CSV. Veuillez noter : Si vous utilisez la version d'évaluation et même si le paramètre de méthode [**TxtSaveOptions.setExportAllSheets(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions/#setExportAllSheets-boolean-) est défini sur true, le programme n'exportera toujours qu'une seule feuille de calcul.

**Exemple :**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Enregistrement de fichiers texte avec séparateur personnalisé**

Les fichiers texte contiennent des données de feuille de calcul sans mise en forme. Le fichier est un type de fichier texte brut qui peut avoir des délimiteurs personnalisés entre ses données

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Enregistrement du fichier dans un flux**

Si les développeurs ont besoin d'enregistrer leurs fichiers dans un **Stream**, ils doivent créer un objet **FileOutputStream** et ensuite enregistrer le fichier sur cet objet **Stream** en appelant la méthode [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) de l'objet [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Les développeurs peuvent également spécifier le format de fichier souhaité (en utilisant l'énumération [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)) lors de l'appel de la méthode [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)).

**Exemple :**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Enregistrement du fichier dans un autre format**

### **Fichiers XLS**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **Fichiers XLSX**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **Fichiers PDF**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **Définir l'option ContentCopyForAccessibility**

Avec la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions), vous pouvez obtenir ou définir l'option PDF [**AccessibilityExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent) pour contrôler l'accès au contenu dans le PDF converti. Cela signifie qu'il permet au logiciel de lecteur d'écran d'utiliser le texte dans le fichier PDF pour lire le fichier PDF. Vous pouvez le désactiver en appliquant un mot de passe de modification des autorisations et en désélectionnant les deux éléments dans la capture d'écran [ici](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Exporter les propriétés personnalisées vers un PDF**

Avec la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions), vous pouvez exporter les propriétés personnalisées du classeur source vers le PDF. L'énumérateur [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport) est fourni pour spécifier la manière dont les propriétés sont exportées. Ces propriétés peuvent être observées dans Adobe Acrobat Reader en cliquant sur Fichier puis sur l'option propriétés comme indiqué dans l'image suivante. Le fichier de modèle "sourceWithCustProps.xlsx" peut être téléchargé [ici](sourceWithCustProps.xlsx) pour des tests et le fichier PDF de sortie "outSourceWithCustProps" est disponible [ici](outSourceWithCustProps.pdf) pour l'analyse.

![todo:image_alt_text](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Convertir un classeur Excel en Markdown**

L'API Aspose.Cells prend en charge l'exportation de feuilles de calcul au format Markdown. Pour exporter la feuille de calcul active au format Markdown, passez [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN) comme second paramètre de la méthode [**Workbook.Save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)). Vous pouvez également utiliser la classe [**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions) pour spécifier des paramètres supplémentaires pour l'exportation de feuille de calcul au format Markdown.

L'exemple de code suivant démontre l'exportation de la feuille de calcul active en Markdown en utilisant un membre d'énumération [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN). Veuillez consulter le [fichier Markdown de sortie](Book1.txt) généré par le code pour référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **Sujets avancés**
- [Ajuster le niveau de compression du classeur](/cells/fr/java/adjust-workbook-compression-level/)
- [Convertir le classeur dans différents formats](/cells/fr/java/converting-workbook-to-different-formats/)
- [Enregistrer le classeur au format strict Open XML Spreadsheet](/cells/fr/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Suivre la progression de la conversion d'Excel en TIFF](/cells/fr/java/track-conversion-progress-of-excel-to-tiff/)
- [Suivre la progression de la conversion des documents](/cells/fr/java/track-document-conversion-progress/)
