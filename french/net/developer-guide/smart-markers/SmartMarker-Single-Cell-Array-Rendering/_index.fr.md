---
title: Rendu d'un tableau à cellule unique avec SmartMarker | Aspose.Cells .NET
linktitle: Rendu d'un tableau à cellule unique avec SmartMarker | Aspose.Cells .NET
description: Apprenez à rendre des données de tableau dans une seule cellule à l'aide des attributs ArrayAsSingle et ExtraDelimiter dans les Smart Markers avec Aspose.Cells for .NET.
keywords: Aspose.Cells, bibliothèque .NET, tableur, marqueurs intelligents, ArrayAsSingle, ExtraDelimiter, tableau à cellule unique, rendu de tableau, modèle
type: docs
weight: 195
url: /fr/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge le rendu de données de tableau dans une seule cellule au moyen de Smart Markers. En utilisant l'attribut `ArrayAsSingle` avec l'attribut `ExtraDelimiter`, les développeurs peuvent contrôler la manière dont les éléments du tableau sont séparés dans une seule cellule, ce qui offre une mise en forme souple pour les rapports et les modèles.
{{% /alert %}}

## **Introduction**
Les Smart Markers d'Aspose.Cells sont une fonctionnalité puissante fondée sur des modèles qui permet de remplir dynamiquement des données de tableur à l'aide d'expressions de marqueur telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur de conception et, lorsque le modèle est traité par `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs de la source de données fournie.
Par défaut, lorsqu'un Smart Marker référence une propriété de tableau, par exemple `&=DataSource.Numbers`, le moteur développe le tableau et place chaque élément dans une cellule adjacente distincte — soit horizontalement sur une ligne, soit verticalement dans une colonne. Bien que ce comportement soit pratique dans de nombreux scénarios, il existe des situations où vous préférez rendre le tableau entier dans une seule cellule, avec les éléments concaténés et séparés par un délimiteur de votre choix.
Les attributs `ArrayAsSingle` et `ExtraDelimiter`, utilisés ensemble dans une balise Smart Marker, répondent précisément à ce besoin. Ils permettent de conserver des mises en page de rapport compactes et prévisibles tout en travaillant nativement avec des sources de données de type tableau.

## **Pourquoi cette fonctionnalité est nécessaire**

### **Comportement par défaut de répartition du tableau**
Lorsqu'un Smart Marker référence une propriété de tableau, Aspose.Cells répartit par défaut les éléments du tableau dans plusieurs cellules. Par exemple, un marqueur tel que `&=Product.Tags` associé à un `string[]` contenant quatre valeurs place chaque valeur dans sa propre cellule, ce qui repousse le reste du contenu du modèle et peut compromettre des mises en page de rapport soigneusement conçues.

### **Limites des cas d'utilisation**
Il existe de nombreux scénarios pratiques dans lesquels le comportement de répartition par défaut n'est pas souhaitable :
- **Rapports de synthèse** nécessitant une disposition compacte avec une ligne par enregistrement.
- **Listes de tags, d'étiquettes ou de mots-clés** devant être affichées sous forme de valeurs séparées par des virgules ou des barres verticales dans une seule cellule.
- **Pastilles de filtre ou indicateurs d'état** regroupant plusieurs valeurs en un seul endroit pour améliorer la lisibilité.
- **Flux en aval** (export CSV, rendu PDF, fusion de courrier) qui attendent une valeur consolidée par cellule plutôt qu'une plage développée.
- **Compatibilité entre plateformes**, où certains consommateurs ne peuvent pas tolérer des tableaux qui se répandent sur plusieurs cellules.

### **La lacune qu'elle comble**
En l'absence de mécanisme intégré, les développeurs seraient forcés de prétraiter les données en C# ou VB.NET — en convertissant les tableaux en chaînes délimitées avant de les lier au `WorkbookDesigner`. Cette approche duplique la logique, complique les modèles de données et augmente les risques d'erreur. Les attributs `ArrayAsSingle` et `ExtraDelimiter` éliminent cette solution de contournement en gérant la mise en forme de manière déclarative dans la balise Smart Marker elle-même.

## **Avantages de la fonctionnalité**
L'utilisation des attributs `ArrayAsSingle` et `ExtraDelimiter` dans vos Smart Markers offre plusieurs avantages :
- **Confinement dans une seule cellule** : Tous les éléments du tableau sont rendus dans une seule et même cellule, ce qui maintient des mises en page compactes et prévisibles.
- **Contrôle du délimiteur** : Spécifiez la chaîne de séparation de votre choix — virgule, point-virgule, trait d'union, barre verticale, saut de ligne ou tout texte personnalisé.
- **Mise en forme pilotée par le modèle** : Aucun code supplémentaire n'est nécessaire pour prétraiter les données ; les règles de mise en forme sont définies dans la balise Smart Marker.
- **Rapports plus propres** : Les données de tableau ne repoussent plus le contenu voisin du modèle vers d'autres lignes ou colonnes.
- **Types de données polyvalents** : Fonctionne avec les chaînes, les nombres, les dates et tout autre type de données pouvant être associé à l'aide d'un délimiteur.
- **Compatibilité ascendante** : Lorsque ces attributs sont omis, le comportement de répartition d'origine est préservé, de sorte que les modèles existants continuent de fonctionner sans aucune modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe du Smart Marker**
Les attributs `ArrayAsSingle` et `ExtraDelimiter` sont transmis sous forme de paires clé-valeur dans les parenthèses d'un Smart Marker standard. La syntaxe générale est la suivante :

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Le marqueur est composé des éléments suivants :
- `&=DataSource.ArrayProperty` — le marqueur Smart Marker standard qui référence la propriété de tableau de la source de données liée.
- `arrayasSingle=true` — indique au moteur de rendre le tableau entier dans une seule cellule. Seule la valeur `true` déclenche le comportement de cellule unique.
- `extraDelimiter=", "` — définit le séparateur placé entre les éléments du tableau. La valeur est un littéral de chaîne ; elle peut être vide, comporter un seul caractère ou contenir plusieurs caractères.

