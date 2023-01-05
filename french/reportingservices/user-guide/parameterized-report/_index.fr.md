---
title: Rapport paramétré
type: docs
weight: 60
url: /fr/reportingservices/parameterized-report/
---
{{% alert color="primary" %}} 

 UNE*rapport paramétré* est un rapport qui accepte les valeurs d'entrée utilisées lors du traitement du rapport.

 Avec un rapport paramétré, vous pouvez faire varier la sortie d'un rapport en fonction des valeurs définies au moment de l'exécution. Reporting Services prend en charge deux types de paramètres : les paramètres de requête et les paramètres de rapport.

- **Paramètres de requête** sont utilisés pour sélectionner ou filtrer les données lors du traitement des données. Si un paramètre de requête est spécifié, une valeur doit être fournie par l'utilisateur ou par les propriétés par défaut pour terminer l'instruction SELECT ou la procédure stockée qui récupère les données d'un rapport.
- **Paramètres du rapport**sont utilisés lors du traitement du rapport pour montrer un aspect différent des données. Un paramètre de rapport est généralement utilisé pour filtrer un grand nombre d'enregistrements, mais il peut avoir d'autres utilisations en fonction des requêtes et des expressions du rapport.

 Les paramètres de rapport diffèrent des paramètres de requête en ce sens qu'ils sont définis dans un rapport et traités par le serveur de rapports, tandis que les paramètres de requête sont définis dans le cadre de la requête de jeu de données et traités sur le serveur de base de données. Dans Aspose.Cells.Report.Designer, les paramètres de requête sont spécifiés au moment de la création de la requête dans Microsoft Query.

Vous pouvez créer des paramètres de rapport et mapper des paramètres de requête au paramètre de rapport correspondant dans Aspose.Cells.Report.Designer. De cette façon, il est possible de sélectionner des valeurs pour les paramètres de rapport et de les transmettre dans la requête pour limiter les données extraites de la source de données.

{{% /alert %}} 
###### **Cette section comprend les rubriques suivantes :**
- [Création de paramètres de rapport](/cells/fr/reportingservices/creating-report-parameters/)
- [Modification des paramètres de rapport](/cells/fr/reportingservices/modifying-report-parameters/)
- [Mappage des paramètres de requête aux paramètres de rapport](/cells/fr/reportingservices/mapping-query-parameters-to-report-parameters/)
