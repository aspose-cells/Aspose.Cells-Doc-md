---
title: Public API Changements dans Aspose.Cells 8.2.2
type: docs
weight: 90
url: /fr/net/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.2.1 à 8.2.2 qui peuvent intéresser les développeurs de modules/applications.

{{% /alert %}} 
## **API ajoutées**
### **Propriété BuiltInDocumentPropertyCollection.Version ajoutée**
La nouvelle propriété Version a été ajoutée à la classe BuiltInDocumentPropertyCollection afin de permettre aux développeurs de récupérer la version de l'application qui a créé une feuille de calcul donnée.

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé[Obtenir la version de l'application qui a créé la feuille de calcul](/cells/fr/net/get-the-version-number-of-the-application-that-created-the-excel-document/) pour plus d'informations.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **Property Chart.Worksheet Ajouté**
Avant la version Aspose.Cells 8.2.2, il n'était pas possible de récupérer l'instance de Worksheet à partir d'un objet Chart qu'elle contient. Aspose.Cells 8.2.2 a comblé cette lacune en fournissant la propriété Chart.Worksheet.

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé[Obtenir la feuille de calcul du graphique](/cells/fr/net/get-worksheet-of-the-chart/) pour plus d'informations.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
