---
title: Utiliser Aspose.Cells for Java avec ColdFusion
type: docs
weight: 40
url: /fr/java/using-aspose-cells-for-java-with-coldfusion/
---

{{% alert color="primary" %}}

Cet article donne les informations de base et le segment de code dont les développeurs ColdFusion ont besoin pour utiliser Aspose.Cells for Java dans leur application ColdFusion.

Cet article montre comment créer une simple page web en utilisant ColdFusion et utiliser Aspose.Cells for Java pour générer un simple fichier Excel.

{{% /alert %}}

## **Aspose.Cells : Le véritable produit**

Avec Aspose.Cells, les développeurs peuvent exporter des données, formater des feuilles de calcul dans les moindres détails et à chaque niveau, importer des images, importer des graphiques, créer des graphiques, manipuler des graphiques, diffuser des données Microsoft Excel, enregistrer dans divers formats, y compris XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML (intégré avec [Aspose.Pdf](https://products.aspose.com/pdf/java/)) et bien plus encore.

Pour plus d'informations sur le produit, les fonctionnalités et pour un guide du programmeur, veuillez vous référer à la documentation et aux démonstrations en ligne de Aspose.Cells ([demos](https://github.com/aspose-cells/Aspose.Cells-for-Java)). Vous pouvez le [télécharger](https://downloads.aspose.com/cells/java) et l'évaluer gratuitement.

### **Prérequis**

Pour utiliser Aspose.Cells for Java dans des applications ColdFusion, copiez le fichier Aspose.Cells.jar dans le dossier {DossierD'Installation\\}\wwwroot\WEB-INF\lib.

N'oubliez pas de redémarrer le serveur d'application ColdFusion après avoir ajouté de nouveaux JAR dans le dossier lib.

### **Utiliser Aspose.Cells for Java & ColdFusion pour créer un fichier Excel**

Ci-dessous, nous créons une application simple qui génère un fichier Excel Microsoft vide, insère du contenu et l'enregistre en tant que fichier XLS.

Voici le code réel (ColdFusion & Aspose.Cells for Java). Après l'exécution du code, un fichier Excel, output.xls, est généré.

**output.xls généré**

![todo:image_alt_text](using-aspose-cells-for-java-with-coldfusion_1.png)

**Java**

{{< highlight java >}}

 <html>

<head><title>Hello World!</title></head>

<body>

    <b>This example shows how to create a simple MS Excel Workbook using Aspose.Cells</b>

    <cfset workbook=CreateObject("java", "com.aspose.cells.Workbook").init()>

    <cfset worksheets = workbook.getWorksheets()>

    <cfset sheet= worksheets.get("Sheet1")>

    <cfset cells= sheet.getCells()>

    <cfset cell= cells.getCell(0,0)>

    <cfset cell.setValue("Hello World!")>

    <cfset workbook.save("C:\output.xls")>

</body>

</html>

{{< /highlight >}}

## **Résumé**

{{% alert color="primary" %}}

Cet article explique comment utiliser Aspose.Cells for Java avec ColdFusion.

Aspose.Cells offre une grande flexibilité et une vitesse, une efficacité et une fiabilité exceptionnelles. Aspose.Cells a bénéficié de nombreuses années de recherche, de conception et d'ajustements minutieux.

Nous accueillons les questions, les commentaires et les suggestions sur le [Forum Aspose.Cells](https://forum.aspose.com/c/cells/9).

{{% /alert %}}
