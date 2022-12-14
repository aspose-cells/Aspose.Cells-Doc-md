---
title: Utilisation de Aspose.Cells for Java avec ColdFusion
type: docs
weight: 40
url: /fr/java/using-aspose-cells-for-java-with-coldfusion/
---
{{% alert color="primary" %}}

Cet article donne les informations de base et le segment de code dont les développeurs ColdFusion ont besoin pour utiliser Aspose.Cells for Java dans leur application ColdFusion.

Cet article explique comment créer une page Web simple à l'aide de ColdFusion et utiliser Aspose.Cells for Java pour générer un fichier Excel simple.

{{% /alert %}}

## **Aspose.Cells : Le vrai produit**

Avec Aspose.Cells, les développeurs peuvent exporter des données, formater des feuilles de calcul dans les moindres détails et à tous les niveaux, importer des images, importer des graphiques, créer des graphiques, manipuler des graphiques, diffuser des données Excel Microsoft, enregistrer dans différents formats, notamment XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML ([Aspose.Pdf](https://products.aspose.com/pdf/java/) intégré) et bien d'autres.

 Pour en savoir plus sur les informations produit, les fonctionnalités et pour un guide du programmeur, reportez-vous à la documentation Aspose.Cells et en ligne en vedette[démos](https://github.com/aspose-cells/Aspose.Cells-for-Java) . Tu peux[Télécharger](https://downloads.aspose.com/cells/java) et évaluez-le gratuitement.

### **Conditions préalables**

Pour utiliser Aspose.Cells for Java dans les applications ColdFusion, copiez le fichier Aspose.Cells.jar dans le dossier {InstallationFolder\\}\wwwroot\WEB-INF\lib.

N'oubliez pas de redémarrer le serveur d'applications ColdFusion après avoir placé de nouveaux fichiers JAR dans le dossier lib.

### **Utilisation de Aspose.Cells for Java et ColdFusion pour créer un fichier Excel**

Ci-dessous, nous créons une application simple qui génère un fichier Excel Microsoft vide, insère du contenu et l'enregistre en tant que fichier XLS.

Voici le code réel (ColdFusion & Aspose.Cells for Java). Après l'exécution du code, un fichier Excel, output.xls, est généré.

**Sortie générée.xls**

![tâche : image_autre_texte](using-aspose-cells-for-java-with-coldfusion_1.png)

**Java**

{{< highlight "java" >}}

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

## **Sommaire**

{{% alert color="primary" %}}

Cet article explique comment utiliser Aspose.Cells for Java avec ColdFusion.

Aspose.Cells offre une grande flexibilité et offre une vitesse, une efficacité et une fiabilité exceptionnelles. Aspose.Cells a bénéficié d'années de recherche, de conception et de réglage minutieux.

 Nous accueillons les questions, commentaires et suggestions dans le[Aspose.CellsForum](https://forum.aspose.com/c/cells/9).

{{% /alert %}}
