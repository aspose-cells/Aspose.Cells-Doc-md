---
title: Convertir Excel en CSV,TSV et Txt
linktitle: Enregistrer sous CSV,TSV et Txt
type: docs
weight: 40
url: /fr/python-net/convert-excel-to-csv-tsv-and-txt/
description: Convertissez Excel en CSV,TSV et Txt en utilisant Aspose.Cells for Python via .NET API.
keywords: Python Convert Excel to CSV,TSV and Txt, Convert Excel to CSV,TSV and Txt in Python via NET, Python Convert Workbook to CSV,TSV and Txt.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET permet de convertir des fichiers Excel, ods, json et autres formats en CSV, TSV et TXT.

{{% /alert %}}

##  **Enregistrement du classeur au format texte ou CSV**

Parfois, vous souhaitez convertir ou enregistrer un classeur contenant plusieurs feuilles de calcul au format texte. Pour les formats de texte (par exemple TXT, TabDelim, CSV, etc.), par défaut, Microsoft Excel et Aspose.Cells for Python via .NET enregistrent uniquement le contenu de la feuille de calcul active.

L'exemple de code suivant explique comment enregistrer un classeur entier au format texte. Chargez le classeur source qui peut être n'importe quel fichier de feuille de calcul Excel ou OpenOffice Microsoft (donc XLS, XLSX, XLSM, XLSB, ODS et ainsi de suite) avec n'importe quel nombre de feuilles de calcul.

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT.

 Vous pouvez modifier le même exemple pour enregistrer votre fichier sous CSV. Par défaut,**[TxtSaveOptions.separator](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/)**est une virgule, donc ne spécifiez pas de séparateur si vous enregistrez au format CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

##  **Enregistrement de fichiers texte avec un séparateur personnalisé**

Les fichiers texte contiennent des données de feuille de calcul sans formatage. Le fichier est une sorte de fichier texte brut qui peut avoir des délimiteurs personnalisés entre ses données.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


##  **Sujets avancés**
- [Conservez les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV](/cells/fr/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Supprimez les premières lignes et colonnes vides lors de l'exportation de feuilles de calcul au format CSV.](/cells/fr/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
