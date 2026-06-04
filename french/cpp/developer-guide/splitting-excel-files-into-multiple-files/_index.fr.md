---
title: Fractionner des fichiers Excel en plusieurs fichiers
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de tableurs, qui prend en charge le fractionnement d'un seul fichier Excel en plusieurs fichiers. Cet article explique comment fractionner des fichiers Excel en copiant chaque feuille de calcul dans un classeur séparé et en copiant des plages de cellules spécifiques dans d'autres classeurs.
keywords: Aspose.Cells, bibliothèque C++, tableur, fractionner un fichier Excel, copier une feuille de calcul, copier une plage, plusieurs classeurs, enregistrer en tant que fichiers séparés
type: docs
weight: 195
url: /fr/cpp/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge le fractionnement d'un seul fichier Excel en plusieurs fichiers. Il existe deux principales méthodes pour y parvenir : (1) copier chaque feuille de calcul du classeur source dans un nouveau classeur et enregistrer chacun d'eux comme un fichier séparé, et (2) copier une plage de cellules spécifique d'une feuille de calcul dans un nouveau classeur. Les deux approches sont utiles lorsque vous devez distribuer des sous-ensembles de données, créer des rapports plus petits pour différents destinataires ou isoler des données pour un traitement individuel.

{{% /alert %}}

## **Introduction**

Il existe de nombreux scénarios concrets dans lesquels un développeur doit diviser un seul fichier Excel en plusieurs fichiers plus petits. Par exemple, un classeur peut contenir une feuille de calcul par département, et chaque responsable de département doit recevoir uniquement sa propre feuille. Dans d'autres cas, vous pouvez souhaiter extraire un tableau particulier ou un bloc de données d'une feuille de calcul et l'envoyer comme fichier autonome par e-mail, sans exposer le reste du classeur. Les grands classeurs consolidés peuvent également devoir être divisés en morceaux plus petits pour faciliter leur manipulation, accélérer le chargement ou permettre un traitement en aval par d'autres systèmes.

Aspose.Cells propose deux approches flexibles pour cette tâche. La première approche parcourt chaque feuille de calcul du classeur source et copie son contenu dans une toute nouvelle instance de `Workbook`, en enregistrant chacune d'elles comme un fichier séparé. La deuxième approche se concentre sur une plage de cellules spécifique dans une feuille de calcul et copie uniquement cette plage dans un nouveau classeur. Dans les deux cas, le flux général est le même : charger le classeur source à l'aide de la classe `Workbook`, accéder aux données pertinentes via les objets `Worksheet` et `Cells`, transférer le contenu vers un `Workbook` de destination, puis enregistrer la destination sur le disque.

## **Fractionner un fichier Excel en copiant chaque feuille de calcul dans un nouveau classeur**

### **Aperçu de l'approche**

Dans cette approche, le classeur source est ouvert une seule fois, puis pour chaque `Worksheet` dans sa collection `Worksheets`, un nouveau `Workbook` de destination est créé. Le contenu de la feuille de calcul source est ensuite copié dans la première feuille de calcul du classeur de destination, et le classeur de destination est enregistré comme un fichier dont le nom est dérivé du nom de la feuille de calcul source. Le résultat est un fichier de sortie par feuille de calcul, chaque fichier de sortie contenant les données d'une seule feuille source.

Cette méthode est le bon choix lorsque chaque feuille de calcul de votre classeur source représente une unité d'information logiquement indépendante (comme un département, une région, un mois ou une ligne de produits) et que vous souhaitez livrer ou traiter chaque unité individuellement.

### **Étapes**

Les étapes suivantes décrivent comment fractionner un fichier Excel en copiant chaque feuille de calcul dans un nouveau classeur :

1. Ouvrez le fichier Excel source en instanciant un objet `Workbook` et en passant le chemin du fichier à son constructeur.
2. Parcourez la collection `Workbook.Worksheets` à l'aide d'une boucle `for` ou `foreach` afin que chaque `Worksheet` du fichier source soit traité.
3. À l'intérieur de la boucle, créez une nouvelle instance de `Workbook` de destination (un classeur vide) pour la feuille de calcul en cours.
4. Ajoutez une nouvelle `Worksheet` au classeur de destination (ou utilisez la première feuille de calcul par défaut) et attribuez-lui un nom significatif, idéalement identique à la propriété `Name` de la feuille de calcul source.
5. Copiez le contenu de la feuille de calcul source dans la feuille de calcul de destination. Cela peut être fait en parcourant les cellules de la collection `Cells` de la feuille de calcul source et en écrivant leurs valeurs dans les cellules correspondantes de la feuille de calcul de destination, ou en utilisant la méthode `Cells.Copy` pour transférer une plage entière en une seule fois.
6. Construisez un chemin de fichier de sortie qui intègre le nom de la feuille de calcul source (par exemple, `dataDir + worksheet.Name + ".xls"`) afin que chaque fichier généré ait un nom unique.
7. Appelez la méthode `Workbook.Save` du classeur de destination pour écrire le fichier sur le disque.
8. Répétez les étapes 3 à 7 pour la feuille de calcul suivante jusqu'à ce que toutes les feuilles de calcul aient été traitées.

