---
title: Fractionner des fichiers Excel en plusieurs fichiers
description: Aspose.Cells est une bibliothèque Python via .NET permettant de travailler avec des fichiers de feuilles de calcul, qui prend en charge le fractionnement d'un seul fichier Excel en plusieurs fichiers. Cet article expliquera comment fractionner des fichiers Excel en copiant chaque feuille de calcul dans un classeur séparé et en copiant des plages de cellules spécifiques dans d'autres classeurs.
keywords: Aspose.Cells, bibliothèque Python via .NET, feuille de calcul, fractionner un fichier Excel, copier une feuille de calcul, copier une plage, plusieurs classeurs, enregistrer en tant que fichiers séparés
type: docs
weight: 195
url: /fr/python-net/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge le fractionnement d'un seul fichier Excel en plusieurs fichiers. Il existe deux méthodes principales pour y parvenir : (1) en copiant chaque feuille de calcul du classeur source dans un nouveau classeur et en enregistrant chacun en tant que fichier séparé, et (2) en copiant une plage de cellules spécifique d'une feuille de calcul dans un nouveau classeur. Les deux approches sont utiles lorsque vous devez distribuer des sous-ensembles de données, créer des rapports plus petits pour différents destinataires, ou isoler des données pour un traitement individuel.

{{% /alert %}}

## **Introduction**

Il existe de nombreux scénarios concrets dans lesquels un développeur doit diviser un seul fichier Excel en plusieurs fichiers plus petits. Par exemple, un classeur peut contenir une feuille de calcul par service, et chaque responsable de service doit recevoir uniquement sa propre feuille. Dans d'autres cas, vous pouvez souhaiter extraire un tableau particulier ou un bloc de données d'une feuille de calcul et l'envoyer en tant que fichier autonome par e-mail, sans exposer le reste du classeur. Les grands classeurs consolidés peuvent également devoir être divisés en éléments plus petits pour faciliter la manipulation, accélérer le chargement, ou pour le traitement en aval par d'autres systèmes.

Aspose.Cells propose deux approches flexibles pour cette tâche. La première approche itère à travers chaque feuille de calcul du classeur source et copie son contenu dans une nouvelle instance de `Workbook`, en enregistrant chacune en tant que fichier séparé. La seconde approche se concentre sur une plage de cellules spécifique dans une feuille de calcul et copie uniquement cette plage dans un nouveau classeur. Dans les deux cas, le flux général est le même : charger le classeur source à l'aide de la classe `Workbook`, accéder aux données pertinentes via les objets `Worksheet` et `Cells`, transférer le contenu vers un `Workbook` de destination, puis enregistrer la destination sur le disque.

## **Fractionner un fichier Excel en copiant chaque feuille de calcul dans un nouveau classeur**

### **Aperçu de l'approche**

Dans cette approche, le classeur source est ouvert une seule fois, puis pour chaque `Worksheet` dans sa collection `worksheets`, un nouveau `Workbook` de destination est créé. Le contenu de la feuille de calcul source est ensuite copié dans la première feuille de calcul du classeur de destination, et le classeur de destination est enregistré en tant que fichier dont le nom est dérivé du nom de la feuille de calcul source. Le résultat est un fichier de sortie par feuille de calcul, chaque fichier de sortie contenant les données d'une seule feuille source.

Cette méthode est le bon choix lorsque chaque feuille de calcul de votre classeur source représente une unité d'information logiquement indépendante (telle qu'un service, une région, un mois ou une gamme de produits) et que vous souhaitez livrer ou traiter chaque unité de manière indépendante.

### **Étapes**

Les étapes suivantes décrivent comment fractionner un fichier Excel en copiant chaque feuille de calcul dans un nouveau classeur :

1. Ouvrez le fichier Excel source en instanciant un objet `Workbook` et en passant le chemin du fichier à son constructeur.
2. Itérez à travers la collection `Workbook.worksheets` à l'aide d'une boucle `for` afin que chaque `Worksheet` du fichier source soit traitée.
3. Dans la boucle, créez une nouvelle instance de `Workbook` de destination (un classeur vide) pour la feuille de calcul en cours.
4. Ajoutez une nouvelle `Worksheet` au classeur de destination (ou utilisez la première feuille de calcul par défaut) et attribuez-lui un nom significatif, idéalement le même que la propriété `name` de la feuille de calcul source.
5. Copiez le contenu de la feuille de calcul source dans la feuille de calcul de destination. Cela peut être fait en itérant les cellules de la collection `Cells` de la feuille de calcul source et en écrivant leurs valeurs dans les cellules correspondantes de la feuille de calcul de destination, ou en utilisant la méthode `Cells.copy` pour transférer une plage entière en une seule fois.
6. Construisez un chemin de fichier de sortie qui incorpore le nom de la feuille de calcul source (par exemple, `dataDir + worksheet.name + ".xls"`) afin que chaque fichier généré ait un nom unique.
7. Appelez la méthode `Workbook.save` du `Workbook` de destination pour écrire le fichier sur le disque.
8. Répétez les étapes 3 à 7 pour la feuille de calcul suivante jusqu'à ce que toutes les feuilles de calcul aient été traitées.

