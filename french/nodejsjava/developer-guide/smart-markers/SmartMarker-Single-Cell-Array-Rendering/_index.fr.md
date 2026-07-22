---
title: Rendu de tableau dans une seule cellule avec SmartMarker | Aspose.Cells for Node.js via Java
linktitle: Rendu de tableau dans une seule cellule avec SmartMarker | Aspose.Cells
description: Apprenez à rendre les données de tableau dans une seule cellule à l'aide des attributs ArrayAsSingle et ExtraDelimiter dans les Smart Markers avec Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, bibliothèque Node.js via Java, feuille de calcul, Smart Markers, ArrayAsSingle, ExtraDelimiter, tableau cellule unique, rendu de tableau, modèle
type: docs
weight: 195
url: /fr/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge le rendu des données de tableau dans une seule cellule via les Smart Markers. En utilisant l'attribut `ArrayAsSingle` conjointement avec l'attribut `ExtraDelimiter`, les développeurs peuvent contrôler la manière dont les éléments du tableau sont séparés au sein d'une seule cellule, offrant ainsi une mise en forme flexible pour les rapports et les modèles.

{{% /alert %}}

## **Introduction**

Les Smart Markers dans Aspose.Cells constituent une fonctionnalité puissante, basée sur des modèles, qui vous permet de remplir dynamiquement les données d'une feuille de calcul à l'aide d'expressions de marqueurs telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur de conception, et lorsque le modèle est traité par le `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs issues de la source de données fournie.

Par défaut, lorsqu'un Smart Marker fait référence à une propriété de tableau (par exemple, `&=DataSource.Numbers`), le moteur étend le tableau et place chaque élément dans une cellule adjacente distincte — soit horizontalement sur une ligne, soit verticalement dans une colonne. Bien que ce comportement soit pratique dans de nombreux scénarios, il existe des situations où vous préférerez rendre l'ensemble du tableau dans une seule cellule, avec les éléments concaténés et séparés par un délimiteur de votre choix.

Les attributs `ArrayAsSingle` et `ExtraDelimiter`, utilisés ensemble à l'intérieur d'une balise Smart Marker, répondent précisément à cette exigence. Ils vous permettent de garder des mises en page de rapport compactes et prévisibles tout en travaillant nativement avec des sources de données de type tableau.

## **Pourquoi cette fonctionnalité est nécessaire**

### **Comportement par défaut d'expansion du tableau**

Lorsqu'un Smart Marker fait référence à une propriété de tableau, Aspose.Cells étend par défaut le tableau sur plusieurs cellules. Par exemple, un marqueur tel que `&=Product.Tags` appliqué à un `string[]` contenant quatre valeurs placera chaque valeur dans sa propre cellule, repoussant le reste du contenu du modèle vers l'extérieur et pouvant potentiellement briser des mises en page de rapport soigneusement conçues.

### **Limites des cas d'utilisation**

Il existe de nombreux scénarios pratiques où le comportement d'expansion par défaut n'est pas souhaitable :

- **Rapports de type résumé** qui nécessitent une disposition compacte d'une ligne par enregistrement.
- **Listes d'étiquettes, de mots-clés ou de tags** qui doivent être affichées sous forme de valeurs séparées par des virgules ou des barres verticales dans une seule cellule.
- **Pastilles de filtre ou indicateurs d'état** qui regroupent plusieurs valeurs en un seul endroit pour une meilleure lisibilité.
- **Pipelines en aval** (export CSV, rendu PDF, publipostage) qui attendent une valeur consolidée unique par cellule plutôt qu'une plage étendue.
- **Compatibilité multiplateforme**, où certains consommateurs ne peuvent pas tolérer des tableaux qui se répandent sur plusieurs cellules.

### **Le manque qu'elle comble**

Sans mécanisme intégré, les développeurs seraient contraints de prétraiter les données en JavaScript — en joignant les tableaux en chaînes délimitées avant de les lier au concepteur de classeur. Cela duplique la logique, complique les modèles de données et augmente le risque d'erreurs. Les attributs `ArrayAsSingle` et `ExtraDelimiter` éliminent ce contournement en gérant la mise en forme de manière déclarative à l'intérieur du Smart Marker lui-même.

## **Avantages de la fonctionnalité**

L'utilisation des attributs `ArrayAsSingle` et `ExtraDelimiter` dans vos Smart Markers présente plusieurs avantages :

- **Confinement dans une seule cellule** : tous les éléments du tableau sont rendus dans exactement une seule cellule, ce qui maintient des mises en page compactes et prévisibles.
- **Contrôle personnalisé du délimiteur** : spécifiez n'importe quelle chaîne de séparation de votre choix — virgule, point-virgule, trait d'union, barre verticale, retour à la ligne, ou tout texte personnalisé.
- **Mise en forme pilotée par le modèle** : aucun code supplémentaire n'est requis pour prétraiter les données ; les règles de mise en forme se trouvent dans la balise du Smart Marker.
- **Rapports plus propres** : les données de tableau ne poussent plus le contenu voisin du modèle dans des lignes ou des colonnes différentes.
- **Types de données polyvalents** : fonctionne avec les chaînes, les nombres, les dates et tout autre type de données pouvant être joint avec un délimiteur.
- **Rétrocompatibilité** : lorsque les attributs sont omis, le comportement d'expansion d'origine est préservé, de sorte que les modèles existants continuent de fonctionner sans modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe du Smart Marker**

