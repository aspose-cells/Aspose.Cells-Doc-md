---
title: Rechercher des tables de requête et des objets de liste liés aux connexions de données externes
type: docs
weight: 20
url: /fr/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---
{{% alert color="primary" %}} 

Parfois, vous devez trouver des tables de requête et des objets de liste liés à une connexion de données externe. Les tables de requête sont liées à l'objet de connexion de données externes avec l'ID de connexion, tandis que les objets de liste sont liés à une table de requête.

{{% /alert %}} 
## **Rechercher des tables de requête et des objets de liste liés aux connexions de données externes**
 Les exemples de codes suivants avec[exemple de fichier excel](5115493.xlsm) expliquer comment rechercher des tables de requête et des objets de liste liés à la connexion de données externes.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

 Voici la sortie de la console de l'exécution des exemples de codes ci-dessus avec ce[exemple de fichier excel](5115493.xlsm).

{{< highlight "java" >}}

 connection: AAPL Connection

querytable hp?s=AAPL+Historical+Prices

refersto: =Sheet1!$Q$1:$W$69

connection: BOSL066360W7_SQLEXPRESS Test

querytable BOSL066360W7_SQLEXPRESS Test

Table Table_BOSL066360W7_SQLEXPRESS_Test

refersto: Sheet1!A1:B3

connection: BOSL066360W7_SQLEXPRESS Test1

querytable BOSL066360W7_SQLEXPRESS Test_1

Table Table_BOSL066360W7_SQLEXPRESS_Test_1

refersto: Sheet1!D1:E2

connection: UWTI Connection

querytable hp?s=UWTI+Historical+Prices

refersto: =Sheet1!$H$1:$N$69


{{< /highlight >}}
