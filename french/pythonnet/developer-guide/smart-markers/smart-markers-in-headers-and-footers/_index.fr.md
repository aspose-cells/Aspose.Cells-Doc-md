---
title: Marqueurs intelligents dans les en-têtes et pieds de page | Aspose.Cells for Python via .NET
linktitle: Marqueurs d’en-tête et de pied de page | Aspose.Cells
description: Placez les espaces réservés de Smart Marker dans les en-têtes et pieds de page avec la syntaxe à doubles chevrons et le commutateur WorkbookDesigner.enable_header_footer_markers en utilisant des implémentations personnalisées de ICellsDataTable ou des sources de données JSON, et liez des images via des URI de données, dans Aspose.Cells for Python via .NET
keywords: Aspose.Cells, Marqueurs intelligents, en-têtes, pieds de page, marqueurs d'en-tête et pied de page, enable_header_footer_markers, WorkbookDesigner, PageSetup, set_header, set_footer, set_json_data_source, set_data_source, ICellsDataTable, table de données personnalisée, liaison de données, image, URI de données, Aspose.Cells for Python via .NET
type: docs
weight: 196
url: /fr/python-net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Les en-têtes et pieds de page contiennent généralement des métadonnées de rapport telles que le titre du rapport, la période du rapport, l'auteur et le service. Lorsque ces informations existent déjà dans la source de données utilisée pour remplir le classeur, les reproduire manuellement crée une duplication inutile.  
La syntaxe classique de Smart Marker, `&=Source.Field`, est traitée dans les cellules du corps de la feuille de calcul. Si vous placez un marqueur classique dans un en-tête ou un pied de page via `page_setup.set_header` ou `page_setup.set_footer`, il reste du texte littéral car les chaînes d'en-tête et de pied de page ne font pas partie de la grille de cellules de la feuille analysée par `workbook_designer.process()`.  
À partir de **Aspose.Cells for Python via .NET 26.11**, le commutateur `workbook_designer.enable_header_footer_markers`, qui vaut `False` par défaut, permet à `process()` de résoudre les espaces réservés écrits sous la forme `<<Source.Field>>` dans les chaînes des sections d'en-tête et de pied de page — définissez-le sur `True` avant d'appeler `process()`. Les espaces réservés d'en-tête et de pied de page utilisent la même source de données que les marqueurs du corps.  
Chaque en-tête et pied de page contient trois sections adressables :
- La section `0` est la section gauche.  
- La section `1` est la section centrale.  
- La section `2` est la section droite.  
Utilisez `page_setup.set_header(section, value)` et `page_setup.set_footer(section, value)` pour écrire ces sections. Après le traitement, utilisez `page_setup.get_header(section)` et `page_setup.get_footer(section)` pour récupérer le texte complet.

{{% alert color="primary" %}}
Un espace réservé tel que `<<Source.Field>>` insère la valeur du champ en texte dans la chaîne de la section. Les images sont liées avec le suffixe `(picture)` et une valeur URI de données.  
{{% /alert %}}

