---
title: Rendu de tableau dans une seule cellule avec SmartMarker | Aspose.Cells for Node.js via Java
description: Découvrez comment rendre des données de tableau dans une seule cellule à l’aide des attributs Smart Marker arrayassingle et arraydelimiter dans Aspose.Cells for Node.js via Java.
linktitle: Rendu dans une seule cellule avec SmartMarker | Aspose.Cells for Node.js via Java
url: /fr/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, bibliothèque Node.js via Java, tableur, Smart Markers, arrayassingle, arraydelimiter, tableau dans une seule cellule, rendu de tableau, modèle
type: docs
weight: 195
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells peut rendre les données d’un tableau dans une seule et même cellule à l’aide des Smart Markers. L’attribut `arrayassingle` désactive la répartition par défaut, élément par élément, et l’attribut `arraydelimiter` choisit le séparateur placé entre les éléments concaténés — une virgule par défaut, ou tout caractère unique ou chaîne multicaractère entre guillemets que vous spécifiez.
{{% /alert %}}

## **Introduction**

Les Smart Markers d’Aspose.Cells sont une fonctionnalité fondée sur les modèles qui remplit dynamiquement les données du tableur à l’aide d’expressions de marqueur telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur modèle. Lorsque ce modèle est traité par `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs de la source de données fournie.
Par défaut, lorsqu’un Smart Marker référence un champ de tableau (par exemple, `&=Product.Tags` lié à un tableau de quatre valeurs), le moteur développe le tableau et place chaque élément dans sa propre cellule, en répartissant les valeurs verticalement dans la colonne sous le marqueur. Bien que ce comportement soit pratique dans de nombreux scénarios, certaines situations nécessitent plutôt de rendre le tableau entier dans une seule cellule, avec les éléments concaténés et séparés par un délimiteur de votre choix.
Les attributs `arrayassingle` et `arraydelimiter`, écrits entre les parenthèses d’un Smart Marker sous la forme `name:value`, répondent précisément à ce besoin. Ils vous permettent de conserver des mises en page de rapport compactes et prévisibles tout en utilisant nativement des sources de données de tableau.

## **Pourquoi cette fonctionnalité est nécessaire**

### **Comportement par défaut de répartition des tableaux**

Lorsqu’un Smart Marker référence un champ de tableau, Aspose.Cells développe le tableau dans plusieurs cellules par défaut. Par exemple, un marqueur tel que `&=Product.Tags`, associé à un tableau contenant quatre valeurs, place chaque valeur dans sa propre cellule sous le marqueur, ce qui décale le reste du contenu du modèle et peut compromettre des mises en page de rapport soigneusement conçues.

### **Limites des cas d’utilisation**

Il existe de nombreux scénarios pratiques dans lesquels le comportement de répartition par défaut est uniquement biopsies :
- **Rapports de type synthèse** qui nécessitent une disposition compacte avec une ligne par enregistrement.
- **Listes de tags, d’étiquettes ou de mots-clés** qui doivent être affichées sous forme de valeurs séparées par des virgules ou des barres verticales dans une seule cellule.
- **Puces de filtre ou indicateurs d’état** qui regroupent plusieurs valeurs en un seul endroit pour améliorer la lisibilité.
- **Chaînes de traitement en aval** (export CSV, rendu PDF, fusion de courrier) qui attendent une valeur consolidée par cellule plutôt qu’une plage développée.
- **Compatibilité multiplateforme**, où certains consommateurs ne peuvent pas accepter des tableaux qui s’étendent sur plusieurs cellules.

### **L’écart comblé**

Sans mécanisme intégré, les développeurs seraient obligés de prétraiter les données en JavaScript — en concaténant les tableaux en chaînes délimitées avant de les lier au concepteur de classeur. Cette approche duplique la logique, complique les modèles de données et augmente les risques d’erreur. Les attributs `arrayassingle` et `arraydelimiter` éliminent ce contournement en gérant la mise en forme de manière déclarative dans le Smart Marker lui-même.

## **Avantages de la fonctionnalité**

L’utilisation des attributs `arrayassingle` et `arraydelimiter` dans vos Smart Markers présente plusieurs avantages :
- **Confinement dans une seule cellule** : Tous les éléments du tableau sont rendus dans une seule cellule, ce qui rend les mises en page compactes et prévisibles.
- **Contrôle du délimiteur personnalisé** : Spécifiez le séparateur de votre choix — la virgule par défaut, un point-virgule, un trait d’union, une barre verticale ou une chaîne multicaractère entre guillemets telle que `" | "`.
- **Mise en forme pilotée par le modèle** : Aucun code supplémentaire n’est nécessaire pour prétraiter les données ; les règles de mise en forme sont intégrées à la balise Smart Marker.
- **Rapports plus propres** : Les données de tableau ne déplacent plus le contenu voisin du modèle vers d’autres lignes ou colonnes.
- **Types de données polyvalents** : Fonctionne avec des tableaux de chaînes fournis sous forme de lignes JSON, y compris des valeurs numériques rendues sous forme de chaînes.
- **Compatibilité ascendante** : Lorsque les attributs sont omis, le comportement de répartition d’origine est conservé, de sorte que les modèles existants continuent de fonctionner sans modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe du Smart Marker**

Les attributs `arrayassingle` et `arraydelimiter` utilisent la grammaire d’attributs `name:value` d’Aspose.Cells entre les parenthèses d’un Smart Marker standard. La syntaxe générale est :

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

Le marqueur est composé des éléments suivants :
- `&=DataSource.ArrayField` — le Smart Marker standard qui référence le champ de tableau de la source de données liée.
- `arrayassingle:true` — indique au moteur de rendre le tableau entier dans une seule cellule au lieu de répartir ses éléments.
- `arraydelimiter:;` — facultatif ; définit le séparateur placé entre les éléments du tableau. Lorsqu’il est omis, une virgule est utilisée.

{{% alert color="warning" %}}
Écrivez les attributs sous la forme `name:value` (un deux-points, pas un signe égal) et séparez plusieurs attributs par une virgule **sans espaces**. Un espace après la virgule décale la valeur analysée d’un caractère — `(arrayassingle:true, arraydelimiter:;)` concaténerait les éléments avec le séparateur erroné `:;` au lieu de `;`.
{{% /alert %}}

### **Formes du délimiteur**

- Un caractère unique est placé directement après le deux-points : `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Un séparateur multicaractère s’écrit entre guillemets doubles : `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Flux de travail étape par étape**

Le flux de travail ci-dessous explique comment rendre un tableau dans une seule cellule à l’aide des Smart Markers.
1. **Préparer la source de données** : Structurez chaque enregistrement sous forme d’objet JSON dont un champ contient un tableau, par exemple `{"Tags": ["C#", "Aspose"]}`. Les objets et tableaux JavaScript ordinaires transmis à `setDataSource` ne sont pas associés sur cette plateforme ; les lignes JSON constituent la forme tabulaire prise en charge.
2. **Créer un classeur modèle** : Créez un nouvel objet `Workbook`, ajoutez une ligne d’en-tête et placez dans une cellule un Smart Marker qui référence le champ de tableau avec l’attribut `arrayassingle` (et `arraydelimiter` lorsqu’un séparateur personnalisé est nécessaire).
3. **Instancier le WorkbookDesigner** : Créez un objet `WorkbookDesigner` autour du classeur et associez vos lignes JSON à l’aide de `setJsonDataSource`.
4. **Traiter les marqueurs** : Appelez la méthode `workbookDesigner.process()` pour développer les Smart Markers et remplir le classeur avec les données réelles.
5. **Enregistrer le résultat** : Enregistrez le classeur obtenu sur le disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu d’un tableau de chaînes**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Tags");
// No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-single.xlsx");
```

