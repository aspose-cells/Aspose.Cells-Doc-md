---
title: Marqueurs intelligents dans les en-têtes et pieds de page | Aspose.Cells for Python via Java
linktitle: Marqueurs d’en-tête et de pied de page | Aspose.Cells
description: Placez des espaces réservés de Marqueur intelligent dans les en-têtes et pieds de page avec une syntaxe à doubles chevrons et le commutateur WorkbookDesigner.setEnableHeaderFooterMarkers utilisant des sources de données tabulaires ou JSON, et liez des images via des URI de données, dans Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Aspose.Cells for Python via Java, Marqueurs intelligents, en-têtes, pieds de page, marqueurs d’en-tête et pied de page, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, ICellsDataTable, table de données personnalisée, liaison de données, image, URI de données, Python via Java
type: docs
weight: 196
url: /fr/python-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Les en-têtes et pieds de page contiennent couramment les métadonnées d’un rapport telles que le titre du rapport, la période de rapport, l’auteur et le département. Lorsque ces informations existent déjà dans la source de données utilisée pour remplir le classeur, les répéter manuellement crée une duplication inutile.  
La syntaxe classique de Marqueur intelligent, `&=Source.Field`, est traitée dans les cellules du corps de la feuille de calcul. Si vous placez un marqueur classique dans un en-tête ou un pied de page via `PageSetup.setHeader` ou `PageSetup.setFooter`, il reste du texte littéral car les chaînes d’en-tête et de pied de page ne font pas partie de la grille de cellules de la feuille parcourue par `WorkbookDesigner.process()`.  
À partir de **Aspose.Cells for Python via Java 26.11**, le commutateur `WorkbookDesigner.setEnableHeaderFooterMarkers`, qui vaut `False` par défaut, fait que `process()` résout les espaces réservés écrits sous la forme `<<Source.Field>>` dans les chaînes des sections d’en-tête et de pied de page — définissez-le à `True` avant d’appeler `process()`. Les espaces réservés d’en-tête et de pied de page utilisent la même source de données que les marqueurs du corps.  
Chaque en-tête et pied de page comporte trois sections adressables :
- La section `0` est la section gauche.  
- La section `1` est la section centrale.  
- La section `2` est la section droite.  
Utilisez `PageSetup.setHeader(int section, str value)` et `PageSetup.setFooter(int section, str value)` pour écrire ces sections. Après le traitement, utilisez `PageSetup.getHeader(int section)` et `PageSetup.getFooter(int section)` pour récupérer le texte finalisé.

{{% alert color="primary" %}}
Un espace réservé tel que `<<Source.Field>>` insère la valeur du champ sous forme de texte dans la chaîne de la section. Les images sont liées avec le suffixe `(picture)` et une valeur URI de données.
{{% /alert %}}