## **Activer les marqueurs d'en-tête/pied de page avec une table de données personnalisée**
Utilisez la séquence suivante pour résoudre les espaces réservés d'en-tête et de pied de page avec une source de données tabulaire personnalisée dans **Aspose.Cells for Python via .NET 26.11** :
1. Créez un `Workbook` et obtenez sa première `Worksheet` à l'index `0`.  
2. Écrivez des espaces réservés `<<Source.Field>>` dans les sections d'en-tête et de pied de page souhaitées avec `page_setup.set_header` et `page_setup.set_footer`.  
3. Définissez une petite classe qui implémente `ICellsDataTable` pour exposer les données tabulaires des lignes — les noms de colonnes, le nombre de lignes, et un curseur avec `before_first()`, `next()`, et l’indexeur `__getitem__` — et utilisez un nom de source correspondant au préfixe utilisé par les espaces réservés. Par exemple, une source nommée `node` alimente les espaces réservés tels que `<<node.Name>>`. Une classe Python simple ou une liste de dictionnaires ne se lie PAS sur cette plateforme ; l’implémentation `ICellsDataTable` constitue la source de données d’objet personnalisé.  
4. Créez un `WorkbookDesigner` pour le classeur.  
5. Définissez `designer.enable_header_footer_markers` sur `True` avant le traitement.  
6. Attachez la table et le nom de source avec `designer.set_data_source("node", table)`.  
7. Appelez `designer.process()`.  
8. Après le traitement, les espaces réservés ne sont plus présents dans le texte de l’en-tête ou du pied de page. Utilisez `get_header` et `get_footer` pour récupérer les chaînes de sections complètes.

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name", "Author"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.page_setup.set_header(1, "Quarterly Report - <<node.Name>>")
worksheet.page_setup.set_footer(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
print("Footer: " + worksheet.page_setup.get_footer(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
```

## **Utiliser une source de données JSON**
Vous pouvez utiliser JSON à la place d'un `ICellsDataTable` personnalisé lorsque les données du rapport sont déjà disponibles au format JSON. Appelez `workbook_designer.set_json_data_source(name, json)` pour attacher la source.  
L'argument `name` a le même rôle que le nom de source utilisé avec les données tabulaires. Par exemple, le nom `node` alimente des espaces réservés tels que `<<node.Company>>` et `<<node.Title>>`.  
Passez les données de ligne directement à `set_json_data_source` :
- Un tableau de lignes, comme un tableau JSON contenant un ou plusieurs objets de ligne, est pris en charge.  
- Un seul objet de ligne peut également être passé directement.  
- Ne placez pas les lignes sous une clé de niveau supérieur nommée, telle que `{"rows":[...]}`. Cet enveloppement n’est pas la forme d’entrée orientée lignes attendue pour ce flux de travail.  

Une source JSON peut alimenter les deux styles de marqueurs lors du même appel `process()`. Elle peut résoudre un marqueur classique `&=` dans une cellule du corps de la feuille et des espaces réservés à doubles chevrons `<<>>` dans les sections d’en-tête et de pied de page. Vous devez toujours activer `enable_header_footer_markers` pour que les espaces réservés d’en-tête et de pied de page soient résolus.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.page_setup.set_header(0, "<<node.Company>>")
worksheet.page_setup.set_header(2, "Page <<node.Title>>")
worksheet.cells.get("A1").put_value("&=node.Company")
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_json_data_source(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.page_setup.get_header(0))
print("Right: " + worksheet.page_setup.get_header(2))
print("Body: " + worksheet.cells.get("A1").string_value)
# This prints:
# Left: Aspose Pty Ltd
# Right: Page Half-Year Report
# Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx")
```

## **Sémantique du commutateur et des sources multi-lignes**
`enable_header_footer_markers` vaut `False` par défaut, et le commutateur ne contrôle que les espaces réservés `<<Source.Field>>` d’en-tête et de pied de page. Lorsque le commutateur est désactivé, `process()` résout toujours les marqueurs classiques `&=` du corps, mais un espace réservé `<<Source.Field>>` dans un en-tête ou un pied de page reste du texte littéral.  
Une section d’en-tête ou de pied de page est une seule chaîne, pas une bande répétitive. Si la source de données contient plusieurs lignes, la première ligne fournit les valeurs d’en-tête et de pied de page. Une fois résolues, les valeurs deviennent du texte d’en-tête ou de pied de page ordinaire. Elles restent dans le classeur après l’appel à `save` et sont présentes lorsque vous chargez à nouveau le classeur enregistré.  

L'exemple suivant crée deux classeurs à partir de la même source de données tabulaire multi-lignes afin de contraster le comportement désactivé et activé. Le `plain_designer` laisse l'espace réservé inchangé, tandis que le `enabled_designer` le résout en utilisant la première ligne.

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
rows = [("First Row",), ("Second Row",)]
# Without the switch the placeholder stays literal text
plain_workbook = ac.Workbook()
plain_sheet = plain_workbook.worksheets[0]
plain_sheet.page_setup.set_header(1, "<<node.Name>>")
plain_designer = ac.WorkbookDesigner(plain_workbook)
plain_designer.set_data_source("node", NodeTable(rows))
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = ac.Workbook()
enabled_sheet = enabled_workbook.worksheets[0]
enabled_sheet.page_setup.set_header(1, "<<node.Name>>")
enabled_designer = ac.WorkbookDesigner(enabled_workbook)
enabled_designer.enable_header_footer_markers = True
enabled_designer.set_data_source("node", NodeTable(rows))
enabled_designer.process()
print("Without switch: " + plain_sheet.page_setup.get_header(1))
print("With switch: " + enabled_sheet.page_setup.get_header(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
```

## **Lier une image dans un en-tête ou un pied de page**
Le suffixe `(picture)` lie une image dans une section d’en-tête ou de pied de page. Écrivez `<<node.logo(picture)>>` à l’endroit où l’image doit apparaître, et fournissez la valeur du champ sous forme d’URI de données — le préfixe `data:image/png;base64,` suivi du texte Base64 des octets de l’image. Une chaîne Base64 seule sans le préfixe `data:` n’intègre pas d’image.  

Après `process()` :
1. L’espace réservé est remplacé par `&G`, le code d’image standard d’en-tête et de pied de page. Comme le marqueur devient un code à l’intérieur de la chaîne de la section, il peut se placer dans un texte plus long tel que `Logo: <<node.logo(picture)>>`.  
2. Les octets de l’image sont intégrés dans le classeur en tant que partie média attachée à la couche de dessin d’en-tête/pied de page de cette feuille, de sorte que l’image s’imprime avec l’en-tête/le pied de page.

```python
import aspose.cells as ac
import base64
class LogoTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["logo"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.page_setup.set_header(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    logo_data_uri = "data:image/png;base64," + base64.b64encode(image_file.read()).decode("ascii")
table = LogoTable([(logo_data_uri,)])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
```

Le `&G` imprimé est le code d’image qu’Excel interprète lors du rendu de l’en-tête — les octets `logo.png` résident désormais dans `HeaderFooterPicture.xlsx`, et l’image s’imprime à la place du code.  
Pour utiliser les Smart Markers d’en-tête et de pied de page, écrivez des espaces réservés `<<Source.Field>>` dans les sections gauche, centre et droite de l’en-tête ou du pied de page avec `set_header` et `set_footer`. Définissez `enable_header_footer_markers` sur `True` sur le `WorkbookDesigner` avant d’appeler `process()`, et fournissez les valeurs via `set_data_source("node", table)` avec une implémentation personnalisée de `ICellsDataTable` ou `set_json_data_source(name, json)`. Lisez les sections complètes avec `get_header` et `get_footer`. La même source de données peut alimenter les marqueurs du corps et les espaces réservés d’en-tête ou de pied de page en une seule passe de traitement. Ajoutez le suffixe `(picture)` avec une valeur URI de données pour lier une image dans une section.

## Articles associés
- [Rendu d'un tableau à cellule unique SmartMarker](/cells/fr/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python-net" >}}