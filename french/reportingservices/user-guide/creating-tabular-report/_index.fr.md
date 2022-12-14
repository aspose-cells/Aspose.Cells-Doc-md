---
title: Création d'un rapport tabulaire
type: docs
weight: 70
url: /fr/reportingservices/creating-tabular-report/
---
{{% alert color="primary" %}} 

Un tableau dans un modèle de rapport Aspose.Cells se compose d'un en-tête, de lignes de données de tableau, de groupes de lignes et de pieds de page. Un exemple de tableau est présenté ci-dessous.

**Un exemple de tableau** 

![tâche : image_autre_texte](creating-tabular-report_1.png)
#### **En-tête de tableau**
L'en-tête de tableau contient normalement le titre de chaque colonne de tableau et d'autres éléments de texte tels que du texte statique, des paramètres de rapport, des variables de rapport globales, etc. L'en-tête du tableau est facultatif. Si vous utilisez un en-tête, la balise d'en-tête doit être placée à gauche de la première colonne de données du tableau pour indiquer que la ligne est un en-tête.
#### **Ligne de données du tableau**
Une ligne de données de tableau est une ligne de cellules contenant des marqueurs intelligents. Un tableau ne peut contenir qu'une seule ligne de données.
#### **Groupe de lignes**
Le groupe de lignes suit de près la ligne de données du tableau et comprend deux parties : la balise de groupe et la ligne de données de groupe.

La balise de groupe doit être placée à gauche de la première colonne de données du tableau pour indiquer que la ligne est la ligne de données du groupe de lignes. Le format de la balise de groupe est ##group{GroupColumn}, par exemple ##group{SalesOrderNumber} où SalesOrderNumber est l'un des noms de colonne de l'ensemble de données. Un tableau ne peut contenir qu'un seul groupe de lignes, mais un groupe de lignes peut contenir plusieurs lignes de données de groupe. La balise de groupe ne peut être placée que dans la première ligne de données, comme illustré dans l'exemple ci-dessus.

La balise de groupe est supprimée du fichier Excel de sortie Microsoft au moment du rendu. Les groupes de lignes sont facultatifs.
#### **Pieds de page**
 Les pieds de page viennent après le groupe de lignes et comprennent trois parties : balise de pied de page, ligne de données de pied de page et zone de texte de pied de page.

La balise de pied de page doit être placée à gauche de la première colonne de la colonne de données du tableau qui indique que la ligne est le pied de page du tableau. Un tableau peut contenir plusieurs lignes de données de pied de page et chaque ligne de pied de page doit être marquée par une balise de pied de page.

La zone de texte du pied de page peut contenir du texte statique, des paramètres de rapport et des variables de rapport globales, comme illustré dans l'exemple ci-dessus.

La balise de pied de page est supprimée du fichier Excel de sortie Microsoft au moment du rendu. Les pieds de page sont facultatifs.

La sortie de l'exemple de modèle est illustrée ci-dessous.

**Exemple de modèle** 

![tâche : image_autre_texte](creating-tabular-report_2.png)

{{% /alert %}} 
###### **Cette section comprend les rubriques suivantes :**
- [Préparation à la création d'un rapport de tableau](/cells/fr/reportingservices/preparing-for-creating-table-report/)
- [Ajout d'informations de base pour le tableau](/cells/fr/reportingservices/adding-base-information-for-table/)
- [Ajout de formules Reporting Services](/cells/fr/reportingservices/adding-reporting-services-formulas/)
- [Ajout d'un groupe de tables](/cells/fr/reportingservices/adding-table-group/)
- [Ajout de pieds de tableau](/cells/fr/reportingservices/adding-table-footers/)
- [Ajout de paramètres de rapport au rapport](/cells/fr/reportingservices/adding-report-parameters-to-report/)
- [Ajout de variables globales Reporting Services au rapport](/cells/fr/reportingservices/adding-reporting-services-global-variables-to-report/)
- [Définition des attributs de rapport](/cells/fr/reportingservices/setting-report-attributes/)
- [Modification des attributs de rapport](/cells/fr/reportingservices/modifying-report-attributes/)
