---
title: Récupération des données de connexion SQL
type: docs
weight: 20
url: /fr/java/retrieving-sql-connection-data/
---
{{% alert color="primary" %}} 

 Aspose.Cells peut vous aider à récupérer les données de connexion SQL. Cela inclut toutes les données requises pour établir une connexion au serveur SQL, par exemple,**URL du serveur**, **Nom d'utilisateur**, **nom de la table**, **requête SQL complète**, **type de requête**, **emplacement du tableau** , et**nom de la plage nommée** associé avec.

{{% /alert %}} 

Dans Microsoft Excel, connectez-vous à une base de données en :

1.  En cliquant sur le**Données** menu et sélection**À partir d'autres sources** suivie par**À partir de SQL Server**.
1.  Sélectionnez ensuite**Données** suivie par**Connexions**.
1. Utilisez l'assistant Connexions pour vous connecter à la base de données et créer une requête de base de données.

**Affichage de l'option de connexion SQL dans Microsoft Excel** 

![tâche : image_autre_texte](retrieving-sql-connection-data_1.png)

Aspose.Cells fournit la méthode Workbook.getDataConnections() pour récupérer les connexions externes. Il renvoie une collection d'objets ExternalConnection dans le classeur.

Si l'objet ExternalConnection contient des données de connexion SQL, il peut être converti en un objet DBConnection dont les propriétés sont utilisées pour récupérer la commande de base de données, le type de commande, la description de la connexion, les informations de connexion, les informations d'identification, etc.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}






