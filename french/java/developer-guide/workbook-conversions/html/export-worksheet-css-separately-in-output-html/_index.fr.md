---
title: Exporter la feuille de calcul CSS séparément dans le HTML de sortie
type: docs
weight: 80
url: /fr/java/export-worksheet-css-separately-in-output-html/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells offre la possibilité d'exporter la feuille de style CSS séparément lorsque vous convertissez votre fichier Excel en HTML. Veuillez utiliser la propriété HtmlSaveOptions.ExportWorksheetCSSSeparately à cette fin et définissez-la sur true lors de l'enregistrement du fichier Excel au format HTML.

## **Exporter la feuille de calcul CSS séparément dans le HTML de sortie**

Le code d'exemple suivant crée un fichier Excel, ajoute du texte dans la cellule B5 en couleur rouge puis l'enregistre au format HTML en utilisant la propriété HtmlSaveOptions.ExportWorksheetCSSSeparately. Veuillez consulter le [fichier HTML de sortie](60489780.zip) généré par le code pour référence. Vous y trouverez le stylesheet.css à l'intérieur comme résultat du code d'exemple.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **Exporter un classeur à feuille unique en HTML**

Lorsqu'un classeur avec plusieurs feuilles est converti en HTML à l'aide d'Aspose.Cells, il crée un fichier HTML accompagné d'un dossier contenant des CSS et plusieurs fichiers HTML. Lorsque ce fichier HTML est ouvert dans un navigateur, les onglets sont visibles. Le même comportement est requis pour un classeur avec une seule feuille lorsqu'il est converti en HTML. Auparavant, aucun dossier distinct n'était créé pour les classeurs à feuille unique et seul un fichier HTML était créé. Ce type de fichier HTML ne montre pas d'onglet lorsqu'il est ouvert dans un navigateur. Excel crée un dossier et un fichier HTML appropriés pour les feuilles uniques et donc le même comportement est implémenté en utilisant Aspose.Cells. Le fichier d'exemple peut être téléchargé à partir du lien suivant pour être utilisé dans le code d'exemple ci-dessous :

[sampleSingleSheet.xlsx](79527948.xlsx)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
{{< app/cells/assistant language="java" >}}
