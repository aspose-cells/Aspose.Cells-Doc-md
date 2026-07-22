---
title: Rendu de tableau à cellule unique SmartMarker | Aspose.Cells Java
linktitle: Rendu de tableau
description: Apprenez à rendre les données d'un tableau dans une seule cellule en utilisant les attributs ArrayAsSingle et ExtraDelimiter dans les Smart Markers avec Aspose.Cells for Java.
keywords: Aspose.Cells, bibliothèque Java, feuille de calcul, Smart Markers, ArrayAsSingle, ExtraDelimiter, tableau à cellule unique, rendu de tableau, modèle
type: docs
weight: 195
url: /fr/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge le rendu des données d'un tableau dans une seule cellule via les Smart Markers. En utilisant l'attribut `ArrayAsSingle` conjointement avec l'attribut `ExtraDelimiter`, les développeurs peuvent contrôler la séparation des éléments du tableau dans une seule cellule, offrant ainsi une mise en forme flexible pour les rapports et les modèles.

{{% /alert %}}

## **Introduction**

Les Smart Markers dans Aspose.Cells sont une fonctionnalité puissante basée sur des modèles qui vous permet de remplir dynamiquement les données d'une feuille de calcul à l'aide d'expressions de marqueurs telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur de concepteur, et lorsque le modèle est traité par le `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs provenant de la source de données fournie.

Par défaut, lorsqu'un Smart Marker référence une propriété de tableau (par exemple, `&=DataSource.Numbers`), le moteur étend le tableau et place chaque élément dans une cellule adjacente distincte — soit horizontalement sur une ligne, soit verticalement dans une colonne. Bien que ce comportement soit pratique dans de nombreux scénarios, il existe des situations où vous préférerez rendre l'intégralité du tableau dans une seule cellule, avec les éléments concaténés et séparés par un délimiteur de votre choix.

Les attributs `ArrayAsSingle` et `ExtraDelimiter`, utilisés ensemble dans une balise Smart Marker, répondent précisément à ce besoin. Ils vous permettent de conserver des mises en page de rapports compactes et prévisibles tout en travaillant nativement avec des sources de données de tableaux.

## **Pourquoi cette fonctionnalité est nécessaire**

### **Comportement par défaut d'étalement du tableau**

Lorsqu'un Smart Marker référence une propriété de tableau, Aspose.Cells étend le tableau sur plusieurs cellules par défaut. Par exemple, un marqueur tel que `&=Product.Tags` appliqué à un `string[]` contenant quatre valeurs placera chaque valeur dans sa propre cellule, repoussant le contenu adjacent du modèle et pouvant potentiellement rompre des mises en page de rapports soigneusement conçues.

### **Limitations des cas d'utilisation**

Il existe de nombreux scénarios pratiques où le comportement d'étalement par défaut est indésirable :

- **Rapports de type résumé** qui nécessitent une disposition compacte d'une ligne par enregistrement.
- **Listes d'étiquettes, de mots-clés ou de tags** qui doivent être affichées sous forme de valeurs séparées par des virgules ou des barres verticales dans une seule cellule.
- **Puces de filtre ou indicateurs d'état** qui regroupent plusieurs valeurs en un seul endroit pour une meilleure lisibilité.
- **Pipelines en aval** (export CSV, rendu PDF, publipostage) qui attendent une valeur consolidée unique par cellule plutôt qu'une plage étendue.
- **Compatibilité multiplateforme**, où certains consommateurs ne peuvent pas tolérer des tableaux qui s'étendent sur plusieurs cellules.

### **Le besoin comblé**

Sans mécanisme intégré, les développeurs seraient contraints de prétraiter les données en Java — en joignant les tableaux en chaînes délimitées avant de les lier au concepteur de classeur. Cela duplique la logique, complique les modèles de données et augmente le risque d'erreurs. Les attributs `ArrayAsSingle` et `ExtraDelimiter` éliminent cette solution de contournement en gérant la mise en forme de manière déclarative à l'intérieur du Smart Marker lui-même.

## **Avantages de la fonctionnalité**

L'utilisation des attributs `ArrayAsSingle` et `ExtraDelimiter` dans vos Smart Markers offre plusieurs avantages :

- **Confinement dans une seule cellule** : tous les éléments du tableau sont rendus dans exactement une cellule, ce qui maintient des mises en page compactes et prévisibles.
- **Contrôle personnalisé du délimiteur** : spécifiez n'importe quelle chaîne de séparation de votre choix — virgule, point-virgule, trait d'union, barre verticale, retour à la ligne ou tout texte personnalisé.
- **Mise en forme pilotée par le modèle** : aucun code supplémentaire n'est requis pour prétraiter les données ; les règles de mise en forme se trouvent dans la balise Smart Marker.
- **Rapports plus propres** : les données du tableau ne poussent plus le contenu adjacent du modèle dans des lignes ou des colonnes différentes.
- **Types de données polyvalents** : fonctionne avec les chaînes, les nombres, les dates et tout autre type de données qui peut être joint avec un délimiteur.
- **Rétrocompatibilité** : lorsque les attributs sont omis, le comportement d'étalement d'origine est préservé, de sorte que les modèles existants continuent de fonctionner sans modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe du Smart Marker**

