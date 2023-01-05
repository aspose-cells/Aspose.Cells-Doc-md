---
title: Insérer un tableau croisé dynamique
linktitle: Tableaux croisés dynamiques
type: docs
weight: 160
url: /fr/net/create-pivot-table/
description: Créer et mettre en forme des tableaux croisés dynamiques de fichiers de feuille de calcul Excel.
---
## **Créer un tableau croisé dynamique**

Il est possible d'utiliser Aspose.Cells pour ajouter des tableaux croisés dynamiques aux feuilles de calcul par programme.

### **Modèle d'objet de tableau croisé dynamique**

Aspose.Cells fournit un ensemble spécial de classes dans le[**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) espace de noms utilisé pour créer et contrôler les tableaux croisés dynamiques. Ces classes sont utilisées pour créer et définir[**Tableau croisé dynamique**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)objets, les blocs de construction d'un tableau croisé dynamique. Les objets sont :

- [**Champ Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) représente un champ dans un[**Tableau croisé dynamique**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollectionPivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) représente une collection de tous les[**Champ Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) des objets dans le[**Tableau croisé dynamique**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**Tableau croisé dynamique**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)représente un tableau croisé dynamique dans une feuille de calcul.
- [**Collection de tableaux croisés dynamiques**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) représente une collection de tous les[**Tableau croisé dynamique**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)objets sur une feuille de calcul.

### **Création d'un tableau croisé dynamique simple à l'aide de Aspose.Cells**

1. Ajouter des données à une feuille de calcul à l'aide de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) objets[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) méthode.
 Ces données seront utilisées comme source de données du tableau croisé dynamique.
1.  Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant le[**Tableaux croisés dynamiques**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) de la collection[**ajouter**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index)méthode, qui est encapsulée dans l'objet Worksheet.
1.  Accéder au nouveau[**Tableau croisé dynamique**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objet de la[**Tableaux croisés dynamiques**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)collection en passant l'index de tableau croisé dynamique.
1.  Utilisez l'un des[**Tableau croisé dynamique**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)objets (expliqués ci-dessus) pour gérer le tableau croisé dynamique.

Après avoir exécuté l'exemple de code, un tableau croisé dynamique est ajouté à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

Lors de l'affectation d'une plage de cellules comme source de données, la plage doit aller du haut à gauche au bas à droite. Par exemple, "A1:C3" est valide mais "C3:A1" ne l'est pas.

{{% /alert %}}

## **Sujets avancés**
- [Fonction Consolidation](/cells/fr/net/consolidation-function/)
- [Tri personnalisé dans le tableau croisé dynamique](/cells/fr/net/custom-sorting-in-pivot-table/)
- [Personnaliser les paramètres de globalisation pour le tableau croisé dynamique](/cells/fr/net/customize-globalization-settings-for-pivot-table/)
- [Désactiver les rubans du tableau croisé dynamique](/cells/fr/net/disable-pivot-table-ribbons/)
- [Rechercher et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent](/cells/fr/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Formatage du tableau croisé dynamique](/cells/fr/net/formatting-pivot-table/)
- [Obtenir la source de données de connexion externe du tableau croisé dynamique](/cells/fr/net/get-external-connection-data-source-of-pivot-table/)
- [Obtenir la date d'actualisation du tableau croisé dynamique et actualiser par qui les informations](/cells/fr/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Champs de groupe de pivot dans le tableau croisé dynamique](/cells/fr/net/group-pivot-fields-in-the-pivot-table/)
- [Analyse des enregistrements en cache Pivot lors du chargement du fichier Excel](/cells/fr/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Tableau croisé dynamique et données source](/cells/fr/net/pivot-table-and-source-data/)
- [Masquer et trier les données du tableau croisé dynamique](/cells/fr/net/pivot-table-hide-and-sort-data/)
- [Actualiser et calculer le tableau croisé dynamique ayant des éléments calculés](/cells/fr/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Enregistrer le tableau croisé dynamique dans le fichier ODS](/cells/fr/net/save-pivot-table-in-ods-file/)
- [Afficher l'option de pages de filtre de rapport](/cells/fr/net/show-report-filter-pages-option/)
- [Utilisation des formats d'affichage de données de DataField dans le tableau croisé dynamique](/cells/fr/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
