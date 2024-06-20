---
title: Convertir CSV, TSV et TXT en Excel
type: docs
weight: 30
url: /fr/net/convert-csv-tsv-and-txt-to-excel/
---

{{% alert color="primary" %}}

En utilisant Aspose.Cells, vous pouvez convertir un fichier CSV en Excel, OpenOffice, Pdf, Json et de nombreux autres formats

{{% /alert %}}


## **Ouverture des fichiers CSV**

Les fichiers au format Valeurs Séparées par des Virgules (CSV) contiennent des enregistrements où les valeurs sont séparées par des virgules. Les données sont stockées sous forme de tableau où chaque colonne est séparée par le caractère virgule et est encadrée par le caractère double quote. Si une valeur de champ contient un caractère de guillemet double, il est échappé avec une paire de caractères de guillemet double. Vous pouvez également utiliser Microsoft Excel pour exporter des données de feuille de calcul vers un fichier CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **Ouverture des fichiers CSV et remplacement des caractères invalides**

Dans Excel, lorsque vous ouvrez un fichier CSV contenant des caractères spéciaux, les caractères sont automatiquement remplacés. La même opération est effectuée par l'API Aspose.Cells, comme le montre l'exemple de code ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **Utilisation de l'analyseur préféré**

Il n'est pas toujours nécessaire d'utiliser les paramètres d'analyseur par défaut pour ouvrir les fichiers CSV. Parfois, l'importation d'un fichier CSV ne crée pas la sortie attendue, comme le format de date qui n'est pas celui attendu ou la manière dont les champs vides sont gérés différemment. Dans ce but, **TxtLoadOptions.PreferredParsers** est disponible pour fournir son propre analyseur préféré pour analyser différents types de données selon les besoins. Le code d'exemple suivant démontre l'utilisation de l'analyseur préféré.  

Le fichier source d'échantillon et les fichiers de sortie peuvent être téléchargés aux liens suivants pour tester cette fonctionnalité.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Ouverture de fichiers texte avec un séparateur personnalisé**

Les fichiers texte sont utilisés pour stocker des données de feuille de calcul sans mise en forme. Le fichier est une sorte de fichier texte brut qui peut avoir des délimiteurs personnalisés.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Ouverture des fichiers à valeurs séparées par des tabulations**

Un fichier délimité par des tabulations (texte) contient des données de feuille de calcul mais sans aucun formatage. Les données sont disposées en lignes et en colonnes comme dans les tableaux et les feuilles de calcul. Fondamentalement, un fichier délimité par des tabulations est un type spécial de fichier texte brut avec une tabulation entre chaque colonne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Ouverture des fichiers à valeurs séparées par des tabulations (TSV)**

Un fichier à valeurs séparées par des tabulations (TSV) contient des données de feuille de calcul mais sans aucun formatage. C'est la même chose avec un fichier délimité par des tabulations où les données sont disposées en lignes et en colonnes comme dans les tableaux et les feuilles de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **Sujets avancés**
- [Charger ou importer un fichier CSV avec des formules](/cells/fr/net/load-or-import-csv-file-with-formulas/)
- [Lecture d'un fichier CSV avec des encodages multiples](/cells/fr/net/reading-csv-file-with-multiple-encodings/)

