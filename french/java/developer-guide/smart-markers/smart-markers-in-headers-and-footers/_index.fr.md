---
title: Smart Markers dans les en-têtes et pieds de page | Aspose.Cells for Java
linktitle: Marqueurs d’en-tête et de pied de page | Aspose.Cells
description: Placez des espaces réservés Smart Marker dans les en-têtes et pieds de page avec une syntaxe à doubles chevrons et le commutateur WorkbookDesigner.setEnableHeaderFooterMarkers en utilisant des listes getter-bean ou des sources de données JSON, et liez des images via des URI de données, dans Aspose.Cells for Java.
keywords: Aspose.Cells for Java, Smart Markers, en-têtes, pieds de page, marqueurs d’en-tête et de pied de page, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, setDataSource, bean getter, source de données JSON, liaison de données, image, URI de données, Java
type: docs
weight: 196
url: /fr/java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Les en-têtes et pieds de page contiennent généralement des métadonnées de rapport telles que le titre du rapport, la période du rapport, l’auteur et le département. Lorsque ces informations existent déjà dans la source de données utilisée pour remplir le classeur, les répéter manuellement crée une duplication inutile.  
La syntaxe classique de Smart Marker, `&=Source.Field`, est traitée dans les cellules du corps de la feuille de calcul. Si vous placez un marqueur classique dans un en-tête ou un pied de page via `PageSetup.setHeader` ou `PageSetup.setFooter`, il reste du texte littéral car les chaînes d’en-tête et de pied de page ne font pas partie de la grille de cellules de la feuille évaluée par `WorkbookDesigner.process()`.  
À partir de **Aspose.Cells for Java 26.11**, l’option de marqueur d’en-tête/pied de page du `WorkbookDesigner` est `false` par défaut. Appelez `designer.setEnableHeaderFooterMarkers(true)` avant d’appeler `designer.process()` pour résoudre les espaces réservés écrits sous la forme `<<Source.Field>>` dans les chaînes de sections d’en-tête et de pied de page. Les espaces réservés d’en-tête et de pied de page utilisent la même source de données que les marqueurs du corps.  
Chaque en-tête et pied de page contient trois sections adressables :
- La section `0` est la section gauche.  
- La section `1` est la section centrale.  
- La section `2` est la section droite.  
Utilisez `PageSetup.setHeader(int section, String value)` et `PageSetup.setFooter(int section, String value)` pour écrire ces sections. Après le traitement, utilisez `PageSetup.getHeader(int section)` et `PageSetup.getFooter(int section)` pour récupérer le texte complété.

{{% alert color="primary" %}}
Un espace réservé tel que `<<Source.Field>>` insère la valeur du champ en tant que texte dans la chaîne de la section. Les images sont liées avec le suffixe `(picture)` et une valeur URI de données.
{{% /alert %}}

