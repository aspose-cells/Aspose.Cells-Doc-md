---
title: Préface
type: docs
weight: 20
url: /fr/reportingservices/preface/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services contient principalement deux composants : Aspose.Cells.Report.Designer et Aspose.Cells.Renderer pour Reporting Services. Le premier est utilisé pour concevoir des rapports directement dans Microsoft Excel et le second est responsable du rendu d'un rapport RDL dans Microsoft Excel. 

{{% /alert %}} 
### **Conception d'un rapport avec le concepteur de rapports**
Les principales étapes pour concevoir un rapport à l'aide de Aspose.Cells.Report.Designer sont :

1. **Créer des sources de données et des requêtes**.
   Microsoft Query est intégré à Aspose.Cells.Report.Designer et utilisé comme un outil graphique pour créer des sources de données et des requêtes. Les utilisateurs peuvent également utiliser un fichier RDL existant dans lequel des sources de données et des requêtes sont disponibles pour les opérations.
1. **Mapper les paramètres**.
   Si les instructions SQL d'une requête incluent des paramètres, les utilisateurs doivent créer des paramètres de rapport et mapper les paramètres SQL aux paramètres de rapport. Vous pouvez désigner des valeurs valides pour un paramètre de rapport dans Aspose.Cells.Report.Designer.
1. **Concevoir le contenu, les styles et les formats du modèle de rapport Microsoft Excel**.
   Un modèle de rapport Aspose.Cells peut contenir un nombre quelconque des types d'éléments de rapport suivants : 
   1. Tableau
   1. Tableau croisé dynamique
   1. Graphique
   1. Zone de texte
   1. Matrice
      Normalement, une requête (c'est-à-dire, un jeu de données) est utilisée comme une source de données pour un élément de rapport. Vous pouvez également utiliser des paramètres de Reporting Services, des formules et des variables globales comme source de données pour certains types d'éléments de rapport. Les styles et formats des éléments de rapport sont simplement spécifiés en définissant les styles et formats des cellules qui composent les éléments de rapport.
1. **Publier le rapport**.
   Après les étapes ci-dessus, le rapport est prêt à être publié. Les utilisateurs peuvent désigner le dossier dans lequel le rapport est publié. Si nécessaire, vous pouvez assigner une source de données partagée sur le serveur de rapports comme source de données pour le rapport.
1. **Aperçu du rapport**.
   Lors de la sélection d'un rapport pour un aperçu sur le Serveur de rapports, vous êtes invité à spécifier le format de fichier dans lequel l'exporter (par exemple, le format XLS binaire Microsoft Excel 97-2003, SpreadsheetML ou le format XLSX Microsoft Excel 2007), ainsi que tout paramètre de rapport créé lors de la conception du rapport. Après cela, le rapport est peuplé de données fournies par les Services de génération de rapports.