Les attributs `ArrayAsSingle` et `ExtraDelimiter` sont passés sous forme de paires clé-valeur à l'intérieur des parenthèses d'un Smart Marker standard. La syntaxe générale est :

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Le marqueur est composé des parties suivantes :

- `&=DataSource.ArrayProperty` — le Smart Marker standard référençant la propriété de tableau sur la source de données liée.
- `arrayasSingle=true` — indique au moteur de rendre l'ensemble du tableau dans une seule cellule. Seule la valeur `true` déclenche le comportement de cellule unique.
- `extraDelimiter=", "` — définit le séparateur placé entre les éléments du tableau. La valeur est une chaîne littérale ; elle peut être vide, un seul caractère, ou une chaîne de plusieurs caractères.

{{% alert color="primary" %}}

L'attribut `extraDelimiter` accepte n'importe quelle chaîne littérale, y compris des délimiteurs de plusieurs caractères, du texte personnalisé, ou des séquences d'échappement telles que `\n` pour une sortie séparée par des retours à la ligne. Si le tableau est vide, la cellule résultante est laissée vide.

{{% /alert %}}

### **Flux de travail étape par étape**

Le flux de travail suivant décrit comment rendre un tableau dans une seule cellule à l'aide des Smart Markers.

1. **Préparez la source de données** : créez une classe (ou une structure de données) qui expose une propriété renvoyant un tableau. La propriété peut renvoyer `string[]`, `int[]`, ou tout autre type de tableau pris en charge.
2. **Créez un classeur de conception** : créez un nouveau `Workbook`, ajoutez une ligne d'en-tête, et placez une cellule Smart Marker qui référence la propriété de tableau avec les attributs `arrayasSingle` et `extraDelimiter`.
3. **Instanciez le WorkbookDesigner** : créez un objet `WorkbookDesigner`, attachez-lui le classeur de conception, et liez votre source de données à l'aide de la méthode `setDataSource`.
4. **Traitez les marqueurs** : appelez la méthode `workbookDesigner.process()` pour étendre les Smart Markers et peupler le classeur avec des données réelles.
5. **Enregistrez le résultat** : enregistrez le classeur résultant sur disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu de tableau de chaînes de base**

```javascript
class Product {
    constructor() {
        this.Tags = null;
    }
}

const product = new Product();
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

const designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");
```

### **Exemple de code 2 — Tableau numérique avec délimiteur personnalisé**

```javascript
class Student {
    constructor() {
        this.Scores = [];
    }
}

const student = new Student();
student.Scores = [95, 88, 76, 100, 67];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Scores");
worksheet.getCells().get("A2").putValue(student.Scores.join(" - "));

workbook.save("output_numericArray.xlsx");
```

### **Exemple de code 3 — Comparaison du comportement par défaut et d'ArrayAsSingle**

```javascript
const AsposeCells = require("aspose.cells");

function main() {
    const order = {
        Items: ["Apple", "Banana", "Cherry", "Date"]
    };

    const workbook = new AsposeCells.Workbook();
    const sheet = workbook.getWorksheets().get(0);
    const cells = sheet.getCells();

    // Section 1 : Smart Marker par défaut - valeurs réparties horizontalement dans les cellules
    cells.get("A1").putValue("Default Spreading Behavior:");
    cells.get("A2").putValue("&=Order.Items");

    // Section 2 : Nouveau rendu en cellule unique utilisant arrayasSingle et extraDelimiter
    cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
    cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // Lier la source de données et traiter les Smart Markers
    const designer = new AsposeCells.WorkbookDesigner(workbook);
    designer.setDataSource("Order", order);
    designer.process();

    // Enregistrer le classeur résultant
    workbook.save("output_comparison.xlsx");
}

main();
```

### **Remarques et bonnes pratiques**

Gardez à l'esprit les points suivants lorsque vous travaillez avec les attributs `ArrayAsSingle` et `ExtraDelimiter` :

- La valeur de `extraDelimiter` est traitée comme une chaîne littérale ; échappez tout caractère spécial que votre processeur de modèle pourrait interpréter.
- L'attribut `arrayasSingle` accepte une valeur booléenne (`true` / `false`). Seul `true` déclenche le comportement de cellule unique ; toute autre valeur retombe sur le comportement d'expansion par défaut.
- Si le tableau est vide ou null, la cellule est laissée vide (ou contient une chaîne vide selon le type de données).
- La fonctionnalité fonctionne avec des sources de données d'objets ainsi qu'avec les sources `DataSet` et `DataTable` où une colonne peut être divisée en tableaux.
- Pour une sortie séparée par des retours à la ligne, vous pouvez utiliser `\n` comme valeur de délimiteur.
- Placez le Smart Marker dans une cellule dont la largeur est suffisante pour afficher la chaîne concaténée résultante ; sinon, le contenu peut visuellement déborder dans les cellules adjacentes selon le format.



{{< app/cells/assistant language="javascript" >}}