## **Activer les marqueurs d’en-tête/pied de page avec une liste Getter-Bean**
1. Créez un `Workbook` et obtenez sa première `Worksheet` à l’index `0`, par exemple avec `workbook.getWorksheets().get(0)`.  
2. Écrivez des espaces réservés `<<Source.Field>>` dans les sections d’en-tête et de pied de page souhaitées à l’aide de `PageSetup.setHeader` et `PageSetup.setFooter`.  
3. Définissez une petite classe bean PUBLIC avec un getter (par exemple, `getName()`) pour chaque champ d’espace réservé, et choisissez un nom de source correspondant au préfixe utilisé par les espaces réservés. Par exemple, une source nommée `node` alimente les espaces réservés tels que `<<node.Name>>`. Deux règles de liaison sont vérifiées sur cette plateforme : un bean avec des champs publics ne lie rien (le moteur lit les getters, pas les champs), et une classe PACKAGE-PRIVATE ne lie rien non plus — l’introspection ne voit que les classes publiques, et un bean non public échoue lors de `process()` avec une NullPointerException.  
4. Créez un `WorkbookDesigner` pour le classeur.  
5. Appelez `designer.setEnableHeaderFooterMarkers(true)` avant le traitement.  
6. Attachez la liste et son nom de source avec `designer.setDataSource("node", table)`.  
7. Appelez `designer.process()`.  
8. Après le traitement, les espaces réservés ne sont plus présents dans le texte d’en-tête ou de pied de page. Utilisez `PageSetup.getHeader` et `PageSetup.getFooter` pour récupérer les chaînes de sections complétées.

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String name;
        private final String author;
        public Node(String name, String author) {
            this.name = name;
            this.author = author;
        }
        public String getName() {
            return name;
        }
        public String getAuthor() {
            return author;
        }
    }
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // Center header and center footer carry <<Source.Field>> placeholders
        worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
        worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
        List<Node> table = Arrays.asList(new Node("Q4 2026", "Aspose.Cells"));
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setDataSource("node", table);
        designer.process();
        System.out.println("Header: " + worksheet.getPageSetup().getHeader(1));
        System.out.println("Footer: " + worksheet.getPageSetup().getFooter(1));
        // This prints:
        // Header: Quarterly Report - Q4 2026
        // Footer: Prepared by Aspose.Cells
        workbook.save("HeaderFooterSmartMarkers.xlsx");
    }
}
```

## **Utiliser une source de données JSON**
Vous pouvez utiliser du JSON à la place d’une liste getter-bean lorsque les données du rapport sont déjà disponibles au format JSON. Appelez `WorkbookDesigner.setJsonDataSource(String name, String json)` pour attacher la source.  
L’argument `name` correspond au nom de source utilisé par les espaces réservés. Par exemple, le nom `node` alimente les espaces réservés tels que `<<node.Company>>` et `<<node.Title>>`.  
Passez les données de ligne directement à `setJsonDataSource` :
- Un tableau de lignes, par exemple un tableau JSON contenant un ou plusieurs objets ligne, est pris en charge.  
- Un objet ligne unique peut également être passé directement.  
- N’enveloppez pas les lignes sous une clé de niveau supérieur nommée, comme `{"rows":[...]}`. Cet emballage n’est pas la forme d’entrée attendue orientée lignes pour ce flux de travail.  
Une source JSON peut alimenter les deux styles de marqueurs lors du même appel `designer.process()`. Elle peut résoudre un marqueur classique `&=` dans une cellule du corps de la feuille et des espaces réservés à doubles chevrons `<<>>` dans les sections d’en-tête et de pied de page. Vous devez toujours activer `EnableHeaderFooterMarkers` pour que les espaces réservés d’en-tête et de pied de page soient résolus.

```java
import com.aspose.cells.*;
public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // Left header, right header, and a classic body marker — one JSON source feeds all three
        worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
        worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
        worksheet.getCells().get("A1").putValue("&=node.Company");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
        designer.process();
        System.out.println("Left: " + worksheet.getPageSetup().getHeader(0));
        System.out.println("Right: " + worksheet.getPageSetup().getHeader(2));
        System.out.println("Body: " + worksheet.getCells().get("A1").getStringValue());
        // This prints:
        // Left: Aspose Pty Ltd
        // Right: Page Half-Year Report
        // Body: Aspose Pty Ltd
        workbook.save("HeaderFooterJsonMarkers.xlsx");
    }
}
```

## **Sémantique du commutateur et source multi-lignes**
Le paramètre `EnableHeaderFooterMarkers` est `false` par défaut, et le commutateur ne contrôle que les espaces réservés d’en-tête/pied de page `<<Source.Field>>`. Lorsque le commutateur est désactivé, `designer.process()` résout toujours les marqueurs classiques `&=` du corps, mais un espace réservé `<<Source.Field>>` dans un en-tête ou un pied de page reste du texte littéral.  
Une section d’en-tête ou de pied de page est une chaîne unique, pas une bande répétée. Si la source de données contient plusieurs lignes, la première ligne fournit les valeurs d’en-tête et de pied de page. Une fois résolues, les valeurs deviennent du texte d’en-tête ou de pied de page ordinaire. Elles restent dans le classeur après l’appel à `workbook.save(...)` et sont présentes lorsque vous chargez à nouveau le classeur enregistré.  
L’exemple suivant crée deux classeurs à partir de la même liste bean multi-lignes afin de contraster le comportement désactivé et activé. Le `plainDesigner` laisse l’espace réservé inchangé, tandis que le `enabledDesigner` le résout en utilisant la première ligne.

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String name;
        public Node(String name) {
            this.name = name;
        }
        public String getName() {
            return name;
        }
    }
    public static void main(String[] args) throws Exception {
        List<Node> table = Arrays.asList(
                new Node("First Row"),
                new Node("Second Row")
        );
        // Without the switch the placeholder stays literal text
        Workbook plainWorkbook = new Workbook();
        Worksheet plainSheet = plainWorkbook.getWorksheets().get(0);
        plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
        WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
        plainDesigner.setDataSource("node", table);
        plainDesigner.process();
        // With the switch on, the FIRST row of a multi-row source wins
        Workbook enabledWorkbook = new Workbook();
        Worksheet enabledSheet = enabledWorkbook.getWorksheets().get(0);
        enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
        WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
        enabledDesigner.setEnableHeaderFooterMarkers(true);
        enabledDesigner.setDataSource("node", table);
        enabledDesigner.process();
        System.out.println("Without switch: " + plainSheet.getPageSetup().getHeader(1));
        System.out.println("With switch: " + enabledSheet.getPageSetup().getHeader(1));
        // This prints:
        // Without switch: <<node.Name>>
        // With switch: First Row
        enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
    }
}
```

