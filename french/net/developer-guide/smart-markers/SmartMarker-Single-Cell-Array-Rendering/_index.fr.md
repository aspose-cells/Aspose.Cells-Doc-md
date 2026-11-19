---
title: Rendu d’un tableau dans une seule cellule avec SmartMarker | Aspose.Cells .NET
linktitle: Rendu d’un tableau dans une seule cellule avec SmartMarker | Aspose.Cells .NET
description: Découvrez comment effectuer le rendu des données d’une source de type tableau dans une seule cellule à l’aide des attributs Smart Marker arrayassingle et arraydelimiter dans Aspose.Cells for .NET.
keywords: Aspose.Cells, bibliothèque .NET, tableur, Smart Markers, arrayassingle, arraydelimiter, tableau dans une seule cellule, rendu de tableau, modèle
type: docs
weight: 195
url: /fr/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells peut effectuer le rendu des données d’une source de type tableau dans une seule cellule à l’aide des Smart Markers. L’attribut `arrayassingle` désactive la répartition par défaut des éléments dans des cellules distinctes, et l’attribut `arraydelimiter` définit le séparateur placé entre les éléments concaténés : par défaut, une virgule ; ou tout caractère unique ou toute chaîne de plusieurs caractères entre guillemets que vous spécifiez.
{{% /alert %}}

## **Introduction**

