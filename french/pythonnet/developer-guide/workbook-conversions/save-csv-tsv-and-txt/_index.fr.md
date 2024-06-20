---
title: Convertir Excel en CSV, TSV et Txt
linktitle: Enregistrer en CSV, TSV et Txt
type: docs
weight: 40
url: /fr/python-net/convert-excel-to-csv-tsv-and-txt/
description: Convertir Excel en CSV, TSV et Txt en utilisant Aspose.Cells pour l API Python via .NET
keywords: Python Convertir Excel en CSV, TSV et Txt, Convertir Excel en CSV, TSV et Txt en Python via NET, Python Convertir le classeur en CSV, TSV et Txt
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET rend possible la conversion de fichiers au format excel, ods, json et autres en CSV, TSV et TXT

{{% /alert %}}

## **Enregistrer le classeur au format texte ou CSV**

Parfois, vous voulez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats de texte (par exemple TXT, TabDelim, CSV, etc.), par défaut, à la fois Microsoft Excel et Aspose.Cells pour Python via .NET sauvegardent uniquement le contenu de la feuille de calcul active

L'exemple de code suivant explique comment enregistrer un classeur entier au format texte. Chargez le classeur source qui peut être n'importe quel fichier de feuille de calcul Microsoft Excel ou OpenOffice (donc XLS, XLSX, XLSM, XLSB, ODS, etc.) avec n'importe quel nombre de feuilles de calcul

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT

Vous pouvez modifier le même exemple pour enregistrer votre fichier au format CSV. Par défaut, [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/) est une virgule, donc ne spécifiez pas de séparateur si vous enregistrez au format CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

## **Enregistrement de fichiers texte avec séparateur personnalisé**

Les fichiers texte contiennent des données de feuille de calcul sans mise en forme. Le fichier est un type de fichier texte brut qui peut avoir des délimiteurs personnalisés entre ses données

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


## **Sujets avancés**
- [Conserver les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV](/cells/fr/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Supprimer les lignes et colonnes vides en tête lors de l'exportation de feuilles de calcul au format CSV](/cells/fr/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
