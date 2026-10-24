---
title: Rendu d’un tableau dans une cellule unique avec SmartMarker | Aspose.Cells for Java
description: Découvrez comment rendre des données de tableau dans une seule cellule à l’aide des attributs ArrayAsSingle et ExtraDelimiter dans les Smart Markers avec Aspose.Cells for Java.
linktitle: Rendu d’un tableau dans une cellule unique avec SmartMarker | Aspose.Cells
url: /fr/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, bibliothèque Java, feuille de calcul, Smart Markers, ArrayAsSingle, ExtraDelimiter, tableau dans une cellule unique, rendu de tableau, modèle
type: docs
weight: 195
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells permet de rendre des données de tableau dans une seule cellule à l’aide de Smart Markers. En utilisant l’attribut `ArrayAsSingle` conjointement avec l’attribut `ExtraDelimiter`, les développeurs peuvent contrôler la manière dont les éléments du tableau sont séparés dans une même cellule, ce qui offre une mise en forme flexible des rapports et des modèles.
{{% /alert %}}

## **Introduction**
Les Smart Markers d’Aspose.Cells constituent une fonctionnalité puissante fondée sur des modèles qui vous permet de remplir dynamiquement des données de feuille de calcul à l’aide d’expressions de marqueur telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur de conception et, lorsque le modèle est traité par `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs de la source de données fournie.
Par défaut, lorsqu’un Smart Marker référence une propriété de tableau (par exemple, `&=DataSource.Numbers`), le moteur déploie le tableau et place chaque élément dans une cellule adjacente distincte, horizontalement sur une ligne ou verticalement dans une colonne. Bien que ce comportement soit pratique dans de nombreux scénarios, certaines situations nécessitent de rendre le tableau entier dans une seule cellule, avec des éléments concaténés et séparés par un délimiteur de votre choix.
Les attributs `ArrayAsSingle` et `ExtraDelimiter`, utilisés ensemble dans une balise Smart Marker, répondent précisément à ce besoin. Ils permettent de conserver des mises en page de rapport compactes et prévisibles tout en utilisant nativement des sources de données de type tableau.

## **Pourquoi cette fonctionnalité est-elle nécessaire**

### **Comportement par défaut de déploiement des tableaux**
Lorsqu’un Smart Marker référence une propriété de tableau, Aspose.Cells déploie le tableau sur plusieurs cellules par défaut. Par exemple, un marqueur tel que `&=Product.Tags`, associé à un `string[]` contenant quatre valeurs, place chaque valeur dans une cellule distincte, décalant ainsi le reste du contenu du modèle et risquant d’altérer des mises en page de rapport soigneusement conçues.

### **Limites des cas d’utilisation**
De nombreux scénarios pratiques(requirement que le comportement de déploiement par défaut ne soit pas souhaitable :
- **Rapports de type synthèse** nécessitant une disposition compacte avec une ligne par enregistrement.
- **Listes de tags, d’étiquettes ou de mots-clés** devant être affichées sous forme de valeurs séparées par des virgules ou des barres verticales dans une seule cellule.
- **Jetons de filtre ou indicateurs d’état** regroupant plusieurs valeurs au même endroit pour améliorer la lisibilité.
- **Chaînes de traitement en aval** (export CSV, rendu PDF, publipostage) qui attendent une valeur consolidée unique par cellule plutôt qu’une plage étendue.
- **Compatibilité multiplateforme**, où certains consommateurs ne tolèrent pas les tableaux qui débordent sur plusieurs cellules.

### **La lacune comblée**
Sans mécanisme intégré, les développeurs seraient obligés de prétraiter les données en Java, en convertissant les tableaux en chaînes délimitées avant de les transmettre au `WorkbookDesigner`. Cette approche duplique la logique, complexifie les modèles de données et augmente les risques d’erreur. Les attributs `ArrayAsSingle` et `ExtraDelimiter` éliminent cette solution de contournement en gérant la mise en forme de manière déclarative à l’intérieur du Smart Marker lui-même.

## **Avantages de la fonctionnalité**
L’utilisation des attributs `ArrayAsSingle` et `ExtraDelimiter` dans vos Smart Markers offre plusieurs avantages :
- **Confinement dans une seule cellule** : tous les éléments du tableau sont rendus dans une cellule unique, ce qui maintient des mises en page compactes et prévisibles.
- **Contrôle personnalisé du délimiteur** : indiquez la chaîne de séparation de votre choix, telle qu’une virgule, un point-virgule, un trait d’union, une barre verticale, un saut de ligne ou tout autre texte personnalisé.
- **Mise en forme pilotée par le modèle** : aucun code supplémentaire n’est requis pour prétraiter les données ; les règles de mise en forme figurent dans la balise Smart Marker.
- **Rapports plus propres** : les données de tableau ne décalent plus le contenu voisin du modèle vers d’autres lignes ou colonnes.
- **Types de données polyvalents** : la fonctionnalité fonctionne avec des chaînes, des nombres, des dates et tout autre type de données pouvant être associé à un délimiteur.
- **Rétrocompatibilité** : lorsque les attributs sont omis, le comportement de déploiement d’origine est préservé et les modèles existants continuent de fonctionner sans modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe du Smart Marker**
Les attributs `ArrayAsSingle` et `ExtraDelimiter` sont fournis sous forme de paires clé-valeur dans les parenthèses d’un Smart Marker standard. La syntaxe générale est la suivante :

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

Le marqueur est composé des éléments suivants :
- `&=DataSource.ArrayProperty` — le Smart Marker standard qui référence la propriété de tableau de la source de données liée.
- `arrayasSingle=true` — indique au moteur de rendre le tableau entier dans une seule cellule. Seule la valeur `true` déclenche ce comportement.
- `extraDelimiter=", "` — définit le séparateur placé entre les éléments du tableau. La valeur est un littéral de chaîne ; elle peut être vide, comporter un seul caractère ou plusieurs caractères.

{{% alert color="primary" %}}
L’attribut `extraDelimiter` accepte n’importe quel littéral de chaîne, y compris des délimiteurs de plusieurs caractères, du texte personnalisé ou des séquences d’échappement telles que `\n` pour produire une sortie séparée par des sauts de ligne. Si le tableau est vide, la cellule résultante reste vide.
{{% /alert %}}

### **Processus étape par étape**
Le processus suivant explique comment rendre un tableau dans une seule cellule à l’aide des Smart Markers.
1. **Préparer la source de données** : créez une classe ou une structure de données qui expose une propriété renvoyant un tableau. La propriété peut renvoyer `String[]`, `int[]` ou tout autre type de tableau pris en charge.
2. **Créer un classeur de conception** : créez un nouvel objet `Workbook`, ajoutez une ligne d’en-tête et placez dans une cellule un Smart Marker qui référence la propriété de tableau avec les attributs `arrayasSingle` et `extraDelimiter`.
3. **Instancier le `WorkbookDesigner`** : créez un objet `WorkbookDesigner`, associez-y le classeur de conception et liez votre source de données à l’aide de la méthode `setDataSource`.
4. **Traiter les marqueurs** : appelez la méthode `WorkbookDesigner.process()` pour développer les Smart Markers et remplir le classeur avec les données réelles.
5. **Enregistrer le résultat** : enregistrez le classeur obtenu sur le disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu d’un tableau de chaînes de caractères**

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

### **Exemple de code 2 — Tableau numérique avec un délimiteur personnalisé**

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

### **Exemple de code 3 — Comparaison entre le comportement par défaut et `ArrayAsSingle`**

### **Remarques et bonnes pratiques**
Gardez les points suivants à l’esprit lorsque vous utilisez les attributs `ArrayAsSingle` et `ExtraDelimiter` :
- La valeur `extraDelimiter` est traitée comme un littéral de chaîne ; échappez tous les caractères spéciaux susceptibles d’être interprétés par votre moteur de traitement des modèles.
- L’attribut `arrayasSingle` accepte une valeur booléenne (`true` / `false`). Seule la valeur `true` déclenche le comportement dans une seule cellule ; toute autre valeur ramène au comportement de déploiement par défaut.
- Si le tableau est vide ou nul, la cellule reste vide ou contient une chaîne vide, selon le type de données.
- La fonctionnalité fonctionne avec des sources de données objet, ainsi qu’avec des sources `DataSet` et `DataTable` dans lesquelles une colonne peut être répartie en tableaux.
- Pour produire une sortie séparée par des sauts de ligne, vous pouvez utiliser `\n` ou `System.lineSeparator()` comme valeur de délimiteur.
- Placez le Smart Marker dans une cellule suffisamment large pour afficher la chaîne concaténée obtenue ; sinon, le contenu peut déborder visuellement sur les cellules adjacentes, selon le format.

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

{{< app/cells/assistant language="java" >}}