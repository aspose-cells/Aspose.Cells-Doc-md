---
title: Récupération des données de connexion SQL
type: docs
weight: 20
url: /fr/java/retrieving-sql-connection-data/
---

{{% alert color="primary" %}} 

Aspose.Cells peut vous aider à récupérer les données de connexion SQL. Cela comprend toutes les données nécessaires pour établir une connexion avec le serveur SQL, par exemple, **URL du serveur**, **nom d'utilisateur**, **nom de la table**, **requête SQL complète**, **type de requête**, **emplacement de la table**, et **nom de la plage nommée** qui lui est associé.

{{% /alert %}} 

Dans Microsoft Excel, se connecter à une base de données en :

1. Cliquant sur le menu **Données** et en sélectionnant **À partir d'autres sources**, puis **Depuis un serveur SQL**.
1. Ensuite, sélectionnez **Données** suivi de **Connexions**.
1. Utilisez l'assistant Connexions pour vous connecter à la base de données et créer une requête de base de données.

**Affichage de l'option de connexion SQL dans Microsoft Excel** 

![todo:image_alt_text](retrieving-sql-connection-data_1.png)

Aspose.Cells fournit la méthode Workbook.getDataConnections() pour récupérer les connexions externes. Elle retourne une collection d'objets ExternalConnection dans le classeur.

Si l'objet ExternalConnection contient des données de connexion SQL, il peut être converti en un objet DBConnection et ses propriétés utilisées pour récupérer la commande de base de données, le type de commande, la description de la connexion, les informations de connexion, les informations d'identification, etc.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}






{{< app/cells/assistant language="java" >}}
