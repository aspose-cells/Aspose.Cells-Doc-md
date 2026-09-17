---
title: Rendu de tableau à cellule unique SmartMarker | Aspose.Cells .NET
linktitle: Rendu de tableau à cellule unique SmartMarker | Aspose.Cells .NET
description: Apprenez à rendre des données de tableau dans une seule cellule à l'aide des attributs ArrayAsSingle et ExtraDelimiter dans les Smart Markers avec Aspose.Cells for .NET.
keywords: Aspose.Cells, bibliothèque .NET, feuille de calcul, Smart Markers, ArrayAsSingle, ExtraDelimiter, tableau à cellule unique, rendu de tableau, modèle
type: docs
weight: 195
url: /fr/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge le rendu des données de tableau dans une seule cellule via les Smart Markers. En utilisant l'attribut `ArrayAsSingle` conjointement avec l'attribut `ExtraDelimiter`, les développeurs peuvent contrôler la manière dont les éléments du tableau sont séparés dans une seule cellule, offrant une mise en forme flexible pour les rapports et les modèles.
{{% /alert %}}

## **Introduction**
Les Smart Markers dans Aspose.Cells sont une fonctionnalité puissante, basée sur des modèles, qui vous permet de remplir dynamiquement les données d'une feuille de calcul à l'aide d'expressions de marqueurs telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur designer, et lorsque le modèle est traité par le `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs provenant de la source de données fournie.
Par défaut, lorsqu'un Smart Marker fait référence à une propriété de tableau (par exemple, `&=DataSource.Numbers`), le moteur développe le tableau et place chaque élément dans une cellule adjacente distincte — soit horizontalement sur une ligne, soit verticalement dans une colonne. Bien que ce comportement soit pratique dans de nombreux scénarios, il existe des situations où vous préféreriez rendre l'intégralité du tableau dans une seule cellule, avec les éléments concaténés et séparés par un délimiteur de votre choix.
Les attributs `ArrayAsSingle` et `ExtraDelimiter`, utilisés ensemble à l'intérieur d'une balise Smart Marker, répondent précisément à cette exigence. Ils vous permettent de conserver des mises en page de rapport compactes et prévisibles tout en travaillant nativement avec des sources de données de tableau.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
Lorsqu'un Smart Marker fait référence à une propriété de tableau, Aspose.Cells développe le tableau sur plusieurs cellules par défaut. Par exemple, un marqueur tel que `&=Product.Tags` appliqué à un `string[]` contenant quatre valeurs placera chaque valeur dans sa propre cellule, repoussant le reste du contenu du modèle et pouvant potentiellement briser des mises en page de rapport soigneusement conçues.

### **Use Case Limitations**
Il existe de nombreux scénarios pratiques où le comportement de répartition par défaut n'est pas souhaitable :
- **Rapports de type résumé** qui nécessitent une disposition compacte d'une ligne par enregistrement.
- **Listes de balises, d'étiquettes ou de mots-clés** qui doivent être affichées sous forme de valeurs séparées par des virgules ou des barres verticales dans une seule cellule.
- **Puces de filtre ou indicateurs d'état** qui regroupent plusieurs valeurs en un seul endroit pour une meilleure lisibilité.
- **Pipelines en aval** (export CSV, rendu PDF, publipostage) qui attendent une valeur consolidée unique par cellule plutôt qu'une plage étendue.
- **Compatibilité multiplateforme**, où certains consommateurs ne tolèrent pas les tableaux qui s'étendent sur plusieurs cellules.

### **The Gap It Fills**
Sans mécanisme intégré, les développeurs seraient contraints de prétraiter les données en C# ou VB.NET — en joignant les tableaux en chaînes délimitées avant de les lier au concepteur de classeur. Cela duplique la logique, complique les modèles de données et augmente le risque d'erreurs. Les attributs `ArrayAsSingle` et `ExtraDelimiter` éliminent cette solution de contournement en gérant la mise en forme de manière déclarative à l'intérieur du Smart Marker lui-même.