{{% alert color="primary" %}}
L'attribut `extraDelimiter` accepte n'importe quel littéral de chaîne, y compris des délimiteurs de plusieurs caractères, du texte personnalisé ou des séquences d'échappement, telles que `\n` pour obtenir une sortie séparée par des sauts de ligne. Si le tableau est vide, la cellule obtenue reste vide.
{{% /alert %}}

### **Procédure étape par étape**
La procédure suivante décrit comment rendre un tableau dans une seule cellule à l'aide de Smart Markers.
1. **Préparer la source de données** : Créez une classe ou une structure de données qui expose une propriété renvoyant un tableau. La propriété peut renvoyer `string[]`, `int[]` ou tout autre type de tableau pris en charge.
2. **Créer un classeur de conception** : Créez un nouvel objet `Workbook`, ajoutez une ligne d'en-tête et placez dans une cellule un Smart Marker qui référence la propriété de tableau et comporte les attributs `arrayasSingle` et `extraDelimiter`.
3. **Instancier le WorkbookDesigner** : Créez un objet `WorkbookDesigner`, attribuez-lui le classeur de conception et liez votre source de données à l'aide de la méthode `SetDataSource`.
4. **Traiter les marqueurs** : Appelez la méthode `WorkbookDesigner.Process()` pour développer les Smart Markers et remplir le classeur avec les données réelles.
5. **Enregistrer le résultat** : Enregistrez le classeur obtenu sur le disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu d'un tableau de chaînes de base**

```csharp
using System;
using Aspose.Cells;
class Program
{
    public class Product
    {
        public string[] Tags { get; set; }
    }
    public static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Tags");
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");
        WorkbookDesigner designer = new WorkbookDesigner();
        designer.Workbook = workbook;
        designer.SetDataSource("Product", product);
        designer.Process();
        workbook.Save("output_arraySingle.xlsx");
    }
}
```

### **Exemple de code 2 — Tableau numérique avec délimiteur personnalisé**

```csharp
public class Student
{
    public int[] Scores { get; set; }
}
public class Program
{
    public static void Main()
    {
        var student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        var workbook = new Workbook();
        var worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        worksheet.Cells["A2"].PutValue(string.Join(" - ", student.Scores));
        workbook.Save("output_numericArray.xlsx");
    }
}
```

### **Exemple de code 3 — Comparaison du comportement par défaut et du comportement ArrayAsSingle**

```csharp
using System;
using Aspose.Cells;
public class Program
{
    public static void Main()
    {
        var order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };
        var workbook = new Workbook();
        var sheet = workbook.Worksheets[0];
        var cells = sheet.Cells;
        // Section 1 : Marqueur intelligent par défaut - valeurs réparties horizontalement dans les cellules
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");
        // Section 2 : Nouveau rendu dans une seule cellule à l'aide de arrayasSingle et extraDelimiter
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");
        // Lier la source de données et traiter les marqueurs intelligents
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();
        // Enregistrer le classeur obtenu
        workbook.Save("output_comparison.xlsx");
    }
}
public class Order
{
    public string[] Items { get; set; }
}
```

### **Notes et bonnes pratiques**
Gardez les points suivants à l'esprit lorsque vous utilisez les attributs `ArrayAsSingle` et `ExtraDelimiter` :
- La valeur `extraDelimiter` est traitée comme un littéral de chaîne ; échappez tout caractère spécial susceptible d'être interprété par le processeur de votre modèle.
- L'attribut `arrayasSingle` accepte une valeur booléenne (`true` / `false`). Seule la valeur `true` déclenche le comportement de cellule unique ; toute autre valeur rétablit le comportement de répartition par défaut.
- Si le tableau est vide ou nul, la cellule reste vide ou contient une chaîne vide, selon le type de données.
- La fonctionnalité fonctionne avec des sources de données orientées objet, ainsi qu'avec des sources `DataSet` et `DataTable` dans lesquelles une colonne peut être divisée en tableaux.
- Pour obtenir une sortie séparée par des sauts de ligne, vous pouvez utiliser `\n` ou `Environment.NewLine` comme valeur de délimiteur.

## Articles connexes

{{< app/cells/assistant language="csharp" >}}