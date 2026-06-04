---
title: Fractionner des fichiers Excel en plusieurs fichiers
description: Aspose.Cells est une bibliothèque Java pour travailler avec des fichiers de tableur, qui prend en charge le fractionnement d'un fichier Excel unique en plusieurs fichiers. Cet article explique comment fractionner des fichiers Excel en copiant chaque feuille de calcul dans un classeur séparé et en copiant des plages de cellules spécifiques dans d'autres classeurs.
keywords: Aspose.Cells, bibliothèque Java, tableur, fractionner fichier Excel, copier feuille de calcul, copier plage, plusieurs classeurs, enregistrer en fichiers séparés
type: docs
weight: 195
url: /fr/java/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge le fractionnement d'un fichier Excel unique en plusieurs fichiers. Il existe deux principales méthodes pour y parvenir : (1) en copiant chaque feuille de calcul du classeur source dans un nouveau classeur et en enregistrant chacune d'elles dans un fichier séparé, et (2) en copiant une plage de cellules spécifique d'une feuille de calcul dans un nouveau classeur. Les deux approches sont utiles lorsque vous devez distribuer des sous-ensembles de données, créer des rapports plus petits pour différents destinataires, ou isoler des données pour un traitement individuel.

{{% /alert %}}

## **Introduction**

Il existe de nombreux scénarios concrets dans lesquels un développeur doit diviser un fichier Excel unique en plusieurs fichiers plus petits. Par exemple, un classeur peut contenir une feuille de calcul par département, et chaque chef de département ne doit recevoir que sa propre feuille. Dans d'autres cas, vous pouvez vouloir extraire un tableau particulier ou un bloc de données d'une feuille de calcul et l'envoyer en tant que fichier autonome par e-mail, sans exposer le reste du classeur. Les grands classeurs consolidés peuvent également devoir être fractionnés en éléments plus petits pour faciliter leur manipulation, accélérer le chargement, ou pour un traitement en aval par d'autres systèmes.

Aspose.Cells propose deux approches flexibles pour cette tâche. La première approche parcourt chaque feuille de calcul du classeur source et copie son contenu dans une nouvelle instance de `Workbook`, en enregistrant chacune d'elles en tant que fichier séparé. La seconde approche se concentre sur une plage de cellules spécifique dans une feuille de calcul et copie uniquement cette plage dans un nouveau classeur. Dans les deux cas, le flux général est le même : charger le classeur source à l'aide de la classe `Workbook`, accéder aux données pertinentes via les objets `Worksheet` et `Cells`, transférer le contenu vers un `Workbook` de destination, puis enregistrer la destination sur le disque.

## **Fractionner un fichier Excel en copiant chaque feuille de calcul dans un nouveau classeur**

### **Aperçu de l'approche**

Dans cette approche, le classeur source est ouvert une seule fois, puis pour chaque `Worksheet` de sa collection `Worksheets`, un nouveau `Workbook` de destination est créé. Le contenu de la feuille de calcul source est ensuite copié dans la première feuille de calcul du classeur de destination, et le classeur de destination est enregistré en tant que fichier dont le nom est dérivé du nom de la feuille de calcul source. Le résultat est un fichier de sortie par feuille de calcul, chaque fichier de sortie contenant les données d'une seule feuille source.

Cette méthode est le bon choix lorsque chaque feuille de calcul de votre classeur source représente une unité d'information logiquement indépendante (comme un département, une région, un mois ou une ligne de produits) et que vous souhaitez livrer ou traiter chaque unité individuellement.

### **Étapes**

Les étapes suivantes décrivent comment fractionner un fichier Excel en copiant chaque feuille de calcul dans un nouveau classeur :

1. Ouvrez le fichier Excel source en instanciant un objet `Workbook` et en passant le chemin du fichier à son constructeur.
2. Parcourez la collection `Workbook.Worksheets` à l'aide d'une boucle `for` ou `foreach` afin que chaque `Worksheet` du fichier source soit traité.
3. À l'intérieur de la boucle, créez une nouvelle instance de `Workbook` de destination (un classeur vide) pour la feuille de calcul en cours.
4. Ajoutez une nouvelle `Worksheet` au classeur de destination (ou utilisez la première feuille de calcul par défaut) et attribuez-lui un nom significatif, idéalement le même que la propriété `Name` de la feuille de calcul source.
5. Copiez le contenu de la feuille de calcul source dans la feuille de calcul de destination. Cela peut être fait en parcourant les cellules de la collection `Cells` de la feuille de calcul source et en écrivant leurs valeurs dans les cellules correspondantes de la feuille de calcul de destination, ou en utilisant la méthode `Cells.copy` pour transférer une plage entière en une seule fois.
6. Construisez un chemin de fichier de sortie qui intègre le nom de la feuille de calcul source (par exemple, `dataDir + worksheet.getName() + ".xls"`) afin que chaque fichier généré ait un nom unique.
7. Appelez la méthode `Workbook.save` de destination pour écrire le fichier sur le disque.
8. Répétez les étapes 3 à 7 pour la feuille de calcul suivante jusqu'à ce que toutes les feuilles de calcul aient été traitées.

