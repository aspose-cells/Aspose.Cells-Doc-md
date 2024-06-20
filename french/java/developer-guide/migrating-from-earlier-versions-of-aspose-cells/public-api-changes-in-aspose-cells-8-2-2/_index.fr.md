---
title: Changements de l API publique dans Aspose.Cells 8.2.2
type: docs
weight: 100
url: /fr/java/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.2.1 à la version 8.2.2 pouvant intéresser les développeurs de modules/applications.

{{% /alert %}} 
## **APIs ajoutées**
### **Propriété Version ajoutée pour la classe BuiltInDocumentPropertyCollection**
La nouvelle propriété Version a été ajoutée à la classe BuiltInDocumentPropertyCollection afin de permettre aux développeurs d'obtenir ou de définir la version de l'application pour une feuille de calcul donnée.

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Obtenir la version de l'application qui a créé la feuille de calcul](/cells/fr/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Propriété Worksheet ajoutée à Chart**
Avant la publication d'Aspose.Cells 8.2.2, il n'était pas possible de récupérer l'instance du Worksheet à partir d'un objet Chart qu'il contient. Aspose.Cells 8.2.2 a comblé ce manque en fournissant la propriété Chart.Worksheet.

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé [Obtenir le Worksheet du Chart](/cells/fr/java/get-worksheet-of-the-chart/) pour plus d'informations.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
