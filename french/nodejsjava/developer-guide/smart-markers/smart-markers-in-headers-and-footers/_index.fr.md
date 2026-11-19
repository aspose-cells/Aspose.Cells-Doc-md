---
title: Smart Markers dans les en-têtes et pieds de page | Aspose.Cells for Node.js via Java
linktitle: Marqueurs d’en-tête et de pied de page | Aspose.Cells for Node.js via Java
description: Placez des espaces réservés Smart Marker dans les en-têtes et pieds de page des pages à l’aide de la syntaxe à doubles chevrons et du commutateur WorkbookDesigner.setEnableHeaderFooterMarkers utilisant des sources de données JSON, et liez des images via des URI de données, dans Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells for Node.js via Java, Smart Markers, en-têtes, pieds de page, marqueurs d’en-tête et pied de page, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, lignes JSON, liaison de données, image, URI de données, JavaScript
type: docs
weight: 196
url: /fr/nodejs-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Les en-têtes et les pieds de page contiennent souvent des métadonnées de rapport telles que le titre du rapport, la période du rapport, l’auteur et le département. Lorsque ces informations existent déjà dans la source de données utilisée pour remplir le classeur, les répéter manuellement crée une duplication inutile.
La syntaxe classique Smart Marker, `&=Source.Field`, est traitée dans les cellules du corps de la feuille de calcul. Si vous placez un marqueur classique dans un en-tête ou un pied de page via `PageSetup.setHeader` ou `PageSetup.setFooter`, il reste du texte littéral car les chaînes d’en-tête et de pied de page ne font pas partie de la grille de cellules de la feuille scannée par `WorkbookDesigner.process()`.
À partir de **Aspose.Cells for Node.js via Java 26.11**, le paramètre `WorkbookDesigner.setEnableHeaderFooterMarkers`, qui est `false` par défaut, fait que `process()` résout les espaces réservés écrits sous la forme `<<Source.Field>>` dans les chaînes des sections d’en-tête et de pied de page. Appelez `designer.setEnableHeaderFooterMarkers(true)` avant d’appeler `process()`. Les espaces réservés d’en-tête et de pied de page utilisent la même source de données que les marqueurs du corps.
Chaque en-tête et pied de page contient trois sections adressables :
- Section `0` correspond à la section gauche.
- Section `1` correspond à la section centrale.
- Section `2` correspond à la section droite.
Utilisez `PageSetup.setHeader(int section, String value)` et `PageSetup.setFooter(int section, String value)` pour écrire ces sections. Après le traitement, utilisez `PageSetup.getHeader(int section)` et `PageSetup.getFooter(int section)` pour récupérer le texte complet.

{{% alert color="primary" %}}
Un espace réservé tel que `<<Source.Field>>` insère la valeur du champ sous forme de texte dans la chaîne de la section. Les images sont liées avec le suffixe `(picture)` et une valeur URI de données.
{{% /alert %}}

