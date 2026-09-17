---
title: SmartMarker Single Cell Array Rendering | Aspose.Cells Java
description: Learn how to render array data into a single cell using the ArrayAsSingle and ExtraDelimiter attributes in Smart Markers with Aspose.Cells for Java.
linktitle: SmartMarker Single Cell Array Rendering | Aspose.Cells
url: /fr/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Java library, spreadsheet, Smart Markers, ArrayAsSingle, ExtraDelimiter, single cell array, array rendering, template
type: docs
weight: 195
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

```
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

{{% alert color="primary" %}}
Aspose.Cells prend en charge le rendu de données de tableau dans une seule cellule via les Smart Markers. En utilisant l'attribut `ArrayAsSingle` conjointement avec l'attribut `ExtraDelimiter`, les développeurs peuvent contrôler la manière dont les éléments du tableau sont séparés dans une seule cellule, offrant ainsi une mise en forme flexible pour les rapports et les modèles.

## **Introduction**
Les Smart Markers dans Aspose.Cells sont une fonctionnalité puissante, basée sur des modèles, qui vous permet de remplir dynamiquement des données de feuille de calcul à l'aide d'expressions de marqueurs telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur de conception, et lorsque le modèle est traité par le `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs de la source de données fournie.
Par défaut, lorsqu'un Smart Marker référence une propriété de tableau (par exemple, `&=DataSource.Numbers`), le moteur développe le tableau et place chaque élément dans une cellule adjacente distincte — soit horizontalement sur une ligne, soit verticalement sur une colonne. Bien que ce comportement soit pratique dans de nombreux scénarios, il existe des situations où vous préférerez rendre le tableau entier dans une seule cellule, avec les éléments concaténés et séparés par un délimiteur de votre choix.
Les attributs `ArrayAsSingle` et `ExtraDelimiter`, utilisés conjointement dans une balise Smart Marker, répondent précisément à cette exigence. Ils vous permettent de conserver des mises en page de rapport compactes et prévisibles tout en travaillant nativement avec des sources de données de tableau.

## **Pourquoi cette fonctionnalité est nécessaire**

### **Comportement par défaut d'expansion du tableau**
Lorsqu'un Smart Marker référence une propriété de tableau, Aspose.Cells développe le tableau sur plusieurs cellules par défaut. Par exemple, un marqueur tel que `&=Product.Tags` face à un `string[]` contenant quatre valeurs placera chaque valeur dans sa propre cellule, repoussant le contenu du modèle vers l'extérieur et pouvant potentiellement compromettre des mises en page de rapport soigneusement conçues.

### **Limitations des cas d'utilisation**
Il existe de nombreux scénarios pratiques où le comportement d'expansion par défaut est indésirable :
- **Rapports de type résumé** nécessitant une disposition compacte d'une ligne par enregistrement.
- **Listes d'étiquettes, de libellés ou de mots-clés** qui doivent être affichées sous forme de valeurs séparées par des virgules ou des barres verticales dans une seule cellule.
- **Puces de filtre ou indicateurs d'état** regroupant plusieurs valeurs au même endroit pour une meilleure lisibilité.
- **Pipelines en aval** (export CSV, rendu PDF, publipostage) qui attendent une valeur consolidée unique par cellule plutôt qu'une plage étendue.
- **Compatibilité multiplateforme**, où certains consommateurs ne peuvent pas tolérer des tableaux qui s'étendent sur plusieurs cellules.

### **Le vide qu'elle comble**
Sans mécanisme intégré, les développeurs seraient contraints de prétraiter les données en Java — en joignant les tableaux en chaînes délimitées avant de les lier au concepteur de classeur. Cela duplique la logique, complique les modèles de données et augmente le risque d'erreurs. Les attributs `ArrayAsSingle` et `ExtraDelimiter` éliminent cette solution de contournement en gérant la mise en forme de manière déclarative à l'intérieur du Smart Marker lui-même.