L’exemple affiche la valeur concaténée du tableau entier. Les quatre tags arrivent dans une seule cellule, séparés par la virgule par défaut :

```
C#,Aspose,SmartMarker,Excel
```

### **Exemple de code 2 — Valeurs numériques avec un délimiteur personnalisé**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Scores");
// arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-numeric.xlsx");
```

Lorsque les scores sont fournis sous forme de chaînes JSON, la sortie concaténée conserve les nombres bruts :

```
95-88-76-100-67
```

{{% alert color="note" %}}
Les nombres JSON transmis via le moteur Java arrivent sous forme de nombres doubles ; ainsi, `[95, 88]` serait concaténé en `95.0-88.0`. Placez les nombres entre guillemets dans les lignes JSON si vous souhaitez obtenir le texte exact des entiers dans la cellule concaténée.
{{% /alert %}}

### **Exemple de code 3 — Comparaison du rendu par défaut et du rendu dans une seule cellule**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();
// Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default");
cells.get("B2").putValue("&=Order.Items");
// Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell");
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]');
designer.process();
for (let row = 1; row <= 5; row++) {
    const b = cells.get(row, 1).getStringValue() || "";
    const c = cells.get(row, 2).getStringValue() || "";
    if (b || c) console.log(`B${row + 1}=[${b}]  C${row + 1}=[${c}]`);
}
workbook.save("output-array-comparison.xlsx");
```

Le marqueur par défaut remplit une cellule par élément dans la colonne B, tandis que le marqueur `arrayassingle` condense le même tableau dans une seule cellule de la colonne C :

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notes et bonnes pratiques**

Gardez les points suivants à l’esprit lorsque vous utilisez les attributs `arrayassingle` et `arraydelimiter` :
- Les valeurs d’attribut utilisent la forme `name:value`. Une forme avec signe égal, telle que `arrayassingle=true`, n’est pas reconnue et revient silencieusement au comportement de répartition par défaut.
- Séparez les attributs par une virgule sans espace ; un espace après la virgule décale la valeur du délimiteur d’un caractère (voir l’avertissement ci-dessus).
- La valeur `arraydelimiter` peut être un caractère unique écrit directement après le deux-points ou une chaîne multicaractère entourée de guillemets doubles.
- Lorsque `arraydelimiter` est omis, les éléments sont concaténés par une virgule.
- Fournissez les champs de tableau via les objets de ligne `setJsonDataSource` ; les objets et tableaux JavaScript ordinaires transmis à `setDataSource` ne sont pas associés sur cette plateforme.
- Les nombres JSON arrivent sous forme de nombres doubles via le moteur Java (`95` est concaténé en `95.0`) ; placez les valeurs numériques entre guillemets dans les lignes JSON si le texte exact des entiers est important.
- Placez le Smart Marker dans une cellule assez large pour afficher la chaîne concaténée résultante ; sinon, le contenu peut déborder visuellement dans les cellules adjacentes, selon le format.

## **Articles connexes**
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for Node.js via Java](/cells/fr/nodejs-java/add-page-field-in-pivot-table/)
- [Appliquer des styles aux Tableaux Croisés Dynamiques dans Aspose.Cells for Node.js via Java](/cells/fr/nodejs-java/apply-style-to-pivot-table/)
- [Modifier la disposition du champ de page dans un tableau croisé dynamique](/cells/fr/nodejs-java/change-page-field-layout/)
- [Convertir un sparkline en image et en HTML dans Aspose.Cells for Node.js via Java](/cells/fr/nodejs-java/convert-sparkline-to-image-and-html/)
- [Conversion d'Excel au format OFD](/cells/fr/nodejs-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="nodejs-java" >}}