### **Exemple de code**

```java
import com.aspose.cells.*;

String dataDir = "data/";
Workbook workbook = new Workbook(dataDir + "book1.xls");

for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet sourceSheet = workbook.getWorksheets().get(i);
    String sheetName = sourceSheet.getName();
    
    Workbook destWorkbook = new Workbook();
    int destIndex = destWorkbook.getWorksheets().add();
    Worksheet destSheet = destWorkbook.getWorksheets().get(destIndex);
    destSheet.setName(sheetName);
    
    destSheet.copy(sourceSheet);
    
    String destFile = dataDir + sheetName + ".xls";
    destWorkbook.save(destFile, SaveFormat.EXCEL_97_TO_2003);
}
```

Le résultat attendu est un ensemble de nouveaux fichiers dans le répertoire de données, un fichier par feuille de calcul du classeur source. Chaque fichier est nommé d'après sa feuille source correspondante, et le fichier contient les données (et éventuellement la mise en forme) de cette feuille unique.

## **Fractionner un fichier Excel en copiant une plage dans un nouveau classeur**

### **Aperçu de l'approche**

Parfois, les données que vous devez fractionner ne correspondent pas à une feuille de calcul entière, mais plutôt à une région rectangulaire spécifique d'une feuille de calcul, telle que `A1:D10` ou une plage nommée qui représente un tableau particulier. Dans ces cas, la copie de feuilles de calcul entières est inutile, et une approche plus précise est nécessaire : identifier la plage source, copier uniquement cette plage dans un nouveau classeur, et enregistrer le nouveau fichier.

Cette approche est idéale lorsque vous souhaitez extraire un seul tableau, bloc de rapport ou zone de données d'une feuille de calcul plus grande tout en supprimant tout contenu non lié. Elle est également utile pour exporter des régions sélectionnées par l'utilisateur d'une feuille en tant que fichiers autonomes.

### **Étapes**

Les étapes suivantes décrivent comment fractionner un fichier Excel en copiant une plage spécifique dans un nouveau classeur :

1. Ouvrez le fichier Excel source en instanciant un objet `Workbook` avec le chemin du fichier.
2. Récupérez la `Worksheet` cible qui contient la plage que vous souhaitez copier, soit par index (par exemple, la première feuille), soit par nom dans la collection `Worksheets`.
3. Identifiez la plage à copier. Il peut s'agir d'une plage de cellules codée en dur telle que `A1:C10`, ou d'une plage nommée obtenue via la collection `Worksheet.Cells`, ou d'une plage créée via `Worksheet.Cells.createRange`.
4. Créez une nouvelle instance de `Workbook` de destination.
5. Accédez à la première `Worksheet` du classeur de destination (la feuille par défaut).
6. Copiez la plage source dans la feuille de calcul de destination, généralement en commençant par la cellule `A1`. La méthode `Cells.copy` sur la collection `Cells` de destination peut être utilisée pour copier une plage entière, ou vous pouvez parcourir les cellules de la plage source et écrire leurs valeurs dans les cellules de destination avec `putValue`. Des `CopyOptions` optionnelles peuvent être fournies pour contrôler ce qui est transféré (valeurs uniquement, valeurs et styles, formules, etc.).
7. Enregistrez le classeur de destination dans un nouveau chemin de fichier sur le disque à l'aide de la méthode `Workbook.save`.

### **Exemple de code**

```java
import com.aspose.cells.*;

// Définir le répertoire de données et les chemins de fichiers
String dataDir = "data/";
String sourcePath = dataDir + "book1.xls";
String outputPath = dataDir + "outputrange.xls";

// Ouvrir le fichier Excel source
Workbook sourceWorkbook = new Workbook(sourcePath);

// Obtenir la première feuille de calcul du classeur source
Worksheet sourceWorksheet = sourceWorkbook.getWorksheets().get(0);

// Définir la plage de cellules source A1:C10 (10 lignes, 3 colonnes commençant à la ligne 0, colonne 0)
Range sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3);

// Créer un nouveau classeur de destination
Workbook destWorkbook = new Workbook();

// Accéder à la première feuille de calcul du classeur de destination
Worksheet destWorksheet = destWorkbook.getWorksheets().get(0);

// Créer la plage de destination à A1 avec les mêmes dimensions que la plage source
Range destRange = destWorksheet.getCells().createRange(0, 0, 10, 3);

// Copier la plage source vers la plage de destination
destRange.copy(sourceRange);

// Enregistrer le classeur de destination dans un nouveau fichier .xls
destWorkbook.save(outputPath, SaveFormat.EXCEL_97_TO_2003);
```

Le résultat attendu est un seul nouveau fichier dans le répertoire de données qui contient uniquement les valeurs (et éventuellement la mise en forme) de la plage spécifiée extraite du classeur source. Le fichier de destination n'a aucune relation avec d'autres données du fichier source ; il contient uniquement la plage extraite, à partir de la cellule `A1` de sa première feuille de calcul.

## **Articles connexes**

- [Copier des lignes et des colonnes](/fr/cells/java/copying-rows-and-columns/)
- [Fusionner et annuler la fusion de cellules](/fr/cells/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}