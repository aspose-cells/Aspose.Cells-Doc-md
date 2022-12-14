---
title: Rechercher des tables de requête et des objets de liste liés aux connexions de données externes
type: docs
weight: 20
url: /fr/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---
## **Rechercher des tables de requête et des objets de liste liés aux connexions de données externes**

Parfois, vous devez trouver des tables de requête et des objets de liste liés à une connexion de données externe. Les tables de requête sont liées à l'objet de connexion de données externes avec l'ID de connexion, tandis que les objets de liste sont liés à une table de requête.

 L'exemple de code suivant explique comment vous pouvez rechercher des tables de requête et des objets de liste liés à la connexion de données externes. Le code utilise le[exemple de fichier excel](5472550.xlsm) que vous pouvez télécharger à partir du lien fourni. Vous pouvez également voir la sortie de cet exemple de code au bas de cet article.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **Sortie console**

 Voici la sortie de la console de l'exemple de code ci-dessus en utilisant this[exemple de fichier excel](5472550.xlsm).

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
