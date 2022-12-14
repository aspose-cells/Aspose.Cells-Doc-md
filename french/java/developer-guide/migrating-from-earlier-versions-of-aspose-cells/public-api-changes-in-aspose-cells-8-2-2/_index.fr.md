---
title: Public API Changements dans Aspose.Cells 8.2.2
type: docs
weight: 100
url: /fr/java/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.2.1 à 8.2.2 qui peuvent intéresser les développeurs de modules/applications.

{{% /alert %}} 
## **API ajoutées**
### **Version de propriété ajoutée pour la classe BuiltInDocumentPropertyCollection**
La nouvelle propriété Version a été ajoutée à la classe BuiltInDocumentPropertyCollection afin de permettre aux développeurs d'obtenir ou de définir la version de l'application pour une feuille de calcul donnée.

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Obtenir la version de l'application qui a créé la feuille de calcul](/cells/fr/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Property Chart.Worksheet Ajouté**
Avant la version Aspose.Cells 8.2.2, il n'était pas possible de récupérer l'instance de Worksheet à partir d'un objet Chart qu'elle contient. Aspose.Cells 8.2.2 a comblé cette lacune en fournissant la propriété Chart.Worksheet.

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé[Obtenir la feuille de calcul du graphique](/cells/fr/java/get-worksheet-of-the-chart/) pour plus d'informations.

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