## **Activer les marqueurs d’en-tête/pied de page avec une table de données personnalisée**
1. Créez un `Workbook` et obtenez sa première `Worksheet` à l’index `0` en utilisant `workbook.getWorksheets().get(0)`.  
2. Écrivez les espaces réservés `<<Source.Field>>` dans les sections d’en-tête et de pied de page souhaitées à l’aide de `worksheet.getPageSetup().setHeader(section, value)` et `worksheet.getPageSetup().setFooter(section, value)`.  
3. Définissez une petite classe implémentant `ICellsDataTable` afin d’exposer les données tabulaires des lignes — les noms de colonnes, le nombre de lignes et un curseur avec `beforeFirst()`, `next()` et `get()` — et utilisez un nom de source qui correspond au préfixe utilisé par les espaces réservés. Par exemple, une source nommée `node` alimente les espaces réservés tels que `<<node.Name>>`. Une classe Python simple ou une liste de dictionnaires ne se lie pas sur cette plateforme ; l’implémentation `ICellsDataTable` constitue la source de données objet personnalisée.  
4. Créez un `WorkbookDesigner` pour le classeur.  
5. Appelez `designer.setEnableHeaderFooterMarkers(True)` avant le traitement.  
6. Attachez la table et le nom de source avec `designer.setDataSource("node", table)`.  
7. Appelez `designer.process()`.  
8. Après le traitement, les espaces réservés ne sont plus présents dans le texte de l’en-tête ou du pied de page. Utilisez `worksheet.getPageSetup().getHeader(section)` et `worksheet.getPageSetup().getFooter(section)` pour récupérer les chaînes des sections finalisées.  

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name", "Author"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>")
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
print("Footer: " + worksheet.getPageSetup().getFooter(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
jpype.shutdownJVM()
```

## **Utiliser une source de données JSON**
Vous pouvez utiliser JSON à la place d’un `ICellsDataTable` personnalisé lorsque les données du rapport sont déjà disponibles au format JSON. Appelez `designer.setJsonDataSource(name, json)` pour attacher la source.  
L’argument `name` a le même rôle que le nom de source utilisé avec les données tabulaires. Par exemple, le nom `node` alimente les espaces réservés tels que `<<node.Company>>` et `<<node.Title>>`.  
Passez les données de lignes directement à `setJsonDataSource` :
- Un tableau de lignes, comme un tableau JSON contenant un ou plusieurs objets de ligne, est pris en charge.  
- Un objet de ligne unique peut également être passé directement.  
- Ne pas envelopper les lignes sous une clé de niveau supérieur nommée comme `{"rows":[...]}`. Cet enveloppement n’est pas la forme d’entrée orientée lignes attendue pour ce flux de travail.  
Une source JSON peut remplir les deux styles de marqueurs lors du même appel `process()`. Elle peut résoudre un marqueur classique `&=` dans une cellule du corps de la feuille et des espaces réservés à doubles chevrons `<<>>` dans les sections d’en-tête et de pied de page. Vous devez toujours activer `setEnableHeaderFooterMarkers` pour que les espaces réservés d’en-tête et de pied de page soient résolus.  

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>")
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>")
worksheet.getCells().get("A1").putValue("&=node.Company")
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setJsonDataSource(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.getPageSetup().getHeader(0))
print("Right: " + worksheet.getPageSetup().getHeader(2))
print("Body: " + worksheet.getCells().get("A1").getStringValue())
workbook.save("HeaderFooterJsonMarkers.xlsx")
jpype.shutdownJVM()
```

## **Sémantique du commutateur et de la source multi-lignes**
Le paramètre de marqueur d’en-tête et de pied de page vaut `False` par défaut, et `designer.setEnableHeaderFooterMarkers(True)` contrôle uniquement les espaces réservés `<<Source.Field>>` d’en-tête et de pied de page. Lorsque le commutateur est désactivé, `process()` résout toujours les marqueurs classiques `&=` du corps, mais un espace réservé `<<Source.Field>>` dans un en-tête ou un pied de page reste du texte littéral.  
Une section d’en-tête ou de pied de page est une chaîne unique, pas une bande répétée. Si la source de données contient plusieurs lignes, la première ligne fournit les valeurs d’en-tête et de pied de page. Une fois résolues, les valeurs deviennent du texte d’en-tête ou de pied de page ordinaire. Elles restent dans le classeur après l’appel à `workbook.save(...)` et sont présentes lorsque vous chargez à nouveau le classeur enregistré.  
L’exemple suivant crée deux classeurs à partir de la même source de données tabulaire multi-lignes afin de contraster le comportement désactivé et activé. Le `plainDesigner` laisse l’espace réservé inchangé, tandis que le `enabledDesigner` le résout en utilisant la première ligne.  

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
table = NodeTable([
    ("First Row",),
    ("Second Row",),
])
# Without the switch the placeholder stays literal text
plain_workbook = Workbook()
plain_sheet = plain_workbook.getWorksheets().get(0)
plain_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
plain_designer = WorkbookDesigner(plain_workbook)
plain_designer.setDataSource("node", table)
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = Workbook()
enabled_sheet = enabled_workbook.getWorksheets().get(0)
enabled_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
enabled_designer = WorkbookDesigner(enabled_workbook)
enabled_designer.setEnableHeaderFooterMarkers(True)
enabled_designer.setDataSource("node", table)
enabled_designer.process()
print("Without switch: " + plain_sheet.getPageSetup().getHeader(1))
print("With switch: " + enabled_sheet.getPageSetup().getHeader(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
jpype.shutdownJVM()
```

## **Lier une image dans un en-tête ou un pied de page**
Le suffixe `(picture)` lie une image dans une section d’en-tête ou de pied de page. Écrivez `<<node.logo(picture)>>` à l’endroit où l’image doit apparaître, et fournissez la valeur du champ sous forme d’URI de données — le préfixe `data:image/png;base64,` suivi du texte Base64 des octets de l’image. L’image décodée est traitée comme un tableau `byte[]`. Une chaîne Base64 seule sans le préfixe `data:` n’intègre pas d’image.  
Après `process()` :
- L’espace réservé est remplacé par `&G`, le code d’image standard d’en-tête et de pied de page. Parce que le marqueur devient un code à l’intérieur de la chaîne de la section, il peut se trouver dans un texte plus long tel que `Logo: <<node.logo(picture)>>`.  
- Les octets de l’image sont intégrés dans le classeur comme une partie média attachée à la couche de dessin d’en-tête/pied de page de cette feuille de calcul, ainsi l’image s’imprime avec l’en-tête ou le pied de page.  

```python
import base64
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["logo"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    image_bytes = image_file.read()
logo_data = "data:image/png;base64," + base64.b64encode(image_bytes).decode("ascii")
table = NodeTable([(logo_data,)])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
jpype.shutdownJVM()
```

Le `&G` imprimé est le code d’image qu’Excel interprète lors du rendu de l’en-tête — les octets `logo.png` résident maintenant dans `HeaderFooterPicture.xlsx`, et l’image s’imprime à la place du code.  
Pour utiliser les marqueurs intelligents d’en-tête et de pied de page, écrivez les espaces réservés `<<Source.Field>>` dans les sections gauche, centrale et droite de l’en-tête ou du pied de page avec `setHeader` et `setFooter`. Appelez `designer.setEnableHeaderFooterMarkers(True)` avant d’appeler `process()`, et fournissez les valeurs soit via `designer.setDataSource("node", table)` avec une implémentation personnalisée de `ICellsDataTable`, soit via `designer.setJsonDataSource(name, json)`. Lisez les sections finalisées avec `getHeader` et `getFooter`. La même source de données peut alimenter les marqueurs du corps et les espaces réservés d’en-tête ou de pied de page en un seul passage de traitement. Ajoutez le suffixe `(picture)` avec une valeur URI de données pour lier une image dans une section.

## Articles associés
- [Rendu d’un tableau à cellule unique SmartMarker](/cells/fr/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python" >}}