---
title: Convertir Excel en CSV,TSV et Txt
linktitle: Enregistrer sous CSV,TSV et Txt
type: docs
weight: 40
url: /fr/net/convert-excel-to-csv-tsv-and-txt/
---
{{% alert color="primary" %}}

Aspose.Cells permet de convertir les fichiers excel, ods, json et autres formats en CSV, TSV et TXT.

{{% /alert %}}

## **Enregistrement du classeur au format texte ou CSV**

Parfois, vous souhaitez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats de texte (par exemple TXT, TabDelim, CSV, etc.), par défaut, Microsoft Excel et Aspose.Cells enregistrent uniquement le contenu de la feuille de calcul active.

L'exemple de code suivant explique comment enregistrer un classeur entier au format texte. Chargez le classeur source qui peut être n'importe quel fichier de feuille de calcul Excel ou OpenOffice Microsoft (donc XLS, XLSX, XLSM, XLSB, ODS, etc.) avec n'importe quel nombre de feuilles de calcul.

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT.

Vous pouvez modifier le même exemple pour enregistrer votre fichier au CSV. Par défaut,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**est une virgule, donc ne spécifiez pas de séparateur si vous enregistrez au format CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Enregistrement de fichiers texte avec un séparateur personnalisé**

Les fichiers texte contiennent des données de feuille de calcul sans formatage. Le fichier est une sorte de fichier texte brut qui peut avoir des délimiteurs personnalisés entre ses données.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **Sujets avancés**
- [Conserver les séparateurs pour les lignes vides lors de l'exportation des feuilles de calcul au format CSV](/cells/fr/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Coupez les premières lignes et colonnes vides lors de l'exportation des feuilles de calcul au format CSV](/cells/fr/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
