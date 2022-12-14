---
title: Exporter la feuille de calcul CSS séparément dans le HTML de sortie
type: docs
weight: 80
url: /fr/net/export-worksheet-css-separately-in-output/
---
## **Scénarios d'utilisation possibles**

 Aspose.Cells fournit la fonctionnalité permettant d'exporter la feuille de calcul CSS séparément lorsque vous convertissez votre fichier Excel en HTML. Veuillez utiliser[**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) propriété à cet effet et réglez-la sur**vrai** lors de l'enregistrement du fichier Excel au format HTML.

## **Exporter la feuille de calcul CSS séparément dans le HTML de sortie**

L'exemple de code suivant crée un fichier Excel, ajoute du texte dans la cellule**B5** dans**Rouge** color puis l'enregistre au format HTML en utilisant[**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately)propriété. Veuillez consulter le[sortie HTML](60489766.zip) généré par le code pour référence. Tu trouveras**feuille de style.css**à l'intérieur à la suite de l'exemple de code.

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Exporter un classeur à feuille unique au format HTML**

Lorsqu'un classeur avec plusieurs feuilles est converti en HTML à l'aide de Aspose.Cells, il crée un fichier HTML avec un dossier contenant CSS et plusieurs fichiers HTML. Lorsque ce fichier HTML est ouvert dans le navigateur, les onglets sont visibles. Le même comportement est requis pour un classeur avec une seule feuille de calcul lorsqu'il est converti en HTML. Auparavant, aucun dossier séparé n'était créé pour les classeurs à feuille unique et seul le fichier HTML était créé. Un tel fichier HTML n'affiche pas d'onglet lorsqu'il est ouvert dans le navigateur. MS Excel crée également le dossier et le code HTML appropriés pour une seule feuille et, par conséquent, le même comportement est implémenté à l'aide des API Aspose.Cells. L'exemple de fichier peut être téléchargé à partir du lien suivant pour être utilisé dans l'exemple de code ci-dessous :

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
