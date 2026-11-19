---
title: Marqueurs intelligents dans les en-têtes et pieds de page | Aspose.Cells .NET
linktitle: Marqueurs d’en-tête et de pied de page | Aspose.Cells
description: Placez des espaces réservés Smart Marker dans les en-têtes et pieds de page en utilisant la syntaxe à double chevron et le commutateur WorkbookDesigner.EnableHeaderFooterMarkers avec des sources de données DataTable ou JSON, et liez des images via des URI de données, dans Aspose.Cells for .NET.
keywords: Aspose.Cells, Marqueurs intelligents, en-têtes, pieds de page, marqueurs en-tête pied de page, EnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, SetHeader, SetFooter, SetJsonDataSource, DataTable, liaison de données, image, URI de données, C#
type: docs
weight: 196
url: /fr/net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Les en-têtes et pieds de page contiennent généralement des métadonnées de rapport telles que le titre du rapport, la période de reporting, l’auteur et le service. Lorsque ces informations existent déjà dans la source de données utilisée pour remplir le classeur, les reproduire manuellement crée une duplication inutile.  
La syntaxe classique Smart Marker, `&=Source.Field`, est traitée dans les cellules du corps de la feuille de calcul. Si vous placez un marqueur classique dans un en-tête ou un pied de page via `PageSetup.SetHeader` ou `PageSetup.SetFooter`, il reste du texte littéral car les chaînes d’en-tête et de pied de page ne font pas partie de la grille de cellules analysée par `WorkbookDesigner.Process()`.  
À partir de **Aspose.Cells for .NET 26.11**, le commutateur `WorkbookDesigner.EnableHeaderFooterMarkers`, qui vaut `false` par défaut, permet à `Process()` de résoudre les espaces réservés écrits sous la forme `<<Source.Field>>` dans les chaînes des sections d’en-tête et de pied de page — réglez-le sur `true` avant d’appeler `Process()`. Les espaces réservés d’en-tête et de pied de page utilisent la même source de données que les marqueurs du corps.  
Chaque en-tête et pied de page contient trois sections adressables :
- La section `0` correspond à la section gauche.  
- La section `1` correspond à la section centrale.  
- La section `2` correspond à la section droite.  

Utilisez `PageSetup.SetHeader(int section, string value)` et `PageSetup.SetFooter(int section, string value)` pour écrire ces sections. Après le traitement, utilisez `PageSetup.GetHeader(int section)` et `PageSetup.GetFooter(int section)` pour récupérer le texte finalisé.

{{% alert color="primary" %}}
Un espace réservé tel que `<<Source.Field>>` insère la valeur du champ sous forme de texte dans la chaîne de la section. Les images sont liées avec le suffixe `(picture)` et une valeur data-URI.  
{{% /alert %}}

## **Activer les marqueurs d’en-tête/pied de page avec un DataTable**
Utilisez la séquence suivante pour résoudre les espaces réservés d’en-tête et de pied de page avec un `DataTable` dans **Aspose.Cells for .NET 26.11** :
1. Créez un `Workbook` et obtenez sa première `Worksheet` à l’indice `0`.  
2. Écrivez des espaces réservés `<<Source.Field>>` dans les sections d’en-tête et de pied de page souhaitées avec `PageSetup.SetHeader` et `PageSetup.SetFooter`.  
3. Créez un `DataTable` dont le nom de table correspond au préfixe source utilisé par les espaces réservés. Par exemple, une table nommée `node` alimente les espaces réservés tels que `<<node.Name>>`.  
4. Créez un `WorkbookDesigner` pour le classeur.  
5. Définissez `designer.EnableHeaderFooterMarkers` sur `true` avant le traitement.  
6. Attachez la table avec `designer.SetDataSource(table)`.  
7. Appelez `designer.Process()`.  
8. Après le traitement, les espaces réservés ne sont plus présents dans le texte d’en-tête ou de pied de page. Utilisez `GetHeader` et `GetFooter` pour récupérer les chaînes de section finalisées.

```csharp
using System;
using System.Data;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.PageSetup.SetHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.PageSetup.SetFooter(1, "Prepared by <<node.Author>>");
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Columns.Add("Author");
table.Rows.Add("Q4 2026", "Aspose.Cells");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
Console.WriteLine("Footer: " + worksheet.PageSetup.GetFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.Save("HeaderFooterSmartMarkers.xlsx");
```

## **Utiliser une source de données JSON**
Vous pouvez utiliser JSON à la place d’un `DataTable` lorsque les données du rapport sont déjà disponibles au format JSON. Appelez `WorkbookDesigner.SetJsonDataSource(string name, string json)` pour attacher la source.  
L’argument `name` a le même rôle que le nom du `DataTable`. Par exemple, le nom `node` alimente les espaces réservés tels que `<<node.Company>>` et `<<node.Title>>`.  
Passez les données de ligne directement à `SetJsonDataSource` :
- Un tableau de lignes, tel qu’un tableau JSON contenant un ou plusieurs objets de ligne, est pris en charge.  
- Un seul objet de ligne peut également être passé directement.  
- Ne regroupez pas les lignes sous une clé de niveau supérieur nommée telle que `{"rows":[...]}`. Ce wrapper n’est pas la forme d’entrée attendue orientée lignes pour ce flux de travail.  

