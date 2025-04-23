---
title: Exporter la feuille de calcul CSS séparément dans le HTML de sortie
type: docs
weight: 80
url: /fr/python-net/export-worksheet-css-separately-in-output/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells pour Python via .NET permet d’exporter séparément le CSS de la feuille de calcul lors de la conversion de votre fichier Excel en HTML. Veuillez utiliser la propriété [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately) pour cela et la définir sur **true** lors de l’enregistrement en HTML.

## **Exporter la feuille de calcul CSS séparément dans le HTML de sortie**

Le code d'exemple suivant crée un fichier Excel, ajoute du texte dans la cellule **B5** en couleur **rouge**, puis le sauvegarde au format HTML en utilisant la propriété [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately). Veuillez consulter le [HTML de sortie](60489766.zip) généré par le code pour référence. Vous y trouverez le fichier **stylesheet.css** comme résultat du code d'exemple.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.py" >}}

## **Exporter un classeur à feuille unique en HTML**

Lorsqu’un classeur avec plusieurs feuilles est converti en HTML avec Aspose.Cells pour Python via .NET, il crée un fichier HTML accompagné d’un dossier contenant le CSS et plusieurs fichiers HTML. Lorsqu’on ouvre ce fichier HTML dans le navigateur, les onglets sont visibles. Le même comportement est requis pour un classeur avec une seule feuille lors de la conversion en HTML. Auparavant, aucun dossier séparé n’était créé pour les classeurs à feuille unique et seul un fichier HTML était créé. Ce fichier HTML ne montre pas l’onglet lorsqu’il est ouvert dans le navigateur. Microsoft Excel crée également un dossier approprié et un HTML pour une seule feuille, et c’est pourquoi le même comportement est implémenté avec l’API Aspose.Cells pour Python via .NET. Le fichier exemple peut être téléchargé à partir du lien suivant pour l’utiliser dans le code d’exemple ci-dessous :

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetSingleSheetTabNameInHtml-1.py" >}}