## **Feature Benefits**
L'utilisation des attributs `ArrayAsSingle` et `ExtraDelimiter` dans vos Smart Markers offre plusieurs avantages :
- **Confinement dans une seule cellule** : tous les éléments du tableau sont rendus dans exactement une seule cellule, ce qui maintient les mises en page compactes et prévisibles.
- **Contrôle personnalisé du délimiteur** : spécifiez n'importe quelle chaîne de séparation que vous souhaitez — virgule, point-virgule, trait d'union, barre verticale, saut de ligne ou tout texte personnalisé.
- **Mise en forme pilotée par le modèle** : aucun code supplémentaire n'est nécessaire pour prétraiter les données ; les règles de mise en forme se trouvent dans la balise Smart Marker.
- **Rapports plus propres** : les données du tableau ne repoussent plus le contenu voisin du modèle dans des lignes ou des colonnes différentes.
- **Types de données polyvalents** : fonctionne avec les chaînes, les nombres, les dates et tout autre type de données pouvant être joint avec un délimiteur.
- **Rétrocompatibilité** : lorsque les attributs sont omis, le comportement de répartition d'origine est préservé, de sorte que les modèles existants continuent à fonctionner sans modification.

## **How to Use This Feature**

### **Smart Marker Syntax**
Les attributs `ArrayAsSingle` et `ExtraDelimiter` sont passés sous forme de paires clé-valeur à l'intérieur des parenthèses d'un Smart Marker standard. La syntaxe générale est la suivante :

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Le marqueur est composé des parties suivantes :
- `&=DataSource.ArrayProperty` — le Smart Marker standard faisant référence à la propriété de tableau sur la source de données liée.
- `arrayasSingle=true` — indique au moteur de rendre l'intégralité du tableau dans une seule cellule. Seule la valeur `true` déclenche le comportement de cellule unique.
- `extraDelimiter=", "` — définit le séparateur placé entre les éléments du tableau. La valeur est une chaîne littérale ; elle peut être vide, un seul caractère ou une chaîne de plusieurs caractères.

{{% alert color="primary" %}}
L'attribut `extraDelimiter` accepte toute chaîne littérale, y compris des délimiteurs multi-caractères, du texte personnalisé ou des séquences d'échappement telles que `\n` pour une sortie séparée par des sauts de ligne. Si le tableau est vide, la cellule résultante reste vide.

### **Step-by-Step Workflow**
Le flux de travail suivant décrit comment rendre un tableau dans une seule cellule à l'aide des Smart Markers.
1. **Préparez la source de données** : créez une classe (ou structure de données) qui expose une propriété renvoyant un tableau. La propriété peut renvoyer `string[]`, `int[]` ou tout autre type de tableau pris en charge.
2. **Créez un classeur designer** : créez un nouveau `Workbook`, ajoutez une ligne d'en-tête et placez une cellule Smart Marker qui fait référence à la propriété de tableau avec les attributs `arrayasSingle` et `extraDelimiter`.
3. **Instanciez le WorkbookDesigner** : créez un objet `WorkbookDesigner`, attachez-lui le classeur designer et liez votre source de données à l'aide de la méthode `SetDataSource`.
4. **Traitez les marqueurs** : appelez la méthode `WorkbookDesigner.Process()` pour développer les Smart Markers et remplir le classeur avec les données réelles.
5. **Enregistrez le résultat** : enregistrez le classeur résultant sur disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Code Example 1 — Basic String Array Rendering**

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

### **Code Example 2 — Numeric Array with Custom Delimiter**

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

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

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
        // Section 1: Default Smart Marker - values spread horizontally across cells
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");
        // Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");
        // Bind the data source and process Smart Markers
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();
        // Save the resulting workbook
        workbook.Save("output_comparison.xlsx");
    }
}
public class Order
{
    public string[] Items { get; set; }
}
```

### **Notes & Best Practices**
Gardez à l'esprit les points suivants lorsque vous travaillez avec les attributs `ArrayAsSingle` et `ExtraDelimiter` :
- La valeur `extraDelimiter` est traitée comme une chaîne littérale ; échappez tous les caractères spéciaux que votre processeur de modèles pourrait interpréter.
- L'attribut `arrayasSingle` accepte une valeur booléenne (`true` / `false`). Seul `true` déclenche le comportement de cellule unique ; toute autre valeur revient au comportement de répartition par défaut.
- Si le tableau est vide ou nul, la cellule est laissée vide (ou contient une chaîne vide selon le type de données).
- La fonctionnalité fonctionne aussi bien avec des sources de données d'objets qu'avec des sources `DataSet` et `DataTable` où une colonne peut être divisée en tableaux.
- Pour une sortie séparée par des sauts de ligne, vous pouvez utiliser `\n` ou `Environment.NewLine` comme valeur de délimiteur.
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for .NET](/cells/fr/net/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for .NET](/cells/fr/net/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/fr/net/change-page-field-layout/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for .NET](/cells/fr/net/convert-sparkline-to-image-and-html/)
- [Converting Excel to OFD Format](/cells/fr/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}