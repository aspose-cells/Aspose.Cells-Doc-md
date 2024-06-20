---
title: Rapport paramétré
type: docs
weight: 60
url: /fr/reportingservices/parameterized-report/
---

{{% alert color="primary" %}} 

Un *rapport paramétré* est un rapport qui accepte des valeurs d'entrée qui sont utilisées lors du traitement du rapport. 

Avec un rapport paramétré, vous pouvez faire varier la sortie d'un rapport en fonction des valeurs définies au moment de l'exécution. Les Services de Reporting prennent en charge deux types de paramètres : les paramètres de requête et les paramètres de rapport. 

- **Les paramètres de requête** sont utilisés pour sélectionner ou filtrer des données lors du traitement des données. Si un paramètre de requête est spécifié, une valeur doit être fournie soit par l'utilisateur soit par les propriétés par défaut pour compléter l'instruction SELECT ou la procédure stockée qui récupère les données pour un rapport.
- **Les paramètres de rapport** sont utilisés pendant le traitement du rapport pour montrer un aspect différent des données. Un paramètre de rapport est généralement utilisé pour filtrer un grand ensemble d'enregistrements, mais il peut avoir d'autres utilisations en fonction des requêtes et des expressions dans le rapport.

Les paramètres de rapport diffèrent des paramètres de requête en ce sens qu'ils sont définis dans un rapport et traités par le serveur de rapports, tandis que les paramètres de requête sont définis comme faisant partie de la requête de l'ensemble de données et traités sur le serveur de base de données. Dans Aspose.Cells.Report.Designer, les paramètres de requête sont spécifiés lors de la création de la requête dans Microsoft Query. 

Vous pouvez créer des paramètres de rapport et mapper les paramètres de requête aux paramètres de rapport correspondants dans Aspose.Cells.Report.Designer. De cette manière, il est possible de sélectionner des valeurs pour les paramètres de rapport et de les transmettre dans la requête pour limiter les données récupérées depuis la source de données.

{{% /alert %}} 
###### **Cette section comprend les sujets suivants :** 
- [Création des paramètres de rapport](/cells/fr/reportingservices/creating-report-parameters/)
- [Modification des paramètres de rapport](/cells/fr/reportingservices/modifying-report-parameters/)
- [Mapping des paramètres de requête aux paramètres de rapport](/cells/fr/reportingservices/mapping-query-parameters-to-report-parameters/)
