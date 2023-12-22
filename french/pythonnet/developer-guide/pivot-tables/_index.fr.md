---
title: Insérer un tableau croisé dynamique
linktitle: Tableaux croisés dynamiques
type: docs
weight: 160
url: /fr/python-net/create-pivot-table/
description: Créez et formatez un tableau croisé dynamique avec Aspose.Cells for Python via .NET.
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
---
##  **Créer un tableau croisé dynamique**

Il est possible d'utiliser Aspose.Cells for Python via .NET pour ajouter des tableaux croisés dynamiques aux feuilles de calcul par programme.

###  **Modèle d'objet de tableau croisé dynamique**

 Aspose.Cells for Python via .NET fournit un ensemble spécial de classes dans le[**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) espaces de noms utilisés pour créer et contrôler les tableaux croisés dynamiques. Ces classes sont utilisées pour créer et définir[**Tableau croisé dynamique**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)objets, les éléments de base d’un tableau croisé dynamique. Les objets sont :

- [**Champ Pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) représente un champ dans un[**Tableau croisé dynamique**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) représente une collection de tous les[**Champ Pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) des objets dans le[**Tableau croisé dynamique**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**Tableau croisé dynamique**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)représente un tableau croisé dynamique sur une feuille de calcul.
- [**Collection de tableaux croisés dynamiques**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) représente une collection de tous les[**Tableau croisé dynamique**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)objets sur une feuille de calcul.

###  **Création d'un tableau croisé dynamique simple à l'aide de Aspose.Cells**

1.  Ajoutez des données à une feuille de calcul à l'aide de l'outil[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) objets[**valeur_put**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) méthode.
 Ces données seront utilisées comme source de données du tableau croisé dynamique.
1.  Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant le[**Tableaux croisés dynamiques**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) la collection[**ajouter**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str)méthode, qui est encapsulée dans l’objet Worksheet.
1.  Accédez au nouveau[**Tableau croisé dynamique**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) objet du[**Tableaux croisés dynamiques**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)collection en passant l'index du tableau croisé dynamique.
1.  Utilisez l'un des[**Tableau croisé dynamique**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)objets (expliqués ci-dessus) pour gérer le tableau croisé dynamique.

Après avoir exécuté l'exemple de code, un tableau croisé dynamique est ajouté à la feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

Lors de l'attribution d'une plage de cellules comme source de données, la plage doit aller du coin supérieur gauche au coin inférieur droit. Par exemple, "A1:C3" est valide mais "C3:A1" ne l'est pas.

{{% /alert %}}

##  **Sujets avancés**
- [Fonction de consolidation](/cells/fr/python-net/consolidation-function/)
- [Tri personnalisé dans le tableau croisé dynamique](/cells/fr/python-net/custom-sorting-in-pivot-table/)
- [Personnaliser les paramètres de globalisation pour le tableau croisé dynamique](/cells/fr/python-net/customize-globalization-settings-for-pivot-table/)
- [Désactiver les rubans de tableau croisé dynamique](/cells/fr/python-net/disable-pivot-table-ribbons/)
- [Rechercher et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent](/cells/fr/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Formatage du tableau croisé dynamique](/cells/fr/python-net/formatting-pivot-table/)
- [Obtenir la source de données de connexion externe du tableau croisé dynamique](/cells/fr/python-net/get-external-connection-data-source-of-pivot-table/)
- [Obtenez la date d'actualisation du tableau croisé dynamique et actualisez les informations par qui](/cells/fr/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Regrouper les champs croisés dynamiques dans le tableau croisé dynamique](/cells/fr/python-net/group-pivot-fields-in-the-pivot-table/)
- [Analyse des enregistrements mis en cache par pivot lors du chargement du fichier Excel](/cells/fr/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Tableau croisé dynamique et données sources](/cells/fr/python-net/pivot-table-and-source-data/)
- [Tableau croisé dynamique Masquer et trier les données](/cells/fr/python-net/pivot-table-hide-and-sort-data/)
- [Actualiser et calculer le tableau croisé dynamique contenant les éléments calculés](/cells/fr/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Enregistrer le tableau croisé dynamique dans le fichier ODS](/cells/fr/python-net/save-pivot-table-in-ods-file/)
- [Option Afficher les pages de filtre du rapport](/cells/fr/python-net/show-report-filter-pages-option/)
- [Travailler avec les formats d'affichage des données de DataField dans le tableau croisé dynamique](/cells/fr/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
