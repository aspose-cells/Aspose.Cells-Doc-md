---
title: Rendu d’un tableau dans une cellule unique avec les marqueurs intelligents | Aspose.Cells for Java
description: Découvrez comment restituer des données sous forme de tableau dans une cellule unique à l’aide des attributs de marqueur intelligent arrayassingle et arraydelimiter dans Aspose.Cells for Java.
linktitle: Rendu d’un tableau dans une cellule unique avec les marqueurs intelligents | Aspose.Cells
url: /fr/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, bibliothèque Java, feuille de calcul, marqueurs intelligents, arrayassingle, arraydelimiter, tableau dans une cellule unique, rendu de tableau, modèle
type: docs
weight: 195
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells peut restituer une source de données de type tableau dans une seule cellule grâce aux marqueurs intelligents. L’attribut `arrayassingle` désactive le déploiement élément par élément par défaut, et l’attribut `arraydelimiter` choisit le délimiteur placé entre les éléments concaténés — une virgule par défaut, ou tout caractère unique ou toute chaîne multicaractère entre guillemets que vous spécifiez.
{{% /alert %}}

## **Introduction**

Les marqueurs intelligents d’Aspose.Cells constituent une fonctionnalité fondée sur des modèles qui renseignent dynamiquement les données d’une feuille de calcul à l’aide d’expressions de marqueur telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur modèle et, lorsque celui-ci est traité par le WorkbookDesigner, les marqueurs sont remplacés par les valeurs de la source de données fournie.
Par défaut, lorsqu’un marqueur intelligent référence une propriété de tableau (par exemple, `&=Product.Tags` lié à un `String[]` de quatre valeurs), le moteur déploie le tableau et place chaque élément dans sa propre cellule, en répartissant les valeurs verticalement dans la colonne située sous le marqueur. Bien que ce comportement soit pratique dans de nombreux scénarios, il existe des situations où vous préférez restituer le tableau entier dans une seule cellule, avec les éléments concaténés et séparés par un délimiteur de votre choix.
Les attributs `arrayassingle` et `arraydelimiter`, écrits entre les parenthèses d’un marqueur intelligent sous la forme `name:value`, répondent précisément à ce besoin. Ils vous permettent de conserver des mises en page de rapport compactes et prévisibles tout en exploitant nativement des sources de données de type tableau.

## **Pourquoi cette fonctionnalité est-elle nécessaire**

### **Comportement par défaut de déploiement des tableaux**

Lorsqu’un marqueur intelligent référence une propriété de tableau, Aspose.Cells déploie le tableau sur plusieurs cellules par défaut. Par exemple, un marqueur tel que `&=Product.Tags` associé à un `String[]` contenant quatre valeurs place chaque valeur dans une cellule distincte sous le marqueur, ce qui décale le reste du contenu du modèle et peut compromettre des mises en page de rapport soigneusement élaborées.

### **Limites des cas d’utilisation**

De nombreux scénarios pratiques rendent le comportement de déploiement par défaut peu souhaitable :
- **Rapports de type résumé** qui nécessitent une mise en page compacte avec une ligne par enregistrement.
- **Listes de marqueurs, d’étiquettes ou de mots-clés** qui doivent être affichées sous forme de valeurs séparées par des virgules ou des barres verticales dans une seule cellule.
- **Pastilles de filtre ou indicateurs d’état** qui regroupent plusieurs valeurs au même endroit pour améliorer la lisibilité.
- **Chaînes de traitement en aval** (export CSV, rendu PDF, publipostage) qui attendent une valeur consolidée par cellule plutôt qu’une plage développée.
- **Compatibilité multiplateforme**, lorsque certains consommateurs ne peuvent pas gérer des tableaux qui débordent sur plusieurs cellules.

### **Le manque comblé**

Sans mécanisme intégré, les développeurs seraient obligés de prétraiter les données en Java — en joignant les éléments des tableaux dans des chaînes délimitées avant de les associer au WorkbookDesigner. Cela duplique la logique, complique les modèles de données et augmente le risque d’erreurs. Les attributs `arrayassingle` et `arraydelimiter` éliminent ce contournement en gérant la mise en forme de manière déclarative directement dans le marqueur intelligent.

## **Avantages de la fonctionnalité**

