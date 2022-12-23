---
title: Rechercher ou rechercher des données
type: docs
weight: 50
url: /fr/net/find-or-search-data/
---
{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de rechercher des cellules dans une feuille de calcul contenant des données spécifiées.

{{% /alert %}}

## **Recherche Cells contenant des données spécifiées**

### **Utilisation d'Excel Microsoft**

 Microsoft Excel permet aux utilisateurs de rechercher des cellules dans une feuille de calcul contenant des données spécifiées. Si vous sélectionnez**Éditer** du**Trouver** menu dans Microsoft Excel, vous verrez une boîte de dialogue dans laquelle vous pouvez spécifier la valeur de recherche.

Ici, nous recherchons la valeur "Oranges". Aspose.Cells permet également aux développeurs de rechercher des cellules dans la feuille de calcul contenant des valeurs spécifiées.

### **En utilisant Aspose.Cells**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection qui représente toutes les cellules de la feuille de calcul. Le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection fournit plusieurs méthodes pour rechercher des cellules dans une feuille de calcul contenant des données spécifiées par l'utilisateur. Quelques-unes de ces méthodes sont décrites ci-dessous plus en détail.

{{% alert color="primary" %}}

Toutes les méthodes Find renvoient les références des cellules contenant les données spécifiées à rechercher.

{{% /alert %}}

## **Trouver Cells contenant une formule**

 Les développeurs peuvent trouver une formule spécifiée dans la feuille de calcul en appelant le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) de la collection[**Trouver**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) méthode. Typiquement, le[**Trouver**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)La méthode accepte trois paramètres :

- **Objet:**Objet à rechercher. Le type doit être int,double,DateTime,string,bool.
- **Cellule précédente :**Cellule précédente avec le même objet. Ce paramètre peut être défini sur null en cas de recherche depuis le début.
- FindOptions : Options de recherche de l'objet requis.

Les exemples ci-dessous utilisent des données de feuille de calcul pour s'entraîner aux méthodes de recherche :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **Recherche de données ou de formules à l'aide de FindOptions**

 Il est possible de trouver des valeurs spécifiées à l'aide de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) de la collection[**Trouver**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) méthode avec divers[**RechercherOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . Typiquement, le[**Trouver**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)La méthode accepte les paramètres suivants :

- **Valeur de recherche**, la donnée ou la valeur à rechercher.
- **Cellule précédente**, la dernière cellule contenant la même valeur. Ce paramètre peut être défini sur null lors de la recherche depuis le début.
- **Trouver des options**, les options de recherche.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Recherche de Cells contenant une valeur de chaîne ou un nombre spécifié**

 Il est possible de trouver des valeurs de chaîne spécifiées en appelant le même[**Trouver**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) méthode trouvée dans le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection avec divers[**RechercherOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 Spécifie le[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) et[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) Propriétés. L'exemple de code suivant illustre comment utiliser ces propriétés pour rechercher des cellules avec un nombre différent de chaînes à la**début** ou à la**centre** ou à la**fin** de la chaîne de la cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **Sujets avancés**
- [Trouver Cells avec un style spécifique](/cells/fr/net/find-cells-with-specific-style/)
- [Rechercher si la valeur de la cellule commence par un guillemet simple](/cells/fr/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Rechercher des données à l'aide des valeurs d'origine](/cells/fr/net/search-data-using-original-values/)
