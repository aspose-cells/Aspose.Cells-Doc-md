---
title: Création de rapport tabulaire
type: docs
weight: 70
url: /fr/reportingservices/creating-tabular-report/
---

{{% alert color="primary" %}} 

Un tableau dans un modèle de rapport Aspose.Cells se compose d'un en-tête, de lignes de données de tableau, de groupes de lignes et de pieds de page. Un tableau d'exemple est présenté ci-dessous.

**Un exemple de tableau** 

![todo:image_alt_text](creating-tabular-report_1.png)
#### **En-tête de tableau**
L'en-tête de tableau contient généralement le titre de chaque colonne du tableau et d'autres éléments textuels tels que du texte statique, des paramètres de rapport, des variables globales de rapport, etc. L'en-tête de tableau est facultatif. En cas d'utilisation d'un en-tête, la balise d'en-tête doit être placée à gauche de la première colonne des données du tableau pour indiquer que la ligne est un en-tête.
#### **Ligne de données de tableau**
Une ligne de données de tableau est une ligne de cellules contenant des marqueurs intelligents. Un tableau ne peut contenir qu'une seule ligne de données.
#### **Groupe de lignes**
Le groupe de lignes suit étroitement la ligne de données du tableau et comprend deux parties : la balise de groupe et la ligne de données de groupe. 

La balise de groupe doit être placée à gauche de la première colonne de données du tableau pour indiquer que la ligne est la ligne de données du groupe. Le format de la balise de groupe est ##group{NomColonneGroupe}, par exemple ##group{NumeroCommandeVente} où NumeroCommandeVente est l'un des noms de colonnes de l'ensemble de données. Un tableau ne peut contenir qu'un groupe de lignes, mais un groupe de lignes peut contenir plus d'une ligne de données de groupe. La balise de groupe ne peut être placée que dans la première ligne de données, comme indiqué dans l'exemple ci-dessus.

La balise de groupe est supprimée du fichier Microsoft Excel en sortie au moment du rendu. Les groupes de lignes sont facultatifs.
#### **Pieds de page**
Les pieds de page viennent après le groupe de lignes et comprennent trois parties : la balise de pied de page, la ligne de données de pied de page et la zone de texte du pied de page. 

La balise de pied de page doit être placée à gauche de la première colonne de la colonne de données du tableau qui indique que la ligne est le pied de page du tableau. Un tableau peut contenir plusieurs lignes de données de pied de page et chaque ligne de pied de page doit être marquée par une balise de pied de page. 

La zone de texte du pied de page peut contenir du texte statique, des paramètres de rapport et des variables globales de rapport, comme indiqué dans l'exemple ci-dessus.

La balise de pied de page est supprimée du fichier Microsoft Excel en sortie au moment du rendu. Les pieds de page sont facultatifs.

La sortie du modèle d'exemple est présentée ci-dessous.

**Modèle d'exemple** 

![todo:image_alt_text](creating-tabular-report_2.png)

{{% /alert %}} 
###### **Cette section comprend les sujets suivants :** 
- [Préparation à la création du rapport de tableau](/cells/fr/reportingservices/preparing-for-creating-table-report/)
- [Ajout des informations de base pour le tableau](/cells/fr/reportingservices/adding-base-information-for-table/)
- [Ajout de formules de services de reporting](/cells/fr/reportingservices/adding-reporting-services-formulas/)
- [Ajout de groupe de tableau](/cells/fr/reportingservices/adding-table-group/)
- [Ajout des pieds de tableau](/cells/fr/reportingservices/adding-table-footers/)
- [Ajout des paramètres de rapport au rapport](/cells/fr/reportingservices/adding-report-parameters-to-report/)
- [Ajout des variables globales de services de reporting au rapport](/cells/fr/reportingservices/adding-reporting-services-global-variables-to-report/)
- [Définition des attributs du rapport](/cells/fr/reportingservices/setting-report-attributes/)
- [Modification des attributs du rapport](/cells/fr/reportingservices/modifying-report-attributes/)
