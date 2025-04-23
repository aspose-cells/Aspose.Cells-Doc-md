---
title: Récupération des données de connexion SQL
type: docs
weight: 10
url: /fr/net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells peut vous aider à récupérer les données de connexion SQL. Cela inclut toutes les données nécessaires pour établir une connexion avec le serveur SQL, par exemple, **URL du serveur**, **nom d'utilisateur**, **nom de la table**, **requête SQL complète**, **type de requête**, **emplacement de la table**, et **nom de la plage nommée** associée.

{{% /alert %}}

Dans Microsoft Excel, se connecter à une base de données en :

1. Cliquant sur le menu **Données** et en sélectionnant **À partir d'autres sources**, puis **Depuis un serveur SQL**.
1. Ensuite, sélectionnez **Données** suivi de **Connexions**.
1. Utilisez l'assistant Connexions pour vous connecter à la base de données et créer une requête de base de données.

Aspose.Cells fournit la propriété Workbook.DataConnections pour récupérer les connexions externes. Elle renvoie une collection d'objets ExternalConnection dans le classeur.

Si l'objet ExternalConnection contient des données de connexion SQL, il peut être converti en objet DBConnection et ses propriétés peuvent être utilisées pour récupérer la commande de base de données, le type de commande, la description de la connexion, les informations de connexion, les informations d'identification, etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