## **Lier une image dans un en-tête ou un pied de page**
Le suffixe `(picture)` lie une image dans une section d’en-tête ou de pied de page. Écrivez `<<node.logo(picture)>>` à l’endroit où l’image doit apparaître, et fournissez la valeur du champ sous forme de data URI — le préfixe `data:image/png;base64,` suivi du texte Base64 des octets de l’image. Une chaîne Base64 seule, sans le préfixe `data:`, n’insère pas d’image.  
Après `designer.process()` :
1. L’espace réservé est remplacé par `&G`, le code standard d’image d’en-tête et de pied de page. Comme le marqueur devient un code à l’intérieur de la chaîne de section, il peut se trouver dans un texte plus long tel que `Logo: <<node.logo(picture)>>`.  
2. Les octets de l’image sont incorporés dans le classeur sous forme de partie média attachée à la couche de dessin d’en-tête/pied de page de cette feuille, de sorte que l’image s’imprime avec l’en-tête ou le pied de page.

```java
import com.aspose.cells.*;
import java.nio.file.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String logo;
        public Node(String logo) {
            this.logo = logo;
        }
        public String getLogo() {
            return logo;
        }
    }
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // The (picture) suffix binds the image named by the data-URI field into the header
        worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
        String logoDataUri = "data:image/png;base64," + Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("logo.png")));
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setDataSource("node", Arrays.asList(new Node(logoDataUri)));
        designer.process();
        System.out.println("Header: " + worksheet.getPageSetup().getHeader(1));
        // This prints:
        // Header: Logo: &G
        workbook.save("HeaderFooterPicture.xlsx");
    }
}
```

Le `&G` imprimé est le code image qu’Excel interprète lors du rendu de l’en-tête — les octets `logo.png` résident maintenant dans `HeaderFooterPicture.xlsx`, et l’image s’imprime à la place du code.  
Pour utiliser les Smart Markers d’en-tête et de pied de page, écrivez des espaces réservés `<<Source.Field>>` dans les sections gauche, centre et droite de l’en-tête ou du pied de page avec `PageSetup.setHeader` et `PageSetup.setFooter`. Appelez `designer.setEnableHeaderFooterMarkers(true)` sur le `WorkbookDesigner` avant d’appeler `designer.process()`, et fournissez les valeurs via `designer.setDataSource(name, list)` avec une liste getter-bean ou `designer.setJsonDataSource(name, json)`. Lisez les sections complétées avec `PageSetup.getHeader` et `PageSetup.getFooter`. La même source de données peut alimenter les marqueurs du corps et les espaces réservés d’en-tête ou de pied de page en un seul passage de traitement. Ajoutez le suffixe `(picture)` avec une valeur data-URI pour lier une image à une section.

## Articles associés
- [Rendu du tableau à une seule cellule SmartMarker](/cells/fr/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="java" >}}