### **Exemple de code**

```python
import aspose.cells as ac
import os

data_dir = "data/"
workbook = ac.Workbook(data_dir + "book1.xls")

for i in range(workbook.worksheets.count):
    source_sheet = workbook.worksheets[i]
    sheet_name = source_sheet.name
    
    dest_workbook = ac.Workbook()
    dest_index = dest_workbook.worksheets.add()
    dest_sheet = dest_workbook.worksheets[dest_index]
    dest_sheet.name = sheet_name
    
    dest_sheet.copy(source_sheet)
    
    dest_file = data_dir + sheet_name + ".xls"
    dest_workbook.save(dest_file, ac.SaveFormat.EXCEL97_TO_2003)
```

Le résultat attendu est un ensemble de nouveaux fichiers dans le répertoire de données, un fichier par feuille de calcul du classeur source. Chaque fichier est nommé d'après sa feuille source correspondante, et le fichier contient les données (et éventuellement la mise en forme) de cette seule feuille.

## **Fractionner un fichier Excel en copiant une plage dans un nouveau classeur**

### **Aperçu de l'approche**

Parfois, les données que vous devez fractionner ne correspondent pas à une feuille de calcul entière, mais plutôt à une région rectangulaire spécifique d'une feuille de calcul, telle que `A1:D10` ou une plage nommée qui représente un tableau particulier. Dans ces cas, copier des feuilles de calcul entières est inutile, et une approche plus précise est nécessaire : identifier la plage source, copier uniquement cette plage dans un nouveau classeur, et enregistrer le nouveau fichier.

Cette approche est idéale lorsque vous souhaitez extraire un seul tableau, bloc de rapport ou zone de données d'une feuille de calcul plus grande tout en supprimant tout contenu non lié. Elle est également utile pour exporter des régions sélectionnées par l'utilisateur d'une feuille en tant que fichiers autonomes.

### **Étapes**

Les étapes suivantes décrivent comment fractionner un fichier Excel en copiant une plage spécifique dans un nouveau classeur :

1. Ouvrez le fichier Excel source en instanciant un objet `Workbook` avec le chemin du fichier.
2. Récupérez la `Worksheet` cible qui contient la plage que vous souhaitez copier, soit par index (par exemple, la première feuille), soit par nom dans la collection `worksheets`.
3. Identifiez la plage à copier. Il peut s'agir d'une plage de cellules codée en dur telle que `A1:C10`, ou d'une plage nommée obtenue via la collection `Worksheet.cells`, ou d'une plage créée via `Worksheet.cells.create_range`.
4. Créez une nouvelle instance de `Workbook` de destination.
5. Accédez à la première `Worksheet` du classeur de destination (la feuille par défaut).
6. Copiez la plage source dans la feuille de calcul de destination, généralement à partir de la cellule `A1`. La méthode `Cells.copy` sur la collection `Cells` de destination peut être utilisée pour copier une plage entière, ou vous pouvez itérer à travers les cellules de la plage source et écrire leurs valeurs dans les cellules de destination avec `put_value`. Des `CopyOptions` facultatives peuvent être fournies pour contrôler ce qui est transféré (valeurs uniquement, valeurs et styles, formules, etc.).
7. Enregistrez le classeur de destination dans un nouveau chemin de fichier sur le disque à l'aide de la méthode `Workbook.save`.

### **Exemple de code**

```python
import aspose.cells as ac
import os

# Définir le répertoire de données et les chemins de fichiers
dataDir = "data/"
sourcePath = os.path.join(dataDir, "book1.xls")
outputPath = os.path.join(dataDir, "outputrange.xls")

# Ouvrir le fichier Excel source
sourceWorkbook = ac.Workbook(sourcePath)

# Obtenir la première feuille de calcul du classeur source
sourceWorksheet = sourceWorkbook.worksheets[0]

# Définir la plage de cellules source A1:C10 (10 lignes, 3 colonnes commençant à la ligne 0, colonne 0)
sourceRange = sourceWorksheet.cells.create_range(0, 0, 10, 3)

# Créer un nouveau classeur de destination
destWorkbook = ac.Workbook()

# Accéder à la première feuille de calcul du classeur de destination
destWorksheet = destWorkbook.worksheets[0]

# Créer la plage de destination à A1 avec les mêmes dimensions que la plage source
destRange = destWorksheet.cells.create_range(0, 0, 10, 3)

# Copier la plage source vers la plage de destination
destRange.copy(sourceRange)

# Enregistrer le classeur de destination dans un nouveau fichier .xls
destWorkbook.save(outputPath, ac.SaveFormat.EXCEL97_TO2003)
```

Le résultat attendu est un seul nouveau fichier dans le répertoire de données qui contient uniquement les valeurs (et éventuellement la mise en forme) de la plage spécifiée extraite du classeur source. Le fichier de destination n'a aucune relation avec d'autres données du fichier source ; il contient uniquement la plage extraite, en commençant à la cellule `A1` de sa première feuille de calcul.

## **Articles connexes**

- [Copier des lignes et des colonnes](/cells/fr/python-net/copying-rows-and-columns/)
- [Fusionner et dissocier des cellules](/cells/fr/python-net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="python" >}}