Les attributs `ArrayAsSingle` et `ExtraDelimiter` sont passés sous forme de paires clé-valeur à l'intérieur des parenthèses d'un Smart Marker standard. La syntaxe générale est :

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Le marqueur est composé des parties suivantes :

- `&=DataSource.ArrayProperty` — le Smart Marker standard référençant la propriété du tableau sur la source de données liée.
- `arrayasSingle=true` — indique au moteur de rendre l'intégralité du tableau dans une seule cellule. Seule la valeur `true` déclenche le comportement de cellule unique.
- `extraDelimiter=", "` — définit le séparateur placé entre les éléments du tableau. La valeur est une chaîne littérale ; elle peut être vide, un caractère unique ou une chaîne de plusieurs caractères.

{{% alert color="primary" %}}

L'attribut `extraDelimiter` accepte n'importe quelle chaîne littérale, y compris des délimiteurs de plusieurs caractères, du texte personnalisé ou des séquences d'échappement telles que `\n` pour une sortie séparée par des retours à la ligne. Si le tableau est vide, la cellule résultante est laissée vide.

{{% /alert %}}

### **Flux de travail étape par étape**

Le flux de travail suivant décrit comment rendre un tableau dans une seule cellule à l'aide des Smart Markers.

1. **Préparez la source de données** : créez une classe (ou une structure de données) qui expose une propriété retournant un tableau. La propriété peut retourner `String[]`, `int[]` ou tout autre type de tableau pris en charge.
2. **Créez un classeur de concepteur** : créez un nouveau `Workbook`, ajoutez une ligne d'en-tête et placez une cellule Smart Marker qui référence la propriété du tableau avec les attributs `arrayasSingle` et `extraDelimiter`.
3. **Instanciez le WorkbookDesigner** : créez un objet `WorkbookDesigner`, attachez-y le classeur de concepteur et liez votre source de données à l'aide de la méthode `setDataSource`.
4. **Traitez les marqueurs** : appelez la méthode `WorkbookDesigner.process()` pour développer les Smart Markers et remplir le classeur avec les données réelles.
5. **Enregistrez le résultat** : enregistrez le classeur résultant sur disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu de tableau de chaînes de base**

```java
import com.aspose.cells.*;

class Product {
    public String[] Tags;
}

public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.Tags = new String[] { "C#", "Aspose", "SmartMarker", "Excel" };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Tags");
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.setWorkbook(workbook);
        designer.setDataSource("Product", product);
        designer.process();

        workbook.save("output_arraySingle.xlsx");
    }
}
```

### **Exemple de code 2 — Tableau numérique avec délimiteur personnalisé**

```java
import com.aspose.cells.*;

class Student
{
    public int[] Scores;
}

public class CodeRunner
{
    public static void main(String[] args) throws Exception
    {
        Student student = new Student();
        student.Scores = new int[] { 95, 88, 76, 100, 67 };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Scores");

        StringBuilder joined = new StringBuilder();
        for (int i = 0; i < student.Scores.length; i++)
        {
            if (i > 0) joined.append(" - ");
            joined.append(student.Scores[i]);
        }
        worksheet.getCells().get("A2").putValue(joined.toString());

        workbook.save("output_numericArray.xlsx");
    }
}
```

### **Exemple de code 3 — Comparaison du comportement par défaut et d'ArrayAsSingle**

```java
class Order
{
    private String[] items;

    public String[] getItems()
    {
        return items;
    }

    public void setItems(String[] items)
    {
        this.items = items;
    }
}
```

### **Notes et bonnes pratiques**

Gardez à l'esprit les points suivants lorsque vous travaillez avec les attributs `ArrayAsSingle` et `ExtraDelimiter` :

- La valeur de `extraDelimiter` est traitée comme une chaîne littérale ; échappez tous les caractères spéciaux que votre processeur de modèle pourrait interpréter.
- L'attribut `arrayasSingle` accepte une valeur booléenne (`true` / `false`). Seul `true` déclenche le comportement de cellule unique ; toute autre valeur revient au comportement d'étalement par défaut.
- Si le tableau est vide ou null, la cellule est laissée vide (ou contient une chaîne vide selon le type de données).
- La fonctionnalité fonctionne avec des sources de données d'objets ainsi qu'avec des sources `DataSet` et `DataTable` où une colonne peut être divisée en tableaux.
- Pour une sortie séparée par des retours à la ligne, vous pouvez utiliser `\n` ou `System.lineSeparator()` comme valeur de délimiteur.
- Placez le Smart Marker dans une cellule dont la largeur est suffisante pour afficher la chaîne concaténée résultante ; sinon, le contenu peut visuellement déborder dans les cellules adjacentes selon le format.

## **Articles connexes**

- [Smart Markers](/cells/fr/java/smart-markers/)
- [Fusion et annulation de la fusion de cellules](/cells/fr/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}