---
title: Rendu de tableau à cellule unique avec SmartMarker | Aspose.Cells for Node.js via C++
linktitle: Rendu de tableau
description: Apprenez à rendre les données de tableau dans une seule cellule à l'aide des attributs ArrayAsSingle et ExtraDelimiter dans les marqueurs intelligents avec Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, bibliothèque Node.js, feuille de calcul, marqueurs intelligents, ArrayAsSingle, ExtraDelimiter, tableau à cellule unique, rendu de tableau, modèle
type: docs
weight: 195
url: /fr/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge le rendu des données de tableau dans une seule cellule via les marqueurs intelligents. En utilisant l'attribut `ArrayAsSingle` conjointement avec l'attribut `ExtraDelimiter`, les développeurs peuvent contrôler la façon dont les éléments du tableau sont séparés dans une seule cellule, offrant ainsi une mise en forme flexible pour les rapports et les modèles.

{{% /alert %}}

## **Introduction**

Les marqueurs intelligents dans Aspose.Cells sont une fonctionnalité puissante basée sur des modèles qui vous permet de remplir dynamiquement des données de feuille de calcul à l'aide d'expressions de marqueurs telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur concepteur, et lorsque le modèle est traité par le `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs provenant de la source de données fournie.

Par défaut, lorsqu'un marqueur intelligent référence une propriété de tableau (par exemple, `&=DataSource.Numbers`), le moteur étend le tableau et place chaque élément dans une cellule adjacente distincte — soit horizontalement sur une ligne, soit verticalement sur une colonne. Bien que ce comportement soit pratique dans de nombreux scénarios, il existe des situations où vous préférerez rendre le tableau entier dans une seule cellule, avec les éléments concaténés et séparés par un délimiteur de votre choix.

Les attributs `ArrayAsSingle` et `ExtraDelimiter`, utilisés ensemble à l'intérieur d'une balise de marqueur intelligent, répondent exactement à cette exigence. Ils vous permettent de conserver des mises en page de rapport compactes et prévisibles tout en travaillant nativement avec des sources de données de tableau.

## **Pourquoi cette fonctionnalité est nécessaire**

### **Comportement par défaut d'extension du tableau**

Lorsqu'un marqueur intelligent référence une propriété de tableau, Aspose.Cells étend le tableau sur plusieurs cellules par défaut. Par exemple, un marqueur tel que `&=Product.Tags` appliqué à un `string[]` contenant quatre valeurs placera chaque valeur dans sa propre cellule, repoussant le reste du contenu du modèle vers l'extérieur et pouvant potentiellement perturber des mises en page de rapport soigneusement conçues.

### **Limitations des cas d'utilisation**

Il existe de nombreux scénarios pratiques où le comportement d'extension par défaut est indésirable :

- **Rapports de type résumé** qui nécessitent une mise en page compacte d'une ligne par enregistrement.
- **Listes de balises, d'étiquettes ou de mots-clés** qui doivent être affichées sous forme de valeurs séparées par des virgules ou des barres obliques dans une seule cellule.
- **Puces de filtre ou indicateurs d'état** qui regroupent plusieurs valeurs en un seul endroit pour une meilleure lisibilité.
- **Pipelines en aval** (exportation CSV, rendu PDF, publipostage) qui attendent une valeur consolidée unique par cellule plutôt qu'une plage étendue.
- **Compatibilité multiplateforme**, où certains consommateurs ne peuvent pas tolérer des tableaux qui se répandent sur plusieurs cellules.

### **La lacune qu'elle comble**

Sans mécanisme intégré, les développeurs seraient contraints de prétraiter les données en JavaScript — en joignant les tableaux en chaînes délimitées avant de les lier au concepteur de classeur. Cela duplique la logique, complique les modèles de données et augmente le risque d'erreurs. Les attributs `ArrayAsSingle` et `ExtraDelimiter` éliminent cette solution de contournement en gérant la mise en forme de manière déclarative à l'intérieur du marqueur intelligent lui-même.

## **Avantages de la fonctionnalité**

L'utilisation des attributs `ArrayAsSingle` et `ExtraDelimiter` dans vos marqueurs intelligents offre plusieurs avantages :

- **Confinement dans une seule cellule** : tous les éléments du tableau sont rendus dans exactement une seule cellule, ce qui maintient les mises en page compactes et prévisibles.
- **Contrôle personnalisé du délimiteur** : spécifiez n'importe quelle chaîne de séparation — virgule, point-virgule, trait d'union, barre oblique, retour à la ligne, ou tout texte personnalisé.
- **Mise en forme pilotée par modèle** : aucun code supplémentaire n'est requis pour prétraiter les données ; les règles de mise en forme se trouvent à l'intérieur de la balise du marqueur intelligent.
- **Rapports plus propres** : les données du tableau ne poussent plus le contenu du modèle voisin dans des lignes ou des colonnes différentes.
- **Types de données polyvalents** : fonctionne avec les chaînes, les nombres, les dates et tout autre type de données pouvant être joint avec un délimiteur.
- **Rétrocompatibilité** : lorsque les attributs sont omis, le comportement d'extension d'origine est préservé, de sorte que les modèles existants continuent de fonctionner sans modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe du marqueur intelligent**

Les attributs `ArrayAsSingle` et `ExtraDelimiter` sont passés sous forme de paires clé-valeur à l'intérieur des parenthèses d'un marqueur intelligent standard. La syntaxe générale est :

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Le marqueur est composé des parties suivantes :

- `&=DataSource.ArrayProperty` — le marqueur intelligent standard référençant la propriété de tableau sur la source de données liée.
- `arrayasSingle=true` — indique au moteur de rendre le tableau entier dans une seule cellule. Seule la valeur `true` déclenche le comportement de cellule unique.
- `extraDelimiter=", "` — définit le séparateur placé entre les éléments du tableau. La valeur est un littéral de chaîne ; elle peut être vide, un caractère unique ou une chaîne de plusieurs caractères.

{{% alert color="primary" %}}

L'attribut `extraDelimiter` accepte tout littéral de chaîne, y compris des délimiteurs à plusieurs caractères, du texte personnalisé ou des séquences d'échappement telles que `\n` pour une sortie séparée par des retours à la ligne. Si le tableau est vide, la cellule résultante est laissée vide.

{{% /alert %}}

### **Flux de travail étape par étape**

Le flux de travail suivant décrit comment rendre un tableau dans une seule cellule à l'aide des marqueurs intelligents.

1. **Préparer la source de données** : créez une classe (ou une structure de données) qui expose une propriété retournant un tableau. La propriété peut retourner `string[]`, `int[]` ou tout autre type de tableau pris en charge.
2. **Créer un classeur concepteur** : créez un nouveau `Workbook`, ajoutez une ligne d'en-tête et placez une cellule de marqueur intelligent qui référence la propriété de tableau avec les attributs `arrayasSingle` et `extraDelimiter`.
3. **Instancier le WorkbookDesigner** : créez un objet `WorkbookDesigner`, attachez-lui le classeur concepteur et liez votre source de données à l'aide de la méthode `setDataSource`.
4. **Traiter les marqueurs** : appelez la méthode `workbookDesigner.process()` pour étendre les marqueurs intelligents et remplir le classeur avec les données réelles.
5. **Enregistrer le résultat** : enregistrez le classeur résultant sur le disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu de tableau de chaînes de base**

```javascript
let product = {
    Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
};