Une même source JSON peut alimenter les deux styles de marqueurs lors d’un même appel à `Process()`. Elle peut résoudre un marqueur classique `&=` dans une cellule du corps de la feuille et des espaces réservés à double chevron `<<>>` dans les sections d’en-tête et de pied de page. Vous devez toujours activer `EnableHeaderFooterMarkers` pour que les espaces réservés d’en-tête et de pied de page soient résolus.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.PageSetup.SetHeader(0, "<<node.Company>>");
worksheet.PageSetup.SetHeader(2, "Page <<node.Title>>");
worksheet.Cells["A1"].PutValue("&=node.Company");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
designer.Process();
Console.WriteLine("Left: " + worksheet.PageSetup.GetHeader(0));
Console.WriteLine("Right: " + worksheet.PageSetup.GetHeader(2));
Console.WriteLine("Body: " + worksheet.Cells["A1"].StringValue);
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.Save("HeaderFooterJsonMarkers.xlsx");
```

## **Sémantique du commutateur et de la source multi-lignes**
`EnableHeaderFooterMarkers` vaut `false` par défaut, et le commutateur ne contrôle que les espaces réservés `<<Source.Field>>` d’en-tête et de pied de page. Lorsque le commutateur est désactivé, `Process()` résout toujours les marqueurs classiques `&=` du corps, mais un espace réservé `<<Source.Field>>` dans un en-tête ou un pied de page reste du texte littéral.  
Une section d’en-tête ou de pied de page est une chaîne unique, et non une bande répétitive. Si la source de données contient plusieurs lignes, la première ligne fournit les valeurs d’en-tête et de pied de page. Une fois résolues, les valeurs deviennent du texte d’en-tête ou de pied de page ordinaire. Elles restent dans le classeur après l’appel à `Save` et sont présentes lors du chargement du classeur enregistré.  

L’exemple suivant crée deux classeurs à partir du même `DataTable` multi-lignes afin de comparer le comportement désactivé et activé. Le `plainDesigner` laisse l’espace réservé inchangé, tandis que le `enabledDesigner` le résout en utilisant la première ligne.

```csharp
using System;
using System.Data;
using Aspose.Cells;
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Rows.Add("First Row");
table.Rows.Add("Second Row");
// Without the switch the placeholder stays literal text
Workbook plainWorkbook = new Workbook();
Worksheet plainSheet = plainWorkbook.Worksheets[0];
plainSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
plainDesigner.SetDataSource(table);
plainDesigner.Process();
// With the switch on, the FIRST row of a multi-row source wins
Workbook enabledWorkbook = new Workbook();
Worksheet enabledSheet = enabledWorkbook.Worksheets[0];
enabledSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
enabledDesigner.EnableHeaderFooterMarkers = true;
enabledDesigner.SetDataSource(table);
enabledDesigner.Process();
Console.WriteLine("Without switch: " + plainSheet.PageSetup.GetHeader(1));
Console.WriteLine("With switch: " + enabledSheet.PageSetup.GetHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.Save("HeaderFooterMarkersEnabled.xlsx");
```

## **Lier une image dans un en-tête ou un pied de page**
Le suffixe `(picture)` lie une image à une section d’en-tête ou de pied de page. Écrivez `<<node.logo(picture)>>` à l’endroit où l’image doit apparaître, et fournissez la valeur du champ sous forme de data-URI — le préfixe `data:image/png;base64,` suivi du texte Base64 des octets de l’image. Une chaîne Base64 seule sans le préfixe `data:` n’incorpore pas d’image.  

Après `Process()` :
1. L’espace réservé est remplacé par `&G`, le code d’image standard pour les en-têtes et pieds de page. Comme le marqueur devient un code à l’intérieur de la chaîne de la section, il peut s’insérer dans un texte plus long tel que `Logo: <<node.logo(picture)>>`.  
2. Les octets de l’image sont incorporés dans le classeur en tant que partie média attachée à la couche de dessin en-tête/pied de page de cette feuille de calcul, de sorte que l’image s’imprime avec l’en-tête ou le pied de page.

```csharp
using System;
using System.Data;
using System.IO;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.PageSetup.SetHeader(1, "Logo: <<node.logo(picture)>>");
DataTable table = new DataTable("node");
table.Columns.Add("logo");
table.Rows.Add("data:image/png;base64," + Convert.ToBase64String(File.ReadAllBytes("logo.png")));
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
// This prints:
// Header: Logo: &G
workbook.Save("HeaderFooterPicture.xlsx");
```

Le `&G` imprimé est le code image qu’Excel interprète lors du rendu de l’en-tête — les octets `logo.png` se trouvent maintenant dans `HeaderFooterPicture.xlsx`, et l’image s’imprime à la place du code.  
Pour utiliser les marqueurs intelligents d’en-tête et de pied de page, écrivez des espaces réservés `<<Source.Field>>` dans les sections gauche, centre et droite de l’en-tête ou du pied de page avec `SetHeader` et `SetFooter`. Réglez `EnableHeaderFooterMarkers` sur `true` sur le `WorkbookDesigner` avant d’appeler `Process()`, et fournissez les valeurs via `SetDataSource(DataTable)` ou `SetJsonDataSource`. Lisez les sections finalisées avec `GetHeader` et `GetFooter`. La même source de données peut alimenter les marqueurs du corps et les espaces réservés d’en-tête ou de pied de page en un seul passage de traitement. Ajoutez le suffixe `(picture)` avec une valeur data-URI pour lier une image à une section.

## **Articles associés**
- [Rendu de tableau à cellule unique SmartMarker](/cells/fr/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="csharp" >}}