Utiliser les attributs `arrayassingle` et `arraydelimiter` dans vos marqueurs intelligents offre plusieurs avantages :
- **Confinement dans une cellule unique** : Tous les éléments du tableau sont restitués dans exactement une cellule, ce qui maintient des mises en page compactes et prévisibles.
- **Contrôle du délimiteur personnalisé** : Spécifiez le délimiteur de votre choix — la virgule par défaut, un point-virgule, un trait d’union, une barre verticale ou une chaîne multicaractère entre guillemets telle que `" | "`.
- **Mise en forme pilotée par le modèle** : Aucun code supplémentaire n’est nécessaire pour prétraiter les données ; les règles de mise en forme sont définies dans la balise du marqueur intelligent.
- **Rapports plus propres** : Les données sous forme de tableau ne décalent plus vers différentes lignes ou colonnes le contenu du modèle situé à proximité.
- **Types de données polyvalents** : Fonctionne avec les tableaux de chaînes ainsi qu’avec les valeurs numériques issues de sources de données à base de JavaBeans et rendues sous forme de chaîne.
- **Compatibilité ascendante** : Lorsque les attributs sont omis, le comportement de déploiement d’origine est conservé, de sorte que les modèles existants continuent de fonctionner sans modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe des marqueurs intelligents**

Les attributs `arrayassingle` et `arraydelimiter` utilisent la grammaire d’attributs `name:value` d’Aspose.Cells dans les parenthèses d’un marqueur intelligent standard. La syntaxe générale est :

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

Le marqueur est composé des éléments suivants :
- `&=DataSource.ArrayProperty` — le marqueur intelligent standard qui référence la propriété de tableau de la source de données associée.
- `arrayassingle:true` — indique au moteur de restituer l’ensemble du tableau dans une seule cellule au lieu d’en déployer les éléments.
- `arraydelimiter:;` — facultatif ; définit le délimiteur placé entre les éléments du tableau. S’il est omis, une virgule est utilisée.

{{% alert color="warning" %}}
Écrivez les attributs sous la forme `name:value` (avec deux-points et non un signe égal) et séparez plusieurs attributs par une virgule **sans espaces**. Un espace après la virgule décale la valeur analysée d’un caractère — `(arrayassingle:true, arraydelimiter:;)` produirait la concaténation avec le délimiteur erroné `:;` au lieu de `;`.
{{% /alert %}}

### **Formes du délimiteur**

- Un caractère unique est écrit directement après les deux-points : `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Un délimiteur multicaractère est écrit entre guillemets doubles : `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Processus détaillé**

Le processus suivant décrit comment restituer un tableau dans une seule cellule à l’aide des marqueurs intelligents.
1. **Préparer la source de données** : Créez une classe JavaBean déclarée `public` avec un accesseur qui renvoie le tableau, tel que `String[] getTags()`, et associez une `java.util.List` de JavaBeans afin que le moteur lise un enregistrement par ligne. Les champs publics seuls ne sont pas associés ; le moteur utilise les accesseurs JavaBean.
2. **Créer un classeur modèle** : Créez un nouveau `Workbook`, ajoutez une ligne d’en-tête et placez dans une cellule un marqueur intelligent qui référence la propriété de tableau avec l’attribut `arrayassingle` (et `arraydelimiter` lorsqu’un délimiteur personnalisé est nécessaire).
3. **Instancer le WorkbookDesigner** : Créez un `WorkbookDesigner` autour du classeur et associez votre liste à l’aide de `setDataSource`.
4. **Traiter les marqueurs** : Appelez la méthode `WorkbookDesigner.process()` pour développer les marqueurs intelligents et renseigner le classeur avec les données réelles.
5. **Enregistrer le résultat** : Enregistrez le classeur obtenu sur le disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu d’un tableau de chaînes simple**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    // The bean must be public and expose a getter; public fields bind nothing
    public static class Product {
        private String[] tags;
        public String[] getTags() { return tags; }
        public void setTags(String[] tags) { this.tags = tags; }
    }

    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.setTags(new String[] { "C#", "Aspose", "SmartMarker", "Excel" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Product", Arrays.asList(product));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-single.xlsx");
    }
}
```

L’exemple imprime la valeur concaténée de l’ensemble du tableau. Les quatre étiquettes sont placées dans une seule cellule, séparées par la virgule par défaut :

```
C#,Aspose,SmartMarker,Excel
```

### **Exemple de code 2 — Valeurs numériques avec un délimiteur personnalisé**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Student {
        private String[] scores;
        public String[] getScores() { return scores; }
        public void setScores(String[] scores) { this.scores = scores; }
    }

    public static void main(String[] args) throws Exception {
        Student student = new Student();
        student.setScores(new String[] { "95", "88", "76", "100", "67" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Scores");
        // arraydelimiter:- joins the values with a hyphen
        worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Student", Arrays.asList(student));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-numeric.xlsx");
    }
}
```