let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue('&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")');

let designer = new AsposeCells.WorkbookDesigner();
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

### **Exemple de code 3 — Comparaison du comportement par défaut et du comportement ArrayAsSingle**

```javascript
var order = {
    Items: ["Apple", "Banana", "Cherry", "Date"]
};

var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Section 1 : Smart Marker par défaut - valeurs réparties horizontalement dans les cellules
cells.get("A1").putValue("Default Spreading Behavior:");
cells.get("A2").putValue("&=Order.Items");

// Section 2 : Nouveau rendu en cellule unique utilisant arrayasSingle et extraDelimiter
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

// Lier la source de données et traiter les Smart Markers
var designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setDataSource("Order", order);
designer.process();

// Enregistrer le classeur résultant
workbook.save("output_comparison.xlsx");
```

### **Remarques et bonnes pratiques**

Gardez les points suivants à l'esprit lorsque vous travaillez avec les attributs `ArrayAsSingle` et `ExtraDelimiter` :

- La valeur `extraDelimiter` est traitée comme un littéral de chaîne ; échappez tous les caractères spéciaux que votre processeur de modèle pourrait interpréter.
- L'attribut `arrayasSingle` accepte une valeur booléenne (`true` / `false`). Seule la valeur `true` déclenche le comportement de cellule unique ; toute autre valeur revient au comportement d'extension par défaut.
- Si le tableau est vide ou null, la cellule est laissée vide (ou contient une chaîne vide selon le type de données).
- La fonctionnalité fonctionne avec des sources de données d'objets ainsi qu'avec des sources `DataSet` et `DataTable` où une colonne peut être divisée en tableaux.
- Pour une sortie séparée par des retours à la ligne, vous pouvez utiliser `\n` ou `os.EOL` comme valeur de délimiteur.
- Placez le marqueur intelligent dans une cellule dont la largeur est suffisante pour afficher la chaîne concaténée résultante ; sinon, le contenu peut visuellement déborder dans les cellules adjacentes en fonction du format.

## **Articles connexes**

- [Fusionner et annuler la fusion de cellules](/cells/fr/nodejs-cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="javascript" >}}