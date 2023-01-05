---
title: Exporter la feuille de calcul CSS séparément dans la sortie HTML
type: docs
weight: 80
url: /fr/java/export-worksheet-css-separately-in-output-html/
---
## **Scénarios d'utilisation possibles**

Aspose.Cells fournit la fonctionnalité permettant d'exporter la feuille de calcul CSS séparément lorsque vous convertissez votre fichier Excel en HTML. Veuillez utiliser la propriété HtmlSaveOptions.ExportWorksheetCSSSeparately à cette fin et définissez-la sur true lors de l'enregistrement du fichier Excel au format HTML.

## **Exporter la feuille de calcul CSS séparément dans la sortie HTML**

L'exemple de code suivant crée un fichier Excel, ajoute du texte dans la cellule B5 en rouge, puis l'enregistre au format HTML à l'aide de la propriété HtmlSaveOptions.ExportWorksheetCSSSeparately. Veuillez consulter le[sortie HTML](60489780.zip)généré par le code pour une référence. Vous y trouverez stylesheet.css à la suite de l'exemple de code.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **Exporter le classeur d'une seule feuille vers HTML**

Lorsqu'un classeur avec plusieurs feuilles est converti en HTML à l'aide de Aspose.Cells, il crée un fichier HTML avec un dossier contenant CSS et plusieurs fichiers HTML. Lorsque ce fichier HTML est ouvert dans le navigateur, les onglets sont visibles. Le même comportement est requis pour un classeur avec une seule feuille de calcul lorsqu'il est converti en HTML. Auparavant, aucun dossier séparé n'était créé pour les classeurs à feuille unique et seul le fichier HTML était créé. Ce fichier HTML n'affiche pas l'onglet lorsqu'il est ouvert dans le navigateur. Excel crée également le dossier approprié et HTML pour les feuilles simples et, par conséquent, le même comportement est implémenté à l'aide de Aspose.Cells. Un exemple de fichier peut être téléchargé à partir du lien suivant pour être utilisé dans l'exemple de code ci-dessous :

[sampleSingleSheet.xlsx](79527948.xlsx)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
