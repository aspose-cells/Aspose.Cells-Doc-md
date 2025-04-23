---
title: Trouver des tables de requête et des objets liste liés aux connexions de données externes
type: docs
weight: 20
url: /fr/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---

## **Trouver des Tables de Requête et des Objets Liste liés aux Connexions de Données Externes**

Parfois, vous devez trouver des tables de requête et des objets liste liés à une connexion de données externe. Les tables de requête sont liées à l'objet de connexion de données externe avec l'ID de connexion, tandis que les objets liste sont liés à une table de requête.

Le code d'exemple suivant explique comment trouver les tables de requête et les objets liste liés à une connexion de données externe. Le code utilise le [fichier Excel exemple](5472550.xlsm) que vous pouvez télécharger à partir du lien fourni. Vous pouvez également voir la sortie de ce code exemple en bas de cet article.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **Sortie console**

Voici la sortie console du code d'exemple ci-dessus en utilisant ce [fichier Excel exemple](5472550.xlsm).

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
{{< app/cells/assistant language="java" >}}
