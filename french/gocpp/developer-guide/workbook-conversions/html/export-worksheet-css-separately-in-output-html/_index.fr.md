---
title: Exporter séparément le CSS de la feuille de calcul dans le HTML de sortie avec Golang via C++
linktitle: Exporter la feuille de calcul CSS séparément dans le HTML de sortie
type: docs
weight: 80
url: /fr/go-cpp/export-worksheet-css-separately-in-output/
description: Apprenez comment exporter le CSS de la feuille de calcul séparément lors de la conversion de fichiers Excel en HTML en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells fournit la fonction d’exportation du CSS de la feuille séparément lors de la conversion de votre fichier Excel en HTML. Veuillez utiliser la propriété [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/) à cette fin et la régler sur **true** lors de l’enregistrement du fichier Excel au format HTML.

## **Exporter la feuille de calcul CSS séparément dans le HTML de sortie**

Le code d'exemple suivant crée un fichier Excel, ajoute du texte dans la cellule **B5** en couleur **rouge**, puis le sauvegarde au format HTML en utilisant la propriété [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/). Veuillez consulter le [HTML de sortie](60489766.zip) généré par le code pour référence. Vous y trouverez le fichier **stylesheet.css** comme résultat du code d'exemple.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml.go" >}}
## **Exporter un classeur à une seule feuille en HTML**

Lorsqu’un classeur avec plusieurs feuilles est converti en HTML avec Aspose.Cells, il crée un fichier HTML ainsi qu’un dossier contenant du CSS et plusieurs fichiers HTML. Lorsqu’on ouvre ce fichier HTML dans le navigateur, les onglets sont visibles. La même fonction est requise pour un classeur avec une seule feuille lors de la conversion en HTML. Auparavant, aucun dossier séparé n’était créé pour les classeurs à une seule feuille, et seul un fichier HTML était créé. Ce fichier HTML ne montre pas d’onglet lorsqu’il est ouvert dans le navigateur. MS Excel crée également un dossier approprié et un HTML pour une seule feuille, c’est pourquoi le même comportement est implémenté via les APIs d’Aspose.Cells. Le fichier d’exemple peut être téléchargé à partir du lien suivant pour être utilisé dans le code exemple ci-dessous :

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml-1.go" >}}