## **Activer les marqueurs d’en-tête/pied de page avec des données de lignes JSON**
Utilisez la séquence suivante pour résoudre les espaces réservés d’en-tête et de pied de page avec des données de lignes JSON dans **Aspose.Cells for Node.js via Java 26.11** :
1. Créez un `Workbook` et obtenez sa première `Worksheet` avec `workbook.getWorksheets().get(0)`.
2. Écrivez les espaces réservés `<<Source.Field>>` dans les sections d’en-tête et de pied de page souhaitées à l’aide de `PageSetup.setHeader` et `PageSetup.setFooter`.
3. Préparez les données de lignes sous forme d’un tableau JSON d’objets de ligne, et choisissez un nom de source qui correspond au préfixe utilisé par les espaces réservés. Par exemple, une source nommée `node` alimente les espaces réservés tels que `<<node.Name>>`. Les objets JavaScript simples et les tableaux passés à `setDataSource` ne se lient pas sur cette plateforme — le JSON est la forme tabulaire prise en charge.
4. Créez un `WorkbookDesigner` pour le classeur.
5. Appelez `designer.setEnableHeaderFooterMarkers(true)` avant le traitement.
6. Attachez le JSON avec `designer.setJsonDataSource("node", '[{"Name":"...","Author":"..."}]')`.
7. Appelez `designer.process()`.
8. Après le traitement, les espaces réservés ne sont plus présents dans le texte d’en-tête ou de pied de page. Utilisez `getHeader` et `getFooter` pour récupérer les chaînes de sections complètes.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource(
  "node",
  '[{"Name":"Q4 2026","Author":"Aspose.Cells"}]'
);
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
console.log("Footer: " + worksheet.getPageSetup().getFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx");
```

## **Utiliser une source de données JSON**
Lorsque les données du rapport sont déjà disponibles sous forme de JSON, un appel à `setJsonDataSource` peut alimenter chaque style de marqueur. Appelez `WorkbookDesigner.setJsonDataSource(String name, String json)` pour attacher la source.
Le paramètre `name` est le nom de la source utilisé par les espaces réservés. Par exemple, le nom `node` alimente les espaces réservés tels que `<<node.Company>>` et `<<node.Title>>`.
Transmettez les données de lignes directement à `setJsonDataSource` :
- Un tableau de lignes, tel qu’un tableau JSON contenant un ou plusieurs objets de ligne, est pris en charge.
- Un seul objet de ligne peut également être transmis directement.
- N’enveloppez pas les lignes sous une clé de niveau supérieur nommée telle que `{"rows":[...]}`. Cet enveloppement n’est pas la forme d’entrée orientée lignes attendue pour ce flux de travail.
Une source JSON peut alimenter les deux styles de marqueurs lors du même appel `process()`. Elle peut résoudre un marqueur classique `&=` dans une cellule du corps de la feuille de calcul et des espaces réservés à double chevron `<<>>` dans les sections d’en-tête et de pied de page. Vous devez toujours appeler `designer.setEnableHeaderFooterMarkers(true)` pour que les espaces réservés d’en-tête et de pied de page soient résolus.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
worksheet.getCells().get("A1").putValue("&=node.Company");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]');
designer.process();
console.log("Left: " + worksheet.getPageSetup().getHeader(0));
console.log("Right: " + worksheet.getPageSetup().getHeader(2));
console.log("Body: " + worksheet.getCells().get("A1").getStringValue());
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx");
```

## **Commutateur et sémantique de source multi-lignes**
`setEnableHeaderFooterMarkers` est `false` par défaut, et ce paramètre contrôle uniquement les espaces réservés `<<Source.Field>>` d’en-tête et de pied de page. Lorsque le commutateur est désactivé, `process()` résout toujours les marqueurs classiques `&=` du corps, mais un espace réservé `<<Source.Field>>` dans un en-tête ou un pied de page reste du texte littéral.
Une section d’en-tête ou de pied de page est une chaîne unique, pas une bande répétitive. Si la source de données contient plusieurs lignes, la première ligne fournit les valeurs d’en-tête et de pied de page. Une fois résolues, les valeurs deviennent du texte d’en-tête ou de pied de page ordinaire. Elles restent dans le classeur après l’appel à `save` et sont présentes lors du rechargement du classeur enregistré.
L’exemple suivant crée deux classeurs à partir de la même source JSON multi-lignes afin de comparer le comportement désactivé et activé. Le `plainDesigner` laisse l’espace réservé tel quel, tandis que le `enabledDesigner` le résout en utilisant la première ligne.

```javascript
const AsposeCells = require("aspose.cells");
const table = '[{"Name":"First Row"},{"Name":"Second Row"}]';
// Without the switch the placeholder stays literal text
const plainWorkbook = new AsposeCells.Workbook();
const plainSheet = plainWorkbook.getWorksheets().get(0);
plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const plainDesigner = new AsposeCells.WorkbookDesigner(plainWorkbook);
plainDesigner.setJsonDataSource("node", table);
plainDesigner.process();
// With the switch on, the FIRST row of a multi-row source wins
const enabledWorkbook = new AsposeCells.Workbook();
const enabledSheet = enabledWorkbook.getWorksheets().get(0);
enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const enabledDesigner = new AsposeCells.WorkbookDesigner(enabledWorkbook);
enabledDesigner.setEnableHeaderFooterMarkers(true);
enabledDesigner.setJsonDataSource("node", table);
enabledDesigner.process();
console.log("Without switch: " + plainSheet.getPageSetup().getHeader(1));
console.log("With switch: " + enabledSheet.getPageSetup().getHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
```

## **Lier une image dans un en-tête ou un pied de page**
Le suffixe `(picture)` lie une image dans une section d’en-tête ou de pied de page. Écrivez `<<node.logo(picture)>>` à l’endroit où l’image doit apparaître, et fournissez la valeur du champ sous forme d’une URI de données — le préfixe `data:image/png;base64,` suivi du texte Base64 des octets de l’image. Une chaîne Base64 nue sans le préfixe `data:` n’insère pas d’image.
Après `process()` :
1. L’espace réservé est remplacé par `&G`, le code d’image standard d’en-tête et de pied de page. Comme le marqueur devient un code à l’intérieur de la chaîne de la section, il peut se situer dans un texte plus long tel que `Logo: <<node.logo(picture)>>`.
2. Les octets de l’image sont intégrés dans le classeur en tant que partie multimédia attachée à la couche de dessins d’en-tête/pied de page de cette feuille de calcul, de sorte que l’image s’imprime avec l’en-tête ou le pied de page.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
const table = [
    {
        logo: "data:image/png;base64," + fs.readFileSync("logo.png").toString("base64")
    }
];
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", JSON.stringify(table));
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
// This prints:
// Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx");
```

Le `&G` imprimé est le code d’image qu’Excel interprète lors du rendu de l’en-tête — les octets `logo.png` résident désormais dans `HeaderFooterPicture.xlsx`, et l’image s’imprime à la place du code.
Pour utiliser les Smart Markers d’en-tête et de pied de page, écrivez les espaces réservés `<<Source.Field>>` dans les sections gauche, centre et droite de l’en-tête ou du pied de page avec `setHeader` et `setFooter`. Appelez `designer.setEnableHeaderFooterMarkers(true)` avant d’appeler `process()`, et fournissez les valeurs via `designer.setJsonDataSource(name, json)`. Lisez les sections complètes avec `getHeader` et `getFooter`. La même source de données peut alimenter les marqueurs du corps et les espaces réservés d’en-tête ou de pied de page en un seul passage de traitement. Ajoutez le suffixe `(picture)` avec une valeur URI de données pour lier une image dans une section.

## Articles associés
- [Rendu de tableau à cellule unique SmartMarker](/cells/fr/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="nodejs-java" >}}