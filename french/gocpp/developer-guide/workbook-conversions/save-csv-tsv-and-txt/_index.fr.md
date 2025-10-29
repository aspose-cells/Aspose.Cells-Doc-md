---
title: Convertir Excel en CSV, TSV et Txt avec Golang via C++
linktitle: Enregistrer en CSV, TSV et Txt
type: docs
weight: 40
url: /fr/go-cpp/convert-excel-to-csv-tsv-and-txt/
description: Convertissez facilement les fichiers Excel en formats CSV, TSV et TXT en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells permet de convertir des fichiers Excel, ODS, JSON, et autres formats en CSV, TSV, et TXT.

{{% /alert %}}

## **Enregistrer le classeur au format texte ou CSV**

Parfois, vous souhaitez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats texte (par exemple TXT, TabDelim, CSV, etc.), par défaut, à la fois Microsoft Excel et Aspose.Cells enregistrent uniquement le contenu de la feuille de calcul active.

L'exemple de code suivant explique comment enregistrer un classeur entier au format texte. Chargez le classeur source qui peut être n'importe quel fichier de feuille de calcul Microsoft Excel ou OpenOffice (donc XLS, XLSX, XLSM, XLSB, ODS, etc.) avec n'importe quel nombre de feuilles de calcul

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT

Vous pouvez modifier le même exemple pour enregistrer votre fichier au format CSV. Par défaut, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/) est une virgule, donc ne spécifiez pas de séparateur si vous enregistrez en format CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt.go" >}}
## **Enregistrement de fichiers texte avec séparateur personnalisé**

Les fichiers texte contiennent des données de feuille de calcul sans mise en forme. Le fichier est un type de fichier texte brut qui peut avoir des délimiteurs personnalisés entre ses données

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt-1.go" >}}
## **Sujets avancés**
- [Conserver les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV](/cells/fr/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Supprimer les lignes et colonnes vides en tête lors de l'exportation de feuilles de calcul au format CSV](/cells/fr/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
