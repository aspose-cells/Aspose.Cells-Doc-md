---
title: Convertir CSV, TSV et TXT en Excel
type: docs
weight: 30
url: /fr/net/convert-csv-tsv-and-txt-to-excel/
---
{{% alert color="primary" %}}

En utilisant Aspose.Cells, vous pouvez convertir un fichier CSV en Excel, OpenOffice, Pdf, Json et de nombreux formats différents.

{{% /alert %}}


## **Ouverture de fichiers CSV**

Les fichiers de valeurs séparées par des virgules (CSV) contiennent des enregistrements dans lesquels les valeurs sont séparées par des virgules. Les données sont stockées sous forme de tableau où chaque colonne est séparée par le caractère virgule et entre guillemets doubles. Si une valeur de champ contient un guillemet double, elle est échappée avec une paire de guillemets doubles. Vous pouvez également utiliser Microsoft Excel pour exporter des données de feuille de calcul vers CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **Ouverture des fichiers CSV et remplacement des caractères invalides**

Dans Excel, lorsque le fichier CSV contenant des caractères spéciaux est ouvert, les caractères sont automatiquement remplacés. La même chose est faite par Aspose.Cells API qui est démontré dans l'exemple de code ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **Utilisation de l'analyseur préféré**

Il n'est pas toujours nécessaire d'utiliser les paramètres d'analyseur par défaut pour ouvrir les fichiers CSV. Parfois, l'importation d'un fichier CSV ne crée pas la sortie attendue, car le format de date n'est pas comme prévu ou les champs vides sont traités différemment. Dans ce but**TxtLoadOptions.PreferredParsers**est disponible pour fournir son propre analyseur préféré pour analyser différents types de données selon les besoins. L'exemple de code suivant illustre l'utilisation de l'analyseur préféré.

Des exemples de fichiers source et de sortie peuvent être téléchargés à partir des liens suivants pour tester cette fonctionnalité.

[exemplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Ouverture de fichiers texte avec un séparateur personnalisé**

Les fichiers texte sont utilisés pour contenir des données de feuille de calcul sans formatage. Le fichier est une sorte de fichier texte brut qui peut avoir des délimiteurs personnalisés.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Ouverture de fichiers délimités par des tabulations**

Le fichier délimité par des tabulations (texte) contient des données de feuille de calcul mais sans aucune mise en forme. Les données sont organisées en lignes et en colonnes comme dans les tableaux et les feuilles de calcul. Fondamentalement, un fichier délimité par des tabulations est un type spécial de fichier texte brut avec une tabulation entre chaque colonne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Ouverture de fichiers de valeurs séparées par des tabulations (TSV)**

Le fichier de valeurs séparées par des tabulations (TSV) contient des données de feuille de calcul mais sans aucune mise en forme. Il en va de même avec le fichier délimité par des tabulations où les données sont disposées en lignes et en colonnes comme dans les tableaux et les feuilles de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **Sujets avancés**
- [Charger ou importer un fichier CSV avec des formules](/cells/fr/net/load-or-import-csv-file-with-formulas/)
- [Lecture d'un fichier CSV avec plusieurs encodages](/cells/fr/net/reading-csv-file-with-multiple-encodings/)

