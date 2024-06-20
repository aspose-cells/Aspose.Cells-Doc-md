---
title: Exporter la feuille de calcul CSS séparément dans le HTML de sortie
type: docs
weight: 80
url: /fr/net/export-worksheet-css-separately-in-output/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells offre la possibilité d'exporter la feuille de calcul CSS séparément lors de la conversion de votre fichier Excel au format HTML. Veuillez utiliser la propriété [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) à cette fin et la définir sur **true** lors de l'enregistrement du fichier Excel au format HTML.

## **Exporter la feuille de calcul CSS séparément dans le HTML de sortie**

Le code d'exemple suivant crée un fichier Excel, ajoute du texte dans la cellule **B5** en couleur **rouge**, puis le sauvegarde au format HTML en utilisant la propriété [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately). Veuillez consulter le [HTML de sortie](60489766.zip) généré par le code pour référence. Vous y trouverez le fichier **stylesheet.css** comme résultat du code d'exemple.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Exporter un classeur à feuille unique en HTML**

Lorsqu'un classeur avec plusieurs feuilles est converti en HTML à l'aide de Aspose.Cells, il crée un fichier HTML ainsi qu'un dossier contenant du CSS et plusieurs fichiers HTML. Lorsque ce fichier HTML est ouvert dans le navigateur, les onglets sont visibles. Le même comportement est requis pour un classeur avec une seule feuille lorsqu'il est converti en HTML. Auparavant, aucun dossier distinct n'était créé pour les classeurs à feuille unique et seul le fichier HTML était créé. Ce fichier HTML ne montre pas d'onglet lorsqu'il est ouvert dans un navigateur. MS Excel crée un dossier et un HTML approprié pour une seule feuille également et donc le même comportement est implémenté à l'aide des API Aspose.Cells. Le fichier d'exemple peut être téléchargé à partir du lien suivant pour être utilisé dans le code d'exemple ci-dessous :

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