Les Smart Markers d’Aspose.Cells sont une fonctionnalité fondée sur les modèles qui peuple dynamiquement les données de tableur au moyen d’expressions de marqueur telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur de conception et, lorsque le modèle est traité par le `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs de la source de données fournie.
Par défaut, lorsqu’un Smart Marker référence une propriété de type tableau (par exemple, `&=Product.Tags` liée à un `string[]` de quatre valeurs), le moteur étend le tableau et place chaque élément dans une cellule distincte, en répartissant les valeurs verticalement dans la colonne située sous le marqueur. Bien que ce comportement soit pratique dans de nombreux scénarios, dans certaines situations, vous préféreriez effectuer le rendu du tableau entier dans une seule cellule, avec les éléments concaténés et séparés par le séparateur de votre choix.
Les attributs `arrayassingle` et `arraydelimiter`, écrits dans les parenthèses d’un Smart Marker sous la forme `name:value`, répondent précisément à ce besoin. Ils permettent de conserver des mises en page de rapports compactes et prévisibles tout en travaillant nativement avec des sources de données de type tableau.

## **Pourquoi cette fonctionnalité est nécessaire**

### **Comportement par défaut de répartition des tableaux**

Lorsqu’un Smart Marker référence une propriété de type tableau, Aspose.Cells répartit par défaut le tableau sur plusieurs cellules. Par exemple, un marqueur tel que `&=Product.Tags` associé à un `string[]` contenant quatre valeurs place chaque valeur dans une cellule distincte sous le marqueur, ce qui repousse les autres éléments du modèle et peut compromettre des mises en page de rapports soigneusement conçues.

### **Limites des cas d’utilisation**

Il existe de nombreux scénarios pratiques dans lesquels le comportement de répartition par défaut n’est pas souhaitable :
- **Rapports de synthèse** qui nécessitent une disposition compacte avec une ligne par enregistrement.
- **Listes de balises, d’étiquettes ou de mots-clés** qui doivent être affichées sous forme de valeurs séparées par des virgules ou des barres verticales dans une seule cellule.
- **Pastilles de filtre ou indicateurs d’état** qui regroupent plusieurs valeurs au même endroit afin d’améliorer la lisibilité.
- **Chaînes de traitement en aval** (exportation CSV, rendu PDF, publipostage) qui attendent une valeur consolidée unique par cellule plutôt qu’une plage étendue.
- **Compatibilité multiplateforme**, où certains consommateurs ne tolèrent pas les tableaux qui débordent sur plusieurs cellules.

### **La lacune comblée**

Sans mécanisme intégré, les développeurs seraient contraints de prétraiter les données en C# ou VB.NET — en concaténant les tableaux en chaînes délimitées avant de les lier au `WorkbookDesigner`. Cette logique dupliquée complexifie les modèles de données et augmente les risques d’erreur. Les attributs `arrayassingle` et `arraydelimiter` éliminent ce contournement en gérant la mise en forme de manière déclarative à l’intérieur du Smart Marker lui-même.

## **Avantages de la fonctionnalité**

L’utilisation des attributs `arrayassingle` et `arraydelimiter` dans les Smart Markers offre plusieurs avantages :
- **Regroupement dans une seule cellule** : Tous les éléments du tableau sont rendus dans une cellule unique, ce qui préserve la compacité et la prévisibilité des mises en page.
- **Contrôle personnalisé du séparateur** : Spécifiez le séparateur de votre choix — une virgule par défaut, un point-virgule, un trait d’union, une barre verticale ou une chaîne de plusieurs caractères entre guillemets, telle que `" | "`.
- **Mise en forme pilotée par le modèle** : Aucun code supplémentaire n’est nécessaire pour prétraiter les données ; les règles de mise en forme sont définies dans le marqueur Smart Marker.
- **Rapports plus propres** : Les données de type tableau ne repoussent plus le contenu voisin du modèle vers d’autres lignes ou colonnes.
- **Prise en charge de plusieurs types de données** : La fonctionnalité fonctionne avec des tableaux de chaînes et des tableaux numériques issus de sources de données constituées d’objets.
- **Rétrocompatibilité** : Lorsque les attributs sont omis, le comportement de répartition d’origine est conservé, de sorte que les modèles existants continuent de fonctionner sans modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe des Smart Markers**

Les attributs `arrayassingle` et `arraydelimiter` utilisent la syntaxe d’attributs `name:value` d’Aspose.Cells dans les parenthèses d’un Smart Marker standard. La syntaxe générale est :

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

Le marqueur est composé des éléments suivants :
- `&=DataSource.ArrayProperty` — le Smart Marker standard qui référence la propriété de tableau de la source de données liée.
- `arrayassingle:true` — indique au moteur d’effectuer le rendu de l’ensemble du tableau dans une seule cellule au lieu de répartir ses éléments.
- `arraydelimiter:;` — facultatif ; définit le séparateur placé entre les éléments du tableau. Lorsqu’il est omis, une virgule est utilisée.

{{% alert color="warning" %}}
Écrivez les attributs sous la forme `name:value` (avec un deux-points, pas un signe égal) et séparez plusieurs attributs par une virgule **sans espaces**. Un espace après la virgule décale la valeur analysée d’un caractère — `(arrayassingle:true, arraydelimiter:;)` joindrait les éléments à l’aide du séparateur erroné `:;` au lieu de `;`.
{{% /alert %}}

### **Formes du séparateur**

- Un caractère unique est placé directement après le deux-points : `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Un séparateur de plusieurs caractères est écrit entre guillemets doubles : `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Flux de travail étape par étape**

Le flux de travail suivant explique comment effectuer le rendu d’un tableau dans une seule cellule à l’aide des Smart Markers.
1. **Préparer la source de données** : Créez une classe qui expose une propriété qui renvoie un tableau, par exemple `string[]` ou `int[]`, et associez cette classe à une `List<T>` afin que le moteur puisse lire un enregistrement par ligne.
2. **Créer le classeur de conception** : Créez un `Workbook`, ajoutez une ligne d’en-tête et placez un Smart Marker dans une cellule qui référence la propriété de tableau avec l’attribut `arrayassingle` (ainsi que `arraydelimiter` lorsqu’un séparateur personnalisé est nécessaire).
3. **Instancier le `WorkbookDesigner`** : Créez un `WorkbookDesigner` pour le classeur et liez votre source de données à l’aide de `SetDataSource`.
4. **Traiter les marqueurs** : Appelez la méthode `WorkbookDesigner.Process()` pour développer les Smart Markers et remplir le classeur avec les données réelles.
5. **Enregistrer le résultat** : Enregistrez le classeur obtenu sur le disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu simple d’un tableau de chaînes**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Product
    {
        public string[] Tags { get; set; }
    }

    static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Product", new List<Product> { product });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-single.xlsx");
    }
}
```

