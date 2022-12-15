---
title: Préface
type: docs
weight: 20
url: /fr/reportingservices/preface/
---
{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services contient principalement deux composants : Aspose.Cells.Report.Designer et Aspose.Cells.Renderer for Reporting Services. Le premier est utilisé pour concevoir des rapports directement dans Microsoft Excel et le second est responsable du rendu d'un rapport RDL vers Microsoft Excel.

{{% /alert %}} 
### **Conception d'un rapport avec le concepteur de rapport**
Les principales étapes de conception d'un rapport à l'aide de Aspose.Cells.Report.Designer sont :

1. **Créer des sources de données et des requêtes**.
 Microsoft Query est intégré à Aspose.Cells.Report.Designer et utilisé comme outil graphique pour créer des sources de données et des requêtes. Les utilisateurs peuvent également utiliser un fichier RDL existant dans lequel les sources de données et les requêtes sont disponibles pour les opérations.
1. **Paramètres de la carte**.
 Si les instructions SQL d'une requête incluent des paramètres, les utilisateurs doivent créer des paramètres de rapport et mapper les paramètres SQL aux paramètres de rapport. Vous pouvez désigner des valeurs valides pour un paramètre de rapport dans Aspose.Cells.Report.Designer.
1. **Conception Microsoft Contenu, styles et formats du modèle de rapport Excel**.
Un modèle de rapport Aspose.Cells peut contenir n'importe quel nombre des types d'éléments de rapport suivants :
 1. Tableau
 1. Tableau croisé dynamique
 1. Graphique
 1. Zone de texte
 1. Matrice
 Normalement, une requête (c'est-à-dire DataSet) est utilisée comme source de données pour l'élément de rapport. Vous pouvez également utiliser des paramètres, des formules et des variables globales Reporting Services comme source de données pour certains types d'éléments de rapport. Les styles et les formats des éléments de rapport sont spécifiés simplement en définissant les styles et les formats des cellules qui composent les éléments de rapport.
1. **Publier le rapport**.
 Après les étapes ci-dessus, le rapport est prêt à être publié. Les utilisateurs peuvent désigner le dossier dans lequel le rapport est publié. Si nécessaire, vous pouvez affecter une source de données partagée sur le serveur de rapports comme source de données pour le rapport.
1. **Aperçu du rapport**.
Lors de la sélection d'un rapport pour l'aperçu sur le serveur de rapports, vous êtes invité à spécifier le format de fichier vers lequel l'exporter (par exemple, format binaire XLS Microsoft Excel 97-2003, SpreadsheetML ou format XLSX Microsoft Excel 2007), ainsi que tous les paramètres de rapport d'entrée créés lors de la conception du rapport. Après cela, le rapport est rempli avec les données fournies par Reporting Services.
