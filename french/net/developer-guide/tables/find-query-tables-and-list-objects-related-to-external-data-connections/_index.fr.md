---
title: Trouver des tables de requête et des objets liste liés aux connexions de données externes
type: docs
weight: 20
url: /fr/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---

{{% alert color="primary" %}} 

Parfois, vous devez trouver des tables de requête et des objets liste liés à une connexion de données externe. Les tables de requête sont liées à l'objet de connexion de données externe avec l'ID de connexion, tandis que les objets liste sont liés à une table de requête.

{{% /alert %}} 
## **Trouver des Tables de Requête et des Objets Liste liés aux Connexions de Données Externes**
Les exemples de code suivants avec [fichier Excel d'exemple](5115493.xlsm) expliquent comment trouver des tables de requête et des objets de liste liés à une connexion de données externe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

Voici la sortie de la console de l'exécution des codes d'exemple ci-dessus avec ce [fichier Excel d'exemple](5115493.xlsm).

{{< highlight java >}}

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
