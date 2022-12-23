---
title: Grouper et dissocier des lignes et des colonnes
type: docs
weight: 50
url: /fr/net/grouping-and-ungrouping-rows-and-columns/
---
## **Introduction**

Dans un fichier Excel Microsoft, vous pouvez créer un plan pour les données afin de vous permettre d'afficher et de masquer les niveaux de détail d'un simple clic de souris.

 Clique le**Symboles de contour**, 1,2,3, + et - pour afficher rapidement uniquement les lignes ou les colonnes qui fournissent des résumés ou des en-têtes pour les sections d'une feuille de calcul, ou vous pouvez utiliser les symboles pour voir les détails sous un résumé ou un en-tête individuel, comme indiqué ci-dessous dans la figure :

|**Regroupement des lignes et des colonnes.**|
|:- |
|![tâche : image_autre_texte](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gestion groupée des lignes et des colonnes**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection qui représente toutes les cellules de la feuille de calcul.

 Le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection fournit plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul, quelques-unes d'entre elles sont décrites ci-dessous plus en détail.

### **Regroupement de lignes et de colonnes**

 Il est possible de grouper des lignes ou des colonnes en appelant le[**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) et[**GroupeColonnes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) méthodes de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) le recueil. Les deux méthodes prennent les paramètres suivants :

- Index de la première ligne/colonne, la première ligne ou colonne du groupe.
- Index de la dernière ligne/colonne, la dernière ligne ou colonne du groupe.
- Est masqué, un paramètre booléen qui spécifie s'il faut masquer ou non les lignes/colonnes après le regroupement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Paramètres de groupe**

Microsoft Excel vous permet de configurer les paramètres de groupe pour afficher :

- Lignes récapitulatives sous les détails.
- Colonnes récapitulatives à droite du détail.

 Les développeurs peuvent configurer ces paramètres de groupe à l'aide de la[**Contour**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) propriété de la[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe.

### **Lignes récapitulatives jusqu'en dessous du détail**

 Il est possible de contrôler si les lignes récapitulatives sont affichées sous les détails en définissant le paramètre[**Contour**](https://reference.aspose.com/cells/net/aspose.cells/outline) classe'[**SummaryRowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) propriété à**vrai** ou alors**faux**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Colonnes récapitulatives à droite du détail**

 Les développeurs peuvent également contrôler l'affichage des colonnes récapitulatives à droite des détails en définissant le paramètre[**RésuméColonneDroite**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) propriété de[**Contour**](https://reference.aspose.com/cells/net/aspose.cells/outline) classe à**vrai** ou alors**faux**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Dégrouper des lignes et des colonnes**

 Pour dégrouper des lignes ou des colonnes groupées, appelez le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) de la collection[**Dissocier les lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) et[**Dissocier les colonnes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns)méthodes. Les deux méthodes prennent deux paramètres :

- Premier index de ligne ou de colonne, la première ligne/colonne à dissocier.
- Index de la dernière ligne ou colonne, la dernière ligne/colonne à dissocier.

[**Dissocier les lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) a une surcharge qui prend un troisième paramètre booléen. Le mettre à**vrai**supprime toutes les informations groupées. Sinon, seules les informations du groupe externe sont supprimées.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