L’exemple affiche la valeur concaténée de l’ensemble du tableau. Les quatre balises sont placées dans une seule cellule et séparées par la virgule par défaut :

```
C#,Aspose,SmartMarker,Excel
```

### **Exemple de code 2 — Tableau numérique avec un séparateur personnalisé**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Student
    {
        public int[] Scores { get; set; }
    }

    static void Main()
    {
        Student student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        // arraydelimiter:- joins the numbers with a hyphen
        worksheet.Cells["A2"].PutValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Student", new List<Student> { student });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-numeric.xlsx");
    }
}
```

Les tableaux numériques sont concaténés exactement comme les tableaux de chaînes — chaque élément conserve son texte numérique brut :

```
95-88-76-100-67
```

### **Exemple de code 3 — Comparaison entre le rendu par défaut et le rendu dans une seule cellule**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Order
    {
        public string[] Items { get; set; }
    }

    static void Main()
    {
        Order order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        Cells cells = sheet.Cells;
        // Column B: default marker — values spread vertically down the column
        cells["B1"].PutValue("Default");
        cells["B2"].PutValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells["C1"].PutValue("Single cell");
        cells["C2"].PutValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", new List<Order> { order });
        designer.Process();
        for (int row = 1; row <= 5; row++)
        {
            string b = cells[row, 1].StringValue;
            string c = cells[row, 2].StringValue;
            if (!string.IsNullOrEmpty(b) || !string.IsNullOrEmpty(c))
                Console.WriteLine($"B{row + 1}=[{b}]  C{row + 1}=[{c}]");
        }
        workbook.Save("output-array-comparison.xlsx");
    }
}
```

Le marqueur par défaut remplit une cellule par élément dans la colonne B, tandis que le marqueur `arrayassingle` regroupe le même tableau dans une seule cellule de la colonne C :

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notes et bonnes pratiques**

Pour travailler avec les attributs `arrayassingle` et `arraydelimiter`, tenez compte des points suivants :
- Les valeurs des attributs utilisent la forme `name:value`. Une forme avec un signe égal, telle que `arrayassingle=true`, n’est pas reconnue ; le comportement de répartition par défaut est alors silencieusement rétabli.
- Séparez les attributs par une virgule, sans espace ; un espace après la virgule décale la valeur du séparateur d’un caractère (voir l’avertissement ci-dessus).
- La valeur de `arraydelimiter` peut être un caractère unique écrit directement après le deux-points, ou une chaîne de plusieurs caractères entourée de guillemets doubles.
- Lorsque `arraydelimiter` est omis, les éléments sont concaténés avec une virgule.
- La source de données doit permettre au moteur d’énumérer les enregistrements : associez une `List<T>` (ou une autre collection) dont le type d’élément expose la propriété de tableau. La liaison d’un objet unique laisse les marqueurs du corps non résolus.
- Les mêmes attributs fonctionnent avec des tableaux de chaînes et numériques ; chaque élément est rendu avec le texte brut de sa valeur.

## **Articles connexes**
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for .NET](/cells/fr/net/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for .NET](/cells/fr/net/apply-style-to-pivot-table/)
- [Modifier la disposition du champ de page dans un tableau croisé dynamique](/cells/fr/net/change-page-field-layout/)
- [Convertir une sparkline en image et en HTML dans Aspose.Cells for .NET](/cells/fr/net/convert-sparkline-to-image-and-html/)
- [Conversion d'Excel au format OFD](/cells/fr/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}