## **Avantages de la fonctionnalité**
L'utilisation des attributs `ArrayAsSingle` et `ExtraDelimiter` dans vos Smart Markers offre plusieurs avantages :
- **Confinement dans une seule cellule** : tous les éléments du tableau sont rendus dans une seule et même cellule, ce qui maintient les mises en page compactes et prévisibles.
- **Contrôle du délimiteur personnalisé** : spécifiez n'importe quelle chaîne de séparation de votre choix — virgule, point-virgule, trait d'union, barre verticale, saut de ligne ou tout texte personnalisé.
- **Mise en forme pilotée par le modèle** : aucun code supplémentaire n'est nécessaire pour prétraiter les données ; les règles de mise en forme sont intégrées dans la balise Smart Marker.
- **Rapports plus propres** : les données de tableau ne repoussent plus le contenu du modèle voisin dans des lignes ou des colonnes différentes.
- **Types de données polyvalents** : fonctionne avec les chaînes, les nombres, les dates et tout autre type de données pouvant être joint avec un délimiteur.
- **Rétrocompatibilité** : lorsque les attributs sont omis, le comportement d'expansion d'origine est préservé, de sorte que les modèles existants continuent de fonctionner sans modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe du Smart Marker**
Les attributs `ArrayAsSingle` et `ExtraDelimiter` sont passés sous forme de paires clé-valeur à l'intérieur des parenthèses d'un Smart Marker standard. La syntaxe générale est la suivante :

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

Le marqueur est composé des parties suivantes :
- `&=DataSource.ArrayProperty` — le Smart Marker standard référençant la propriété de tableau sur la source de données liée.
- `arrayasSingle=true` — indique au moteur de rendre le tableau entier dans une seule cellule. Seule la valeur `true` déclenche le comportement en cellule unique.
- `extraDelimiter=", "` — définit le séparateur placé entre les éléments du tableau. La valeur est une chaîne littérale ; elle peut être vide, un seul caractère ou une chaîne de plusieurs caractères.

{{% alert color="primary" %}}
L'attribut `extraDelimiter` accepte toute chaîne littérale, y compris des délimiteurs de plusieurs caractères, du texte personnalisé ou des séquences d'échappement telles que `\n` pour une sortie séparée par des sauts de ligne. Si le tableau est vide, la cellule résultante reste vide.

### **Flux de travail étape par étape**
Le flux de travail suivant décrit comment rendre un tableau dans une seule cellule à l'aide des Smart Markers.
1. **Préparez la source de données** : créez une classe (ou structure de données) qui expose une propriété renvoyant un tableau. La propriété peut renvoyer `String[]`, `int[]` ou tout autre type de tableau pris en charge.
2. **Créez un classeur de conception** : créez un nouveau `Workbook`, ajoutez une ligne d'en-tête et placez une cellule Smart Marker qui référence la propriété de tableau avec les attributs `arrayasSingle` et `extraDelimiter`.
3. **Instanciez le WorkbookDesigner** : créez un objet `WorkbookDesigner`, attachez-y le classeur de conception et liez votre source de données à l'aide de la méthode `setDataSource`.
4. **Traitez les marqueurs** : appelez la méthode `WorkbookDesigner.process()` pour développer les Smart Markers et remplir le classeur avec des données réelles.
5. **Enregistrez le résultat** : enregistrez le classeur résultant sur disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu de tableau de chaînes de base**

```java
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

### **Exemple de code 2 — Tableau numérique avec délimiteur personnalisé**

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

### **Exemple de code 3 — Comparaison du comportement par défaut et ArrayAsSingle**

### **Notes et bonnes pratiques**
Gardez les points suivants à l'esprit lorsque vous travaillez avec les attributs `ArrayAsSingle` et `ExtraDelimiter` :
- La valeur `extraDelimiter` est traitée comme une chaîne littérale ; échappez tout caractère spécial que votre processeur de modèle pourrait interpréter.
- L'attribut `arrayasSingle` accepte une valeur booléenne (`true` / `false`). Seule la valeur `true` déclenche le comportement en cellule unique ; toute autre valeur retombe sur le comportement d'expansion par défaut.
- Si le tableau est vide ou null, la cellule reste vide (ou contient une chaîne vide selon le type de données).
- La fonctionnalité fonctionne avec des sources de données d'objet ainsi qu'avec des sources `DataSet` et `DataTable` où une colonne peut être divisée en tableaux.
- Pour une sortie séparée par des sauts de ligne, vous pouvez utiliser `\n` ou `System.lineSeparator()` comme valeur de délimiteur.
- Placez le Smart Marker dans une cellule dont la largeur est suffisante pour afficher la chaîne concaténée résultante ; sinon, le contenu peut visuellement déborder dans les cellules adjacentes selon le format.
{{% /alert %}}

{{% /alert %}}

## Articles connexes
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for Java](/cells/fr/java/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for Java](/cells/fr/java/apply-style-to-pivot-table/)
- [Modifier la disposition des champs de page dans un tableau croisé dynamique](/cells/fr/java/change-page-field-layout/)
- [Convertir une sparkline en image et HTML dans Aspose.Cells for Java](/cells/fr/java/convert-sparkline-to-image-and-html/)
- [Conversion d'Excel au format OFD](/cells/fr/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}