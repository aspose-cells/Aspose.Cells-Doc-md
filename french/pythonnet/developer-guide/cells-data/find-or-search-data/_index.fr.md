---
title: Trouver ou rechercher des données
type: docs
weight: 50
url: /fr/python-net/find-or-search-data/
description: Apprenez à trouver ou rechercher des cellules dans une feuille de calcul contenant des données spécifiées via l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Recherche de données Python, Recherche de données Python, Recherche de cellules Python contenant une formule, Recherche de cellules Python contenant une formule, Recherche de données ou de formules à l aide de FindOptions Python, Recherche de données ou de formules à l aide de FindOptions Python, Recherche de cellules contenant une valeur ou un nombre de chaîne spécifié Python, Recherche de cellules contenant des données spécifiées Python
---

{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de trouver des cellules dans une feuille de calcul contenant des données spécifiées.

{{% /alert %}}

## **Recherche de cellules contenant des données spécifiées**

### **Utilisation de Microsoft Excel**

Microsoft Excel permet aux utilisateurs de trouver des cellules dans une feuille de calcul contenant des données spécifiées. Si vous sélectionnez **Modifier** dans le menu **Rechercher** de Microsoft Excel, vous verrez une boîte de dialogue où vous pouvez spécifier la valeur de recherche.

Ici, nous recherchons la valeur "Oranges". Aspose.Cells permet également aux développeurs de trouver des cellules dans la feuille de calcul contenant des valeurs spécifiées.

### **Utilisation d'Aspose.Cells**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) qui représente toutes les cellules de la feuille de calcul. La collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) propose plusieurs méthodes pour trouver des cellules dans une feuille de calcul contenant des données spécifiées. Quelques-unes de ces méthodes sont discutées ci-dessous en détail.

{{% alert color="primary" %}}

Toutes les méthodes de recherche renvoient les références des cellules contenant les données spécifiées à rechercher.

{{% /alert %}}

## **Recherche de cellules contenant une formule**

Les développeurs peuvent trouver une formule spécifiée dans la feuille de calcul en appelant la méthode [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) de la collection [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions). En général, la méthode [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) accepte trois paramètres :

- **qu'est-ce que:** L'objet à rechercher. Le type doit être int, double, DateTime, string, bool.
- **cellule_précédente:** Cellule précédente avec le même objet. Ce paramètre peut être défini sur null s'il s'agit d'une recherche depuis le début.
- **options_de_recherche:** Options pour trouver l'objet requis.

Les exemples ci-dessous utilisent les données de la feuille de calcul pour apprendre les méthodes de recherche.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingFormula-1.py" >}}

## **Recherche de données ou de formules à l'aide de FindOptions**

Il est possible de trouver des valeurs spécifiées en utilisant la méthode [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) avec divers [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions). En général, la méthode [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) accepte les paramètres suivants :

- **qu'est-ce que:**, les données ou la valeur à rechercher.
- **cellule_précédente**, la dernière cellule qui contenait la même valeur. Ce paramètre peut être défini sur null lors d'une recherche depuis le début.
- **find_options**, les options de recherche.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingDataOrFormulasUsingFindOptions-1.py" >}}

## **Recherche des cellules contenant une valeur de chaîne spécifiée ou un nombre.**

Il est possible de trouver des valeurs de chaîne spécifiées en appelant la même méthode [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) trouvée dans la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) avec divers [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions).

Spécifiez les propriétés [**FindOptions.look_in_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_in_type/) et [**FindOptions.look_at_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_at_type/). L'exemple de code suivant illustre comment utiliser ces propriétés pour trouver des cellules avec un nombre varié de chaînes au **début** ou au **centre** ou à la **fin** de la chaîne de la cellule.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingStringValueOrNumber-1.py" >}}

## **Sujets avancés**
- [Rechercher des cellules avec un style spécifique](/cells/fr/python-net/find-cells-with-specific-style/)
- [Trouver si la valeur de la cellule commence par un guillemet simple](/cells/fr/python-net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Rechercher des données en utilisant des valeurs originales](/cells/fr/python-net/search-data-using-original-values/)
{{< app/cells/assistant language="python-net" >}}
