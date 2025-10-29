---
title: Ajuster automatiquement les colonnes et les lignes lors du chargement du HTML dans le classeur
type: docs
weight: 120
url: /fr/python-net/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Ce sujet vous montre comment ajuster automatiquement les colonnes et les lignes lors du chargement de HTML dans le classeur à l aide d Aspose.Cells pour Python via NET.
keywords: Ajuster automatiquement les colonnes et les lignes lors du chargement de HTML dans le classeur, Ajuster automatiquement les colonnes et les lignes lors du chargement de HTML.
---

## **Scénarios d'utilisation possibles**

Vous pouvez ajuster automatiquement les colonnes et les lignes lors du chargement de votre fichier HTML à l'intérieur de l'objet Workbook. Veuillez définir la propriété [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) sur **true** à cette fin.

## **Ajuster automatiquement les colonnes et les lignes lors du chargement du HTML dans le classeur**

Le code d'exemple suivant charge d'abord le fichier HTML d'exemple dans Workbook sans aucune option de chargement et l'enregistre au format XLSX. Ensuite, il charge à nouveau le fichier HTML d'exemple dans Workbook mais cette fois, il charge le HTML après avoir défini la propriété [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) sur **true** et l'enregistre au format XLSX. Veuillez télécharger les deux fichiers Excel en sortie, à savoir [Fichier Excel en sortie sans ajustement automatique des colonnes et des lignes](outputWithout_AutoFitColsAndRows.xlsx) et [Fichier Excel en sortie avec ajustement automatique des colonnes et des lignes](outputWith_AutoFitColsAndRows.xlsx). La capture d'écran suivante montre l'effet de la propriété [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) sur les deux fichiers Excel en sortie.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
