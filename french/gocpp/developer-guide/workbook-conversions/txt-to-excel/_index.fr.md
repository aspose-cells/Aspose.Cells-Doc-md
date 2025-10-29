---
title: Convertir CSV, TSV et TXT en Excel avec Golang via C++
linktitle: Convertir CSV, TSV, et TXT en Excel
type: docs
weight: 30
url: /fr/go-cpp/convert-csv-tsv-and-txt-to-excel/
description: Apprenez comment convertir des fichiers CSV, TSV, et TXT en Excel en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 Avec Aspose.Cells for C++, vous pouvez convertir des fichiers CSV en Excel, OpenOffice, PDF, JSON, et bien d'autres formats.

{{% /alert %}}

## **Ouverture des fichiers CSV**

Les fichiers valeurs séparées par des virgules (CSV) contiennent des enregistrements où les valeurs sont séparées par des virgules. Les données sont stockées sous forme de tableau où chaque colonne est séparée par le caractère virgule et entourée de guillemets doubles. Si une valeur de champ contient un caractère de guillemet double, elle est échappée avec une paire de guillemets doubles. Vous pouvez également utiliser Microsoft Excel pour exporter les données de feuilles de calcul en CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel.go" >}}
## **Ouverture de fichiers CSV et remplacement des caractères invalides**

Dans Excel, lorsqu'un fichier CSV avec des caractères spéciaux est ouvert, les caractères sont automatiquement remplacés. La même chose est effectuée par l'API Aspose.Cells, comme le montre l'exemple de code ci-dessous.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-1.go" >}}
## **Utilisation du parseur préféré**

Il n'est pas toujours nécessaire d'utiliser les paramètres par défaut du parseur pour ouvrir des fichiers CSV. Parfois, l'importation d'un fichier CSV ne crée pas la sortie attendue, par exemple lorsque le format de date n'est pas conforme ou lorsque les champs vides sont traités différemment. À cette fin, **TxtLoadOptions.PreferredParsers** est disponible pour fournir votre propre parseur préféré afin d'analyser différents types de données selon vos besoins. Le code d'exemple suivant démontre l'utilisation d'un parseur préféré.

Le fichier source d'échantillon et les fichiers de sortie peuvent être téléchargés aux liens suivants pour tester cette fonctionnalité.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-2.go" >}}
### **Ouverture de fichiers texte avec un séparateur personnalisé**

Les fichiers texte sont utilisés pour stocker des données de feuille de calcul sans mise en forme. Le fichier est une sorte de fichier texte brut qui peut avoir des délimiteurs personnalisés.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-3.go" >}}
### **Ouverture de fichiers délimités par des tabulations**

Les fichiers délimités par une tabulation (Texte) contiennent des données de tableur mais sans mise en forme. Les données sont organisées en lignes et en colonnes comme dans des tableaux et des feuilles de calcul. En gros, un fichier délimité par une tabulation est un type particulier de fichier texte simple avec une tabulation entre chaque colonne.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-4.go" >}}
### **Ouverture des fichiers à valeurs séparées par des tabulations (TSV)**

Les fichiers de valeurs séparées par des tabulations (TSV) contiennent des données de tableur mais sans mise en forme. C'est la même chose qu'un fichier délimité par une tabulation où les données sont arrangées en lignes et en colonnes comme dans des tableaux et des feuilles de calcul.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-5.go" >}}
## **Sujets avancés**
- [Charger ou importer un fichier CSV avec des formules](/cells/fr/cpp/load-or-import-csv-file-with-formulas/)
- [Lecture d'un fichier CSV avec des encodages multiples](/cells/fr/cpp/reading-csv-file-with-multiple-encodings/)