### **Exemple de code**

```cpp
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "data/";
    Workbook wb(U16String((dataDir + "book1.xls").c_str()));

    int sheetCount = wb.GetWorksheets().GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet sourceSheet = wb.GetWorksheets().Get(i);
        U16String sheetName = sourceSheet.GetName();

        Workbook destWorkbook;
        int destIndex = destWorkbook.GetWorksheets().Add();
        Worksheet destSheet = destWorkbook.GetWorksheets().Get(destIndex);
        destSheet.SetName(sheetName);

        destSheet.Copy(sourceSheet);

        std::string destFile = dataDir + sheetName.ToUtf8() + ".xls";
        destWorkbook.Save(U16String(destFile.c_str()), SaveFormat::Excel97To2003);
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Le résultat attendu est un ensemble de nouveaux fichiers dans le répertoire de données, un fichier par feuille de calcul du classeur source. Chaque fichier est nommé d'après sa feuille source correspondante, et le fichier contient les données (et éventuellement la mise en forme) de cette seule feuille.

## **Fractionner un fichier Excel en copiant une plage dans un nouveau classeur**

### **Aperçu de l'approche**

Parfois, les données que vous devez fractionner ne correspondent pas à une feuille de calcul entière, mais plutôt à une région rectangulaire spécifique d'une feuille de calcul, telle que `A1:D10` ou une plage nommée qui représente un tableau particulier. Dans ces cas, copier des feuilles de calcul entières est inutile, et une approche plus précise est requise : identifier la plage source, copier uniquement cette plage dans un nouveau classeur, et enregistrer le nouveau fichier.

Cette approche est idéale lorsque vous souhaitez extraire un seul tableau, bloc de rapport ou zone de données d'une feuille de calcul plus grande tout en éliminant tout contenu non lié. Elle est également utile pour exporter des régions sélectionnées par l'utilisateur d'une feuille comme fichiers autonomes.

### **Étapes**

Les étapes suivantes décrivent comment fractionner un fichier Excel en copiant une plage spécifique dans un nouveau classeur :

1. Ouvrez le fichier Excel source en instanciant un objet `Workbook` avec le chemin du fichier.
2. Récupérez la `Worksheet` cible qui contient la plage que vous souhaitez copier, soit par index (par exemple, la première feuille), soit par nom à partir de la collection `Worksheets`.
3. Identifiez la plage à copier. Il peut s'agir d'une plage de cellules codée en dur telle que `A1:C10`, ou d'une plage nommée obtenue via la collection `Worksheet.Cells`, ou d'une plage créée via `Worksheet.Cells.CreateRange`.
4. Créez une nouvelle instance de `Workbook` de destination.
5. Accédez à la première `Worksheet` du classeur de destination (la feuille par défaut).
6. Copiez la plage source dans la feuille de calcul de destination, généralement à partir de la cellule `A1`. La méthode `Cells.Copy` de la collection `Cells` de destination peut être utilisée pour copier une plage entière, ou vous pouvez parcourir les cellules de la plage source et écrire leurs valeurs dans les cellules de destination avec `PutValue`. Des `CopyOptions` facultatives peuvent être fournies pour contrôler ce qui est transféré (valeurs uniquement, valeurs et styles, formules, etc.).
7. Enregistrez le classeur de destination dans un nouveau chemin de fichier sur le disque à l'aide de la méthode `Workbook.Save`.

### **Exemple de code**

```cpp
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Définir le répertoire de données et les chemins de fichiers
    std::string dataDir = "data/";
    std::string sourcePath = dataDir + "book1.xls";
    std::string outputPath = dataDir + "outputrange.xls";

    // Ouvrir le fichier Excel source
    Workbook sourceWorkbook(U16String(sourcePath.c_str()));

    // Obtenir la première feuille de calcul du classeur source
    Worksheet sourceWorksheet = sourceWorkbook.GetWorksheets().Get(0);

    // Définir la plage de cellules source A1:C10 (10 lignes, 3 colonnes commençant à la ligne 0, colonne 0)
    Range sourceRange = sourceWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // Créer un nouveau classeur de destination
    Workbook destWorkbook;

    // Accéder à la première feuille de calcul du classeur de destination
    Worksheet destWorksheet = destWorkbook.GetWorksheets().Get(0);

    // Créer la plage de destination à A1 avec les mêmes dimensions que la plage source
    Range destRange = destWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // Copier la plage source vers la plage de destination
    destRange.Copy(sourceRange);

    // Enregistrer le classeur de destination dans un nouveau fichier .xls
    destWorkbook.Save(U16String(outputPath.c_str()), SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Le résultat attendu est un seul nouveau fichier dans le répertoire de données qui contient uniquement les valeurs (et éventuellement la mise en forme) de la plage spécifiée extraite du classeur source. Le fichier de destination n'a aucune relation avec d'autres données du fichier source ; il contient uniquement la plage extraite, commençant à la cellule `A1` de sa première feuille de calcul.

## **Articles connexes**

- [Copier des lignes et des colonnes](/cells/fr/cpp/copying-rows-and-columns/)
- [Fusionner et défusionner des cellules](/cells/fr/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}