Tout comme les chaînes, les valeurs numériques sont concaténées de la même manière lorsque la propriété de tableau renvoie un `String[]` :

```
95-88-76-100-67
```

{{% alert color="note" %}}
En Java, conservez la propriété de tableau sous forme de `String[]`. Une propriété primitive de type `int[]`, concaténée dans une seule cellule, restitue la représentation textuelle de l’objet de tableau via `toString` (par exemple `[I@1a2b3c4d`) au lieu des nombres, car la concaténation s’applique à la forme textuelle de chaque élément et qu’un tableau primitif constitue un seul élément opaque.
{{% /alert %}}

### **Exemple de code 3 — Comparaison du rendu par défaut et du rendu dans une seule cellule**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Order {
        private String[] items;
        public String[] getItems() { return items; }
        public void setItems(String[] items) { this.items = items; }
    }

    public static void main(String[] args) throws Exception {
        Order order = new Order();
        order.setItems(new String[] { "Apple", "Banana", "Cherry", "Date" });
        Workbook workbook = new Workbook();
        Cells cells = workbook.getWorksheets().get(0).getCells();
        // Column B: default marker — values spread vertically down the column
        cells.get("B1").putValue("Default");
        cells.get("B2").putValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells.get("C1").putValue("Single cell");
        cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Order", Arrays.asList(order));
        designer.process();
        for (int row = 1; row <= 5; row++) {
            String b = cells.get(row, 1).getStringValue();
            String c = cells.get(row, 2).getStringValue();
            if (b != null && !b.isEmpty() || c != null && !c.isEmpty())
                System.out.println("B" + (row + 1) + "=[" + b + "]  C" + (row + 1) + "=[" + c + "]");
        }
        workbook.save("output-array-comparison.xlsx");
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

Gardez les points suivants à l’esprit lorsque vous travaillez avec les attributs `arrayassingle` et `arraydelimiter` :
- Les valeurs d’attribut utilisent la forme `name:value`. Une forme avec un signe égal, telle que `arrayassingle=true`, n’est pas reconnue et le moteur revient silencieusement au comportement de déploiement par défaut.
- Séparez les attributs par une virgule et sans espaces ; un espace après la virgule décale la valeur du délimiteur d’un caractère (voir l’avertissement ci-dessus).
- La valeur `arraydelimiter` peut être un caractère unique écrit directement après les deux-points, ou une chaîne multicaractère entourée de guillemets doubles.
- Lorsque `arraydelimiter` est omis, les éléments sont concaténés avec une virgule.
- Liez une `java.util.List` de JavaBeans publics munis d’accesseurs de tableau. Un seul objet JavaBean ou des champs publics seuls laissent les marqueurs non résolus.
- Conservez les propriétés de tableau sous forme de `String[]` ; un `int[]` primitif restitue sa représentation textuelle via `toString` lors de la concaténation (voir la note ci-dessus).
- Placez le marqueur intelligent dans une cellule suffisamment large pour afficher la chaîne concaténée obtenue ; sinon, le contenu peut déborder visuellement dans les cellules adjacentes selon le format.

## **Articles connexes**
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for Java](/cells/fr/java/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for Java](/cells/fr/java/apply-style-to-pivot-table/)
- [Modifier la disposition du champ de page dans un tableau croisé dynamique](/cells/fr/java/change-page-field-layout/)
- [Convertir une sparkline en image et en HTML avec Aspose.Cells for Java](/cells/fr/java/convert-sparkline-to-image-and-html/)
- [Conversion d'Excel au format OFD](/cells/fr/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}